<!-- source: py/source/extensions/isaacsim.gui.components/docs/index.html | title: [isaacsim.gui.components] Isaac Sim UI Utilities — Isaac Sim -->

# [isaacsim.gui.components] Isaac Sim UI Utilities
Version: 1.2.1
Core UI Elements for Isaac Sim

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API
UI Utils (Shared UI Elements)

[TABLE]
setup_ui_headers | Creates the Standard UI Elements at the top of each Isaac Extension.
[/TABLE]
UI Utils (Builder Functions)

[TABLE]
btn_builder | Creates a stylized button.
state_btn_builder | Creates a State Change Button that changes text when pressed.
multi_btn_builder | Creates a Row of Stylized Buttons
cb_builder | Creates a Stylized Checkbox
multi_cb_builder | Creates a Row of Stylized Checkboxes.
str_builder | Creates a Stylized Stringfield Widget
int_builder | Creates a Stylized Intfield Widget
float_builder | Creates a Stylized Floatfield Widget
combo_cb_str_builder | Creates a Stylized Checkbox + Stringfield Widget
dropdown_builder | Creates a Stylized Dropdown Combobox
multi_dropdown_builder | Creates a Stylized Multi-Dropdown Combobox
combo_cb_dropdown_builder | Creates a Stylized Dropdown Combobox with an Enable Checkbox
combo_intfield_slider_builder | Creates a Stylized IntField + Stringfield Widget
combo_floatfield_slider_builder | Creates a Stylized FloatField + FloatSlider Widget
scrolling_frame_builder | Creates a Labeled Scrolling Frame with CopyToClipboard button
combo_cb_scrolling_frame_builder | Creates a Labeled, Checkbox-enabled Scrolling Frame with CopyToClipboard button
xyz_builder | [summary]
color_picker_builder | Creates a Color Picker Widget
progress_bar_builder | Creates a Progress Bar Widget
[/TABLE]
UI Utils (Plotting Functions)

[TABLE]
plot_builder | Creates a stylized static plot
combo_cb_plot_builder | Creates a Checkbox-Enabled dyanamic plot
xyz_plot_builder | Creates a stylized static XYZ plot
combo_cb_xyz_plot_builder | [summary]
[/TABLE]
UI Utils (Aesthetic Functions)

[TABLE]
add_separator | Aesthetic element to adds a Line Separator.
[/TABLE]
UI Element Wrappers

[TABLE]
Frame | Create a Frame UI element
CollapsableFrame | Create a CollapsableFrame UI element
ScrollingFrame | Create a ScrollingFrame UI element with a specified size.
IntField | Creates a IntField UI element.
FloatField | Creates a FloatField UI element.
StringField | Create StringField UI Element.
Button | Create a Button UI Element
CheckBox | Create a CheckBox UI Element
StateButton | Creates a State Button UI element.
DropDown | Create a DropDown UI element.
ColorPicker | Create a ColorPicker UI element to allow user-selection of an RGBA color
TextBlock | Create a text block that is only modifiable through code.
XYPlot |
[/TABLE]

#### Shared UI Elements
ui_utils.setup_ui_headers(
file_path,
title='MyCustomExtension',
doc_link='https://docs.isaacsim.omniverse.nvidia.com/latest/index.html',
overview='',
info_collapsed=True,
)Creates the Standard UI Elements at the top of each Isaac Extension.
Parameters:

- ext_id (str) – Extension ID.

- file_path (str) – File path to source code.

- title (str, optional) – Name of Extension. Defaults to “My Custom Extension”.

- doc_link (str, optional) – Hyperlink to Documentation. Defaults to “https://docs.isaacsim.omniverse.nvidia.com/latest/index.html ”.

- overview (str, optional) – Overview Text explaining the Extension. Defaults to “”.

#### Builder Functions
ui_utils.btn_builder(
type='button',
text='button',
tooltip='',
on_clicked_fn=None,
)Creates a stylized button.
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “button”.

- text (str, optional) – Text rendered on the button. Defaults to “button”.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (Callable, optional) – Call-back function when clicked. Defaults to None.

Returns:
Button

Return type:
ui.Button

ui_utils.state_btn_builder(
type='state_button',
a_text='STATEA',
b_text='STATEB',
tooltip='',
on_clicked_fn=None,
)Creates a State Change Button that changes text when pressed.
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “button”.

- a_text (str, optional) – Text rendered on the button for State A. Defaults to “STATE A”.

- b_text (str, optional) – Text rendered on the button for State B. Defaults to “STATE B”.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (Callable, optional) – Call-back function when clicked. Defaults to None.

ui_utils.multi_btn_builder(
type='multi_button',
count=2,
text=['button','button'],
tooltip=['','',''],
on_clicked_fn=[None,None],
)Creates a Row of Stylized Buttons
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “multi_button”.

- count (int, optional) – Number of UI elements to create. Defaults to 2.

- text (list, optional) – List of text rendered on the UI elements. Defaults to [“button”, “button”].

- tooltip (list, optional) – List of tooltips to display over the UI elements. Defaults to [“”, “”, “”].

- on_clicked_fn (list, optional) – List of call-backs function when clicked. Defaults to [None, None].

Returns:
List of Buttons

Return type:
list(ui.Button)

ui_utils.cb_builder(
type='checkbox',
default_val=False,
tooltip='',
on_clicked_fn=None,
)Creates a Stylized Checkbox
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “checkbox”.

- default_val (bool, optional) – Checked is True, Unchecked is False. Defaults to False.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (Callable, optional) – Call-back function when clicked. Defaults to None.

Returns:
model

Return type:
ui.SimpleBoolModel

ui_utils.multi_cb_builder(
type='multi_checkbox',
count=2,
text=['',''],
default_val=[False,False],
tooltip=['','',''],
on_clicked_fn=[None,None],
)Creates a Row of Stylized Checkboxes.
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “multi_checkbox”.

