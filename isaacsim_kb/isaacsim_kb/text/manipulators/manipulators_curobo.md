<!-- source: manipulators/manipulators_curobo.html | title: cuRobo and cuMotion — Isaac Sim Documentation -->

# cuRobo and cuMotion
Note
There are known issues with using NvBlox examples within cuRobo. This tutorial will be updated when cuRobo is updated to resolve these issues.
Note
This cuRobo tutorial is not supported on aarch64 platforms.

## Learning Objectives
cuRobo (also on GitHub ) is a high-performance, GPU-accelerated robotics motion generation library for robot manipulators, developed by NVIDIA Research. It is a standalone Python library that interfaces directly with NVIDIA Isaac Sim, simplifying both testing in simulation and deploying on physical robots.
NVIDIA cuMotion , available as a Developer Preview in Isaac 3.0, is a production motion generation package for manipulators. The current version leverages cuRobo as its backend, providing collision-free motion planning using a plugin for MoveIt 2 and a set of supporting ROS 2 packages. For an example of using cuMotion with NVIDIA Isaac Sim using the ROS 2 bridge, see the relevant section of the Isaac ROS documentation. This example is somewhat limited in Isaac 3.0 but will be expanded in a future release.
In the remainder of this tutorial, we focus on direct integration of cuRobo into NVIDIA Isaac Sim, covering cuRobo installation and use, with examples for collision-free inverse kinematics, motion planning, and reactive control (MPPI).
[image: ../_images/isaac_tutorial_advanced_cuRobo.gif]

## Getting Started
Prerequisites

- Complete the Adding a Manipulator Robot tutorial prior to beginning this tutorial.

## Installation
Follow the cuRobo installation instructions for installing cuRobo and required libraries. cuRobo supports NVIDIA Isaac Sim 2022.2.1 and later. Follow the workstation installation instructions to install NVIDIA Isaac Sim.

## Examples

### Using Isaac Sim with cuRobo
In the cuRobo documentation, refer to the “Using Isaac Sim” section for an overview of how cuRobo is interfaced to Isaac Sim, along with a series of standalone examples demonstrating collision checking, motion generation, inverse kinematics, model-predictive control, and multi-arm reaching.

### Using Isaac Sim with cuRobo and nvblox
In the cuRobo documentation, refer to the “Using with Depth Camera” section for examples of obstacle-aware motion generation in NVIDIA Isaac Sim, both with pre-generated signed distance fields (SDFs) from nvblox and with online mapping leveraging nvblox with a physical RealSense depth camera.
