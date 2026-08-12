<!-- source: utilities/custom_interactive_examples.html | title: Custom Interactive Examples — Isaac Sim Documentation -->

# Custom Interactive Examples
You can create custom examples in NVIDIA Isaac Sim Examples Browser, so that your examples are accessible in the same browser as rest of the examples.

## BaseSampleUITemplate & BaseSample Classes
The BaseSampleUITemplate and BaseSample classes provide the basic structure for creating an interactive examples that looks similar to our other examples in the Examples Browser. It produces a Load button and a Reset button, each button abstracts away the complexity of asynchronously interacting with the simulator and making the interactiveness work.
To create your own, follow the steps below:

- Copy the current files to the `user_examples` folder under `isaacsim/examples/interactive`.

```
cd exts/isaacsim.examples.interactive/isaacsim/examples/interactive
cp hello_world/hello_world* user_examples/
```

- Edit the highlighted lines in `exts/isaacsim.examples.interactive/isaacsim/examples/interactive/user_examples/hello_world_extension.py`:

```
import os
import omni.ext
from isaacsim.examples.interactive.base_sample import BaseSampleUITemplate
from isaacsim.examples.interactive.user_examples import HelloWorld

class HelloWorldExtension(omni.ext.IExt):
def on_startup(self, ext_id: str):
self.example_name = "Awesome Example"
self.category = "MyExamples"

ui_kwargs = {
"ext_id": ext_id,
"file_path": os.path.abspath(__file__),
"title": "My Awesome Example",
"doc_link": "https://docs.omniverse.nvidia.com/isaacsim/latest/core_api_tutorials/tutorial_core_hello_world.html",
"overview": "This Example introduces the user on how to do cool stuff with Isaac Sim through scripting in asynchronous mode.",
"sample": HelloWorld(),
}

ui_handle = BaseSampleUITemplate(**ui_kwargs)

# register the example with examples browser
get_browser_instance().register_example(
name=self.example_name,
execute_entrypoint=ui_handle.build_window,
ui_hook=ui_handle.build_ui,
category=self.category,
)

return
```

- Add the following lines to `exts/isaacsim.examples.interactive/isaacsim/examples/interactive/user_examples/__init__.py`.

```
from isaacsim.examples.interactive.user_examples.hello_world import HelloWorld
from isaacsim.examples.interactive.user_examples.hello_world_extension import HelloWorldExtension
```

Note
Every time the code is edited or changed, Press Ctrl+S to save the code and hot-reload NVIDIA Isaac Sim.
If you want to add more complexity and more buttons, feel free to browse through the other Examples. You can always access the underlying script by clicking on the folder icon in the upper right hand corner of the Example Browser.
