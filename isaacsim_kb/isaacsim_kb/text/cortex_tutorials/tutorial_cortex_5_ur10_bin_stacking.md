<!-- source: cortex_tutorials/tutorial_cortex_5_ur10_bin_stacking.html | title: Walkthrough: UR10 Bin Stacking — Isaac Sim Documentation -->

# Walkthrough: UR10 Bin Stacking
This tutorial walks through a complete bin stacking application using the UR10 robot. In this example, we use a pre-designed USD environment containing a conveyor belt, a pallet where the bins should be stacked, and a UR10 robot with a suction gripper. Our application doesn’t add to the scene (aside from invisible collision obstacles), and instead controls the existing USD elements in the pre-designed USD environment.
In all command line examples, we use the abbreviation `isaac_python` for the Isaac Sim python script (`<isaac_sim_root>/python.sh` on Linux and `<isaac_sim_root>\python.bat` on Windows). The command lines are written relative to the working directory `standalone_examples/api/isaacsim.cortex.framework`.
Run the following demo

```
isaac_python demo_ur10_conveyor_main.py
```
Press play once Isaac Sim has started up. You’ll see the bin stacking demo running.
This tutorial will step through the demo.
The setting is a UR10 robot with a suction gripper moving bins from a conveyor to a pallet. Bins need to be stacked upside down, so any bin that that comes right-side up is flipped at a flip station before stacking.
This demo uses a shallow decider network with a top-level dispatch node choosing among multiple sequential state machines.
The individual behaviors demonstrate a common RMPflow programming technique where obstacle regions are automatically toggled on and off strategically to shape the motion behavior. These obstacle regions are modeled in the scene USD but are invisible by default. Try toggling their visibility. Go to `World/Ur10Table/Obstacles` and toggle the visibility of the `FlipStationSphere`, `NavigationDome`, `NavigationBarrier`, and `NavigationFlipStation` to see them.
The bin placement behavior also leverages the reactivity of RMPflow in conjunction with its approach direction parameters to create an automatic adjustment behavior to correct on the fly for misalignment between bins.

## Top-level dispatch
The entry point to the decider network is the `Dispatch` node as we can see in the construction. `DfNetwork` is the decider network structure; it’s passed the root (the `Dispatch` node) and the context object that will be available as a member within every decider/state node:

```
def make_decider_network(robot):
return DfNetwork(Dispatch(), context=BinStackingContext(robot))
```
The context object gives each node access to the robot’s command API as well as any logical state extracted by its monitors. The `Dispatch` node’s `decide()` logic is pretty simple given the logical state.

```
class Dispatch(DfDecider):
def __init__(self):
super().__init__()

self.add_child("flip_bin", FlipBin())
self.add_child("pick_bin", PickBin())
self.add_child("place_bin", PlaceBin())
self.add_child("go_home", make_go_home())
self.add_child("do_nothing", DfStateMachineDecider(DoNothing()))

def decide(self):
if self.context.stack_complete:
return DfDecision("go_home")

if self.context.has_active_bin:
if not self.context.active_bin.is_attached:
return DfDecision("pick_bin")
elif self.context.active_bin.needs_flip:
return DfDecision("flip_bin")
else:
return DfDecision("place_bin")
else:
return DfDecision("go_home")
```
The logical state includes:

- stack_complete: Notes whether all bins are on the pallet.

- active_bin: The bin that’s currently in play. The bin remains active until it’s been placed on the stack. Then a new bin is selected from the bins at the end of the conveyor.

- active_bin.is_attached: Indicates whether the active bin is attached to the end-effector via the suction gripper.

- active_bin.needs_flip: Indicates whether the bin attached to the end-effector is right-side-up (needs flip) or up-side-down (doesn’t need flip).

The decision logic becomes simply: If the stack is complete or there’s no active bin, then go home. Otherwise, if there’s an active bin, pick the bin if it’s not already in the gripper, and flip it if it needs to be flipped. Then place the bin on the stack. Decider networks make it easy to write this decision logic in a readable form.

## Sequential state machines
The sequential state machines that implement the pick, flip and place behaviors are each similar in structure.

