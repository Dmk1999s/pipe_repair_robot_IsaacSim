<!-- source: omniverse_usd/open_usd.html | title: OpenUSD Fundamentals — Isaac Sim Documentation -->

# OpenUSD Fundamentals
The language used in Isaac Sim to describe the robot and its environment is the Universal Scene Description (USD) .

## Why USD?
USD enables seamless interchange of 3D content among diverse content creation apps with its rich, extensible language. With concepts of layering and variants, it’s a powerful tool that enables live collaboration on the same asset and scene. And when properly used, it permits working on assets without overwriting and erasing someone else’s work.
USD provides a text-based format for direct editing (.usda). For higher performance and space optimization, there is a binary-encoded format (.usd). All aspects of USD can be accessed through coding in C++ or Python.
APIs are available for you to set up a scene or tune a robot directly in USD, but, typically it is not necessary to use them.

## Hello World
Let’s start by creating a basic USD file from code:

```
1from pxr import Usd, UsdGeom
2
3stage = Usd.Stage.CreateNew('/path/to/HelloWorld.usda')
4xformPrim = UsdGeom.Xform.Define(stage, '/hello')
5spherePrim = UsdGeom.Sphere.Define(stage, '/hello/world')
6# generic_spherePrim = stage.DefinePrim('/hello/world_generic', 'Sphere')
7stage.GetRootLayer().Save()
```
Replacing `/path/to/` with the desired save folder. You can execute this code in the script editor (Window > Script Editor) in Isaac Sim, and it yields the following USD file:

```
#usda 1.0

def Xform "hello"
{
def Sphere "world"
{
}
}
```
This example contains a couple of powerful things we can take away from it:

- Type: Elements in USD (called Prims) have a defined type. In the case of `hello`, it is of type `Xform`, a type used everywhere, and it defines elements that contain a transform in the world. `World` is of type Sphere, which represents a primitive geometry.

- Composition: Prims can have nested prims. These nested prims are, for all effects, fully defined elements, with their own attributes.

- Introspection: If uncommented, the line `generic_spherePrim = stage.DefinePrim('/hello/world_generic', 'Sphere')` would yield a sphere just like the `/hello/world`. Prim types can be defined directly through their schema name.

- Namespaces: Both Xform and Sphere are part of the standard pxr namespace UsdGeom, a set of types that represent geometry elements in the scene.

You can open this USD file in Isaac Sim in the script editor window with:

```
1import omni
2omni.usd.get_context().open_stage("/path/to/HelloWorld.usda")
```

### Inspecting and Authoring Properties
With a basic scene, you can start making modifications to the elements. Start by opening and getting the elements from the scene:

```
1from pxr import Usd, Vt
2stage = Usd.Stage.Open('/path/to/HelloWorld.usda')
3xform = stage.GetPrimAtPath('/hello')
4sphere = stage.GetPrimAtPath('/hello/world')
5print(xform.GetPropertyNames())
6print(sphere.GetPropertyNames())
```
The output for the code above is:

```
['proxyPrim', 'purpose', 'visibility', 'xformOpOrder']
['doubleSided', 'extent', 'orientation', 'primvars:displayColor' 'primvars:displayOpacity', 'proxyPrim', 'purpose', 'radius', 'visibility', 'xformOpOrder']
```
USD offers polymorphism. If you review both lists you can see the common attributes. By having a common `XFormable` ancestor, Xforms and Spheres share a subset of properties, while sphere contains some unique elements that only make sense for its specialization (for example, radius).
To update these attributes, you can append the following to the code above:

```
radiusAttr = sphere.GetAttribute('radius')
print(radiusAttr.Get())
radiusAttr.Set(0.50)
print(radiusAttr.Get())
```
Because the stage was still open from the previous sample, you’ll see the sphere reducing from radius 1.0 to 0.5, but it also prints these values in the console.
To move the sphere to a new position use `xformOpOrder`, which is common to `Xform` and `Sphere`. Many different transforms can be applied to a prim, each from potentially different layers. The `xformOpOrder` tracks and manages the different transforms, it is like a list of `Xform` operations, applied in the order specified from first to last.
Our sphere doesn’t have its own, so to create a new one:

