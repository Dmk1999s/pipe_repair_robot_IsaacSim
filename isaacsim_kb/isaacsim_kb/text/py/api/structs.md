<!-- source: py/api/structs.html | title: Structs — Isaac Sim -->

# Structs
Bounds
Axis-aligned bounding box representation using lower and upper corner points.

Material
OBJ-style material definition with PBR properties.

MaterialAssignment
Defines which triangles and indices use a specific material.

Matrix22
2x2 matrix representation with column-major storage.

Matrix33
3x3 matrix representation with column-major storage.

Mesh
Core mesh data structure with geometry and material information.

TextureData
Container for texture image data and metadata.

Transform
3D transformation represented by position and rotation.

USDMesh
USD-compatible mesh data structure.

UVInfo
UV texture coordinate information for mesh surfaces.

isaacsim::asset::gen::conveyor::IOmniIsaacConveyor
Interface for the OmniIsaacConveyor plugin.

isaacsim::asset::gen::omap::OccupancyMap
Interface for occupancy map generation.

isaacsim::asset::importer::mjcf::ContactNode
A node in the contact graph representing collision relationships.

isaacsim::asset::importer::mjcf::ImportConfig
Configuration settings for importing MJCF files.

isaacsim::asset::importer::mjcf::MJCFEqualityConnect
Equality constraint that connects two bodies at a fixed relative position.

isaacsim::asset::importer::mjcf::MeshInfo
Information about a mesh used in the MJCF model.

isaacsim::asset::importer::mjcf::Mjcf
Interface for MJCF file import functionality.

isaacsim::asset::importer::urdf::ImportConfig
Configuration parameters for URDF import operations.

isaacsim::asset::importer::urdf::Urdf
Interface for URDF parsing and import operations.

isaacsim::asset::importer::urdf::UrdfAxis
Joint axis definition for URDF joints.

isaacsim::asset::importer::urdf::UrdfCamera
Camera sensor configuration extending base sensor.

isaacsim::asset::importer::urdf::UrdfCollision
Collision element definition for URDF links.

isaacsim::asset::importer::urdf::UrdfColor
RGBA color specification for URDF materials.

isaacsim::asset::importer::urdf::UrdfContact
Contact sensor configuration.

isaacsim::asset::importer::urdf::UrdfDynamics
Joint dynamics properties for URDF joints.

isaacsim::asset::importer::urdf::UrdfForce
Force sensor configuration.

isaacsim::asset::importer::urdf::UrdfGeometry
Geometric shape definition for URDF visual and collision elements.

isaacsim::asset::importer::urdf::UrdfGps
GPS sensor configuration.

isaacsim::asset::importer::urdf::UrdfImu
Inertial measurement unit sensor configuration.

isaacsim::asset::importer::urdf::UrdfInertia
Inertia tensor components for a rigid body.

isaacsim::asset::importer::urdf::UrdfInertial
Inertial properties of a URDF link.

isaacsim::asset::importer::urdf::UrdfJoint
Joint definition connecting two links in URDF robot model.

isaacsim::asset::importer::urdf::UrdfJointDrive
Joint drive configuration for actuated joints.

isaacsim::asset::importer::urdf::UrdfJointMimic
Joint mimic configuration for coupled joint motion.

isaacsim::asset::importer::urdf::UrdfLimit
Joint motion limits for URDF joints.

isaacsim::asset::importer::urdf::UrdfLink
Link definition in URDF robot model.

isaacsim::asset::importer::urdf::UrdfLoopJoint
Loop joint definition for closed kinematic chains.

isaacsim::asset::importer::urdf::UrdfMagnetometer
Magnetometer sensor configuration.

isaacsim::asset::importer::urdf::UrdfMaterial
Material definition for URDF visual elements.

isaacsim::asset::importer::urdf::UrdfNoise
Noise characteristics for sensor measurements.

isaacsim::asset::importer::urdf::UrdfRay
Ray-based sensor configuration for lidar/laser scanners.

isaacsim::asset::importer::urdf::UrdfRayDim
Ray dimension configuration for lidar sensors.

