<!-- source: manipulators/concepts/lula_rrt.html | title: Lula RRT — Isaac Sim Documentation -->

# Lula RRT
We provide a Lula implementation of the classic Randomly-Exploring Random Tree (RRT) algorithm to fulfill the PathPlanner interface. Specifically, the c-space RRT is using RRT-Connect based on [ 2 ] , and the task-space RRT is using Jacobian transpose RRT based on [ 3 ] . The RRT implementation does not support orientation targets.

## Lula RRT Configuration
Three files are necessary to configure Lula RRT for use with a new robot:

- A URDF (universal robot description file), used for specifying robot kinematics as well as joint and link names. Position limits for each joint are also required. Other properties in the URDF are ignored and can be omitted; these include masses, moments of inertia, visual and collision meshes.

- A supplemental robot description file in YAML format. In addition to enumerating the list of actuated joints that define the configuration space (c-space) for the robot, this file also includes sections for specifying the default c-space configuration. This file can also be used to specify fixed positions for unactuated joints.

- A configuration file in the YAML format specifying parameters for the RRT algorithm such as termination conditions, exploration weights, and step size. These parameters can be modified programmatically with the RRT.set_param() function.

## References
[2 ]J. J. Kuffner and S. M. LaValle, “RRT-connect: An efficient approach to single-query path planning,” Proceedings 2000 ICRA. Millennium Conference. IEEE International Conference on Robotics and Automation. Symposia Proceedings (Cat. No.00CH37065), 2000, pp. 995-1001 vol.2, doi: 10.1109/ROBOT.2000.844730.
[3 ]M. Vande Weghe, D. Ferguson and S. S. Srinivasa, “Randomized path planning for redundant manipulators without inverse kinematics,” 2007 7th IEEE-RAS International Conference on Humanoid Robots, 2007, pp. 477-482, doi: 10.1109/ICHR.2007.4813913.