- count (int, optional) – Number of UI elements to create. Defaults to 2.

- text (list, optional) – List of text rendered on the UI elements. Defaults to [” “, “ “].

- default_val (list, optional) – List of default values. Checked is True, Unchecked is False. Defaults to [False, False].

- tooltip (list, optional) – List of tooltips to display over the UI elements. Defaults to [“”, “”, “”].

- on_clicked_fn (list, optional) – List of call-backs function when clicked. Defaults to [None, None].

Returns:
List of models

Return type:
list(ui.SimpleBoolModel)

ui_utils.str_builder(
type='stringfield',
default_val='',
tooltip='',
on_clicked_fn=None,
use_folder_picker=False,
read_only=False,
item_filter_fn=None,
bookmark_label=None,
bookmark_path=None,
folder_dialog_title='SelectOutputFolder',
folder_button_title='SelectFolder',
)Creates a Stylized Stringfield Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “stringfield”.

- default_val (str, optional) – Text to initialize in Stringfield. Defaults to “ “.

- tooltip (str, optional) – Tooltip to display over the UI elements. Defaults to “”.

- use_folder_picker (bool, optional) – Add a folder picker button to the right. Defaults to False.

- read_only (bool, optional) – Prevents editing. Defaults to False.

- item_filter_fn (Callable, optional) – filter function to pass to the FilePicker

- bookmark_label (str, optional) – bookmark label to pass to the FilePicker

- bookmark_path (str, optional) – bookmark path to pass to the FilePicker

Returns:
model of Stringfield

Return type:
AbstractValueModel

ui_utils.int_builder(
type='intfield',
default_val=0,
tooltip='',
min=-9223372036854775807,
max=9223372036854775807,
)Creates a Stylized Intfield Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “intfield”.

- default_val (int, optional) – Default Value of UI element. Defaults to 0.

- tooltip (str, optional) – Tooltip to display over the UI elements. Defaults to “”.

- min (int, optional) – Minimum limit for int field. Defaults to sys.maxsize * -1

- max (int, optional) – Maximum limit for int field. Defaults to sys.maxsize * 1

Returns:
model

Return type:
AbstractValueModel

ui_utils.float_builder(
type='floatfield',
default_val=0,
tooltip='',
min=-inf,
max=inf,
step=0.1,
format='%.2f',
)Creates a Stylized Floatfield Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “floatfield”.

- default_val (int, optional) – Default Value of UI element. Defaults to 0.

- tooltip (str, optional) – Tooltip to display over the UI elements. Defaults to “”.

Returns:
model

Return type:
AbstractValueModel

ui_utils.combo_cb_str_builder(type='checkbox_stringfield',default_val=[False,''],tooltip='',on_clicked_fn=<function<lambda>>,use_folder_picker=False,read_only=False,folder_dialog_title='SelectOutputFolder',folder_button_title='SelectFolder')
Creates a Stylized Checkbox + Stringfield Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “checkbox_stringfield”.

- default_val (str, optional) – Text to initialize in Stringfield. Defaults to [False, “ “].

- tooltip (str, optional) – Tooltip to display over the UI elements. Defaults to “”.

- use_folder_picker (bool, optional) – Add a folder picker button to the right. Defaults to False.

- read_only (bool, optional) – Prevents editing. Defaults to False.

Returns:
(cb_model, str_field_model)

Return type:
Tuple(ui.SimpleBoolModel, AbstractValueModel)

ui_utils.dropdown_builder(
type='dropdown',
default_val=0,
items=['Option1','Option2','Option3'],
tooltip='',
on_clicked_fn=None,
)Creates a Stylized Dropdown Combobox
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “dropdown”.

- default_val (int, optional) – Default index of dropdown items. Defaults to 0.

- items (list, optional) – List of items for dropdown box. Defaults to [“Option 1”, “Option 2”, “Option 3”].

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (Callable, optional) – Call-back function when clicked. Defaults to None.

Returns:
model

Return type:
AbstractItemModel

ui_utils.multi_dropdown_builder(
type='multi_dropdown',
count=2,
default_val=[0,0],
items=[['Option1','Option2','Option3'],['OptionA','OptionB','OptionC']],
tooltip='',
on_clicked_fn=[None,None],
)Creates a Stylized Multi-Dropdown Combobox
Returns:
model

Return type:
AbstractItemModel

Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “multi_dropdown”.

- count (int, optional) – Number of UI elements. Defaults to 2.

- default_val (list(int), optional) – List of default indices of dropdown items. Defaults to 0.. Defaults to [0, 0].

- items (list(list), optional) – List of list of items for dropdown boxes. Defaults to [[“Option 1”, “Option 2”, “Option 3”], [“Option A”, “Option B”, “Option C”]].

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (list(Callable), optional) – List of call-back function when clicked. Defaults to [None, None].

Returns:
list(models)

Return type:
list(AbstractItemModel)

ui_utils.combo_cb_dropdown_builder(type='checkbox_dropdown',default_val=[False,0],items=['Option1','Option2','Option3'],tooltip='',on_clicked_fn=[<function<lambda>>,None])
Creates a Stylized Dropdown Combobox with an Enable Checkbox
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “checkbox_dropdown”.

- default_val (list, optional) – list(cb_default, dropdown_default). Defaults to [False, 0].

- items (list, optional) – List of items for dropdown box. Defaults to [“Option 1”, “Option 2”, “Option 3”].

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (list, optional) – List of callback functions. Defaults to [lambda x: None, None].

Returns:
(cb_model, combobox)

Return type:
Tuple(ui.SimpleBoolModel, ui.ComboBox)

ui_utils.combo_intfield_slider_builder(
type='intfield_stringfield',
default_val=0.5,
min=0,
max=1,
step=0.01,
tooltip=['',''],
)Creates a Stylized IntField + Stringfield Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “intfield_stringfield”.

