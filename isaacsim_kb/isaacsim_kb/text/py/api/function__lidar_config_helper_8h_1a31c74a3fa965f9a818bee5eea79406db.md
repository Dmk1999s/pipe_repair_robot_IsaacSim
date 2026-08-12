<!-- source: py/api/function__lidar_config_helper_8h_1a31c74a3fa965f9a818bee5eea79406db.html | title: getTransformFromSensorPose — Isaac Sim -->

# getTransformFromSensorPose
Fully qualified name: `isaacsim::sensors::rtx::getTransformFromSensorPose`
voidisaacsim ::sensors ::rtx ::getTransformFromSensorPose(
constomni ::sensors::FrameAtTime&inPose,
omni ::math::linalg::matrix4d&matrixOutput,
)
Converts a sensor pose to a 4x4 transformation matrix.
This function takes a sensor pose containing position and orientation data and converts it into a 4x4 transformation matrix. The position is extracted from the pose and set as the translation component, while the orientation quaternion is used to set the rotation component.
The function handles the quaternion component ordering conversion from the input format (i,j,k,w) to the quaternion constructor format (w,i,j,k).
Note
The input orientation quaternion is ordered as (i,j,k,w) but the quatd constructor expects (w,i,j,k) ordering, so the components are reordered during construction
Note
The matrixOutput is first set to identity before applying rotation and translation
Parameters:

- inPose – [in] The sensor pose containing position and orientation data

- matrixOutput – [out] The output 4x4 transformation matrix
