<!-- source: py/api/structisaacsim_1_1sensors_1_1physics_1_1_cs_raw_data.html | title: CsRawData — Isaac Sim -->

# CsRawData
Fully qualified name: `isaacsim::sensors::physics::CsRawData`
structCsRawData

Raw contact data from the physics simulation.
Public Members
floattime={0.0f}

Simulation timestamp.

floatdt={0.0f}

Simulation time step for the impulse.

uint64_tbody0

First body involved in the contact.

uint64_tbody1

Second body involved in the contact.

carb::Float3position={0.0f,0.0f,0.0f}

Contact position in world coordinates.

carb::Float3normal={0.0f,0.0f,0.0f}

Contact normal in world coordinates.

carb::Float3impulse={0.0f,0.0f,0.0f}

Contact impulse in world coordinates.
