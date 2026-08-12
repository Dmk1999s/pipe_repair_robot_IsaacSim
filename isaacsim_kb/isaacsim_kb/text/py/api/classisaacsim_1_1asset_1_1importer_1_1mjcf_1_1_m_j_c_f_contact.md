<!-- source: py/api/classisaacsim_1_1asset_1_1importer_1_1mjcf_1_1_m_j_c_f_contact.html | title: MJCFContact — Isaac Sim -->

# MJCFContact
Fully qualified name: `isaacsim::asset::importer::mjcf::MJCFContact`
classMJCFContact

Contact definition for collision filtering and contact parameters.
Defines contact behavior between pairs of geometries or bodies, including collision inclusion/exclusion rules and contact constraint parameters. Used to customize collision detection and contact dynamics.
Public Types
enumType

Enumeration of contact types for collision filtering.
Values:
enumeratorPAIR

Include contact between specified geometries/bodies.

enumeratorEXCLUDE

Exclude contact between specified geometries/bodies.

enumeratorDEFAULT

Default contact behavior when not explicitly specified.

Public Functions
inlineMJCFContact()

Public Members
Type type

Type of contact definition (pair, exclude, or default).

std ::stringname

Name identifier for the contact definition.

std ::stringgeom1

Name of the first geometry in the contact pair.

std ::stringgeom2

Name of the second geometry in the contact pair.

intcondim

Number of contact constraint dimensions.

std ::stringbody1

Name of the first body in the contact pair.

std ::stringbody2

Name of the second body in the contact pair.
