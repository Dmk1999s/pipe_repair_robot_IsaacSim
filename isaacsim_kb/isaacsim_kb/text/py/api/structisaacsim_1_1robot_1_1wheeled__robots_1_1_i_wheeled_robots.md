<!-- source: py/api/structisaacsim_1_1robot_1_1wheeled__robots_1_1_i_wheeled_robots.html | title: IWheeledRobots — Isaac Sim -->

# IWheeledRobots
Fully qualified name: `isaacsim::robot::wheeled_robots::IWheeledRobots`
structIWheeledRobots

Interface for wheeled robot control functionality.
This interface provides the foundation for wheeled robot control in Isaac Sim. While it contains no direct functions, implementing this interface:

- Enables plugin loading and initialization

- Triggers carbOnPluginStartup() and carbOnPluginShutdown() lifecycle methods

- Provides access to the Carbonite plugin ecosystem

Extensions can build upon this interface by defining custom functionality and Python bindings as needed.