- default_val (float, optional) – Default Value. Defaults to 0.5.

- min (int, optional) – Minimum Value. Defaults to 0.

- max (int, optional) – Maximum Value. Defaults to 1.

- step (float, optional) – Step. Defaults to 0.01.

- tooltip (list, optional) – List of tooltips. Defaults to [“”, “”].

Returns:
(flt_field_model, flt_slider_model)

Return type:
Tuple(AbstractValueModel, IntSlider)

ui_utils.combo_floatfield_slider_builder(
type='floatfield_stringfield',
default_val=0.5,
min=0,
max=1,
step=0.01,
tooltip=['',''],
)Creates a Stylized FloatField + FloatSlider Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “floatfield_stringfield”.

- default_val (float, optional) – Default Value. Defaults to 0.5.

- min (int, optional) – Minimum Value. Defaults to 0.

- max (int, optional) – Maximum Value. Defaults to 1.

- step (float, optional) – Step. Defaults to 0.01.

- tooltip (list, optional) – List of tooltips. Defaults to [“”, “”].

Returns:
(flt_field_model, flt_slider_model)

Return type:
Tuple(AbstractValueModel, IntSlider)

ui_utils.scrolling_frame_builder(
type='scrolling_frame',
default_val='NoData',
tooltip='',
)Creates a Labeled Scrolling Frame with CopyToClipboard button
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “scrolling_frame”.

- default_val (str, optional) – Default Text. Defaults to “No Data”.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

Returns:
label

Return type:
ui.Label

ui_utils.combo_cb_scrolling_frame_builder(type='cb_scrolling_frame',default_val=[False,'NoData'],tooltip='',on_clicked_fn=<function<lambda>>)
Creates a Labeled, Checkbox-enabled Scrolling Frame with CopyToClipboard button
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “cb_scrolling_frame”.

- default_val (list, optional) – List of Checkbox and Frame Defaults. Defaults to [False, “No Data”].

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

- on_clicked_fn (Callable, optional) – Callback function when clicked. Defaults to lambda x : None.

Returns:
(model, label)

Return type:
list(SimpleBoolModel, ui.Label)

ui_utils.xyz_builder(
tooltip='',
axis_count=3,
default_val=[0.0,0.0,0.0,0.0],
min=-inf,
max=inf,
step=0.001,
on_value_changed_fn=[None,None,None,None],
)[summary]
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “”.

- axis_count (int, optional) – Number of Axes to Display. Max 4. Defaults to 3.

- default_val (list, optional) – List of default values. Defaults to [0.0, 0.0, 0.0, 0.0].

- min (float, optional) – Minimum Float Value. Defaults to float(“-inf”).

- max (float, optional) – Maximum Float Value. Defaults to float(“inf”).

- step (float, optional) – Step. Defaults to 0.001.

- on_value_changed_fn (list, optional) – List of callback functions for each axes. Defaults to [None, None, None, None].

Returns:
list(model)

Return type:
list(AbstractValueModel)

ui_utils.color_picker_builder(
type='color_picker',
default_val=[1.0,1.0,1.0,1.0],
tooltip='ColorPicker',
)Creates a Color Picker Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “color_picker”.

- default_val (list, optional) – List of (R,G,B,A) default values. Defaults to [1.0, 1.0, 1.0, 1.0].

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “Color Picker”.

Returns:
ui.ColorWidget.model

Return type:
AbstractItemModel

ui_utils.progress_bar_builder(
type='progress_bar',
default_val=0,
tooltip='Progress',
)Creates a Progress Bar Widget
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- type (str, optional) – Type of UI element. Defaults to “progress_bar”.

- default_val (int, optional) – Starting Value. Defaults to 0.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “Progress”.

Returns:
ui.ProgressBar().model

Return type:
AbstractValueModel

#### Plotting Functions
ui_utils.plot_builder(
data=None,
min=-1,
max=1,
type=omni.ui.Type.LINE,
value_stride=1,
color=None,
tooltip='',
)Creates a stylized static plot
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- data (list(float), optional) – Data to plot. Defaults to None.

- min (int, optional) – Minimum Y Value. Defaults to -1.

- max (int, optional) – Maximum Y Value. Defaults to 1.

- type (ui.Type, optional) – Plot Type. Defaults to ui.Type.LINE.

- value_stride (int, optional) – Width of plot stride. Defaults to 1.

- color (int, optional) – Plot color. Defaults to None.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

Returns:
plot

Return type:
ui.Plot

ui_utils.combo_cb_plot_builder(
default_val=False,
on_clicked_fn=<function<lambda>>,
data=None,
min=-1,
max=1,
type=omni.ui.Type.LINE,
value_stride=1,
color=None,
tooltip='',
)Creates a Checkbox-Enabled dyanamic plot
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- default_val (bool, optional) – Checkbox default. Defaults to False.

- on_clicked_fn (Callable, optional) – Checkbox Callback function. Defaults to lambda x: None.

- data (list(), optional) – Data to plat. Defaults to None.

- min (int, optional) – Min Y Value. Defaults to -1.

- max (int, optional) – Max Y Value. Defaults to 1.

- type (ui.Type, optional) – Plot Type. Defaults to ui.Type.LINE.

- value_stride (int, optional) – Width of plot stride. Defaults to 1.

- color (int, optional) – Plot color. Defaults to None.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

Returns:
(cb_model, plot)

Return type:
list(SimpleBoolModel, ui.Plot)

ui_utils.xyz_plot_builder(data=[], min=-1, max=1, tooltip='')
Creates a stylized static XYZ plot
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- data (list(float), optional) – Data to plot. Defaults to [].

- min (int, optional) – Minimum Y Value. Defaults to -1.

- max (int, optional) – Maximum Y Value. Defaults to “”.

- tooltip (str, optional) – Tooltip to display over the Label.. Defaults to “”.

Returns:
list(x_plot, y_plot, z_plot)

