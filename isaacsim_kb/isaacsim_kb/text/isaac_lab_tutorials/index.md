<!-- source: isaac_lab_tutorials/index.html | title: Isaac Lab — Isaac Sim Documentation -->

# Isaac Lab

## Overview
Isaac Lab is the official robot learning framework for Isaac Sim, providing APIs and examples for reinforcement learning, imitation learning, and more. The framework provides the ability to design tasks in different workflows, including a modular design to easily and efficiently create robot learning environments, while leveraging the latest simulation capabilities.
Some of its core features include:

- Modular configuration-driven system to easily create and modify environments

- Flexible user-designed workflow for optimized performance

- Suite of robot learning environments for training and evaluation

- Support for different reinforcement learning and imitation learning libraries

- Connection to peripheral devices, such as game-pads and keyboards, for collecting demonstrations

- Ability to augment simulation with custom actuator models for sim-to-real transfer

## Isaac Lab Resources
For more information and documentation for Isaac Lab, see the following external references:

- Isaac Lab Repository

- Isaac Lab Documentation

## Suggested Isaac Sim Tutorials
The following set of tutorials details usage of reinforcement learning related components in Isaac Sim.
Robot Setup

- Importing URDF

- Importing MJCF

- Simulation Fundamentals

Deploying Policies

- Rigging a Legged Robot for Policy Inference

- Policy Deployment

- Policy Deployment in ROS 2

Data Generation

- Getting Started with Cloner

- Instanceable Assets

Python Scripting

- Python Scripting

## Troubleshooting
Common Isaac Lab issues and their solutions are documented in the Isaac Lab Troubleshooting page. For general simulation troubleshooting, see Troubleshooting .

## Deprecated Frameworks
Isaac Lab will be replacing previously released frameworks for robot learning and reinforcement learning, including IsaacGymEnvs for the Isaac Gym Preview Release , OmniIsaacGymEnvs for Isaac Sim, and Orbit for Isaac Sim.
These frameworks are now deprecated in favor of continuing development in Isaac Lab. We encourage users of these frameworks to migrate your work over to Isaac Lab. Migration guides are available to support the migration process:

- Migrating from IsaacGymEnvs and Isaac Gym Preview Release: link

- Migrating from OmniIsaacGymEnvs: link

- Migrating from Orbit: link
