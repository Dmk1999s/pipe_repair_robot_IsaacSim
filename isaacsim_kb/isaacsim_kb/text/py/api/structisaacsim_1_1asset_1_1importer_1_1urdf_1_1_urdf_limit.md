<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_limit.html | title: UrdfLimit — Isaac Sim -->

# UrdfLimit
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfLimit`
structUrdfLimit

Joint motion limits for URDF joints.
Defines the allowable range of motion, maximum effort, and maximum velocity for joints. Used to constrain joint motion in simulation.
Public Members
floatlower=-FLT_MAX

Lower joint limit (radians for revolute, meters for prismatic).

floatupper=FLT_MAX

Upper joint limit (radians for revolute, meters for prismatic).

floateffort=FLT_MAX

Maximum joint effort (force or torque).

floatvelocity=FLT_MAX

Maximum joint velocity.
