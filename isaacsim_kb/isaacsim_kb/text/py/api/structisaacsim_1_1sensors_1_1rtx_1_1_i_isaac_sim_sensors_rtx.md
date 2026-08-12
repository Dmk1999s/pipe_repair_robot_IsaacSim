<!-- source: py/api/structisaacsim_1_1sensors_1_1rtx_1_1_i_isaac_sim_sensors_rtx.html | title: IIsaacSimSensorsRtx — Isaac Sim -->

# IIsaacSimSensorsRtx
Fully qualified name: `isaacsim::sensors::rtx::IIsaacSimSensorsRtx`
structIIsaacSimSensorsRtx

Minimal interface.
It doesn’t have any functions, but just implementing it and acquiring will load your plugin, trigger call of carbOnPluginStartup() and carbOnPluginShutdown() methods and allow you to use other Carbonite plugins. That by itself can get you quite far and useful as basic building block for Kit extensions. One can define their own interface with own python python bindings when needed and abandon that one.
