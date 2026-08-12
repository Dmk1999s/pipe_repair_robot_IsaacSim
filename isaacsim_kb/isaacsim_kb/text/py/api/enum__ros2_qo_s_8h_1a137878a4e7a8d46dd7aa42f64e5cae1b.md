<!-- source: py/api/enum__ros2_qo_s_8h_1a137878a4e7a8d46dd7aa42f64e5cae1b.html | title: Ros2QoSLivelinessPolicy — Isaac Sim -->

# Ros2QoSLivelinessPolicy
Fully qualified name: `isaacsim::ros2::bridge::Ros2QoSLivelinessPolicy`
enumclassisaacsim ::ros2 ::bridge ::Ros2QoSLivelinessPolicy

Enumerations of ROS 2 QoS Liveliness policy.
Defines the liveliness policy options for ROS 2 QoS settings, determining how the system monitors the presence of entities.
See also
ROS 2 QoS policies
Values:
enumeratoreSystemDefault

Use the system default liveliness setting.

enumeratoreAutomatic

System automatically monitors liveliness.

enumeratoreManualByNode

Node must manually assert liveliness (Deprecated)

enumeratoreManualByTopic

Publisher must manually assert liveliness.

enumeratoreUnknown

Unknown or invalid liveliness policy.