```
class PickBin(DfStateMachineDecider):
def __init__(self):
super().__init__(
DfStateSequence(
[
ReachToPick(),
DfWaitState(wait_time=0.5),
DfSetLockState(set_locked_to=True, decider=self),
CloseSuctionGripper(),
DfTimedDeciderState(DfLift(0.3), activity_duration=0.4),
DfSetLockState(set_locked_to=False, decider=self),
],
)
)

class FlipBin(DfStateMachineDecider):
def __init__(self):
super().__init__(
DfStateSequence(
[
LiftAndTurn(),
MoveToFlipStation(),
DfSetLockState(set_locked_to=True, decider=self),
OpenSuctionGripper(),
ReleaseFlipStationBin(duration=0.65),
DfSetLockState(set_locked_to=False, decider=self),
]
)
)

class PlaceBin(DfStateMachineDecider):
def __init__(self):
super().__init__(
DfStateSequence(
[
ReachToPlace(),
DfWaitState(wait_time=0.5),
DfSetLockState(set_locked_to=True, decider=self),
OpenSuctionGripper(),
DfTimedDeciderState(DfLift(0.1), activity_duration=0.25),
DfWriteContextState(lambda ctx: ctx.mark_active_bin_as_complete()),
DfSetLockState(set_locked_to=False, decider=self),
],
)
)
```
One feature to note is the use of locking and unlocking the decider network. Decider networks are reactive by nature, so atomic state machine behaviors that shouldn’t be preempted need to be explicitly locked. The sequential state machines make use of `DfSetLockState` to lock and unlock the decider network. Additionally, `PlaceBin` uses `DfWriteContextState` to call a context function which marks the active bin as complete once it’s performed the placement procedure.

## Navigation obstacle monitors
The underlying motion generator for the `MotionCommander` is `RMPflow` which will automatically avoid registered obstacles. However, there are times where those obstacles need to be turned off to enable interaction. E.g. en route we want to avoid a manipulable object as obstacle, but once we’re there we should grab it. The `ObstacleMonitor` and `ObstacleMonitorContext` classes of `isaacsim.cortex.framework/isaacsim/cortex/framework/obstacle_monitor_context.py` facilitate developing obstacle monitors which automatically toggle obstacles on and off based on programmed conditions.
Take a look at the `ObstacleMonitor` implementation in the file listed above. On construction it takes a set of obstacles which it will monitor as well as the context object, and the API requires deriving classes to implement `is_obstacle_required()` to define when the obstacles should be enabled and disabled based on information accessible from the context object. The method has access to the context as `self.context` similar to the decider / state objects. The API also supplies `activate_autotoggle()` and `deactivate_autotoggle()` to activate and deactivate the monitor. When active, it’ll automatically enable and disable the obstacles based on the truth value of `is_obstacle_required()`. When deactivated, the obstacles will be disabled and remain disabled until the monitor is reactivated.
`ObstacleMonitorContext` is a convenient base class which adds a `monitor_obstacles` logical state monitor automatically, so deriving classes only need to add the obstacle monitor objects using `add_obstacle_monitors()`.
The `BinStackingContext` object derives from `ObstacleMonitorContext` and adds two obstacle monitors which it uses to shape both the navigation behavior moving between the pallet and the conveyor and the navigation around the bin flip station while flipping the bin. They’re constructed and added in the `BinStackingContext` constructor:

```
class BinStackingContext(ObstacleMonitorContext):
def __init__(self, robot):
super().__init__()

...

self.flip_station_obs_monitor = FlipStationObstacleMonitor(self)
self.navigation_obs_monitor = NavigationObstacleMonitor(self)
self.add_obstacle_monitors([self.flip_station_obs_monitor, self.navigation_obs_monitor])
```
Both monitors have simple logic:

```
class FlipStationObstacleMonitor(ObstacleMonitor):
def __init__(self, context):
super().__init__(context, [context.world.scene.get_object("flip_station_sphere")])

def is_obstacle_required(self):
eff_T = self.context.robot.arm.get_fk_T()
eff_R, eff_p = math_util.unpack_T(eff_T)
eff_ax, _, _ = math_util.unpack_R(eff_R)

grasp_p = self.context.active_bin.grasp_T[:3, 3]
grasp_ax = self.context.active_bin.grasp_T[:3, 0]
v = eff_p - grasp_p
dist = v.dot(grasp_ax)
orth_dist = np.linalg.norm(v - dist * grasp_ax)
return not (dist < 0.02 and grasp_ax.dot(eff_ax) > 0.75 and orth_dist < 0.03)

class NavigationObstacleMonitor(ObstacleMonitor):
def __init__(self, context):
obstacles = [
context.world.scene.get_object("navigation_dome_obs"),
context.world.scene.get_object("navigation_barrier_obs"),
context.world.scene.get_object("navigation_flip_station_obs"),
]
super().__init__(context, obstacles)

def is_obstacle_required(self):
target_p, _ = self.context.robot.arm.target_prim.get_world_pose()

ref_p = np.array([0.6, 0.37, -0.99])
eff_p = self.context.robot.arm.get_fk_p()

ref_p[2] = 0.0
eff_p[2] = 0.0
target_p[2] = 0.0

s_target = np.sign(np.cross(target_p, ref_p)[2])
s_eff = np.sign(np.cross(eff_p, ref_p)[2])
is_required = s_target * s_eff < 0.0
return is_required
```
The `FlipStationObstacleMonitor` monitors the `flip_station_sphere` which is a spherical obstacle around the flip station. When active, it’ll enable the obstacle until the end-effector is descending along the approach direction of its motion command toward the pose target. The monitor is used to avoid the flip station and bin (resting on the station) after releasing it from the bottom and moving to pick it from the top. It’s activated on entry to the `ReachToPick` class (used any time the bin needs to be picked, independent of whether the bin is on the flip station) and deactivated on exit.

