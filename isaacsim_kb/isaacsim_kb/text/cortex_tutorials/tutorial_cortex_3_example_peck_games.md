<!-- source: cortex_tutorials/tutorial_cortex_3_example_peck_games.html | title: Behavior Examples: Peck Games — Isaac Sim Documentation -->

# Behavior Examples: Peck Games
This tutorial shows how to design simple behaviors and explores the tradeoffs between state machines and decider networks. It steps through two implementations of a simple ground-pecking behavior with the Franka robot where the robot must peck around the blocks. The first implementation uses a state machine and is unable to react to blocks moved in front of its path. We fix that issue in the second implementation with a simple decider network that internally leverages parts of the original state machine. The state machine is effectively the same, but the higher-level decider can preempt the state machine as needed for reactivity. Finally, we implement a reactive pick game using a pure decider network. In that final example, we demonstrate the utility of the custom context object and its monitors.
In all command line examples, we use the abbreviation `isaac_python` for the Isaac Sim python script (`<isaac_sim_root>/python.sh` on Linux and `<isaac_sim_root>\python.bat` on Windows). The command lines are written relative to the working directory `standalone_examples/api/isaacsim.cortex.framework`.
Each example will launch Isaac Sim without playing the simulation. Press play to run the simulation and behavior.

## Designing reactivity using decider networks
We start with a simple behavior that has the robot peck at the ground avoiding regions occupied by blocks.

### State machine implementation
The `peck_state_machine` module implements this simple peck behavior as a state machine. Run the behavior using:

```
isaac_python franka_examples_main.py --behavior=peck_state_machine
```
The Franka robot will peck at the ground avoiding the blocks. You can move the blocks around to see how that affects where the robot chooses to peck.
The implementation is straightforward:

```
class PeckState(DfState):
...
def enter(self):
# On entry, sample a target.
target_p = self.sample_target_p_away_from_obs()
target_q = make_target_rotation(target_p)
self.target = PosePq(target_p, target_q)
approach_params = ApproachParams(direction=np.array([0.0, 0.0, -0.1]), std_dev=0.04)
self.context.robot.arm.send_end_effector(self.target, approach_params=approach_params)

def step(self):
target_dist = np.linalg.norm(self.context.robot.arm.get_fk_p() - self.target.p)
if target_dist < 0.01:
return None # Exit
return self # Keep going

def make_decider_network(robot):
root = DfStateMachineDecider(
DfStateSequence(
[
DfCloseGripper(width=0.0),
PeckState(),
DfTimedDeciderState(DfLift(height=0.05), activity_duration=0.25)
],
loop=True,
)
)
return DfNetwork(root, context=PeckContext(robot))
```
With the simple state machine implementation, however, there’s an error case in reactivity. Try moving a block directly into the path of a current peck. The behavior will hang trying unsuccessfully to get the end-effector to the target.
The state machine chooses the target on entry and keeps it fixed throughout the behavior. It, therefore, doesn’t react to the changing environment. State machines, by themselves, aren’t great at modeling reactive behavior. We’ll use decider networks to fix this problem.

### Decider network implementation
The `peck_decider_network` module augments this simple peck behavior by adding a reactive `Dispatch` decider node. Run the behavior using:

```
isaac_python franka_examples_main.py --behavior=peck_decider_network
```
The decider network uses a logical state monitor to monitor whether there’s a block that would prevent the end-effector from reaching the current peck target. If there is, it triggers the system to re-choose the target.

```
class PeckContext(DfContext):
def __init__(self, robot):
super().__init__(robot)
self.robot = robot
self.reset()
self.add_monitors([PeckContext.monitor_active_target_p])

def reset(self):
self.is_done = True
self.active_target_p = None

# Monitor whether a block is too close to the active target.
def monitor_active_target_p(self):
if self.active_target_p is not None and self.is_near_obs(self.active_target_p):
self.is_done = True

# Called by a special state at the end of the peck behavior.
def set_is_done(self):
self.is_done = True

...

class PeckState(DfState):
def enter(self):
target_p = self.context.active_target_p
target_q = make_target_rotation(target_p)
self.target = PosePq(target_p, target_q)
approach_params = ApproachParams(direction=np.array([0.0, 0.0, -0.1]), std_dev=0.04)
self.context.robot.arm.send_end_effector(self.target, approach_params=approach_params)

def step(self):
# Send the command each cycle so exponential smoothing will converge.
target_dist = np.linalg.norm(self.context.robot.arm.get_fk_p() - self.target.p)
if target_dist < 0.01:
return None # Exit
return self # Keep going

class Dispatch(DfDecider):
def __init__(self):
super().__init__()

self.add_child("choose_target", ChooseTarget())
self.add_child(
"peck",
DfStateMachineDecider(
DfStateSequence(
[
CloseGripper(),
PeckState(),
DfTimedDeciderState(DfLift(height=0.05), activity_duration=0.25),
DfWriteContextState(lambda context: context.set_is_done()),
]
)
),
)

def decide(self):
if self.context.is_done:
return DfDecision("choose_target")
else:
return DfDecision("peck")

def make_decider_network(robot):
return DfNetwork(Dispatch(), context=PeckContext(robot))
```
Note that the top-level `Dispatch()` decider can immediately preempt the sequential “peck” state machine if the monitor `monitor_active_target_p()` detects a block to close to the target.
Try moving the block under the end-effector. This time, every time the block gets too close to the end-effector’s target, it immediately chooses a different target.

## Designing logical state contexts
Now let’s implement a simple game where the robot pecks the block that’s most recently been moved. We use decider networks to make it simple to program reactivity to the block movements. This example demonstrates how simple behaviors can be when the logical state is sufficiently modeled by the context object.
The behavior is implemented in `peck_game`. Run the behavior using:

```
isaac_python franka_examples_main.py --behavior=peck_game
```
The `PeckContext` class handles monitoring block movement and setting the latest active target accordingly. It also monitors whether the end-effector is close to the block which is useful in deciding whether the robot needs to lift away from the block before moving to it’s next target.

```
class PeckContext(DfLogicalState):
def __init__(self, robot):
super().__init__()
self.robot = robot

self.monitors = [
PeckContext.monitor_block_movement,
PeckContext.monitor_active_target_p,
PeckContext.monitor_active_block,
PeckContext.monitor_eff_block_proximity,
PeckContext.monitor_diagnostics,
]
```
Given the logical state monitored by the context object, the main logic can be concisely written as the following `Dispatch` decider node:

```
class Dispatch(DfDecider):
def enter(self):
self.add_child("peck", PeckAction())
self.add_child("lift", DfLift(height=0.1))
self.add_child("go_home", make_go_home())

def decide(self):
if self.context.is_eff_close_to_inactive_block:
return DfDecision("lift")

if self.context.has_active_block:
return DfDecision("peck")

# If we aren't doing anything else, always just go home.
return DfDecision("go_home")
```
In words, it reasons according to the following rules: If the end-effector is close to an inactive block, we need to just lift away from it (it’s too close). Otherwise, if there’s an active block, move to peck it. If no block is active, go home. This `decide()` method is ticked every cycle so immediately once the active block monitor notices a block has moved, it acts on it.