Return type:
list(ui.Plot)

ui_utils.combo_cb_xyz_plot_builder(
default_val=False,
on_clicked_fn=<function<lambda>>,
data=[],
min=-1,
max=1,
type=omni.ui.Type.LINE,
value_stride=1,
tooltip='',
)[summary]
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- default_val (bool, optional) – Checkbox default. Defaults to False.

- on_clicked_fn (Callable, optional) – Checkbox Callback function. Defaults to lambda x: None.

- list (data) – Data to plat. Defaults to None.

- min (int, optional) – Min Y Value. Defaults to -1.

- max (int, optional) – Max Y Value. Defaults to 1.

- type (ui.Type, optional) – Plot Type. Defaults to ui.Type.LINE.

- value_stride (int, optional) – Width of plot stride. Defaults to 1.

- tooltip (str, optional) – Tooltip to display over the Label. Defaults to “”.

Returns:
([plot_0, plot_1, plot_2], [val_model_x, val_model_y, val_model_z])

Return type:
Tuple(list(ui.Plot), list(AbstractValueModel))

#### Aesthetic Functions
ui_utils.add_separator()
Aesthetic element to adds a Line Separator.

#### UI Element Wrappers
classFrame(
enabled:bool=True,
visible:bool=True,
build_fn:Callable=None,
)Bases: `UIWidgetWrapper`
Create a Frame UI element
Parameters:

- enabled (bool, optional) – Frame is enabled. Defaults to True.

- visible (bool, optional) – Frame is visible. Defaults to True.

- build_fn (Callable, optional) – A function that can be called to specify what should fill the Frame. Function should take no arguments. Return values will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

rebuild()
Rebuild the Frame using the specified build_fn

set_build_fn(build_fn:Callable)
Set the build_fn to use when rebuilding the frame.
Parameters:
build_fn (Callable) – Build function to use when rebuilding the frame. Function should take no arguments. Return values will not be used.

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyframe:omni.ui.Frame
Returns: omni.ui.Frame: A UI Frame

propertyvisible:bool

classCollapsableFrame(
title:str,
collapsed:bool=True,
enabled:bool=True,
visible:bool=True,
build_fn:Callable=None,
)Bases: Frame
Create a CollapsableFrame UI element
Parameters:

- title (str) – Title of Collapsable Frame

- collapsed (bool, optional) – Frame is collapsed. Defaults to True.

- enabled (bool, optional) – Frame is enabled. Defaults to True.

- visible (bool, optional) – Frame is visible. Defaults to True.

- build_fn (Callable, optional) – A function that can be called to specify what should fill the Frame. Function should take no arguments. Return values will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

rebuild()
Rebuild the Frame using the specified build_fn

set_build_fn(build_fn:Callable)
Set the build_fn to use when rebuilding the frame.
Parameters:
build_fn (Callable) – Build function to use when rebuilding the frame. Function should take no arguments. Return values will not be used.

propertycollapsed:bool
Returns: bool: CollapsableFrame is collapsed

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyframe:omni.ui.Frame
Returns: omni.ui.Frame: A UI Frame

propertytitle:str
Returns: str: Title text of CollapsableFrame

propertyvisible:bool

classScrollingFrame(
num_lines=None,
enabled:bool=True,
visible:bool=True,
build_fn:Callable=None,
)Bases: Frame
Create a ScrollingFrame UI element with a specified size.
Parameters:

- num_lines (int, optional) – Determines height of ScrollingFrame element in terms of the typical line height of UI elements. If not specified, the ScrollingFrame will fill the space it can in the UI Window.

- enabled (bool, optional) – Frame is enabled. Defaults to True.

- visible (bool, optional) – Frame is visible. Defaults to True.

- build_fn (Callable, optional) – A function that can be called to specify what should fill the Frame. Function should take no arguments. Return values will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

rebuild()
Rebuild the Frame using the specified build_fn

set_build_fn(build_fn:Callable)
Set the build_fn to use when rebuilding the frame.
Parameters:
build_fn (Callable) – Build function to use when rebuilding the frame. Function should take no arguments. Return values will not be used.

set_num_lines(num_lines:int)
Set the height of the ScrollingFrame element in terms of the typical line height of other UI elements.
Parameters:
num_lines (int) – Number of lines that should be shown in a ScrollingFrame.

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyframe:omni.ui.Frame
Returns: omni.ui.Frame: A UI Frame

propertyvisible:bool

classIntField(
label:str,
tooltip:str='',
default_value:int=0,
lower_limit:int=None,
upper_limit:int=None,
on_value_changed_fn:Callable=None,
)Bases: `UIWidgetWrapper`
Creates a IntField UI element.
Parameters:

- label (str) – Short descriptive text to the left of the IntField.

- tooltip (str, optional) – Text to appear when the mouse hovers over the IntField. Defaults to “”.

- default_value (int, optional) – Default value of the IntField. Defaults to 0.

- lower_limit (int, optional) – Lower limit of float. Defaults to None.

- upper_limit (int, optional) – Upper limit of float. Defaults to None.

- on_value_changed_fn (Callable, optional) – Function to be called when the value of the int is changed. The function should take an int as an argument. The return value will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

get_lower_limit()→int
Get the lower limit on the IntField.
Returns:
Lower Limit on IntField

Return type:
int

get_upper_limit()→int
Get the upper limit on the IntField.
Returns:
Upper Limit on IntField

Return type:
int

get_value()→int
Get the current value of the int field
Returns:
Current value of the int field

Return type:
int

set_lower_limit(lower_limit:int)
Set lower limit of IntField. If current value is lower than lower_limit, the current value will be clipped to lower_limit
Parameters:
lower_limit (int) – lower limit of IntField

set_on_value_changed_fn(
on_value_changed_fn:Callable,
)Set function that is called when the value of the IntField is modified
Parameters:
on_value_changed_fn (Callable) – Function that is called when the value of the IntField is modified. Function should take a int as the argument. The return value will not be used.