```
from pxr import Gf

translation = Gf.Vec3d(1,0,0)
sphere_xformable = UsdGeom.Xformable(sphere)
move_sphere_op = sphere_xformable.AddTranslateOp(opSuffix="moveSphereOp")
move_sphere_op.Set(translation)
```
Notice that the sphere has jumped to a new position along the X-axis. Alternatively, you could apply the translation to the parent `xform` instead.

```
translation = Gf.Vec3d(0,0,1)
xform_xformable = UsdGeom.Xformable(xform)
move_parent_op = xform_xformable.AddTranslateOp(opSuffix='moveParentOp')
move_parent_op.Set(translation)
```
Verify that you see the sphere jump to a new location, which is the composition of both the parent and child transforms.
A consequence of the universal nature of USD is that when you fetch a prim by path, it is always of type `prim` and needs to be cast appropriately before performing operations with or on it.
To create and bind a material to the prim to change its color, first create it:

```
from pxr import Sdf, UsdShade

# create the material and shader
material_path = '/hello/material'
mat_prim = stage.DefinePrim(Sdf.Path(material_path), "Material")
material_prim = UsdShade.Material.Get(stage, mat_prim.GetPath())

shader_path = stage.DefinePrim(Sdf.Path("{}/Shader".format(material_path)), "Shader")
shader_prim = UsdShade.Shader.Get(stage, shader_path.GetPath())

with Sdf.ChangeBlock():
# connect up the shader graph
shader_out = shader_prim.CreateOutput("out", Sdf.ValueTypeNames.Token)
material_prim.CreateSurfaceOutput("mdl").ConnectToSource(shader_out)
material_prim.CreateVolumeOutput("mdl").ConnectToSource(shader_out)
material_prim.CreateDisplacementOutput("mdl").ConnectToSource(shader_out)
shader_prim.GetImplementationSourceAttr().Set(UsdShade.Tokens.sourceAsset)
shader_prim.SetSourceAsset(Sdf.AssetPath("OmniPBR.mdl"), "mdl")
shader_prim.SetSourceAssetSubIdentifier("OmniPBR", "mdl")

omni.usd.create_material_input(
mat_prim,
"diffuse_color_constant",
Gf.Vec3f(1,0,0),
Sdf.ValueTypeNames.Color3f,
)
omni.usd.create_material_input(
mat_prim,
"emissive_color",
Gf.Vec3f(1,0,0),
Sdf.ValueTypeNames.Color3f,
)
```
Material color shading is complicated. After creating the prim and appropriate attributes, you must link those attributes and properties together to form a `shader graph` that is processed to produce the desired material effect. After it’s created, the material can then be bound to the prim, thus changing its apparent color in the viewport.

```
#bind the material
material = UsdShade.Material(material_prim)
binding_api = UsdShade.MaterialBindingAPI.Apply(sphere)
binding_api.Bind(material)
```
If you save the stage and examine the USDA file, you can see the material.

```
#usda 1.0

def Material "material"
{
token outputs:mdl:displacement.connect = </hello/material/Shader.outputs:out>
token outputs:mdl:surface.connect = </hello/material/Shader.outputs:out>
token outputs:mdl:volume.connect = </hello/material/Shader.outputs:out>

def Shader "Shader"
{
uniform token info:implementationSource = "sourceAsset"
uniform asset info:mdl:sourceAsset = @OmniPBR.mdl@
uniform token info:mdl:sourceAsset:subIdentifier = "OmniPBR"
color3f inputs:diffuse_color_constant = (1, 0, 0) (
customData = {
float3 default = (0.2, 0.2, 0.2)
}
displayGroup = "Albedo"
displayName = "Albedo Color"
doc = "This is the albedo base color"
hidden = false
renderType = "color"
)
color3f inputs:emissive_color = (1, 0, 0) (
customData = {
float3 default = (1, 0.1, 0.1)
}
displayGroup = "Emissive"
displayName = "Emissive Color"
doc = "The emission color"
hidden = false
renderType = "color"
)
token outputs:out
}
}
```
and specifically, the `diffuse_color_constant` attribute type. To directly modify this attribute to change the color of our sphere:

```
new_shader = UsdShade.Shader.Get(stage, "/hello/material/Shader")
new_shader.GetInput("diffuse_color_constant").Set(Gf.Vec3f(0,0,1))
```
Of course, this level of direct manipulation of USD can become tedious. For situations like this, there are a set of predefined commands through the kit API, which dramatically simplifies working with USD in code. For example, you could have done the following instead:

```
import omni.kit.commands

omni.kit.commands.execute('CreateAndBindMdlMaterialFromLibrary',
mdl_name='OmniSurface.mdl',
mtl_name='OmniSurface',
mtl_created_list=['/Looks/OmniSurface'])

new_material = UsdShade.Material.Get(stage, "/Looks/OmniSurface")

binding_api = UsdShade.MaterialBindingAPI.Apply(sphere)
binding_api.Bind(new_material)
```

## Further Reading
For a complete tutorial on USD, see the openUSD tutorials . With a few tweaks, as shown on the basic examples above, these tutorials can be run from the Script editor or in the Isaac Python shell .
For more in-depth content, see guided learning content or the independent learning .

## Units in USD
By default, Isaac Sim USD uses the following default units:

[TABLE]
Unit | Default
Distance | meters (m)
Time | seconds (s)
Mass | Kilogram (kg)
Angle | Degrees
[/TABLE]
For more Isaac Sim conventions, see Isaac Sim Conventions .
There are cases when assets coming from different apps follow a different standard. By default, Isaac Sim has enabled the Metrics Assembler , which automatically converts the asset scale for the distance unit, mass unit, and Up Axis.
For more details about how USD handles units, see Units in USD .

## Useful USD Snippets
Here are some useful snippets that can be useful when dealing with USD in code. These snippets assume that `stage` and `prim`: are respectively pxr.UsdStage and pxr.UsdPrim types, and if any additional type is used, the necessary imports are included in the snippet.

### Traversing Stage or Prim

```
1# For stage traversal there's a built-in method:
2for a in stage.Traverse():
3 do_something(a)
4
5# For prim, it's not the same method though
6from pxr import Usd
7
8prim = stage.GetDefaultPrim()
9for a in Usd.PrimRange(prim):
10 do_something(a)
```

### Working with Multiple Layers

```
1from pxr import Sdf
2
3# Get References to all layers
4root_layer = stage.GetRootLayer()
5session_layer = stage.GetSessionLayer()
6
7# Add a SubLayer to the Root Layer
8additional_layer = layer = Sdf.Layer.FindOrOpen("my_layer.usd")
9root_layer.subLayerPaths.append(additional_layer.identifier)
10
11# Set Edit Layer
12# Method 1
13with Usd.EditContext(stage, root_layer):
14 do_something()
15
16# Method 2
17stage.SetEditTarget(additional_layer)
18
19
20# Make non-persistent changes to the stage (won't be saved regardless if you call stage.Save)
21
22with Usd.EditContext(stage, session_layer):
23 do_something()
```

### Converting Transform Pose in Position, Orient, Scale
Note
You can use this to create a set_pose method that receives a transform and applies to the prim.

```
1from pxr import Gf, Usd, UsdGeom
2
3def convert_ops_from_transform(prim:pxr.UsdPrim):
4
5 # Get the Xformable from prim
6 xform = UsdGeom.Xformable(prim)
7
8 # Gets local transform matrix - used to convert the Xform Ops.
9 pose = omni.usd.get_local_transform_matrix(prim)
10
11 # Compute Scale
12 x_scale = Gf.Vec3d(pose[0][0], pose[0][1], pose[0][2]).GetLength()
13 y_scale = Gf.Vec3d(pose[1][0], pose[1][1], pose[1][2]).GetLength()
14 z_scale = Gf.Vec3d(pose[2][0], pose[2][1], pose[2][2]).GetLength()
15
16 # Clear Transforms from xform.
17 xform.ClearXformOpOrder()
18
19 # Add the Transform, orient, scale set
20 xform_op_t = xform.AddXformOp(UsdGeom.XformOp.TypeTranslate, UsdGeom.XformOp.PrecisionDouble, "")
21 xform_op_r = xform.AddXformOp(UsdGeom.XformOp.TypeOrient, UsdGeom.XformOp.PrecisionDouble, "")
22 xform_op_s = xform.AddXformOp(UsdGeom.XformOp.TypeScale, UsdGeom.XformOp.PrecisionDouble, "")
23
24 xform_op_t.Set(pose.ExtractTranslation())
25 xform_op_r.Set(pose.ExtractRotationQuat().GetNormalized())
26 xform_op_s.Set(Gf.Vec3d(x_scale, y_scale, z_scale))
```
