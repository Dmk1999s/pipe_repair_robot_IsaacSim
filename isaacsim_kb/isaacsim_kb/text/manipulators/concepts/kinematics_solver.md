<!-- source: manipulators/concepts/kinematics_solver.html | title: Kinematics Solvers — Isaac Sim Documentation -->

# Kinematics Solvers
Like a Motion Policy Algorithm , a Kinematics Solvers is an interface class with a single provided implementation. A KinematicsSolver is able to compute forward and inverse kinematics. A single implementation is provided using the NVIDIA-developed Lula library. (see Lula Kinematics Solver )
includes:

- Kinematics Solver

- Articulation Kinematics Solver

- Lula Kinematics Solver

## Kinematics Solver
The KinematicsSolver interface specifies functions for computing both forward and inverse kinematics at any available frame in the robot. Like a Motion Policy Algorithm , an instance of the KinematicsSolver class is not expected to use the same USD robot representation as NVIDIA Isaac Sim. A KinematicsSolver can have its own internal representation of the robot, and there are necessary interface functions for performing the mapping between the internal robot representation and the robot Articulation.

### Joint Names
An instance of the KinematicsSolver class must fulfill a function KinematicsSolver.get_joint_names() that specifies the joints of interest to the solver, and the order in which it expects them. Think of a robot arm mounted on a moving base. A KinematicsSolver can use only the URDF for the robot arm without knowing about the robot base. In this case, many of the joints in the robot Articulation would not be recognized by the KinematicsSolver.
When computing forward kinematics, the joint positions that are passed to the solver must correspond to the output of KinematicsSolver.get_joint_names(). Likewise, the output of inverse kinematics will have the same shape as KinematicsSolver.get_joint_names(). A mapping layer between the robot Articulation and the KinematicsSolver is provided in the Articulation Kinematics Solver class.

### Frame Names
An instance of the KinematicsSolver class must fulfill a function KinematicsSolver.get_all_frame_names() to provide a list of frames in the robot’s kinematics chain that can have their positions referenced by name when solving either forward or inverse kinematics. The frame names returned by a KinematicsSolver do not have to match the frames present in the robot Articulation. Like joint names, the frame names come from the individual solver’s config file structure.

### Robot Base Pose
As with a Motion Policy Algorithm , a the KinematicsSolver interface includes a function set_robot_base_pose() that allows the caller to specify the location of the robot base. If this function has been called, the KinematicsSolver must apply appropriate transformations when computing forward and inverse kinematics. A KinematicsSolver operates in world coordinates. The solution to the forward kinematics will be translated and rotated according to the robot base pose to return the position of the end effector relative to the world frame, and the input to the inverse kinematics will be provided in the world coordinates and transformed so that it is relative to the robot base frame. If you prefers that the solver inputs are relative to the robot base frame, they can simply set the robot base pose to the origin.

### Collision Awareness
Implementations of the KinematicsSolver class do not need to be collision aware with external objects, but they have the option. A function KinematicsSolver.supports_collision_avoidance() -> bool must be implemented to indicate whether a particular KinematicsSolver supports collision avoidance. If a KinematicsSolver supports collision avoidance, it can fulfill the same set of world functions as a MotionPolicy (Inputs: World State ). If a solver is collision aware, it is especially important to specify the robot base pose correctly, as the positions of objects can only be queried relative to the world frame, and it is up to the solver to compute the positions of obstacles relative to the robot.

## Articulation Kinematics Solver
The ArticulationKinematicsSolver class exists to handle the mapping between the robot Articulation and an implementation of a Kinematics Solvers .

### Forward Kinematics
ArticulationKinematicsSolver wraps the forward kinematics function of a KinematicsSolver to query the joint positions of the robot Articulation and pass the appropriate joint positions to the KinematicsSolver in the order specified by KinematicsSolver.get_joint_names(). This allows the current position of the simulated robot end effector to be queried easily.

### Inverse Kinematics
ArticulationKinematicsSolver wraps the inverse kinematics to return the resulting joint positions as an ArticulationAction that can be directly applied to the robot Articulation. The current robot Articulation joint positions at the time this method is called are automatically used as a warm start in the IK calculation.

## Lula Kinematics Solver
The LulaKinematicsSolver implements the Kinematics Solvers interface. The solver does not support collision avoidance with objects in the world. In addition to the functions in the KinematicsSolver interface, the LulaKinematicsSolver includes getters and setters for changing internal settings such as LulaKinematicsSolver.set_max_iterations() to set the maximum number of iterations before the IK computation returns a failure.

### Lula Kinematics Solver Configuration
Two files are necessary to configure Lula Kinematics for use with a new robot:

- A URDF (universal robot description file), used for specifying robot kinematics as well as joint and link names. Position limits for each joint are also required. Other properties in the URDF are ignored and can be omitted; these include masses, moments of inertia, visual and collision meshes.

- A supplemental robot description file in YAML format. In addition to enumerating the list of actuated joints that define the configuration space (c-space) for the robot, this file also includes sections for specifying the default c-space configuration. This file can also be used to specify fixed positions for unactuated joints.