set_upper_limit(upper_limit:int)
Set upper limit of IntField. If current value is higher than upper_limit, the current value will be clipped to upper_limit
Parameters:
upper_limit (int) – Upper limit of IntField

set_value(val:int)
Set the value in the IntField
Parameters:
val (int) – Value to fill IntField

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyint_field:omni.ui.IntField
Returns: omni.ui.IntField: UI IntField elements

propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyvisible:bool

classFloatField(
label:str,
tooltip:str='',
default_value:float=0.0,
step:float=0.01,
format:str='%.2f',
lower_limit:float=None,
upper_limit:float=None,
on_value_changed_fn:Callable=None,
on_end_edit_fn:Callable=None,
)Bases: `UIWidgetWrapper`
Creates a FloatField UI element.
Parameters:

- label (str) – Short descriptive text to the left of the FloatField.

- tooltip (str, optional) – Text to appear when the mouse hovers over the FloatField. Defaults to “”.

- default_value (float, optional) – Default value of the Float Field. Defaults to 0.0.

- step (float, optional) – Smallest increment that the user can change the float by when dragging mouse. Defaults to 0.01.

- format (str, optional) – Formatting string for float. Defaults to “%.2f”.

- lower_limit (float, optional) – Lower limit of float. Defaults to None.

- upper_limit (float, optional) – Upper limit of float. Defaults to None.

- on_value_changed_fn (Callable, optional) – Function to be called when the value of the float is changed. The function should take a float as an argument. The return value will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

get_lower_limit()→float
Get the lower limit on the FloatField
Returns:
Lower limit on FloatField

Return type:
float

get_upper_limit()→float
Get the upper limit on the FloatField
Returns:
Upper limit on FloatField

Return type:
float

get_value()→float
Return the current value of the FloatField
Returns:
Current value of the FloatField

Return type:
float

set_lower_limit(lower_limit:float)
Set lower limit of FloatField. If current value is lower than lower_limit, the current value will be clipped to lower_limit
Parameters:
lower_limit (float) – lower limit of FloatField

set_on_end_edit_fn(on_end_edit_fn:Callable)
Set function that is called when the user finishes editing the FloatField
Parameters:
on_end_edit_fn (Callable) – Function that is called when the user finishes editing the FloatField. Function should take a float as the argument. The return value will not be used.

set_on_value_changed_fn(
on_value_changed_fn:Callable,
)Set function that is called when the value of the FloatField is modified
Parameters:
on_value_changed_fn (Callable) – Function that is called when the value of the FloatField is modified. Function should take a float as the argument. The return value will not be used.

set_upper_limit(upper_limit:float)
Set upper limit of FloatField. If current value is higher than upper_limit, the current value will be clipped to upper_limit
Parameters:
upper_limit (float) – Upper limit of FloatField

set_value(val:float)
Set the value in the FloatField
Parameters:
val (float) – Value to fill FloatField

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyfloat_field:omni.ui.FloatField
Returns: omni.ui.FloatField: UI FloatField element

propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyvisible:bool

classStringField(
label:str,
tooltip:str='',
default_value:str='',
read_only=False,
multiline_okay=False,
on_value_changed_fn:Callable=None,
use_folder_picker=False,
item_filter_fn=None,
bookmark_label=None,
bookmark_path=None,
folder_dialog_title='SelectOutputFolder',
folder_button_title='SelectFolder',
)Bases: `UIWidgetWrapper`
Create StringField UI Element.
Starting at use_folder_picker, the arguments to the StringField all pertain to the folder_picker. If the folder_picker is not used, these arguments may all be ignored.
Parameters:

- label (str, optional) – Label to the left of the UI element. Defaults to “”.

- tooltip (str, optional) – Tooltip to display over the UI elements. Defaults to “”.

- default_val (str, optional) – Text to initialize in Stringfield. Defaults to “ “.

- read_only (bool, optional) – Prevents editing. Defaults to False.

- multiline_okay (bool, optional) – If True, allow newline character in input strings. Defaults to False.

- on_value_changed_fn (Callable, optional) – The function should take a string as an argument. The return value will not be used. Defaults to None.

- use_folder_picker (bool, optional) – Add a folder picker button to the right. Defaults to False.

- item_filter_fn (Callable, optional) – Filter function to pass to the FilePicker. This function should take a string as an argument and return a boolean. When the user opens the file picker, every file in the directory they are viewing will be passed to item_filter_fn, and when True is returned, the file will be shown. When False is returned, the file will not be shown. This can be used to ensure that the user may only select valid file types.

- bookmark_label (str, optional) – Bookmark label to pass to the FilePicker. This will create a bookmark when the file picker is used with the label specified here.

- bookmark_path (str, optional) – Bookmark path to pass to the FilePicker. This will create a bookmark when the file picker is used with the path specified here.

add_folder_picker_icon(
on_click_fn,
item_filter_fn=None,
bookmark_label=None,
bookmark_path=None,
dialog_title='SelectOutputFolder',
button_title='SelectFolder',
)cleanup()
Perform any necessary cleanup

get_value()→str
Return the current value of the StringField
Returns:
Current value of the StringField

Return type:
str

set_item_filter_fn(item_filter_fn:Callable)
Set the filter function that will be used with the file picker
Parameters:
item_filter_fn (Callable) – Filter function that will be called to filter the files shown in the picker. This function should take a string file_path as the argument. The return value should be a bool, with True indicating the the file should be shown to the user in the file picker.

set_multiline_okay(multiline_okay:bool)
Set the StringFiled to allow the newline character
Parameters:
multiline_okay (bool) – If True, allow newline character in strings.

set_on_value_changed_fn(
on_value_changed_fn:Callable,
)Set function that is called when the value of the StringField is modified
Parameters:
on_value_changed_fn (Callable) – Function that is called when the value of the StringField is modified. Function should take a string as the argument. The return value will not be used.

