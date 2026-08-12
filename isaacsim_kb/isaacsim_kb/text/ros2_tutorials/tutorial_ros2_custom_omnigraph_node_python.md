<!-- source: ros2_tutorials/tutorial_ros2_custom_omnigraph_node_python.html | title: ROS 2 Python Custom OmniGraph Node — Isaac Sim Documentation -->

# ROS 2 Python Custom OmniGraph Node

## Learning Objectives
This is an optional, advanced tutorial where you will learn how to

- Use ROS 2 rclpy Python interface with Isaac Sim

- Create a basic custom OmniGraph Python node (using the Isaac Sim VS Code Edition ) that can subscribe to a topic (with message type `std_msgs/msg/Int32`) and output the Fibonacci computation of the published number.

## Getting Started
Prerequisite

- Completed ROS 2 Installation : installed ROS2, enabled the ROS2 extension, built the provided Isaac Sim ROS 2 workspace, and set up the necessary environment variables.

- Completed the tutorial for writing custom Python nodes: Custom Python Nodes

## Creating the ROS 2 Custom OmniGraph Python Node Template

- Go to Template > Extension in the Isaac Sim VS Code Edition (VS Code extension) to open a wizard to create a new Isaac Sim extension.
Take action on the following fields:

- Ext. name: Set to `custom.python.ros2_node`

- Ext. path: Define the target path where the extension will be created.

- Ext. title: Set to `ROS 2 Python Custom OmniGraph Node`

- Ready-to-use extension: Check it to create a ready-to-use extension in Python.

- Omnigraph node: Check it to generate OmniGraph-specific files/folders when creating the extension.

- Edit the extension configuration file (`custom.python.ros2_node/config/extension.toml`) to add the Isaac Sim’s ROS 2 Bridge extension as dependencies (under `[dependencies]`)

```
"isaacsim.ros2.bridge" = {}
```

- Edit the OmniGraph definition file (`OgnCustomPythonRos2NodePy.ogn` located in the `custom.python.ros2_node/custom/python/ros2_node/ogn/python/nodes` folder) with the following specification.
This specification defines an OmniGraph node with two inputs (the input execution trigger, and the topic name to subscribe to (a string)) and two outputs (the output execution trigger, and the computed Fibonacci number (an integer)).
Hint
Visit the OGN Reference Guide for a detailed guide to the syntax of `.ogn` files. Visit OmniGraph’s Attribute Data Types for more details about the supported attribute data types for inputs and outputs.

```
{
"CustomPythonRos2NodePy": {
"version": 1,
"language": "python",
"icon": "icons/icon.svg",
"uiName": "Custom Python ROS 2 Node",
"description": [
"This node subscribes to a ROS 2 topic (with message type 'std_msgs/msg/Int32') and computes and outputs the Fibonacci number"
],
"categoryDefinitions": "config/CategoryDefinition.json",
"categories": ["extension:Category"],
"inputs": {
"execIn": {
"type": "execution",
"description": "Input execution trigger"
},
"topic": {
"type": "string",
"uiName": "Subscription topic",
"description": "Topic to subscribe to",
"default": "/number"
}
},
"outputs": {
"execOut": {
"type": "execution",
"description": "Output execution trigger"
},
"fibonacci": {
"type": "uint64",
"uiName": "Fibonacci",
"description": "Computed Fibonacci number"
}
}
}
}
```

- Edit the OmniGraph Python source code file (`OgnCustomPythonRos2NodePy.py` located in the `custom.python.ros2_node/custom/python/ros2_node/ogn/python/nodes` folder) with the following content.
The code is self-commented enough. Basically, the `OgnCustomPythonRos2NodePyInternalState` class handles the communication with ROS. It creates the ROS 2 node, the subscription and handles the received messages. On the other hand, the `OgnCustomPythonRos2NodePy` class implements the custom OmniGraph node. It computes and sets the outputs according to the input values and the internal state.

