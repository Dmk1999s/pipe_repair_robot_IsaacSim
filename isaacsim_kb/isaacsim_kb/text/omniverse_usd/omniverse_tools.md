<!-- source: omniverse_usd/omniverse_tools.html | title: Commands — Isaac Sim Documentation -->

# Commands
You can run many of the UI commands through `omni.kit.commands.execute("CommandName", args)`. To find a list of available commands, and what args to use, open Window > Commands, then click on `Search Commands`. On the window that appears, you will find an extensive list of all the commands available, and their respective documentation. Each command comes from a source Extension, and enabling/disabling extensions will change the list of available commands.
More information can be found Command History

# Registered Actions
An action is a pre-defined sequence of API and/or UI commands. Open the Utilities > Registered Actions to see a list of all the registered actions. The actions are registered by the extensions, and enabling/disabling extensions will change the list of available actions. Double clicking on the action name will execute the action.
You can also call these functions from Python scripts when using the `onclick_action` variable.
You can create your own actions using Kit Action API :

```
import omni.kit.actions.core

action_registry = omni.kit.actions.core.get_action_registry()
action_registry.register_action(
extension_id,
action_name,
action_function_callable,
)

# deregistered action at extension shutdown
action_registry.deregister_action(
extension_id,
action_name,
)
```