set_read_only(read_only:bool)
Set this StringField to be read only
Parameters:
read_only (bool) – If True, StringField cannot be modified through the UI; it can still be modified programmatically with set_value()

set_value(val:str)
Set the value of the StringField
Parameters:
val (str) – Value to fill StringField

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyfile_picker_btn:omni.ui.Button
Returns: omni.ui.Button: Button to activate file picker

propertyfile_picker_frame:omni.ui.Frame
Returns: omni.ui.Frame: UI Frame containing FilePicker

propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertystring_field:omni.ui.StringField
Returns: omni.ui.StringField: UI StringField element

propertyvisible:bool

classButton(label:str, text:str, tooltip='', on_click_fn=None)
Bases: `UIWidgetWrapper`
Create a Button UI Element
Parameters:

- label (str) – Short descriptive text to the left of the Button

- text (str) – Text on the Button

- tooltip (str, optional) – Text to appear when the mouse hovers over the Button. Defaults to “”.

- on_click_fn (Callable, optional) – Callback function that will be called when the button is pressed. Function should take no arguments. The return value will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

set_on_click_fn(on_click_fn:Callable)
Set the callback function for when the Button is clicked.
Parameters:
on_click_fn (Callable) – Callback function for when Button is clicked. The function should take a single bool argument. The return value will not be used.

trigger_click()
Trigger identical behavior as if the user pressed the Button through the UI.

propertybutton:omni.ui.Button
Returns: omni.ui.Button: UI Button element

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyvisible:bool

classCheckBox(
label:str,
default_value:bool=False,
tooltip='',
on_click_fn=None,
)Bases: `UIWidgetWrapper`
Create a CheckBox UI Element
Parameters:

- label (str) – Short descriptive text to the left of the CheckBox

- default_value (bool, optional) – If True, CheckBox will be checked. Defaults to False.

- tooltip (str, optional) – Text to appear when the mouse hovers over the CheckBox. Defaults to “”.

- on_click_fn (_type_, optional) – Callback function that will be called when the CheckBox is pressed. Function should take a single bool argument. The return value will not be used. Defaults to None.

cleanup()
Perform any necessary cleanup

get_value()→bool
Returns:
Check box is checked

Return type:
bool

set_on_click_fn(on_click_fn:Callable)
Set the function that will be called when the CheckBox is clicked.
Parameters:
on_click_fn (Callable) – Callback function for when CheckBox is clicked. The function should take a single bool argument. The return value will not be used.

set_value(val:bool)
Parameters:
val (bool) – If True, set CheckBox to checked state

propertycheckbox:omni.ui.CheckBox
Returns: omni.ui.CheckBox: UI CheckBox element

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyvisible:bool

classStateButton(
label:str,
a_text:str,
b_text:str,
tooltip='',
on_a_click_fn:Callable=None,
on_b_click_fn:Callable=None,
physics_callback_fn:Callable=None,
)Bases: `UIWidgetWrapper`
Creates a State Button UI element. A StateButton is a button that changes between two states A and B when clicked. In state A, the StateButton has a_text written on it, and in state B, the StateButton has b_text written on it.
Parameters:

- label (str) – Short descriptive text to the left of the StateButton

- a_text (str) – Text on the StateButton in one of its two states

- b_text (str) – Text on the StateButton in the other of its two states

- tooltip (str, optional) – Text that appears when the mouse hovers over the button. Defaults to “”.

- on_a_click_fn (Callable, optional) – A function that should be called when the button is clicked while in state A. Function should have 0 arguments. The return value will not be used. Defaults to None.

- on_b_click_fn (Callable, optional) – A function that should be called when the button is clicked while in state B. Function should have 0 arguments. The return value will not be used. Defaults to None.

- physics_callback_fn (Callable, optional) – A function that will be called on every physics step while the button is in state B (a_text was pressed). The function should have one argument for physics step size (float). The return value will not be used. Defaults to None.

cleanup()
Remove physics callback created by the StateButton if exists.

get_current_text()→str
Get the current text on the button.

is_in_a_state()→bool
Return True if the StateButton is in the a state. False implies that it is in the b state.
Returns:
True when the StateButton is in the b state.

Return type:
bool

reset()
Reset StateButton to state A.

set_on_a_click_fn(on_a_click_fn:Callable)
Set a function that is called when the button is clicked in state A.
Parameters:
on_a_click_fn (Callable) – A function that is called when the button is clicked in state A. Function should take no arguments. The return value will not be used.

set_on_b_click_fn(on_b_click_fn:Callable)
Set a function that is called when the button is clicked in state B.
Parameters:
on_b_click_fn (Callable) – A function that is called when the button is clicked in state B. Function should take no arguments. The return value will not be used.

set_physics_callback_fn(
physics_callback_fn:Callable,
)Set a physics callback function that will be called on every physics step while the StateButton is in state B.
Parameters:
physics_callback_fn (Callable) – A function that will be called on every physics step while the button is in state B (a_text was pressed). The function should have one argument for physics step size (float). The return value will not be used.

trigger_click_if_a_state()
If in the A state, trigger button to execute the same behavior as if it were clicked by the user. If the button is in the B state, nothing will happen.

trigger_click_if_b_state()
If in the B state, trigger button to execute the same behavior as if it were clicked by the user. If the button is in the A state, nothing will happen. This is distinct from calling reset() because the user on_b_click_fn() will be triggered.

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertystate_button:omni.ui.Button
Returns: omni.ui.Button: UI Button element

propertyvisible:bool

classDropDown(
label:str,
tooltip:str='',
populate_fn:Callable=None,
on_selection_fn:Callable=None,
keep_old_selections:bool=False,
add_flourish:bool=True,
)Bases: `UIWidgetWrapper`
Create a DropDown UI element. A DropDown menu can be populated by the user, with a callback function specified for when an item is selected.
Parameters:

- label (str) – Short descriptive text to the left of the DropDown

- tooltip (str, optional) – Text to appear when the mouse hovers over the DropDown. Defaults to “”.

- populate_fn (Callable, optional) – A user-defined function that returns a list[str] of items that should populate the drop-down menu. This Function should have 0 arguments. Defaults to None.

- on_selection_fn (Callable, optional) – A user-defined callback function for when an element is selected from the DropDown. The function should take in a string argument of the selection. The return value will not be used. Defaults to None.

- keep_old_selections (bool, optional) – When the DropDown is repopulated with the user-defined populate_fn, the default behavior is to reset the selection in the DropDown to be at index 0. If the user sets keep_old_selections=True, when the DropDown is repopulated and the old selection is still one of the options, the new selection will match the old selection. Defaults to False.

cleanup()
Perform any necessary cleanup

get_items()→List[str]
Get the items in the DropDown
Returns:
A list of the options in the DropDown

Return type:
List[str]

get_selection()→str
Get current selection in DropDown
Returns:
Current selection in DropDown

Return type:
str

get_selection_index()→int
Get index of selection in DropDown menu
Returns:
Index of selection in DropDown menu

Return type:
int

repopulate()
A function that the user can call to make the DropDown menu repopulate. This will call the populate_fn set by the user.

set_items(items:List[str], select_index:int=None)
Set the items in the DropDown explicitly.
Parameters:

- items (List[str]) – New set of items in the DropDown

- select_index (int, optional) – Index of item to select. If left as None, behavior is determined by the keep_old_selections flag. Defaults to None.

set_keep_old_selection(val:bool)
Set keep_old_selection flag to determine behavior when repopulating the DropDown
Parameters:
val (bool) – When the DropDown is repopulated with the user-defined populate_fn, the default behavior is to reset the selection in the DropDown to be at index 0. If the user sets keep_old_selections=True, when the DropDown is repopulated and the old selection is still one of the options, the new selection will match the old selection, and the on_selection_fn() will not be called.

set_on_selection_fn(on_selection_fn:Callable)
Set the function that gets called when a new item is selected from the DropDown
Parameters:
on_selection_fn (Callable) – A function that is called when a new item is selected from the DropDown. he function should take in a string argument of the selection. Its return value is not used.

set_populate_fn(
populate_fn:Callable,
repopulate:bool=True,
)Set the populate_fn for this DropDown
Parameters:

- populate_fn (Callable) – Function used to specify the options that fill the DropDown. Function should take no arguments and return a list[str].

- repopulate (bool, optional) – If true, repopulate the DropDown using the new populate_fn. Defaults to True.

set_populate_fn_to_find_all_usd_objects_of_type(
object_type:str,
repopulate=True,
)Set the populate_fn to find all objects of a specified type on the USD stage. This is included as a convenience function to fulfill one common use-case for a DropDown menu. This overrides the populate_fn set by the user.
Parameters:

- object_type (str) – A string name of the type of USD object matching the output of get_prim_object_type(prim_path)

- repopulate (bool, optional) – Repopulate the DropDown immediately. Defaults to True.

set_selection(selection:str)
Set the selected item in the DropDown. If the specifified selection is not in the DropDown, nothing will happen.
Parameters:
selection (str) – Item to select in the DropDown

set_selection_by_index(select_index:int)
Set the selected item in the DropDown by index. If the provided index is out of bounds, nothing will happen.
Parameters:
select_index (int) – Index of item to select from DropDown

trigger_on_selection_fn_with_current_selection()
Call the user on_selection_fn() with whatever item is currently selected in the DropDown.

propertycombobox:omni.ui.ComboBox
Returns: omni.ui.ComboBox: UI ComboBox element.

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyvisible:bool

classColorPicker(
label:str,
default_value:List[float]=[1.0,1.0,1.0,1.0],
tooltip:str='',
on_color_picked_fn:Callable=None,
)Bases: `UIWidgetWrapper`
Create a ColorPicker UI element to allow user-selection of an RGBA color
Parameters:

- label (str) – Short descriptive text to the left of the ColorPicker

- default_value (List[float], optional) – RGBA color values between 0 and 1. Defaults to [1.0, 1.0, 1.0, 1.0].

- tooltip (str, optional) – Text to appear when the mouse hovers over the ColorPicker. Defaults to “”.

- on_color_picked_fn (Callable, optional) – Function that will be called if the user picks a new color. Function should expect a List[float] as an argument with four RGBA color values between 0 and 1. The return value will not be used.

cleanup()
Perform any necessary cleanup

get_color()→List[float]
Get the RGBA value of the selected color
Returns:
RGBA color value with four values between 0 and 1

Return type:
List[float]

set_color(color:List[float])
Set the RGBA color value of the selected color
Parameters:
color (List[float]) – RGBA color value with four values between 0 and 1

set_on_color_picked_fn(
on_color_picked_fn:Callable,
)Set the function that should be called if the user picks a new color
Parameters:
on_color_picked_fn (Callable) – Function that will be called if the user picks a new color. Function should expect a List[float] as an argument with four RGBA color values between 0 and 1. The return value will not be used.

propertycolor_picker:omni.ui.ColorWidget
Returns: omni.ui.ColorWidget: UI ColorWidget element

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyvisible:bool

classTextBlock(
label:str,
text:str='',
tooltip:str='',
num_lines=5,
include_copy_button:bool=True,
)Bases: `UIWidgetWrapper`
Create a text block that is only modifiable through code. The user may not set the value of the text in the UI.
Parameters:

- label (str) – Short description of the contents of the TextBlock

- text (str, optional) – Text to put in the TextBlock. Defaults to “”.

- tooltip (str, optional) – Text to appear when the mouse hovers over the TextBlock. Defaults to “”.

