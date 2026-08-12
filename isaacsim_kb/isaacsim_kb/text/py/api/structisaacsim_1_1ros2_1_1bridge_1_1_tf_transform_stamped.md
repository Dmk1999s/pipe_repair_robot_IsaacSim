<!-- source: py/api/structisaacsim_1_1ros2_1_1bridge_1_1_tf_transform_stamped.html | title: TfTransformStamped — Isaac Sim -->

# TfTransformStamped
Fully qualified name: `isaacsim::ros2::bridge::TfTransformStamped`
structTfTransformStamped

Structure that encapsulates geometry_msgs/msg/TransformStamped data.
Provides a container for transform data between coordinate frames, including timestamp, frame IDs, translation, and rotation components.
Public Members
doubletimeStamp

Time in seconds.

std ::stringparentFrame

Transform frame with which this data is associated.

std ::stringchildFrame

Frame ID of the child frame to which this transform points.

doubletranslationX

Translation of child frame from parent frame (x-axis) in meters.

doubletranslationY

Translation of child frame from parent frame (y-axis) in meters.

doubletranslationZ

Translation of child frame from parent frame (z-axis) in meters.

doublerotationX

Rotation of child frame from parent frame (quaternion x-component).

doublerotationY

Rotation of child frame from parent frame (quaternion y-component).

doublerotationZ

Rotation of child frame from parent frame (quaternion z-component).

doublerotationW

Rotation of child frame from parent frame (quaternion w-component).
