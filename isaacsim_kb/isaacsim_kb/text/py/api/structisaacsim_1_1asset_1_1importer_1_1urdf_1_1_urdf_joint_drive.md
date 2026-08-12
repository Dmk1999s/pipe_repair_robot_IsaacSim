<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_joint_drive.html | title: UrdfJointDrive — Isaac Sim -->

# UrdfJointDrive
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfJointDrive`
structUrdfJointDrive

Joint drive configuration for actuated joints.
Defines the control parameters for joint actuation including target values, control gains, and drive characteristics. Used for position and velocity control of joints in simulation.
Public Members
floattarget=0.0

Target value for joint control (position or velocity).

floatstrength=0.0f

Control strength/gain for the joint drive.

floatdamping=0.0f

Damping coefficient for the joint drive.

UrdfJointTargetType targetType=UrdfJointTargetType ::POSITION

Type of target control (position or velocity).

UrdfJointDriveType driveType=UrdfJointDriveType ::ACCELERATION

Type of drive actuation (acceleration or force).

floatnaturalFrequency=25.0f

Natural frequency for control system tuning.
Default is 25Hz for stable simulation at 60Hz timestep.

floatdampingRatio=0.005f

Damping ratio for control system tuning.
Low damping allows oscillation but ensures settling.