isaacsim::asset::importer::urdf::UrdfRfid
RFID reader sensor configuration.

isaacsim::asset::importer::urdf::UrdfRfidTag
RFID tag sensor configuration.

isaacsim::asset::importer::urdf::UrdfRobot
Complete URDF robot model definition.

isaacsim::asset::importer::urdf::UrdfSensor
Base sensor definition for URDF sensors.

isaacsim::asset::importer::urdf::UrdfSonar
Sonar sensor configuration.

isaacsim::asset::importer::urdf::UrdfVisual
Visual element definition for URDF links.

isaacsim::core::simulation_manager::ISimulationManager
Interface for managing simulation state and callbacks.

isaacsim::robot::schema::custom::hash
Hash function object for enum types.

isaacsim::robot::surface_gripper::PhysxAction
Queued PhysX action to be executed serially by the manager.

isaacsim::robot::surface_gripper::SurfaceGripperInterface
Interface for controlling surface gripper functionality.

isaacsim::robot::surface_gripper::UsdAction
Queued USD action to be executed serially by the manager.

isaacsim::robot::wheeled_robots::IWheeledRobots
Interface for wheeled robot control functionality.

isaacsim::ros2::bridge::DynamicMessageField
Structure that encapsulates a dynamic message field.

isaacsim::ros2::bridge::Ros2QoSProfile
ROS 2 QoS Profile configuration.

isaacsim::ros2::bridge::Ros2QoSTime
ROS 2 QoS time representation.

isaacsim::ros2::bridge::TfTransformStamped
Structure that encapsulates geometry_msgs/msg/TransformStamped data.

isaacsim::sensors::physics::ContactPair
Represents a pair of bodies in contact.

isaacsim::sensors::physics::CsProperties
Properties configuration for a contact sensor.

isaacsim::sensors::physics::CsRawData
Raw contact data from the physics simulation.

isaacsim::sensors::physics::CsReading
Contact sensor reading data structure.

isaacsim::sensors::physics::IsProperties
Properties configuration for an IMU sensor.

isaacsim::sensors::physics::IsRawData
Raw IMU data from the physics simulation.

isaacsim::sensors::physics::IsReading
IMU sensor reading data structure.

isaacsim::sensors::rtx::IIsaacSimSensorsRtx
Minimal interface.

omni::isaac::dynamic_control::DcArticulation
Represents an articulation in the physics simulation.

omni::isaac::dynamic_control::DcArticulationProperties
Properties of an articulation.

omni::isaac::dynamic_control::DcAttractor
Represents an attractor in the physics simulation.

omni::isaac::dynamic_control::DcAttractorProperties
Properties to set up a pose attractor.

omni::isaac::dynamic_control::DcD6Joint
Represents a D6 joint in the physics simulation.

omni::isaac::dynamic_control::DcD6JointProperties
Properties to set up a D6 Joint.

omni::isaac::dynamic_control::DcDof
Represents a degree of freedom in the physics simulation.

omni::isaac::dynamic_control::DcDofProperties
Properties of a degree-of-freedom.

omni::isaac::dynamic_control::DcDofState
State of a degree of freedom.

omni::isaac::dynamic_control::DcJoint
Represents a joint in the physics simulation.

omni::isaac::dynamic_control::DcRayCastResult
Result of a Raycast.

omni::isaac::dynamic_control::DcRigidBody
Represents a rigid body in the physics simulation.

omni::isaac::dynamic_control::DcRigidBodyProperties
Properties of a rigid body.

omni::isaac::dynamic_control::DcRigidBodyState
State of a rigid body.

omni::isaac::dynamic_control::DcShape
Shape descriptor for tensors.

omni::isaac::dynamic_control::DcTransform
Transform .

omni::isaac::dynamic_control::DcVelocity
Velocity.

omni::isaac::dynamic_control::DynamicControl
Interface for controlling physics objects in Isaac Sim.

omni::kit::IRunLoopRunnerImpl
Interface for controlling the run loop execution.