- num_lines (int, optional) – Number of lines that should be visible in the TextBlock at one time. Defaults to 5.

- include_copy_button (bool, optional) – Include a copy_to_clipboard button. Defaults to True.

cleanup()
Perform any necessary cleanup

get_text()→str
Returns:
Text in the text block

Return type:
str

set_num_lines(num_lines:int)
Set the number of lines that should be visible in the TextBlock at one time.
Parameters:
num_lines (int) – Number of lines that should be visible in the TextBlock at one time.

set_text(text:str)
Parameters:
text (str) – Set the text in the text block.

propertycontainer_frame:omni.ui.Frame
propertycopy_btn:omni.ui.Button
Returns: omni.ui.Button: Copy Button. If the TextBlock was built without a copy button, this will return None.

propertyenabled:bool
propertylabel:omni.ui.Label
Returns: omni.ui.Label: UI Label element that contains the descriptive text

propertyscrolling_frame:omni.ui.ScrollingFrame
Returns: omni.ui.ScrollingFrame: Scrolling Frame that contains the TextBlock text

propertytext_block:omni.ui.Label
Returns: omni.ui.Label: UI element that contains the text in the text block

propertyvisible:bool

classXYPlot(
label:str,
tooltip:str='',
x_data:List[List]|List=[],
y_data:List[List]|List=[],
x_min:float=None,
x_max:float=None,
y_min:float=None,
y_max:float=None,
x_label:str='X',
y_label:str='Y',
plot_height:int=10,
show_legend:bool=False,
legends:List[str]=None,
plot_colors:List[List[int]]=None,
)Bases: `UIWidgetWrapper`
cleanup()
Perform any necessary cleanup

get_legends()→List[str]
Get the legends for the plotted data.
Returns:
Legends for the plotted data

Return type:
List[str]

get_plot_colors()→List[List[int]]
Get the colors of the data in the plot
Returns:
List of lists where each inner list has length 3 corresponding to r,g,b values.

Return type:
List[List[int]]

get_plot_height()→int
Get the height of the plot, proportional to the height of a line of text
Returns:
Height of the plot

Return type:
int

get_x_data()→List[List[float]]
x_data in the plot
Returns:
A possibly ragged list of lists where each ith inner list is the x coordinates for plot i.

Return type:
List[List[float]]

get_x_max()→float
Get the maximum value of x shown in the plot.
Returns:
Maximum value of x shown in the plot.

Return type:
float

get_x_min()→float
Get the minimum value of x shown in the plot.
Returns:
Minimum value of x shown in the plot.

Return type:
float

get_y_data()→List[List[float]]
y_data in the plot
Returns:
A possibly ragged list of lists where each ith inner list is the y coordinates for plot i.

Return type:
List[List[float]]

get_y_max()→float
Get the maximum value of y shown in the plot.
Returns:
Maximum value of y shown in the plot.

Return type:
float

get_y_min()→float
Get the minimum value of y shown in the plot.
Returns:
Minimum value of y shown in the plot.

Return type:
float

set_data(
x_data:List[List]|List,
y_data:List[List]|List,
)Set the data to plot
Parameters:

- x_data (Union[List[List],List]) – A possibly ragged list of lists where each ith inner list is the x coordinates for plot i. For a single plot, the data may be provided as a list of floats. x_data must have exactly the same shape as y_data.

- y_data (Union[List[List],List]) – A possibly ragged list of lists where each ith inner list is the y coordinates for plot i. For a single plot, the data may be provided as a list of floats. y_data must have exactly the same shape as x_data.

set_legend_by_index(idx:int, legend:str)
Set the legend for a specific plot whose index corresponds to the rows of x_data and y_data
Parameters:

- idx (int) – Index of legend to set.

- legend (str) – Legend

set_legends(legends:List[str])
Set legends for each plot.
Parameters:
legends (List[str]) – List of legends for each plot.

set_plot_color_by_index(index:int, r:int, g:int, b:int)
Set the color of a specific plot.
Parameters:

- index (int) – Index of the plot corresponding to the rows of x_data and y_data.

- r (int) – Value for red in [0,255]

- g (int) – Value for green in [0,255]

- b (int) – Value for blue in [0,255]

set_plot_colors(plot_colors:List[List[int]])
Set the colors for every plot
Parameters:
plot_colors (List[List[int]]) – A list of lists where each index corresponds to the rows of x_data and y_data. Each inner list must contain [r,g,b] color values in [0,255]

set_plot_height(plot_height:int)
Set the height of the plot.
Parameters:
plot_height (int) – Height of the plot, proportional to the height of a line of text.

set_plot_visible_by_index(index:int, visible:bool)
Hide or show a specific plot
Parameters:

- index (int) – Index of plot to show

- visible (bool) – If True, show the plot, otherwise hide it.

set_show_legend(show_legend:bool)
Hide or show the legend for this Widget
Parameters:
show_legend (bool) – If True, show a legend for the Widget.

set_x_max(x_max:float)
Set maximum value of x shown on the plot. If this value is not greater than x_min, x_min will be updated to x_max - 1.
Parameters:
x_max (float) – Maximum value of x shown on the plot.

set_x_min(x_min:float)
Set the minimum value of x shown on the plot. If this value is not less than x_max, x_max will be updated to x_min + 1.
Parameters:
x_min (float) – Minimum value of x shown on the plot.

set_y_max(y_max:float)
Set maximum value of y shown on the plot. If this value is not greater than y_min, y_min will be updated to y_max - 1.
Parameters:
y_max (float) – Maximum value of y shown on the plot.

set_y_min(y_min:float)
Set the minimum value of y shown on the plot. If this value is not less than y_max, y_max will be updated to y_min + 1.
Parameters:
y_min (float) – Minimum value of y shown on the plot.

propertycontainer_frame:omni.ui.Frame
propertyenabled:bool
propertyvisible:bool
