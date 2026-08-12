<!-- source: physics/index.html | title: Physics — Isaac Sim Documentation -->

# Physics
On a high-level, simulations with Omniverse™ Physics work as follows:

- The USD Physics schema of robot and environment assets are parsed and corresponding objects are created in the PhysX SDK backend.

- Then, for each discrete-time step of the simulation, Physics advances the PhysX SDK objects given their current state and additional inputs such as, for example, control-policy torques.

- The updated state is written back to USD by default, where the state can be further processed by the user, a reinforcement-learning policy, or other extensions such as the Omniverse RTX Renderer.

- Omniverse™ Physics propagates runtime changes to physics parameters in USD to the PhysX SDK objects.

## Tools

## Additional Resources

- Omniverse™ Physics core documentation and programming guide

- USD Physics Schemas and PhysX SDK-engine-specific Physx Schemas

- Explore further Omniverse simulation extensions .

- PhysX SDK

- Omniverse Visual Debugger

- Flow: Fluid Dynamics

- NVIDIA Warp
