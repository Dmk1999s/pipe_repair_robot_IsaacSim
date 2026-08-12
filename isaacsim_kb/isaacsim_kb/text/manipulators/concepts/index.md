<!-- source: manipulators/concepts/index.html | title: Motion Generation — Isaac Sim Documentation -->

# Motion Generation
The Motion Generation provides an API that you can use to control objects within Isaac Sim. The API is made up of abstract interfaces for adding motion control algorithms to Isaac Sim. The interfaces in the Motion Generation provide two basic utilities:

- Simplify the integration of new robotics algorithms into NVIDIA Isaac Sim.

- Provide a standard structure with which to compare similar robotics algorithms.

For example, if you have a robot that has not previously been described to Isaac Sim, you can use these APIs to define that robot and how it moves.

- Simplify the integration of new robotics algorithms into NVIDIA Isaac Sim.

- Provide a standard structure with which to compare similar robotics algorithms.

For example, if you have a robot that has not previously been described to Isaac Sim, you can use these APIs to define that robot and how it moves.
Three interfaces are provided in the Motion Generation Extension:

- Motion Policy Algorithm

- Path Planner

- Kinematics Solvers

In Isaac Sim, the robot is specified using a USD file that gets added to the stage. However, we expect that robotics algorithms will have their own way of specifying the robot’s kinematic structure and custom parameters. To avoid interfering with any particular robot description format, the interfaces in the Motion Generation Extension include functions that facilitate the translation between the USD robot and a specific algorithm. Specifically, an algorithm can specify which joints in the robot it cares about, and the order in which it expects those joints to be listed. The helper classes provided in this extension, Articulation Motion Policy , Path Planner Visualizer , and Articulation Kinematics Solver , use the interface functions to appropriately map robot joint states between the USD robot articulation and an interface implementation.
In Isaac Sim, we use the word Articulation to refer to the simulated robot represented through USD. The word “Articulation” is used as a prefix in the Motion Generation Extension to indicate utility classes that handle interfacing an algorithm with the simulated robot.
In addition, the Motion Generation extension includes a handful of special-purpose controllers that do not leverage MotionPolicy or PathPlanner.

## References
