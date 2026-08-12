<!-- source: py/api/classisaacsim_1_1ros2_1_1tf__viewer_1_1_tf2_factory.html | title: Tf2Factory — Isaac Sim -->

# Tf2Factory
Fully qualified name: `isaacsim::ros2::tf_viewer::Tf2Factory`
classTf2Factory

Base class for creating ROS 2 tf2 related functions/objects according to the sourced ROS 2 distribution.
This abstract factory class provides an interface for creating tf2 related objects that are compatible with the currently loaded ROS 2 distribution.
Subclassed by isaacsim::ros2::tf_viewer::Tf2FactoryImpl
Public Functions
virtual~Tf2Factory()=default

Virtual destructor with default implementation.

virtualstd ::shared_ptr<Ros2BufferCore >createBuffer()=0

Creates a ROS 2 tf2 `BufferCore`.
Factory method to instantiate a new buffer appropriate for the ROS 2 distribution.
Returns:
Pointer to the newly created buffer.
