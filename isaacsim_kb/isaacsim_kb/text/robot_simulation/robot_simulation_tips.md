<!-- source: robot_simulation/robot_simulation_tips.html | title: Robot Simulation Tips — Isaac Sim Documentation -->

# Robot Simulation Tips
How do I speed up the simulation?You can speed up the simulation by reducing the number of objects in the scene, reducing the complexity of the objects in the scene, or reducing the number of simulation steps. For more information, see Isaac Sim Performance Optimization Handbook for more details.
My wheels are sliding or slipping on the ground.You can try to add and adjust friction parameters to both the wheels and the ground. See Adding Contact and Friction Parameters for instructions.
My gripper are not picking up the object.

- You can increase the friction parameters on both the fingers and object. See Adding Contact and Friction Parameters for instructions.

- Use the Physics Authoring Toolbar (Tools > Physics Toolbar), especially the Mass Distribution Tool to make sure the weight of the object and weight of the arms are reasonable.

- Increase the stiffness of your joints at the gripper.
