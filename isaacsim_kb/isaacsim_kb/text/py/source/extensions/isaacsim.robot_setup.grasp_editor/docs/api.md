<!-- source: py/source/extensions/isaacsim.robot_setup.grasp_editor/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

[TABLE]
import_grasps_from_file | Parse an isaac_grasp YAML file for use in Isaac Sim.
GraspSpec |
[/TABLE]

import_grasps_from_file(
file_path:str,
)→GraspSpec Parse an isaac_grasp YAML file for use in Isaac Sim. The resulting GraspSpec class will allow you to look up the data for each grasp by its name.
Parameters:
file_path (str) – A path to an isaac_grasp YAML file with format version 1.0.

Returns:
A data class that stores the information needed to replicate a grasp in Isaac Sim. This class also includes convenience functions to compute the desired pose of the gripper frame as a function of the of object position, or to compute the desired object position as a function of gripper pose.

Return type:
GraspSpec

classGraspSpec(imported_data:dict)
Bases: `object`
compute_gripper_pose_from_rigid_body_pose(
grasp_name:str,
rb_trans:array,
rb_quat:array,
)→Tuple[array,array]Given a position of the rigid body in the world or robot frame, compute the position of the gripper in that same frame to replicate the grasp associated grasp_name.
Parameters:

- grasp_name (str) – Name of an imported grasp.

- rb_trans (np.array) – Translation of the rigid body in the desired frame of reference.

- rb_quat (np.array) – Quaternion orientation of the rigid body in the desired frame of reference.

Returns:
Translation and orientation of the gripper in the desired frame of reference.

Return type:
Tuple[np.array, np.array]

compute_rigid_body_pose_from_gripper_pose(
grasp_name:str,
gripper_trans:array,
gripper_quat:array,
)→Tuple[array,array]Given a position of the gripper in the world or robot frame, compute the position of the rigid body in that same frame to replicate the grasp associated grasp_name.
Parameters:

- grasp_name (str) – Name of an imported grasp.

- gripper_trans (np.array) – Translation of the gripper in the desired frame of reference.

- gripper_quat (np.array) – Quaternion orientation of the gripper in the desired frame of reference.

Returns:
Translation and orientation of the rigid body in the desired frame of reference.

Return type:
Tuple[np.array, np.array]

get_grasp_dict_by_name(name:str)→dict
Get a dictionary of all data associated with a specific grasp name.
Parameters:
name (str) – Valid grasp name.

Returns:
Dictionary containing the data associated with this grasp. This includes
confidence (float):
A confidence value between 0.0 and 1.0 indicating the quality of this grasp.

position (np.array):
Translation of the gripper frame relative to the rigid body frame.

orientation (dict):
Dictionary with w and xyz components that define the orientation of the gripper frame relative to the rigid body frame.

cspace_position (dict):
A dictionary mapping each DOF that is considered to be part of the gripper to the position it was in when grasping this object.

pregrasp_cspace_position (dict):
A dictionary mapping each DOF that is considered to be part of the gripper to its open position. I.e. a grasp of this object can be acheived by moving from the pregrasp_cspace_position to cspace_position while the gripper is at the relative pose specified by position and orientation.

Return type:
dict

get_grasp_dicts()→dict
Get a dictionary of dictionaries that specify each grasp in the imported file. The get_grasp_dict_by_name() function describes the content of each inner dictionary, and the get_grasp_names() function provides the keys to this dictionary.
Returns:
A dictionary of dictionaries that define each grasp in the imported file.

Return type:
dict

get_grasp_names()→List[str]
Get a list of valid grasp names stored in the imported isaac_grasp file.
Returns:
List of valid grasp names.

Return type:
List[str]
