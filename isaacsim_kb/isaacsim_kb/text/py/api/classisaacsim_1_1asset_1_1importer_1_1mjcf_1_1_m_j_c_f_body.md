<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_body.html | title: MJCFBody — Isaac Sim -->

# MJCFBody
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFBody`
classMJCFBody

Represents a rigid body in the MJCF model hierarchy.
A body is the fundamental element in the kinematic tree that can contain geometry for collision/visualization, joints for articulation, sites for sensors, and child bodies for hierarchical structure. Bodies have inertial properties and spatial positioning within their parent’s coordinate frame.
Public Functions
inlineMJCFBody()

inline~MJCFBody()

Public Members
std ::stringname

Name identifier for the body.

Vec3 pos

Position offset relative to the parent body frame.

Quat quat

Quaternion orientation relative to the parent body frame.

Vec3 zaxis

Z-axis direction for orientation specification.

MJCFInertial *inertial

Pointer to inertial properties of this body.

std ::vector<MJCFGeom *>geoms

Collection of geometry elements attached to this body.

std ::vector<MJCFJoint *>joints

Collection of joints that connect this body to its children.

std ::vector<MJCFBody *>bodies

Collection of child bodies in the kinematic hierarchy.

std ::vector<MJCFSite *>sites

Collection of sites (reference points) attached to this body.

boolhasVisual

Whether this body has visual elements for rendering.