```
class ReachToPick(MoveWithNavObs):
...

def enter(self):
super().enter()
self.context.flip_station_obs_monitor.activate_autotoggle()

def step(self):
...

def exit(self):
super().exit()
self.context.flip_station_obs_monitor.deactivate_autotoggle()
```
Similarly, the `NavigationObstacleMonitor` monitors a collection of obstacles which shape the navigation behavior between the pallet and conveyor (both directions) to avoid the robot base and current bin stack in transit. They’re needed while moving from one to the other, but not needed once the arm reaches the region of its destination (either the pallet or conveyor).
The `MoveWithNavObs` state object extends the `Move` state with entry and exit conditions that automatically toggle the navigation obstacle:

```
class MoveWithNavObs(Move):
def enter(self):
super().enter()
self.context.navigation_obs_monitor.activate_autotoggle()

def exit(self):
super().exit()
self.context.navigation_obs_monitor.deactivate_autotoggle()
```
This class is the base class for both the `ReachToPick` state and the `ReachToPlace` state used by `PickBin` and `PlaceBin` listed above.

## Robustness reactivity on placement
The bin attachment to the end-effector and the stacking alignment of the bins are both physically simulated. Just blindly grasping and moving the bin to a target without adjusting for errors will result in slightly misaligned bins which don’t rest against each other correctly. Since we’re using a reactive motion generator (RMPflow), implementing reactive adjustments is straightforward. In `ReachToPlace` the adjustments are made every cycle in the `step()` method:

```
class ReachToPlace(MoveWithNavObs):
...
def step(self):
if self.bin_under is not None:
bin_under_p, _ = self.bin_under.bin_obj.get_world_pose()
bin_grasped_p, _ = self.context.active_bin.bin_obj.get_world_pose()
xy_err = bin_under_p[:2] - bin_grasped_p[:2]
if np.linalg.norm(xy_err) < 0.02:
self.target_p[:2] += 0.1 * (bin_under_p[:2] - bin_grasped_p[:2])

target_pose = PosePq(self.target_p, math_util.matrix_to_quat(self.target_R))

approach_params = ApproachParams(direction=0.15 * np.array([0.0, 0.0, -1.0]), std_dev=0.005)
posture_config = self.context.robot.default_config
self.update_command(
MotionCommand(target_pose=target_pose, approach_params=approach_params, posture_config=posture_config)
)
```
If we’re placing a bin on top of another bin (`bin_under`) this code adjusts the end-effector target based on the xy position alignment error between the bin in the gripper and the bin under it. (The orientational alignment generally is already sufficient for successful placement.)
Additionally, RMPflow is configured to take reactive state feedback from the simulator, and we use tight approach parameters for reaching the target (`std_dev=0.005`) so it needs to follow a narrow funnel on approach. If the bin is misaligned on first approach, the bin physics will shove the end-effector out of that funnel and it’ll attempt the approach again.
In combination, this gets the robot to reactively adjust the positioning of the bin and retry the approach (repeatedly if needed) until it gets it right. Often the adjustment process is sufficient, but periodically it needs to retry the approach. Usually a single retry suffices. This is a subtle behavior and the code is concise, but it’s the difference between approximately 85% successful bin placement and 100% success.

## Logical state context
The `BinStackingContext` object additionally monitors all logical state needed to support the above behaviors. These monitors are set up in the constructor and the logical state is reset/initialized in the `reset()` method:

```
class BinStackingContext(ObstacleMonitorContext):
def __init__(self, robot):
super().__init__()
...

self.add_monitors(
[
BinStackingContext.monitor_bins,
BinStackingContext.monitor_active_bin,
BinStackingContext.monitor_active_bin_grasp_T,
BinStackingContext.monitor_active_bin_grasp_reached,
self.diagnostics_monitor.monitor,
]
)

def reset(self):
super().reset()

# Find the collection of bins in the world scene.
self.bins = []
i = 0
while True:
name = "bin_{}".format(i)
bin_obj = self.world.scene.get_object(name)
if bin_obj is None:
break
self.bins.append(BinState(bin_obj))
i += 1

self.active_bin = None
self.stacked_bins.clear()
```
These monitors perform the following:

- Monitor bins: If there’s no active bin, it checks whether there’s a bin at the end of the conveyor and activates it if so.

- Monitor the active bin: Deactivates a bin if it’s dropped on the floor.

- Monitor the grasp transform of the active bin: Monitors the best grasp for the current active bin.

- Monitor whether the active bin is reached: Sets the `active_bin.{is_grasp_reached,is_attached}` flags based on the proximity between the end-effector and desired grasp transform, and whether the suction gripper is “closed”.

- Monitor diagnostics: Prints some information about the logical state at a readable (throttled) rate.