```
import rclpy
import std_msgs.msg

import omni.graph.core
from isaacsim.core.nodes import BaseResetNode

from custom.python.ros2_node.ogn.OgnCustomPythonRos2NodePyDatabase import OgnCustomPythonRos2NodePyDatabase

class OgnCustomPythonRos2NodePyInternalState(BaseResetNode):
"""Convenience class for maintaining per-node state information.

It inherits from ``BaseResetNode`` to do custom reset operation when the timeline is stopped."""

def __init__(self):
"""Instantiate the per-node state information"""
self._data = None
self._ros2_node = None
self._subscription = None
# call parent class to set up timeline event for custom reset
super().__init__(initialize=False)

@property
def data(self):
"""Get received data, and clean it after reading"""
tmp = self._data
self._data = None
return tmp

def _callback(self, msg):
"""Function that is called when a message is received by the subscription."""
self._data = msg.data

def initialize(self, node_name, topic_name):
"""Intitialize ROS 2 node and subscription."""
try:
rclpy.init()
except:
pass
# create ROS 2 node
if not self._ros2_node:
self._ros2_node = rclpy.create_node(node_name=node_name)
# create ROS 2 subscription
if not self._subscription:
self._subscription = self._ros2_node.create_subscription(
msg_type=std_msgs.msg.Int32, topic=topic_name, callback=self._callback, qos_profile=10
)
self.initialized = True

def spin_once(self, timeout_sec=0.01):
"""Do ROS 2 work to take an incoming message from the topic, if any."""
rclpy.spin_once(self._ros2_node, timeout_sec=timeout_sec)

def custom_reset(self):
"""On timeline stop, destroy ROS 2 subscription and node."""
if self._ros2_node:
self._ros2_node.destroy_subscription(self._subscription)
self._ros2_node.destroy_node()

self._data = None
self._ros2_node = None
self._subscription = None
self.initialized = False

rclpy.try_shutdown()

class OgnCustomPythonRos2NodePy:
"""The OmniGraph node class"""

@staticmethod
def fibonacci(n):
"""Compute the Fibonacci sequence value for the given number iteratively"""
if n <= 0:
return 0
elif n == 1:
return 1
a, b = 0, 1
for _ in range(2, n + 1):
a, b = b, a + b
return b

@staticmethod
def internal_state():
"""Get per-node state information."""
return OgnCustomPythonRos2NodePyInternalState()

@staticmethod
def compute(db) -> bool:
"""Compute the output based on inputs and internal state."""
state = db.per_instance_state

try:
# check if state (ROS 2 node and subscriber is initialized)
if not state.initialized:
state.initialize(node_name="custom_python_ros2_node", topic_name=db.inputs.topic)
# spin state to take incoming messages
state.spin_once()

# cache incomming data
number = state.data
if number is not None:
# compute the Fibonacci sequence value for the given number
value = OgnCustomPythonRos2NodePy.fibonacci(number)
# check for uint64 overflow
if value > 2**64:
db.log_warn(f"Fibonacci number {number} exceeds uint64's storage capacity")
return False
# output value and trigger output execution
db.outputs.fibonacci = value
db.outputs.execOut = omni.graph.core.ExecutionAttributeState.ENABLED
except Exception as e:
db.log_error(f"Computation error: {e}")
return False
return True

@staticmethod
def release(node):
"""Release per-node state information."""
try:
state = OgnCustomPythonRos2NodePyDatabase.per_instance_internal_state(node)
except Exception as e:
return
# reset state
state.reset()
state.initialized = False
```

## Running the Custom OmniGraph Node
Warning
The custom extension must first be activated for the OmniGraph node to be available.
Open the extension manager using the Window > Extensions menu and search for the `custom.python.ros2_node` extension to enable it.

- In a new stage, go to Window > Graph Editors > Action Graph to create an Action Graph and add, connect and configure the following OmniGraph nodes into the Action Graph:

- On Playback Tick node to execute other graph nodes every simulation frame.

- Custom Python ROS 2 Node custom node.

- To String node to convert the output of our custom node to a string.

- Print Text node to display the output of our custom node (as string) to the viewport or terminal. Edit this node’s properties, in the Property panel, and check the To Screen attribute to display the text in the viewport.

- Play the simulation

- In a new ROS 2-sourced terminal, run the next command to publish a number to the `/number` topic.

```
ros2 topic pub -1 /number std_msgs/msg/Int32 "{data: 10}"
```

- After messages are being received from the topic, the Fibonacci number will appear in the top-left corner of the viewport. If no new values are received, the display will fade over time.
Note
To view the values in the Isaac Sim console, you can edit the Print Text node properties and uncheck the To Screen attribute and set the Log Level attribute to Warning.

- Publish different number using previous ROS 2 topic command and notice the change in Isaac Sim.

## Summary
This tutorial covered the following topics:

- Creating a custom OmniGraph Python node in an extension.

- Using rclpy interface to create a ROS 2 node within a custom OmniGraph node to subscribe to a topic, perform the Fibonacci computation and trigger downstream nodes when the computed OmniGraph output is ready.

### Next Steps
Continue on to the next tutorial in our ROS2 Tutorials series, ROS 2 Custom C++ OmniGraph Node .
