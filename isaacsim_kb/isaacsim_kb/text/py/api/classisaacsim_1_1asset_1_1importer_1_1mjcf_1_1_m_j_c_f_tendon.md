<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_tendon.html | title: MJCFTendon — Isaac Sim -->

# MJCFTendon
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFTendon`

## Structs
FixedJoint
Fixed joint connection for fixed tendons.

SpatialAttachment
Spatial attachment point for spatial tendons.

SpatialPulley
Pulley mechanism for spatial tendons.

classMJCFTendon

Tendon element for creating cable-like constraints between bodies.
Tendons are flexible constraints that can span multiple bodies and joints, creating cable-like connections. They can be either fixed (connecting specific joints) or spatial (following geometric paths through attachments and pulleys).
Public Types
enumType

Enumeration of tendon types.
Values:
enumeratorSPATIAL

Spatial tendon that follows geometric paths.

enumeratorFIXED

Fixed tendon that connects specific joints.

enumeratorDEFAULT

Default tendon type when not specified.

Public Functions
inlineMJCFTendon()

inline~MJCFTendon()

Public Members
Type type

Type of tendon (spatial, fixed, or default).

std ::stringname

Name identifier for the tendon.

boollimited

Whether the tendon has length limits.

Vec2 range

Length limits [min, max] for the tendon.

Vec3 solimplimit

Constraint solver impedance parameters for limits.

Vec2 solreflimit

Constraint solver reference parameters for limits.

Vec3 solimpfriction

Constraint solver impedance parameters for friction.

Vec2 solreffriction

Constraint solver reference parameters for friction.

floatmargin

Contact margin for tendon interactions.

floatfrictionloss

Friction loss coefficient.

floatwidth

Visual width of the tendon for rendering.

std ::stringmaterial

Name of the material for tendon visualization.

Vec4 rgba

RGBA color for tendon visualization.

floatspringlength

Natural length of the tendon spring.

floatstiffness

Spring stiffness coefficient.

floatdamping

Damping coefficient for the tendon.

std ::vector<FixedJoint *>fixedJoints

Collection of fixed joint connections for fixed tendons.

std ::vector<SpatialAttachment *>spatialAttachments

Collection of spatial attachment points for spatial tendons.

std ::vector<SpatialPulley *>spatialPulleys

Collection of spatial pulleys for spatial tendons.

std ::map<int,std ::vector<SpatialAttachment *>>spatialBranches

Spatial attachments organized by branch identifier.

structFixedJoint

Fixed joint connection for fixed tendons.
Public Members
std ::stringjoint

Name of the joint connected to the tendon.

floatcoef

Coupling coefficient for the joint connection.

structSpatialAttachment

Spatial attachment point for spatial tendons.
Public Types
enumType

Type of attachment point.
Values:
enumeratorGEOM

Attachment to a geometry element.

enumeratorSITE

Attachment to a site element.

Public Members
std ::stringgeom

Name of the geometry for geom-type attachments.

std ::stringsidesite=""

Name of the side site for spatial routing.

std ::stringsite

Name of the site for site-type attachments.

Type type

Type of this attachment (geom or site).

intbranch

Branch identifier for multi-branch tendons.

structSpatialPulley

Pulley mechanism for spatial tendons.
Public Members
floatdivisor=0.0

Pulley gear ratio divisor.

intbranch

Branch identifier for the pulley.
