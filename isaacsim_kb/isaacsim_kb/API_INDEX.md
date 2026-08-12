# Isaac Sim 5.1 Python API 색인 (자동 생성)

`py/**.html` 1,121개 문서에서 추출한 클래스/함수/메서드 시그니처. 모듈 → 클래스 → 멤버 순.
설명 본문은 `text/py/**.md` 또는 원문 HTML 참조.


## isaacsim.asset.gen.omap.bindings._omap

### Generator
- [class] class Generator
- [method] __init__(self: isaacsim.asset.gen.omap.bindings._omap.Generator, arg0: omni::physx::IPhysx, arg1: int)
- [method] generate2d(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] generate3d(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] get_buffer(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] get_colored_byte_buffer(self: isaacsim.asset.gen.omap.bindings._omap.Generator, arg0: carb::Int4, arg1: carb::Int4, arg2: carb::Int4)
- [method] get_dimensions(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] get_free_positions(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] get_max_bound(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] get_min_bound(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] get_occupied_positions(self : isaacsim.asset.gen.omap.bindings._omap.Generator)
- [method] set_transform(self: isaacsim.asset.gen.omap.bindings._omap.Generator, arg0: carb::Float3, arg1: carb::Float3, arg2: carb::Float3)
- [method] update_settings(self : isaacsim.asset.gen.omap.bindings._omap.Generator, arg0 : float, arg1 : float, arg2 : float, arg3 : float)
- [attribute] None

## isaacsim.asset.importer.mjcf._mjcf

### ImportConfig
- [class] class ImportConfig
- [method] set_convex_decomp(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_create_body_for_fixed_joint(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_create_physics_scene(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_default_drive_strength(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : float)
- [method] set_density(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : float)
- [method] set_distance_scale(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : float)
- [method] set_fix_base(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_import_inertia_tensor(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_import_sites(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_instanceable_usd_path(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : str)
- [method] set_make_default_prim(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_make_instanceable(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_merge_fixed_joints(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_override_com(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_override_inertia(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_self_collision(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [method] set_visualize_collision_geoms(self : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, arg0 : bool)
- [property] property convex_decomp
- [property] property create_body_for_fixed_joint
- [property] property create_physics_scene
- [property] property default_drive_strength
- [property] property density
- [property] property distance_scale
- [property] property fix_base
- [property] property import_inertia_tensor
- [property] property instanceable_usd_path
- [property] property make_default_prim
- [property] property make_instanceable
- [property] property merge_fixed_joints
- [property] property override_com
- [property] property override_inertia_tensor
- [property] property self_collision

### Mjcf
- [class] class Mjcf
- [method] create_asset_mjcf(self : isaacsim.asset.importer.mjcf._mjcf.Mjcf, fileName : str, primName : str, config : isaacsim.asset.importer.mjcf._mjcf.ImportConfig, stage_identifier : str = '')

## isaacsim.asset.importer.mjcf.impl.commands

### MJCFCreateAsset
- [class] class MJCFCreateAsset ( * args : Any , ** kwargs : Any )

### MJCFCreateImportConfig
- [class] class MJCFCreateImportConfig ( * args : Any , ** kwargs : Any )

## isaacsim.asset.importer.urdf._urdf

### ImportConfig
- [class] class ImportConfig
- [method] set_collision_from_visuals(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_convex_decomp(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_create_physics_scene(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_default_drive_strength(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : float)
- [method] set_default_drive_type(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : int)
- [method] set_default_position_drive_damping(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : float)
- [method] set_density(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : float)
- [method] set_distance_scale(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : float)
- [method] set_fix_base(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_import_inertia_tensor(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_make_default_prim(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_merge_fixed_joints(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_override_joint_dynamics(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_parse_mimic(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_replace_cylinders_with_capsules(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_self_collision(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : bool)
- [method] set_subdivision_scheme(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : int)
- [method] set_up_vector(self : isaacsim.asset.importer.urdf._urdf.ImportConfig, arg0 : float, arg1 : float, arg2 : float)
- [property] property collision_from_visuals
- [property] property convex_decomp
- [property] property create_physics_scene
- [property] property default_drive_strength
- [property] property default_drive_type
- [property] property default_position_drive_damping
- [property] property density
- [property] property distance_scale
- [property] property fix_base
- [property] property import_inertia_tensor
- [property] property make_default_prim
- [property] property merge_fixed_joints
- [property] property override_joint_dynamics
- [property] property parse_mimic
- [property] property replace_cylinders_with_capsules
- [property] property self_collision
- [property] property subdivision_scheme
- [property] property up_vector

### Urdf
- [class] class Urdf
- [method] compute_natural_stiffness(self : isaacsim.asset.importer.urdf._urdf.Urdf, arg0 : isaacsim.asset.importer.urdf._urdf.UrdfRobot, arg1 : str, arg2 : float)
- [method] get_kinematic_chain(self : isaacsim.asset.importer.urdf._urdf.Urdf, arg0 : isaacsim.asset.importer.urdf._urdf.UrdfRobot)
- [method] import_robot(self : isaacsim.asset.importer.urdf._urdf.Urdf, assetRoot : str, assetName : str, robot : isaacsim.asset.importer.urdf._urdf.UrdfRobot, importConfig : isaacsim.asset.importer.urdf._urdf.ImportConfig, stage : str = '', getArticulationRoot : bool = False)
- [method] parse_string_urdf(self : isaacsim.asset.importer.urdf._urdf.Urdf, arg0 : str, arg1 : isaacsim.asset.importer.urdf._urdf.ImportConfig)
- [method] parse_urdf(self : isaacsim.asset.importer.urdf._urdf.Urdf, arg0 : str, arg1 : str, arg2 : isaacsim.asset.importer.urdf._urdf.ImportConfig)

## isaacsim.asset.importer.urdf.impl.commands

### URDFCreateImportConfig
- [class] class URDFCreateImportConfig ( * args : Any , ** kwargs : Any )

### URDFImportRobot
- [class] class URDFImportRobot ( * args : Any , ** kwargs : Any )

### URDFParseAndImportFile
- [class] class URDFParseAndImportFile ( * args : Any , ** kwargs : Any )

### URDFParseFile
- [class] class URDFParseFile ( * args : Any , ** kwargs : Any )

### URDFParseText
- [class] class URDFParseText ( * args : Any , ** kwargs : Any )

## isaacsim.benchmark.services.base_isaac_benchmark

### BaseIsaacBenchmark
- [class] class BaseIsaacBenchmark(benchmark_name : str = 'BaseIsaacBenchmark', backend_type : str = 'OmniPerfKPIFile', report_generation : bool = True, workflow_metadata : dict = {}, gpu_frametime : bool = False)
- [method] fully_load_stage ( usd_path : str ) → None
- [method] set_phase(phase : str, start_recording_frametime : bool = True, start_recording_runtime : bool = True)
- [method] stop ( )
- [method] store_custom_measurement(phase_name: str, custom_measurement: <module 'isaacsim.benchmark.services.metrics.measurements' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.benchmark.services/isaacsim/benchmark/services/metrics/measurements.py'>)
- [method] store_measurements(stop_recording_time : bool = True)

## isaacsim.benchmark.services.base_isaac_benchmark_async

### BaseIsaacBenchmarkAsync
- [class] class BaseIsaacBenchmarkAsync ( * args : Any , ** kwargs : Any )
- [method] async fully_load_stage ( usd_path )
- [method] async setUp ( backend_type : str = 'JSONFileMetrics' )
- [method] set_phase(phase : str, start_recording_frametime : bool = True, start_recording_runtime : bool = True)
- [method] async store_custom_measurement(phase_name: str, custom_measurement: <module 'isaacsim.benchmark.services.metrics.measurements' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.benchmark.services/isaacsim/benchmark/services/metrics/measurements.py'>)
- [method] async store_measurements(stop_recording_time : bool = True)
- [method] async tearDown ( )

## isaacsim.core.api.controllers

### ArticulationController
- [class] class ArticulationController
- [method] apply_action(control_actions : ArticulationAction)
- [method] get_applied_action ( ) → ArticulationAction
- [method] get_effort_modes ( ) → List [ str ]
- [method] get_gains ( ) → Tuple [ ndarray , ndarray ]
- [method] get_joint_limits ( ) → Tuple [ ndarray , ndarray ]
- [method] get_max_efforts ( ) → ndarray
- [method] initialize ( articulation_view ) → None
- [method] set_effort_modes(mode : str, joint_indices : ndarray | list | None = None)
- [method] set_gains(kps : ndarray | None = None, kds : ndarray | None = None, save_to_usd : bool = False)
- [method] set_max_efforts(values : ndarray, joint_indices : ndarray | list | None = None)
- [method] switch_control_mode ( mode : str ) → None
- [method] switch_dof_control_mode(dof_index : int, mode : str)

### BaseController
- [class] class BaseController ( name : str )
- [method] abstract forward(* args, ** kwargs)
- [method] reset ( ) → None

### BaseGripperController
- [class] class BaseGripperController ( name : str )
- [method] abstract close(current_joint_positions : ndarray)
- [method] forward(action : str, current_joint_positions : ndarray)
- [method] abstract open(current_joint_positions : ndarray)
- [method] reset ( ) → None

## isaacsim.core.api.loggers

### DataLogger
- [class] class DataLogger
- [method] add_data(data : dict, current_time_step : float, current_time : float)
- [method] add_data_frame_logging_func(func : Callable [ [ List [ BaseTask ] , Scene ] , Dict ])
- [method] get_data_frame(data_frame_index : int)
- [method] get_num_of_data_frames ( ) → int
- [method] is_started ( ) → bool
- [method] load ( log_path : str ) → None
- [method] pause ( ) → None
- [method] reset ( ) → None
- [method] save ( log_path : str ) → None
- [method] start ( ) → None

## isaacsim.core.api.materials

### DeformableMaterial
- [class] class DeformableMaterial(prim_path : str, name : str | None = 'deformable_material', dynamic_friction : float | None = None, youngs_modulus : float | None = None, poissons_ratio : float | None = None, elasticity_damping : float | None = None, damping_scale : float | None = None)
- [method] get_damping_scale ( ) → float
- [method] get_dynamic_friction ( ) → float
- [method] get_elasticity_damping ( ) → float
- [method] get_poissons_ratio ( ) → float
- [method] get_youngs_modululs ( ) → float
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] post_reset ( ) → None
- [method] set_damping_scale ( value : float ) → None
- [method] set_dynamic_friction ( value : float ) → None
- [method] set_elasticity_damping ( value : float ) → None
- [method] set_poissons_ratio ( value : float ) → None
- [method] set_youngs_modululs ( value : float ) → None
- [property] property material : pxr.UsdShade.Material
- [property] property name : str | None
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### DeformableMaterialView
- [class] class DeformableMaterialView(prim_paths_expr : str, name : str = 'deformable_material_view', dynamic_frictions : ndarray | Tensor | None = None, youngs_moduli : ndarray | Tensor | None = None, poissons_ratios : ndarray | Tensor | None = None, elasticity_dampings : ndarray | Tensor | None = None, damping_scales : ndarray | Tensor | None = None)
- [method] get_damping_scales(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_dynamic_frictions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_elasticity_dampings(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_poissons_ratios(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_youngs_moduli(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | None = None)
- [method] post_reset ( ) → None
- [method] set_damping_scales(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_dynamic_frictions(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_elasticity_dampings(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_poissons_ratios(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_youngs_moduli(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [property] property count : int
- [property] property name : str

### OmniGlass
- [class] class OmniGlass(prim_path : str, name : str = 'omni_glass', shader : pxr.UsdShade.Shader | None = None, color : ndarray | None = None, ior : float | None = None, depth : float | None = None, thin_walled : bool | None = None)
- [method] get_color ( ) → ndarray | None
- [method] get_depth ( ) → float | None
- [method] get_ior ( ) → float | None
- [method] get_thin_walled ( ) → float | None
- [method] set_color ( color : ndarray ) → None
- [method] set_depth ( depth : float ) → None
- [method] set_ior ( ior : float ) → None
- [method] set_thin_walled ( thin_walled : float ) → None
- [property] property material : pxr.UsdShade.Material
- [property] property name : str
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property shaders_list : List [ pxr.UsdShade.Shader ]

### OmniPBR
- [class] class OmniPBR(prim_path : str, name : str = 'omni_pbr', shader : pxr.UsdShade.Shader | None = None, texture_path : str | None = None, texture_scale : ndarray | None = None, texture_translate : ndarray | None = None, color : ndarray | None = None)
- [method] get_color ( ) → ndarray
- [method] get_metallic_constant ( ) → float
- [method] get_project_uvw ( ) → bool
- [method] get_reflection_roughness ( ) → float
- [method] get_texture ( ) → str
- [method] get_texture_scale ( ) → ndarray
- [method] get_texture_translate ( ) → ndarray
- [method] set_color ( color : ndarray ) → None
- [method] set_metallic_constant ( amount : float ) → None
- [method] set_project_uvw ( flag : bool ) → None
- [method] set_reflection_roughness ( amount : float ) → None
- [method] set_texture ( path : str ) → None
- [method] set_texture_scale ( x : float , y : float ) → None
- [method] set_texture_translate ( x : float , y : float ) → None
- [property] property material : pxr.UsdShade.Material
- [property] property name : str
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property shaders_list : List [ pxr.UsdShade.Shader ]

### ParticleMaterial
- [class] class ParticleMaterial(prim_path : str, name : str | None = 'particle_material', friction : float | None = None, particle_friction_scale : float | None = None, damping : float | None = None, viscosity : float | None = None, vorticity_confinement : float | None = None, surface_tension : float | None = None, cohesion : float | None = None, adhesion : float | None = None, particle_adhesion_scale : float | None = None, adhesion_offset_scale : float | None = None, gravity_scale : float | None = None, lift : float | None = None, drag : float | None = None)
- [method] get_adhesion ( ) → float
- [method] get_adhesion_offset_scale ( ) → float
- [method] get_cohesion ( ) → float
- [method] get_damping ( ) → float
- [method] get_drag ( ) → float
- [method] get_friction ( ) → float
- [method] get_gravity_scale ( ) → float
- [method] get_lift ( ) → float
- [method] get_particle_adhesion_scale ( ) → float
- [method] get_particle_friction_scale ( ) → float
- [method] get_surface_tension ( ) → float
- [method] get_viscosity ( ) → float
- [method] get_vorticity_confinement ( ) → float
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] post_reset ( ) → None
- [method] set_adhesion ( value : float ) → None
- [method] set_adhesion_offset_scale ( value : float ) → None
- [method] set_cohesion ( value : float ) → None
- [method] set_damping ( value : float ) → None
- [method] set_drag ( value : float ) → None
- [method] set_friction ( value : float ) → None
- [method] set_gravity_scale ( value : float ) → None
- [method] set_lift ( value : float ) → None
- [method] set_particle_adhesion_scale ( value : float ) → None
- [method] set_particle_friction_scale ( value : float ) → None
- [method] set_surface_tension ( value : float ) → None
- [method] set_viscosity ( value : float ) → None
- [method] set_vorticity_confinement ( value : float ) → None
- [property] property material : pxr.UsdShade.Material
- [property] property name : str | None
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### ParticleMaterialView
- [class] class ParticleMaterialView(prim_paths_expr : str, name : str = 'particle_material_view', frictions : ndarray | Tensor | None = None, particle_friction_scales : ndarray | Tensor | None = None, dampings : ndarray | Tensor | None = None, viscosities : ndarray | Tensor | None = None, vorticity_confinements : ndarray | Tensor | None = None, surface_tensions : ndarray | Tensor | None = None, cohesions : ndarray | Tensor | None = None, adhesions : ndarray | Tensor | None = None, particle_adhesion_scales : ndarray | Tensor | None = None, adhesion_offset_scales : ndarray | Tensor | None = None, gravity_scales : ndarray | Tensor | None = None, lifts : ndarray | Tensor | None = None, drags : ndarray | Tensor | None = None)
- [method] get_adhesion_offset_scales(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_adhesions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_cohesions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_dampings(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_drags(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_frictions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_gravity_scales(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_lifts(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_particle_adhesion_scales(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_particle_friction_scales(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_surface_tensions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_viscosities(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_vorticity_confinements(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | None = None)
- [method] post_reset ( ) → None
- [method] set_adhesion_offset_scales(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_adhesions(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_cohesions(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_dampings(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_drags(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_frictions(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_gravity_scales(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_lifts(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_particle_adhesion_scales(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_particle_friction_scales(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_surface_tensions(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_viscosities(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_vorticity_confinements(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [property] property count : int
- [property] property name : str

### PhysicsMaterial
- [class] class PhysicsMaterial(prim_path : str, name : str = 'physics_material', static_friction : float | None = None, dynamic_friction : float | None = None, restitution : float | None = None)
- [method] get_dynamic_friction ( ) → float
- [method] get_restitution ( ) → float
- [method] get_static_friction ( ) → float
- [method] set_dynamic_friction ( friction : float ) → None
- [method] set_restitution ( restitution : float ) → None
- [method] set_static_friction ( friction : float ) → None
- [property] property material : pxr.UsdShade.Material
- [property] property name : str
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### PreviewSurface
- [class] class PreviewSurface(prim_path : str, name : str = 'preview_surface', shader : pxr.UsdShade.Shader | None = None, color : ndarray | None = None, roughness : float | None = None, metallic : float | None = None)
- [method] get_color ( ) → ndarray
- [method] get_metallic ( ) → float
- [method] get_roughness ( ) → float
- [method] set_color ( color : ndarray ) → None
- [method] set_metallic ( metallic : float ) → None
- [method] set_roughness ( roughness : float ) → None
- [property] property material : pxr.UsdShade.Material
- [property] property name : str
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property shaders_list : List [ pxr.UsdShade.Shader ]

### VisualMaterial
- [class] class VisualMaterial(name : str, prim_path : str, prim : pxr.Usd.Prim, shaders_list : List [ pxr.UsdShade.Shader ], material : pxr.UsdShade.Material)
- [property] property material : pxr.UsdShade.Material
- [property] property name : str
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property shaders_list : List [ pxr.UsdShade.Shader ]

## isaacsim.core.api.objects

### DynamicCapsule
- [class] class DynamicCapsule(prim_path : str, name : str = 'dynamic_capsule', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, height : ndarray | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None, mass : float | None = None, density : float | None = None, linear_velocity : Sequence [ float ] | None = None, angular_velocity : Sequence [ float ] | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] get_angular_velocity ( )
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_com ( ) → float
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → DynamicState
- [method] get_density ( ) → float
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] set_density ( density : float ) → None
- [method] set_height ( height : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### DynamicCone
- [class] class DynamicCone(prim_path : str, name : str = 'dynamic_cone', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, height : ndarray | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None, mass : float | None = None, density : float | None = None, linear_velocity : Sequence [ float ] | None = None, angular_velocity : Sequence [ float ] | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] get_angular_velocity ( )
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_com ( ) → float
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → DynamicState
- [method] get_density ( ) → float
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] set_density ( density : float ) → None
- [method] set_height ( height : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### DynamicCuboid
- [class] class DynamicCuboid(prim_path : str, name : str = 'dynamic_cube', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, size : float | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None, mass : float | None = None, density : float | None = None, linear_velocity : Sequence [ float ] | None = None, angular_velocity : Sequence [ float ] | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] get_angular_velocity ( )
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_com ( ) → float
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → DynamicState
- [method] get_density ( ) → float
- [method] get_friction_data(dt : float = 1.0)
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_rest_offset ( ) → float
- [method] get_size ( ) → ndarray
- [method] get_sleep_threshold ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] set_density ( density : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_size ( size : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### DynamicCylinder
- [class] class DynamicCylinder(prim_path : str, name : str = 'dynamic_cylinder', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, height : ndarray | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None, mass : float | None = None, density : float | None = None, linear_velocity : Sequence [ float ] | None = None, angular_velocity : Sequence [ float ] | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] get_angular_velocity ( )
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_com ( ) → float
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → DynamicState
- [method] get_density ( ) → float
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] set_density ( density : float ) → None
- [method] set_height ( height : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### DynamicSphere
- [class] class DynamicSphere(prim_path : str, name : str = 'dynamic_sphere', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None, mass : float | None = None, density : float | None = None, linear_velocity : Sequence [ float ] | None = None, angular_velocity : Sequence [ float ] | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] get_angular_velocity ( )
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_com ( ) → float
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → DynamicState
- [method] get_density ( ) → float
- [method] get_friction_data(dt : float = 1.0)
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] set_density ( density : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### FixedCapsule
- [class] class FixedCapsule(prim_path : str, name : str = 'fixed_capsule', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, height : float | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_height ( height : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### FixedCone
- [class] class FixedCone(prim_path : str, name : str = 'fixed_cone', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, height : float | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation ( approximation_type : str ) → None
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_height ( height : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### FixedCuboid
- [class] class FixedCuboid(prim_path : str, name : str = 'fixed_cube', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, size : float | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_rest_offset ( ) → float
- [method] get_size ( ) → ndarray
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_size ( size : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### FixedCylinder
- [class] class FixedCylinder(prim_path : str, name : str = 'fixed_cylinder', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, height : float | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_height ( height : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### FixedSphere
- [class] class FixedSphere(prim_path : str, name : str = 'fixed_sphere', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, radius : ndarray | None = None, visual_material : VisualMaterial | None = None, physics_material : PhysicsMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### GroundPlane
- [class] class GroundPlane(prim_path : str, name : str = 'ground_plane', size : float | None = None, z_position : float | None = None, scale : ndarray | None = None, visible : bool | None = None, color : ndarray | None = None, physics_material : PhysicsMaterial | None = None, visual_material : VisualMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_default_state ( ) → XFormPrimState
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] post_reset ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property collision_geometry_prim : SingleGeometryPrim
- [property] property name : str | None
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property xform_prim : SingleXFormPrim

### VisualCapsule
- [class] class VisualCapsule(prim_path : str, name : str = 'visual_capsule', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, color : ndarray | None = None, radius : float | None = None, height : float | None = None, visual_material : VisualMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_height ( height : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### VisualCone
- [class] class VisualCone(prim_path : str, name : str = 'visual_cone', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, color : ndarray | None = None, radius : float | None = None, height : float | None = None, visual_material : VisualMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_height ( height : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### VisualCuboid
- [class] class VisualCuboid(prim_path : str, name : str = 'visual_cube', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, color : ndarray | None = None, size : float | None = None, visual_material : VisualMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_rest_offset ( ) → float
- [method] get_size ( ) → ndarray
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_size ( size : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### VisualCylinder
- [class] class VisualCylinder(prim_path : str, name : str = 'visual_cylinder', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, color : ndarray | None = None, radius : float | None = None, height : float | None = None, visual_material : VisualMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_height ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_height ( height : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### VisualSphere
- [class] class VisualSphere(prim_path : str, name : str = 'visual_sphere', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = True, color : ndarray | None = None, radius : float | None = None, visual_material : VisualMaterial | None = None)
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_radius ( ) → float
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius ( radius : float ) → None
- [method] set_radius ( radius : float ) → None
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

## isaacsim.core.api.physics_context

### PhysicsContext
- [class] class PhysicsContext(physics_dt : float | None = None, prim_path : str = '/physicsScene', sim_params : dict = None, set_defaults : bool = True)
- [method] enable_ccd ( flag : bool ) → None
- [method] enable_fabric ( enable )
- [method] enable_gpu_dynamics ( flag : bool ) → None
- [method] enable_residual_reporting ( flag : bool )
- [method] enable_stablization ( flag : bool ) → None
- [method] get_bounce_threshold ( ) → float
- [method] get_broadphase_type ( ) → str
- [method] get_current_physics_scene_prim ( ) → pxr.Usd.Prim | None
- [method] get_enable_scene_query_support ( ) → bool
- [method] get_friction_correlation_distance ( ) → float
- [method] get_friction_offset_threshold ( ) → float
- [method] get_gpu_collision_stack_size ( ) → int
- [method] get_gpu_found_lost_aggregate_pairs_capacity ( ) → int
- [method] get_gpu_found_lost_pairs_capacity ( ) → int
- [method] get_gpu_heap_capacity ( ) → int
- [method] get_gpu_max_num_partitions ( ) → int
- [method] get_gpu_max_particle_contacts ( ) → int
- [method] get_gpu_max_rigid_contact_count ( ) → int
- [method] get_gpu_max_rigid_patch_count ( ) → int
- [method] get_gpu_max_soft_body_contacts ( ) → int
- [method] get_gpu_temp_buffer_capacity ( ) → int
- [method] get_gpu_total_aggregate_pairs_capacity ( ) → int
- [method] get_gravity ( ) → Tuple [ List , float ]
- [method] get_invert_collision_group_filter ( ) → int
- [method] get_physics_dt ( ) → float
- [method] get_physx_update_transformations_settings ( ) → Tuple [ bool , bool , bool , bool ]
- [method] get_solve_articulation_contact_last ( ) → bool
- [method] get_solver_position_residual ( report_max : bool = True )
- [method] get_solver_type ( ) → str
- [method] get_solver_velocity_residual ( report_max : bool = True )
- [method] is_ccd_enabled ( ) → bool
- [method] is_gpu_dynamics_enabled ( ) → bool
- [method] is_stablization_enabled ( ) → bool
- [method] set_bounce_threshold ( value : float ) → None
- [method] set_broadphase_type ( broadcast_type : str ) → None
- [method] set_enable_scene_query_support(enable_scene_query_support : bool)
- [method] set_friction_correlation_distance ( value : float ) → None
- [method] set_friction_offset_threshold ( value : float ) → None
- [method] set_gpu_collision_stack_size ( value : int ) → None
- [method] set_gpu_found_lost_aggregate_pairs_capacity(value : int)
- [method] set_gpu_found_lost_pairs_capacity ( value : int ) → None
- [method] set_gpu_heap_capacity ( value : int ) → None
- [method] set_gpu_max_num_partitions ( value : int ) → None
- [method] set_gpu_max_particle_contacts ( value : int ) → None
- [method] set_gpu_max_rigid_contact_count ( value : int ) → None
- [method] set_gpu_max_rigid_patch_count ( value : int ) → None
- [method] set_gpu_max_soft_body_contacts ( value : int ) → None
- [method] set_gpu_temp_buffer_capacity ( value : int ) → None
- [method] set_gpu_total_aggregate_pairs_capacity(value : int)
- [method] set_gravity ( value : float ) → None
- [method] set_invert_collision_group_filter(invert_collision_group_filter : bool)
- [method] set_physics_dt(dt : float = 0.016666666666666666, substeps : int = 1)
- [method] set_physx_update_transformations_settings(update_to_usd : bool | None = None, update_velocities_to_usd : bool | None = None, output_velocities_local_space : bool | None = None)
- [method] set_solve_articulation_contact_last(solve_articulation_contact_last : bool)
- [method] set_solver_type ( solver_type : str ) → None
- [method] warm_start ( )
- [property] property device : str
- [property] property prim_path
- [property] property use_fabric
- [property] property use_gpu_pipeline
- [property] property use_gpu_sim

## isaacsim.core.api.robots

### Robot
- [class] class Robot(prim_path : str, name : str = 'robot', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool = True, articulation_controller : ArticulationController | None = None)
- [method] apply_action(control_actions : ArticulationAction)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_gravity ( ) → None
- [method] enable_gravity ( ) → None
- [method] get_angular_velocity ( ) → ndarray
- [method] get_applied_action ( ) → ArticulationAction
- [method] get_applied_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_articulation_body_count ( ) → int
- [method] get_articulation_controller ( ) → ArticulationController
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_enabled_self_collisions ( ) → int
- [method] get_joint_positions(joint_indices : List | ndarray | None = None)
- [method] get_joint_velocities(joint_indices : List | ndarray | None = None)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_measured_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_measured_joint_forces(joint_indices : List | ndarray | None = None)
- [method] get_position_residual ( report_max : bool | None = True ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_solver_velocity_iteration_count ( ) → int
- [method] get_stabilization_threshold ( ) → float
- [method] get_velocity_residual ( report_max : bool | None = True ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] get_world_velocity ( ) → ndarray
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_enabled_self_collisions ( flag : bool ) → None
- [method] set_joint_efforts(efforts : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_positions(positions : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_velocities(velocities : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joints_default_state(positions : ndarray | None = None, velocities : ndarray | None = None, efforts : ndarray | None = None)
- [method] set_linear_velocity ( velocity : ndarray ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale ( scale : Sequence [ float ] | None ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_solver_position_iteration_count ( count : int ) → None
- [method] set_solver_velocity_iteration_count ( count : int )
- [method] set_stabilization_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_world_velocity ( velocity : ndarray )
- [property] property dof_names : List [ str ]
- [property] property dof_properties : ndarray
- [property] property handles_initialized : bool
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### RobotView
- [class] class RobotView(prim_paths_expr : str, name : str = 'rigid_prim_view', positions : ndarray | Tensor | None = None, translations : ndarray | Tensor | None = None, orientations : ndarray | Tensor | None = None, scales : ndarray | Tensor | None = None, visibilities : ndarray | Tensor | None = None)
- [method] apply_action(control_actions : ArticulationActions, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] get_angular_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_applied_actions(clone : bool = True)
- [method] get_applied_joint_efforts(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_armatures(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_articulation_body_count ( ) → int
- [method] get_body_coms(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_disable_gravity(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_index ( body_name : str ) → int
- [method] get_body_inertias(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_inv_inertias(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_inv_masses(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_masses(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_coriolis_and_centrifugal_forces(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_dof_limits ( ) → ndarray | Tensor
- [method] get_dof_types(dof_names : List [ str ] = None)
- [method] get_drive_types ( ) → ndarray | Tensor
- [method] get_effort_modes(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] get_enabled_self_collisions(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_fixed_tendon_dampings(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_limit_stiffnesses(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_limits(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_offsets(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_rest_lengths(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_stiffnesses(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_friction_coefficients(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_gains(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_generalized_gravity_forces(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_jacobian_shape ( ) → ndarray | Tensor | warp.array
- [method] get_jacobians(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_joint_index ( joint_name : str ) → int
- [method] get_joint_max_velocities(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_joint_positions(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_joint_velocities(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone = True)
- [method] get_link_index ( link_name : str ) → int
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_mass_matrices(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_mass_matrix_shape ( ) → ndarray | Tensor | warp.array
- [method] get_max_efforts(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_measured_joint_efforts(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_measured_joint_forces(indices : ndarray | List | Tensor | None = None, joint_indices : ndarray | List | Tensor | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_position_residuals(indices : ndarray | list | Tensor | warp.array | None = None, report_max : bool = True)
- [method] get_sleep_thresholds(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_solver_position_iteration_counts(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_solver_velocity_iteration_counts(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_stabilization_thresholds(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_velocity_residuals(indices : ndarray | list | Tensor | warp.array | None = None, report_max : bool = True)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] pause_motion ( ) → None
- [method] post_reset ( ) → None
- [method] resume_motion ( )
- [method] set_angular_velocities(velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_armatures(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_body_coms(positions : ndarray | Tensor | warp.array = None, orientations : ndarray | Tensor | warp.array = None, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_body_disable_gravity(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_body_inertias(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_body_masses(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_effort_modes(mode : str, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | None = None, joint_names : List [ str ] | None = None)
- [method] set_enabled_self_collisions(flags : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_fixed_tendon_properties(stiffnesses : ndarray | Tensor | warp.array = None, dampings : ndarray | Tensor | warp.array = None, limit_stiffnesses : ndarray | Tensor | warp.array = None, limits : ndarray | Tensor | warp.array = None, rest_lengths : ndarray | Tensor | warp.array = None, offsets : ndarray | Tensor | warp.array = None, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_friction_coefficients(values : ndarray | Tensor, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_gains(kps : ndarray | Tensor | warp.array | None = None, kds : ndarray | Tensor | warp.array | None = None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, save_to_usd : bool = False)
- [method] set_joint_efforts(efforts : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_position_targets(positions : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_positions(positions : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_velocities(velocities : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_velocity_targets(velocities : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joints_default_state(positions : ndarray | Tensor | warp.array | None = None, velocities : ndarray | Tensor | warp.array | None = None, efforts : ndarray | Tensor | warp.array | None = None)
- [method] set_linear_velocities(velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_max_efforts(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_max_joint_velocities(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_sleep_thresholds(thresholds : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_solver_position_iteration_counts(counts : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_solver_velocity_iteration_counts(counts : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_stabilization_thresholds(thresholds : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_velocities(velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] switch_control_mode(mode : str, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] switch_dof_control_mode(mode : str, dof_index : int, indices : ndarray | List | Tensor | warp.array | None = None)
- [property] property body_names : List [ str ]
- [property] property count : int
- [property] property dof_names : List [ str ]
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property joint_names : List [ str ]
- [property] property name : str
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property num_fixed_tendons : int
- [property] property num_joints : int
- [property] property num_shapes : int
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

## isaacsim.core.api.scenes

### Scene
- [class] class Scene
- [method] add(obj : SingleXFormPrim)
- [method] add_default_ground_plane(z_position : float = 0, name = 'default_ground_plane', prim_path : str = '/World/defaultGroundPlane', static_friction : float = 0.5, dynamic_friction : float = 0.5, restitution : float = 0.8)
- [method] add_ground_plane(size : float | None = None, z_position : float = 0, name = 'ground_plane', prim_path : str = '/World/groundPlane', static_friction : float = 0.5, dynamic_friction : float = 0.5, restitution : float = 0.8, color : ndarray | None = None)
- [method] clear ( registry_only : bool = False ) → None
- [method] compute_object_AABB(name : str)
- [method] disable_bounding_boxes_computations ( ) → None
- [method] enable_bounding_boxes_computations ( ) → None
- [method] get_object(name : str)
- [method] object_exists ( name : str ) → bool
- [method] post_reset ( ) → None
- [method] remove_object ( name : str , registry_only : bool = False ) → None
- [property] property stage : pxr.Usd.Stage

### SceneRegistry
- [class] class SceneRegistry
- [method] add_articulated_system(name : str, articulated_system : SingleArticulation)
- [method] add_articulated_view(name : str, articulated_view : Articulation)
- [method] add_cloth(name : str, cloth : SingleClothPrim)
- [method] add_cloth_view(name : str, cloth_prim_view : ClothPrim)
- [method] add_deformable(name : str, deformable : SingleDeformablePrim)
- [method] add_deformable_material(name : str, deformable_material : DeformableMaterial)
- [method] add_deformable_material_view(name : str, deformable_material_view : DeformableMaterialView)
- [method] add_deformable_view(name : str, deformable_prim_view : DeformablePrim)
- [method] add_geometry_object(name : str, geometry_object : SingleGeometryPrim)
- [method] add_geometry_prim_view(name : str, geometry_prim_view : GeometryPrim)
- [method] add_particle_material(name : str, particle_material : ParticleMaterial)
- [method] add_particle_material_view(name : str, particle_material_view : ParticleMaterialView)
- [method] add_particle_system(name : str, particle_system : SingleParticleSystem)
- [method] add_particle_system_view(name : str, particle_system_view : ParticleSystem)
- [method] add_rigid_contact_view(name : str, rigid_contact_view : RigidContactView)
- [method] add_rigid_object(name : str, rigid_object : SingleRigidPrim)
- [method] add_rigid_prim_view(name : str, rigid_prim_view : RigidPrim)
- [method] add_robot(name : str, robot : Robot)
- [method] add_robot_view(name : str, robot_view : RobotView)
- [method] add_sensor(name : str, sensor : BaseSensor)
- [method] add_xform(name : str, xform : SingleXFormPrim)
- [method] add_xform_view(name : str, xform_prim_view : XFormPrim)
- [method] get_object(name : str)
- [method] name_exists ( name : str ) → bool
- [method] remove_object ( name : str ) → None
- [property] property articulated_systems : dict
- [property] property articulated_views : dict
- [property] property cloth_prim_views : dict
- [property] property cloth_prims : dict
- [property] property deformable_material_views : dict
- [property] property deformable_materials : dict
- [property] property deformable_prim_views : dict
- [property] property deformable_prims : dict
- [property] property geometry_prim_views : dict
- [property] property particle_material_views : dict
- [property] property particle_materials : dict
- [property] property particle_system_views : dict
- [property] property particle_systems : dict
- [property] property rigid_contact_views : dict
- [property] property rigid_objects : dict
- [property] property rigid_prim_views : dict
- [property] property robot_views : dict
- [property] property robots : dict
- [property] property sensors : dict
- [property] property xform_prim_views : dict
- [property] property xforms : dict

## isaacsim.core.api.sensors

### BaseSensor
- [class] class BaseSensor(prim_path : str, name : str = 'base_sensor', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_default_state ( ) → XFormPrimState
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### RigidContactView
- [class] class RigidContactView(prim_paths_expr : str | List [ str ], filter_paths_expr : List [ str ] | List [ List [ str ] ], name : str = 'rigid_contact_view', prepare_contact_sensors : bool = True, disable_stablization : bool = True, max_contact_count : int = 0)
- [method] get_contact_force_data(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_contact_force_matrix(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_friction_data(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_net_contact_forces(indices : ndarray | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [property] property num_filters : int
- [property] property num_shapes : int

## isaacsim.core.api.simulation_context

### SimulationContext
- [class] class SimulationContext ( * args , ** kwargs )
- [method] add_physics_callback(callback_name : str, callback_fn : Callable [ [ float ] , None ])
- [method] add_render_callback(callback_name : str, callback_fn : Callable)
- [method] add_stage_callback(callback_name : str, callback_fn : Callable)
- [method] add_timeline_callback(callback_name : str, callback_fn : Callable)
- [method] clear ( ) → None
- [method] clear_all_callbacks ( ) → None
- [method] classmethod clear_instance ( ) → None
- [method] clear_physics_callbacks ( ) → None
- [method] clear_render_callbacks ( ) → None
- [method] clear_stage_callbacks ( ) → None
- [method] clear_timeline_callbacks ( ) → None
- [method] get_block_on_render ( ) → bool
- [method] get_physics_context ( ) → PhysicsContext
- [method] get_physics_dt ( ) → float
- [method] get_rendering_dt ( ) → float
- [method] initialize_physics ( ) → None
- [method] async initialize_simulation_context_async ( ) → None
- [method] classmethod instance ( ) → SimulationContext
- [method] is_playing ( ) → bool
- [method] is_simulating ( ) → bool
- [method] is_stopped ( ) → bool
- [method] pause ( ) → None
- [method] async pause_async ( ) → None
- [method] physics_callback_exists ( callback_name : str ) → bool
- [method] play ( ) → None
- [method] async play_async ( ) → None
- [method] remove_physics_callback ( callback_name : str ) → None
- [method] remove_render_callback ( callback_name : str ) → None
- [method] remove_stage_callback ( callback_name : str ) → None
- [method] remove_timeline_callback ( callback_name : str ) → None
- [method] render ( ) → None
- [method] async render_async ( ) → None
- [method] render_callback_exists ( callback_name : str ) → bool
- [method] reset ( soft : bool = False ) → None
- [method] async reset_async ( soft : bool = False ) → None
- [method] set_block_on_render ( block : bool ) → None
- [method] set_simulation_dt(physics_dt : float | None = None, rendering_dt : float | None = None)
- [method] skip_next_stage_open_callback ( )
- [method] stage_callback_exists ( callback_name : str ) → bool
- [method] step(render : bool = True, update_fabric : bool = False)
- [method] stop ( ) → None
- [method] async stop_async ( ) → None
- [method] timeline_callback_exists ( callback_name : str ) → bool
- [property] property app : omni.kit.app.IApp
- [property] property backend : str
- [property] property backend_utils
- [property] property current_time : float
- [property] property current_time_step_index : int
- [property] property device : str
- [property] property physics_sim_view
- [property] property stage : pxr.Usd.Stage

## isaacsim.core.api.tasks

### BaseTask
- [class] class BaseTask ( name : str , offset : ndarray | None = None )
- [method] calculate_metrics ( ) → dict
- [method] cleanup ( ) → None
- [method] get_description ( ) → str
- [method] get_observations ( ) → dict
- [method] get_params ( ) → dict
- [method] get_task_objects ( ) → dict
- [method] is_done ( ) → bool
- [method] post_reset ( ) → None
- [method] pre_step(time_step_index : int, simulation_time : float)
- [method] set_params ( * args , ** kwargs ) → None
- [method] set_up_scene(scene : Scene)
- [property] property device
- [property] property name : str
- [property] property scene : Scene

### FollowTarget
- [class] class FollowTarget(name : str, target_prim_path : str | None = None, target_name : str | None = None, target_position : ndarray | None = None, target_orientation : ndarray | None = None, offset : ndarray | None = None)
- [method] add_obstacle ( position : ndarray = None )
- [method] calculate_metrics ( ) → dict
- [method] cleanup ( ) → None
- [method] get_description ( ) → str
- [method] get_observations ( ) → dict
- [method] get_obstacle_to_delete ( ) → None
- [method] get_params ( ) → dict
- [method] get_task_objects ( ) → dict
- [method] is_done ( ) → bool
- [method] obstacles_exist ( ) → bool
- [method] post_reset ( ) → None
- [method] pre_step(time_step_index : int, simulation_time : float)
- [method] remove_obstacle ( name : str | None = None ) → None
- [method] set_params(target_prim_path : str | None = None, target_name : str | None = None, target_position : ndarray | None = None, target_orientation : ndarray | None = None)
- [method] abstract set_robot ( ) → None
- [method] set_up_scene(scene : Scene)
- [method] target_reached ( ) → bool
- [property] property device
- [property] property name : str
- [property] property scene : Scene

### PickPlace
- [class] class PickPlace(name : str, cube_initial_position : ndarray | None = None, cube_initial_orientation : ndarray | None = None, target_position : ndarray | None = None, cube_size : ndarray | None = None, offset : ndarray | None = None)
- [method] calculate_metrics ( ) → dict
- [method] cleanup ( ) → None
- [method] get_description ( ) → str
- [method] get_observations ( ) → dict
- [method] get_params ( ) → dict
- [method] get_task_objects ( ) → dict
- [method] is_done ( ) → bool
- [method] post_reset ( ) → None
- [method] pre_step(time_step_index : int, simulation_time : float)
- [method] set_params(cube_position : ndarray | None = None, cube_orientation : ndarray | None = None, target_position : ndarray | None = None)
- [method] abstract set_robot ( ) → None
- [method] set_up_scene(scene : Scene)
- [property] property device
- [property] property name : str
- [property] property scene : Scene

### Stacking
- [class] class Stacking(name : str, cube_initial_positions : ndarray, cube_initial_orientations : ndarray | None = None, stack_target_position : ndarray | None = None, cube_size : ndarray | None = None, offset : ndarray | None = None)
- [method] calculate_metrics ( ) → dict
- [method] cleanup ( ) → None
- [method] get_cube_names ( ) → List [ str ]
- [method] get_description ( ) → str
- [method] get_observations ( ) → dict
- [method] get_params ( ) → dict
- [method] get_task_objects ( ) → dict
- [method] is_done ( ) → bool
- [method] post_reset ( ) → None
- [method] pre_step(time_step_index : int, simulation_time : float)
- [method] set_params(cube_name : str | None = None, cube_position : str | None = None, cube_orientation : str | None = None, stack_target_position : str | None = None)
- [method] abstract set_robot ( ) → None
- [method] set_up_scene(scene : Scene)
- [property] property device
- [property] property name : str
- [property] property scene : Scene

## isaacsim.core.api.world

### World
- [class] class World ( * args , ** kwargs )
- [method] add_physics_callback(callback_name : str, callback_fn : Callable [ [ float ] , None ])
- [method] add_render_callback(callback_name : str, callback_fn : Callable)
- [method] add_stage_callback(callback_name : str, callback_fn : Callable)
- [method] add_task(task : BaseTask)
- [method] add_timeline_callback(callback_name : str, callback_fn : Callable)
- [method] calculate_metrics ( task_name : str | None = None ) → None
- [method] clear ( ) → None
- [method] clear_all_callbacks ( ) → None
- [method] classmethod clear_instance ( )
- [method] clear_physics_callbacks ( ) → None
- [method] clear_render_callbacks ( ) → None
- [method] clear_stage_callbacks ( ) → None
- [method] clear_timeline_callbacks ( ) → None
- [method] get_block_on_render ( ) → bool
- [method] get_current_tasks ( ) → List [ BaseTask ]
- [method] get_data_logger ( ) → DataLogger
- [method] get_observations ( task_name : str | None = None ) → dict
- [method] get_physics_context ( ) → PhysicsContext
- [method] get_physics_dt ( ) → float
- [method] get_rendering_dt ( ) → float
- [method] get_task(name : str)
- [method] initialize_physics ( ) → None
- [method] async initialize_simulation_context_async ( ) → None
- [method] classmethod instance ( ) → SimulationContext
- [method] is_done ( task_name : str | None = None ) → bool
- [method] is_playing ( ) → bool
- [method] is_simulating ( ) → bool
- [method] is_stopped ( ) → bool
- [method] is_tasks_scene_built ( ) → bool
- [method] pause ( ) → None
- [method] async pause_async ( ) → None
- [method] physics_callback_exists ( callback_name : str ) → bool
- [method] play ( ) → None
- [method] async play_async ( ) → None
- [method] remove_physics_callback ( callback_name : str ) → None
- [method] remove_render_callback ( callback_name : str ) → None
- [method] remove_stage_callback ( callback_name : str ) → None
- [method] remove_timeline_callback ( callback_name : str ) → None
- [method] render ( ) → None
- [method] async render_async ( ) → None
- [method] render_callback_exists ( callback_name : str ) → bool
- [method] reset ( soft : bool = False ) → None
- [method] async reset_async ( soft : bool = False ) → None
- [method] async reset_async_no_set_up_scene ( soft : bool = False ) → None
- [method] async reset_async_set_up_scene ( soft : bool = False ) → None
- [method] set_block_on_render ( block : bool ) → None
- [method] set_simulation_dt(physics_dt : float | None = None, rendering_dt : float | None = None)
- [method] skip_next_stage_open_callback ( )
- [method] stage_callback_exists ( callback_name : str ) → bool
- [method] step(render : bool = True, step_sim : bool = True, update_fabric : bool = False)
- [method] step_async ( step_size : float | None = None ) → None
- [method] stop ( ) → None
- [method] async stop_async ( ) → None
- [method] timeline_callback_exists ( callback_name : str ) → bool
- [property] property app : omni.kit.app.IApp
- [property] property backend : str
- [property] property backend_utils
- [property] property current_time : float
- [property] property current_time_step_index : int
- [property] property device : str
- [property] property physics_sim_view
- [property] property scene : Scene
- [property] property stage : pxr.Usd.Stage

## isaacsim.core.cloner

### Cloner
- [class] class Cloner ( stage : pxr.Usd.Stage = None )
- [method] clone(source_prim_path : str, prim_paths : List [ str ], positions : ndarray | Tensor = None, orientations : ndarray | Tensor = None, replicate_physics : bool = False, base_env_path : str = None, root_path : str = None, copy_from_source : bool = False, unregister_physics_replication : bool = False, enable_env_ids : bool = False, clone_in_fabric : bool = False)
- [method] define_base_env ( base_env_path : str )
- [method] disable_change_listener ( )
- [method] enable_change_listener ( )
- [method] filter_collisions(physicsscene_path : str, collision_root_path : str, prim_paths : List [ str ], global_paths : List [ str ] = [])
- [method] generate_paths ( root_path : str , num_paths : int )
- [method] replicate_physics(source_prim_path : str, prim_paths : list, base_env_path : str, root_path : str, enable_env_ids : bool = False, clone_in_fabric : bool = False)

### GridCloner
- [class] class GridCloner(spacing : float, num_per_row : int = -1, stage : pxr.Usd.Stage = None)
- [method] clone(source_prim_path : str, prim_paths : List [ str ], position_offsets : ndarray = None, orientation_offsets : ndarray = None, replicate_physics : bool = False, base_env_path : str = None, root_path : str = None, copy_from_source : bool = False, enable_env_ids : bool = False, clone_in_fabric : bool = False)
- [method] define_base_env ( base_env_path : str )
- [method] disable_change_listener ( )
- [method] enable_change_listener ( )
- [method] filter_collisions(physicsscene_path : str, collision_root_path : str, prim_paths : List [ str ], global_paths : List [ str ] = [])
- [method] generate_paths ( root_path : str , num_paths : int )
- [method] get_clone_transforms(num_clones : int, position_offsets : ndarray = None, orientation_offsets : ndarray = None)
- [method] replicate_physics(source_prim_path : str, prim_paths : list, base_env_path : str, root_path : str, enable_env_ids : bool = False, clone_in_fabric : bool = False)

## isaacsim.core.experimental.materials

### OmniGlassMaterial
- [class] class OmniGlassMaterial ( paths : str | list [ str ] )
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_input_values(name : str, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_input_values(name : str, values : str | bool | int | float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property shaders : list [ pxr.UsdShade.Shader ]
- [property] property valid : bool

### OmniPbrMaterial
- [class] class OmniPbrMaterial ( paths : str | list [ str ] )
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_input_values(name : str, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_input_values(name : str, values : str | bool | int | float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property shaders : list [ pxr.UsdShade.Shader ]
- [property] property valid : bool

### PhysicsMaterial
- [class] class PhysicsMaterial ( paths : str | list [ str ] , * , resolve_paths : bool = True )
- [method] abstract static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### PreviewSurfaceMaterial
- [class] class PreviewSurfaceMaterial ( paths : str | list [ str ] )
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_input_values(name : str, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_input_values(name : str, values : str | bool | int | float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property shaders : list [ pxr.UsdShade.Shader ]
- [property] property valid : bool

### RigidBodyMaterial
- [class] class RigidBodyMaterial(paths : str | list [ str ], *, static_frictions : float | list | np.ndarray | wp.array | None = None, dynamic_frictions : float | list | np.ndarray | wp.array | None = None, restitutions : float | list | np.ndarray | wp.array | None = None, densities : float | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_combine_modes(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_compliant_contact_gains(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_densities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_compliant_contacts(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_friction_coefficients(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_restitution_coefficients(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_combine_modes(frictions : Literal [ 'average' , 'max' , 'min' , 'multiply' ] | list [ Literal [ 'average' , 'max' , 'min' , 'multiply' ] ] | None = None, restitutions : Literal [ 'average' , 'max' , 'min' , 'multiply' ] | list [ Literal [ 'average' , 'max' , 'min' , 'multiply' ] ] | None = None, dampings : Literal [ 'average' , 'max' , 'min' , 'multiply' ] | list [ Literal [ 'average' , 'max' , 'min' , 'multiply' ] ] | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_compliant_contact_gains(stiffnesses : float | list | np.ndarray | wp.array | None = None, dampings : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_densities(densities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_compliant_contacts(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_friction_coefficients(static_frictions : float | list | np.ndarray | wp.array = None, dynamic_frictions : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_restitution_coefficients(restitutions : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### SurfaceDeformableMaterial
- [class] class SurfaceDeformableMaterial(paths : str | list [ str ], *, static_frictions : float | list | np.ndarray | wp.array | None = None, dynamic_frictions : float | list | np.ndarray | wp.array | None = None, youngs_moduli : float | list | np.ndarray | wp.array | None = None, poissons_ratios : float | list | np.ndarray | wp.array | None = None, densities : float | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_densities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_friction_coefficients(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_poissons_ratios(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_surface_stiffnesses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_surface_thicknesses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_youngs_moduli(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_densities(densities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_friction_coefficients(static_frictions : float | list | np.ndarray | wp.array = None, dynamic_frictions : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_poissons_ratios(poissons_ratios : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_surface_stiffnesses(stretch_stiffnesses : float | list | np.ndarray | wp.array | None = None, shear_stiffnesses : float | list | np.ndarray | wp.array | None = None, bend_stiffnesses : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_surface_thicknesses(surface_thicknesses : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_youngs_moduli(youngs_moduli : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### VisualMaterial
- [class] class VisualMaterial ( paths : str | list [ str ] , * , resolve_paths : bool = True )
- [method] abstract static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_input_values(name : str, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_input_values(name : str, values : str | bool | int | float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property shaders : list [ pxr.UsdShade.Shader ]
- [property] property valid : bool

### VolumeDeformableMaterial
- [class] class VolumeDeformableMaterial(paths : str | list [ str ], *, static_frictions : float | list | np.ndarray | wp.array | None = None, dynamic_frictions : float | list | np.ndarray | wp.array | None = None, youngs_moduli : float | list | np.ndarray | wp.array | None = None, poissons_ratios : float | list | np.ndarray | wp.array | None = None, densities : float | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_densities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_friction_coefficients(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_poissons_ratios(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_youngs_moduli(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_densities(densities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_friction_coefficients(static_frictions : float | list | np.ndarray | wp.array = None, dynamic_frictions : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_poissons_ratios(poissons_ratios : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_youngs_moduli(youngs_moduli : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property materials : list [ pxr.UsdShade.Material ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

## isaacsim.core.experimental.objects

### Capsule
- [class] class Capsule(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, heights : float | list | np.ndarray | wp.array | None = None, axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_axes(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_heights(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_axes(axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_heights(heights : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Capsule ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Cone
- [class] class Cone(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, heights : float | list | np.ndarray | wp.array | None = None, axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_axes(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_heights(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_axes(axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_heights(heights : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Cone ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Cube
- [class] class Cube(paths : str | list [ str ], *, sizes : float | list | np.ndarray | wp.array | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_sizes(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_sizes(sizes : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Cube ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Cylinder
- [class] class Cylinder(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, heights : float | list | np.ndarray | wp.array | None = None, axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_axes(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_heights(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_axes(axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_heights(heights : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Cylinder ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### CylinderLight
- [class] class CylinderLight(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, lengths : float | list | np.ndarray | wp.array | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_treat_as_lines(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_lengths(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_treat_as_lines(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_lengths(lengths : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### DiskLight
- [class] class DiskLight(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### DistantLight
- [class] class DistantLight(paths : str | list [ str ], *, angles : float | list | np.ndarray | wp.array | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_angles(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_angles(angles : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### DomeLight
- [class] class DomeLight(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, texture_files : str | list [ str ] | None = None, texture_formats : Literal [ 'automatic' , 'latlong' , 'mirroredBall' , 'angular' , 'cubeMapVerticalCross' ] | list [ Literal [ 'automatic' , 'latlong' , 'mirroredBall' , 'angular' , 'cubeMapVerticalCross' ] ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_guide_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_texture_files(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_texture_formats(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_guide_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_texture_files(texture_files : str | list [ str ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_texture_formats(texture_formats : Literal [ 'automatic' , 'latlong' , 'mirroredBall' , 'angular' , 'cubeMapVerticalCross' ] | list [ Literal [ 'automatic' , 'latlong' , 'mirroredBall' , 'angular' , 'cubeMapVerticalCross' ] ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### GroundPlane
- [class] class GroundPlane(paths : str | list [ str ], *, sizes : float | list | np.ndarray | wp.array = 100.0, colors : list | np.ndarray | wp.array = [0.5, 0.5, 0.5], positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_physics_materials(materials : type [ 'PhysicsMaterial' ] | list [ type [ 'PhysicsMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_physics_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_collisions(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_offsets(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_torsional_patch_radii(*, indices : int | list | np.ndarray | wp.array | None = None, minimum : bool = False)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_collisions(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_offsets(contact_offsets : float | list | np.ndarray | wp.array = None, rest_offsets : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_torsional_patch_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, minimum : bool = False)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property meshes : Mesh
- [property] property paths : list [ str ]
- [property] property planes : Plane
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Light
- [class] class Light(paths : str | list [ str ], *, resolve_paths : bool = True, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] abstract static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Mesh
- [class] class Mesh(paths : str | list [ str ], *, primitives : Literal [ 'Cone' , 'Cube' , 'Cylinder' , 'Disk' , 'Plane' , 'Sphere' , 'Torus' ] | list [ Literal [ 'Cone' , 'Cube' , 'Cylinder' , 'Disk' , 'Plane' , 'Sphere' , 'Torus' ] ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_corner_specs(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_crease_specs(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_face_specs(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_normals(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_points(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_subdivision_specs(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_corner_specs(corner_indices : list [ list | np.ndarray | wp.array ], corner_sharpnesses : list [ list | np.ndarray | wp.array ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_crease_specs(crease_indices : list [ list | np.ndarray | wp.array ], crease_lengths : list [ list | np.ndarray | wp.array ], crease_sharpnesses : list [ list | np.ndarray | wp.array ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_face_specs(vertex_indices : list [ list | np.ndarray | wp.array ] | None = None, vertex_counts : list [ list | np.ndarray | wp.array ] | None = None, varying_linear_interpolations : list [ Literal [ 'none' , 'cornersOnly' , 'cornersPlus1' , 'cornersPlus2' , 'boundaries' , 'all' ] ] | None = None, hole_indices : list [ list | np.ndarray | wp.array ] | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_normals(normals : list [ list | np.ndarray | wp.array ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_points(points : list [ list | np.ndarray | wp.array ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_subdivision_specs(subdivision_schemes : list [ Literal [ 'catmullClark' , 'loop' , 'bilinear' , 'none' ] ] | None = None, interpolate_boundaries : list [ Literal [ 'none' , 'edgeOnly' , 'edgeAndCorner' ] ] | None = None, triangle_subdivision_rules : list [ Literal [ 'catmullClark' , 'smooth' ] ] | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Mesh ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Mesh ]
- [property] property is_non_root_articulation_link : bool
- [property] property num_faces : list [ int ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Plane
- [class] class Plane(paths : str | list [ str ], *, widths : float | list | np.ndarray | wp.array | None = None, lengths : float | list | np.ndarray | wp.array | None = None, axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_axes(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_lengths(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_widths(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_axes(axes : Literal [ 'X' , 'Y' , 'Z' ] | list [ Literal [ 'X' , 'Y' , 'Z' ] ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_lengths(lengths : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_widths(widths : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Plane ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### RectLight
- [class] class RectLight(paths : str | list [ str ], *, widths : float | list | np.ndarray | wp.array | None = None, heights : float | list | np.ndarray | wp.array | None = None, texture_files : str | list [ str ] | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_heights(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_texture_files(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_widths(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_heights(heights : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_texture_files(texture_files : str | list [ str ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_widths(widths : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Shape
- [class] class Shape(paths : str | list [ str ], *, resolve_paths : bool = True, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] abstract static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] abstract static update_extents ( geoms : list [ pxr.UsdGeom.Gprim ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Sphere
- [class] class Sphere(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static update_extents ( geoms : list [ pxr.UsdGeom.Sphere ] ) → None
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### SphereLight
- [class] class SphereLight(paths : str | list [ str ], *, radii : float | list | np.ndarray | wp.array | None = None, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static are_of_type(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static fetch_instances(paths : str | Usd.Prim | list [ str | Usd.Prim ])
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_colors(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_color_temperatures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_normalizations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_treat_as_points(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_exposures(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_intensities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_multipliers(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_radii(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_color_temperatures(color_temperatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_colors(colors : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_color_temperatures(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_normalizations(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_treat_as_points(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_exposures(exposures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_intensities(intensities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_multipliers(diffuse_multipliers : float | list | np.ndarray | wp.array = None, specular_multipliers : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property lights : list [ pxr.UsdLux.Light ]
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

## isaacsim.core.experimental.prims

### Articulation
- [class] class Articulation(paths : str | list [ str ], *, resolve_paths : bool = True, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False, enable_residual_reports : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_armatures(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_coriolis_and_centrifugal_compensation_forces(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_drive_model_properties(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_drive_types(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_efforts(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_friction_properties(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_gains(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_gravity_compensation_forces(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_indices ( names : str | list [ str ] ) → warp.array
- [method] get_dof_limits(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_max_efforts(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_max_velocities(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_position_targets(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_positions(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_projected_joint_forces(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_velocities(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_dof_velocity_targets(*, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_self_collisions(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_fixed_tendon_dampings(*, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_fixed_tendon_limit_stiffnesses(*, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_fixed_tendon_limits(*, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_fixed_tendon_offsets(*, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_fixed_tendon_rest_lengths(*, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_fixed_tendon_stiffnesses(*, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_jacobian_matrices(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_joint_indices ( names : str | list [ str ] ) → warp.array
- [method] get_link_coms(*, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_link_enabled_gravities(*, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_link_incoming_joint_force(*, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_link_indices ( names : str | list [ str ] ) → warp.array
- [method] get_link_inertias(*, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None, inverse : bool = False)
- [method] get_link_masses(*, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None, inverse : bool = False)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_mass_matrices(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_sleep_thresholds(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_solver_iteration_counts(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_solver_residual_reports(*, indices : int | list | np.ndarray | wp.array | None = None, report_maximum : bool = True)
- [method] get_stabilization_thresholds(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_velocities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] is_physics_tensor_entity_initialized ( ) → bool
- [method] is_physics_tensor_entity_valid ( ) → bool
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, linear_velocities : list | np.ndarray | wp.array | None = None, angular_velocities : list | np.ndarray | wp.array | None = None, dof_positions : float | list | np.ndarray | wp.array | None = None, dof_velocities : float | list | np.ndarray | wp.array | None = None, dof_efforts : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_armatures(armatures : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_drive_model_properties(speed_effort_gradients : float | list | np.ndarray | wp.array | None = None, maximum_actuator_velocities : float | list | np.ndarray | wp.array | None = None, velocity_dependent_resistances : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_drive_types(types : str | list [ list [ str ] ], *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_efforts(efforts : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_friction_properties(static_frictions : float | list | np.ndarray | wp.array | None = None, dynamic_frictions : float | list | np.ndarray | wp.array | None = None, viscous_frictions : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_gains(stiffnesses : float | list | np.ndarray | wp.array | None = None, dampings : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None, update_default_gains : bool = True)
- [method] set_dof_limits(lower : float | list | np.ndarray | wp.array | None = None, upper : float | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_max_efforts(max_efforts : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_max_velocities(max_velocities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_position_targets(positions : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_positions(positions : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_velocities(velocities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_dof_velocity_targets(velocities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_self_collisions(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_fixed_tendon_properties(*, stiffnesses : float | list | np.ndarray | wp.array | None = None, dampings : float | list | np.ndarray | wp.array | None = None, limit_stiffnesses : float | list | np.ndarray | wp.array | None = None, lower_limits : float | list | np.ndarray | wp.array | None = None, upper_limits : float | list | np.ndarray | wp.array | None = None, rest_lengths : float | list | np.ndarray | wp.array | None = None, offsets : float | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None, tendon_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_link_coms(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_link_enabled_gravities(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_link_inertias(inertias : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_link_masses(masses : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, link_indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_sleep_thresholds(thresholds : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_solver_iteration_counts(position_counts : int | list | np.ndarray | wp.array | None = None, velocity_counts : int | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_stabilization_thresholds(thresholds : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_velocities(linear_velocities : list | np.ndarray | wp.array | None = None, angular_velocities : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] switch_dof_control_mode(mode : str, *, indices : int | list | np.ndarray | wp.array | None = None, dof_indices : int | list | np.ndarray | wp.array | None = None)
- [property] property dof_names : list [ str ]
- [property] property dof_paths : list [ list [ str ] ]
- [property] property dof_types : list [ omni.physics.tensors.DofType ]
- [property] property is_non_root_articulation_link : bool
- [property] property jacobian_matrix_shape : tuple [ int , int , int ]
- [property] property joint_names : list [ str ]
- [property] property joint_paths : list [ list [ str ] ]
- [property] property joint_types : list [ omni.physics.tensors.JointType ]
- [property] property link_names : list [ str ]
- [property] property link_paths : list [ list [ str ] ]
- [property] property mass_matrix_shape : tuple [ int , int ]
- [property] property num_dofs : int
- [property] property num_fixed_tendons : int
- [property] property num_joints : int
- [property] property num_links : int
- [property] property num_shapes : int
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### DeformablePrim
- [class] class DeformablePrim(paths : str | list [ str ], *, resolve_paths : bool = False, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False, deformable_type : Literal [ 'surface' , 'volume' ] | None = None)
- [method] apply_physics_materials(materials : type [ 'PhysicsMaterial' ] | list [ type [ 'PhysicsMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_physics_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_element_indices(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_nodal_gradients(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_nodal_kinematic_position_targets(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_nodal_positions(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_nodal_rotations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_nodal_stresses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_nodal_velocities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] is_physics_tensor_entity_valid ( ) → bool
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_nodal_kinematic_position_targets(positions : list | np.ndarray | wp.array | None = None, enabled : bool | list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_nodal_positions(positions : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_nodal_velocities(velocities : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property collision_mesh_paths : list [ str ]
- [property] property deformable_type : Literal [ 'surface' , 'volume' ]
- [property] property is_non_root_articulation_link : bool
- [property] property num_elements_per_body : tuple [ int , int , int ]
- [property] property num_nodes_per_body : tuple [ int , int , int ]
- [property] property num_nodes_per_element : int
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property simulation_mesh_paths : list [ str ]
- [property] property valid : bool

### GeomPrim
- [class] class GeomPrim(paths : str | list [ str ], *, resolve_paths : bool = True, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False, apply_collision_apis : bool = False)
- [method] apply_collision_apis(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] apply_physics_materials(materials : type [ 'PhysicsMaterial' ] | list [ type [ 'PhysicsMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_physics_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_collision_approximations(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_collisions(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_offsets(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_torsional_patch_radii(*, indices : int | list | np.ndarray | wp.array | None = None, minimum : bool = False)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_collision_approximations(approximations : str | list [ str ], *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_collisions(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_offsets(contact_offsets : float | list | np.ndarray | wp.array = None, rest_offsets : float | list | np.ndarray | wp.array = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_torsional_patch_radii(radii : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, minimum : bool = False)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property geoms : list [ pxr.UsdGeom.Gprim ]
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### Prim
- [class] class Prim ( paths : str | list [ str ] , * , resolve_paths : bool = True )
- [method] __len__ ( ) → int
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### RigidPrim
- [class] class RigidPrim(paths : str | list [ str ], *, resolve_paths : bool = True, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False, masses : float | list | np.ndarray | wp.array | None = None, densities : float | list | np.ndarray | wp.array | None = None)
- [method] apply_forces(forces : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None, local_frame : bool = False)
- [method] apply_forces_and_torques_at_pos(forces : list | np.ndarray | wp.array | None = None, torques : list | np.ndarray | wp.array | None = None, *, positions : list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None, local_frame : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_coms(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_densities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_gravities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_enabled_rigid_bodies(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_inertias(*, indices : int | list | np.ndarray | wp.array | None = None, inverse : bool = False)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_masses(*, indices : int | list | np.ndarray | wp.array | None = None, inverse : bool = False)
- [method] get_sleep_thresholds(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_velocities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] is_physics_tensor_entity_valid ( ) → bool
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_coms(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, linear_velocities : list | np.ndarray | wp.array | None = None, angular_velocities : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_densities(densities : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_gravities(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_enabled_rigid_bodies(enabled : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_inertias(inertias : list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_masses(masses : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_sleep_thresholds(thresholds : float | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_velocities(linear_velocities : list | np.ndarray | wp.array | None = None, angular_velocities : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property num_shapes : int
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

### XformPrim
- [class] class XformPrim(paths : str | list [ str ], *, resolve_paths : bool = True, positions : list | np.ndarray | wp.array | None = None, translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, scales : list | np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = False)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

## isaacsim.core.experimental.utils.impl.backend
- [function] get_current_backend(supported_backends : list [ str ], *, raise_on_unsupported : bool | None = None)
- [function] is_backend_set ( ) → bool
- [function] should_raise_on_fallback ( ) → bool
- [function] should_raise_on_unsupported ( ) → bool
- [function] use_backend(backend : Literal [ 'usd' , 'usdrt' , 'fabric' , 'tensor' ], *, raise_on_unsupported : bool = False, raise_on_fallback : bool = False)

## isaacsim.core.experimental.utils.impl.foundation
- [function] get_value_type_names(*, format: Literal[str, Sdf.ValueTypeNames, usdrt.Sdf.ValueTypeNames] = <class 'str'>)
- [function] resolve_value_type_name(type_name : str | Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName, *, backend : str | None = None)
- [function] value_type_name_to_str(type_name : str | Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName)

## isaacsim.core.experimental.utils.impl.ops
- [function] broadcast_to(x : bool | int | float | list | np.ndarray | wp.array, *, shape : list [ int ], dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] place(x : bool | int | float | list | np.ndarray | wp.array, *, dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] resolve_indices(x : bool | int | float | list | np.ndarray | wp.array | None, *, count : int | None = None, dtype : type | None = warp.int32, device : str | wp.context.Device | None = None)

## isaacsim.core.experimental.utils.impl.prim
- [function] create_prim_attribute(prim : str | Usd.Prim | usdrt.Usd.Prim, *, name : str, type_name : Sdf.ValueTypeName | usdrt.Sdf.ValueTypeName, exist_ok : bool = True)
- [function] get_all_matching_child_prims(prim : str | Usd.Prim | usdrt.Usd.Prim, *, predicate : Callable [ [ Usd.Prim | usdrt.Usd.Prim , str ] , bool ], include_self : bool = False, max_depth : int | None = None)
- [function] get_first_matching_child_prim(prim : str | Usd.Prim | usdrt.Usd.Prim, *, predicate : Callable [ [ Usd.Prim | usdrt.Usd.Prim , str ] , bool ], include_self : bool = False)
- [function] get_first_matching_parent_prim(prim : str | Usd.Prim | usdrt.Usd.Prim, *, predicate : Callable [ [ Usd.Prim | usdrt.Usd.Prim , str ] , bool ], include_self : bool = False)
- [function] get_prim_at_path ( path : str ) → Usd.Prim | usdrt.Usd.Prim
- [function] get_prim_path ( prim : Usd.Prim | usdrt.Usd.Prim ) → str
- [function] get_prim_variant_collection(prim : str | Usd.Prim)
- [function] get_prim_variants ( prim : str | Usd.Prim ) → list [ tuple [ str , str ] ]
- [function] has_api(prim : str | Usd.Prim, api : str | type | list [ str | type ], *, test : Literal [ 'all' , 'any' , 'none' ] = 'all')
- [function] set_prim_variants(prim : str | Usd.Prim, *, variants : list [ tuple [ str , str ] ])

## isaacsim.core.experimental.utils.impl.stage
- [function] add_reference_to_stage(usd_path : str, path : str, *, prim_type : str = 'Xform', variants : list [ tuple [ str , str ] ] = [])
- [function] close_stage ( ) → bool
- [function] create_new_stage ( * , template : str | None = None ) → pxr.Usd.Stage
- [function] async create_new_stage_async(*, template : str | None = None)
- [function] define_prim(path : str, type_name : str = 'Xform')
- [function] generate_next_free_path(path : str | None = None, *, prepend_default_prim : bool = True)
- [function] get_current_stage(*, backend : str | None = None)
- [function] get_stage_id ( stage : pxr.Usd.Stage ) → int
- [function] get_stage_time_code ( ) → tuple [ float , float , float ]
- [function] get_stage_units ( ) → tuple [ float , float ]
- [function] get_stage_up_axis ( ) → Literal [ 'Y' , 'Z' ]
- [function] is_stage_set ( ) → bool
- [function] open_stage ( usd_path : str ) → tuple [ bool , Usd.Stage | None ]
- [function] async open_stage_async ( usd_path : str ) → tuple [ bool , Usd.Stage | None ]
- [function] save_stage ( usd_path : str ) → bool
- [function] set_stage_time_code(*, start_time_code : float | None = None, end_time_code : float | None = None, time_codes_per_second : float | None = None)
- [function] set_stage_units(*, meters_per_unit : float | None = None, kilograms_per_unit : float | None = None)
- [function] set_stage_up_axis ( up_axis : Literal [ 'Y' , 'Z' ] ) → None
- [function] use_stage ( stage : pxr.Usd.Stage ) → Generator [ None , None , None ]

## isaacsim.core.experimental.utils.impl.transform
- [function] euler_angles_to_quaternion(euler_angles : list | np.ndarray | wp.array, *, degrees : bool = False, extrinsic : bool = True, dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] euler_angles_to_rotation_matrix(euler_angles : list | np.ndarray | wp.array, *, degrees : bool = False, extrinsic : bool = True, dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] quaternion_conjugate(quaternion : list | np.ndarray | wp.array, *, dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] quaternion_multiplication(first_quaternion : list | np.ndarray | wp.array, second_quaternion : list | np.ndarray | wp.array, *, dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] quaternion_to_rotation_matrix(quaternion : list | np.ndarray | wp.array, *, dtype : type | None = None, device : str | wp.context.Device | None = None)
- [function] rotation_matrix_to_quaternion(rotation_matrix : list | np.ndarray | wp.array, *, dtype : type | None = None, device : str | wp.context.Device | None = None)

## isaacsim.core.prims

### Articulation
- [class] class Articulation(prim_paths_expr : str | List [ str ], name : str = 'articulation_prim_view', positions : ndarray | Tensor | warp.array | None = None, translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, scales : ndarray | Tensor | warp.array | None = None, visibilities : ndarray | Tensor | warp.array | None = None, reset_xform_properties : bool = True, enable_residual_reports : bool = False)
- [method] apply_action(control_actions : ArticulationActions, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] get_angular_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_applied_actions(clone : bool = True)
- [method] get_applied_joint_efforts(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_armatures(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_articulation_body_count ( ) → int
- [method] get_body_coms(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_disable_gravity(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_index ( body_name : str ) → int
- [method] get_body_inertias(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_inv_inertias(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_inv_masses(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_body_masses(indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_coriolis_and_centrifugal_forces(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_dof_limits ( ) → ndarray | Tensor
- [method] get_dof_types(dof_names : List [ str ] = None)
- [method] get_drive_types ( ) → ndarray | Tensor
- [method] get_effort_modes(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] get_enabled_self_collisions(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_fixed_tendon_dampings(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_limit_stiffnesses(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_limits(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_offsets(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_rest_lengths(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_fixed_tendon_stiffnesses(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_friction_coefficients(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_gains(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_generalized_gravity_forces(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_jacobian_shape ( ) → ndarray | Tensor | warp.array
- [method] get_jacobians(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_joint_index ( joint_name : str ) → int
- [method] get_joint_max_velocities(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_joint_positions(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_joint_velocities(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone = True)
- [method] get_link_index ( link_name : str ) → int
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_mass_matrices(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_mass_matrix_shape ( ) → ndarray | Tensor | warp.array
- [method] get_max_efforts(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_measured_joint_efforts(indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_measured_joint_forces(indices : ndarray | List | Tensor | None = None, joint_indices : ndarray | List | Tensor | None = None, joint_names : List [ str ] | None = None, clone : bool = True)
- [method] get_position_residuals(indices : ndarray | list | Tensor | warp.array | None = None, report_max : bool = True)
- [method] get_sleep_thresholds(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_solver_position_iteration_counts(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_solver_velocity_iteration_counts(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_stabilization_thresholds(indices : ndarray | List | Tensor | warp.array | None = None)
- [method] get_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_velocity_residuals(indices : ndarray | list | Tensor | warp.array | None = None, report_max : bool = True)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] pause_motion ( ) → None
- [method] post_reset ( ) → None
- [method] resume_motion ( )
- [method] set_angular_velocities(velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_armatures(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_body_coms(positions : ndarray | Tensor | warp.array = None, orientations : ndarray | Tensor | warp.array = None, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_body_disable_gravity(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_body_inertias(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_body_masses(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, body_indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_effort_modes(mode : str, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | None = None, joint_names : List [ str ] | None = None)
- [method] set_enabled_self_collisions(flags : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_fixed_tendon_properties(stiffnesses : ndarray | Tensor | warp.array = None, dampings : ndarray | Tensor | warp.array = None, limit_stiffnesses : ndarray | Tensor | warp.array = None, limits : ndarray | Tensor | warp.array = None, rest_lengths : ndarray | Tensor | warp.array = None, offsets : ndarray | Tensor | warp.array = None, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_friction_coefficients(values : ndarray | Tensor, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_gains(kps : ndarray | Tensor | warp.array | None = None, kds : ndarray | Tensor | warp.array | None = None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None, save_to_usd : bool = False)
- [method] set_joint_efforts(efforts : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_position_targets(positions : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_positions(positions : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_velocities(velocities : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joint_velocity_targets(velocities : ndarray | Tensor | warp.array | None, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_joints_default_state(positions : ndarray | Tensor | warp.array | None = None, velocities : ndarray | Tensor | warp.array | None = None, efforts : ndarray | Tensor | warp.array | None = None)
- [method] set_linear_velocities(velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_max_efforts(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_max_joint_velocities(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] set_sleep_thresholds(thresholds : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_solver_position_iteration_counts(counts : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_solver_velocity_iteration_counts(counts : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_stabilization_thresholds(thresholds : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_velocities(velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] switch_control_mode(mode : str, indices : ndarray | List | Tensor | warp.array | None = None, joint_indices : ndarray | List | Tensor | warp.array | None = None, joint_names : List [ str ] | None = None)
- [method] switch_dof_control_mode(mode : str, dof_index : int, indices : ndarray | List | Tensor | warp.array | None = None)
- [property] property body_names : List [ str ]
- [property] property count : int
- [property] property dof_names : List [ str ]
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property joint_names : List [ str ]
- [property] property name : str
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property num_fixed_tendons : int
- [property] property num_joints : int
- [property] property num_shapes : int
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

### ClothPrim
- [class] class ClothPrim(prim_paths_expr : str, particle_systems : ndarray | Tensor = None, particle_materials : ndarray | Tensor | None = None, name : str = 'cloth_prim_view', reset_xform_properties : bool = True, positions : ndarray | Tensor | None = None, translations : ndarray | Tensor | None = None, orientations : ndarray | Tensor | None = None, scales : ndarray | Tensor | None = None, visibilities : ndarray | Tensor | None = None, particle_masses : ndarray | Tensor | None = None, pressures : ndarray | Tensor | None = None, particle_groups : ndarray | Tensor | None = None, self_collisions : ndarray | Tensor | None = None, self_collision_filters : ndarray | Tensor | None = None, stretch_stiffnesses : ndarray | Tensor | None = None, bend_stiffnesses : ndarray | Tensor | None = None, shear_stiffnesses : ndarray | Tensor | None = None, spring_dampings : ndarray | Tensor | None = None)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_cloths_bend_stiffnesses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_cloths_dampings(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_cloths_shear_stiffnesses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_cloths_stretch_stiffnesses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_particle_groups(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_particle_masses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_pressures(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_self_collision_filters(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_self_collisions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_spring_dampings(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_stretch_stiffnesses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_velocities(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] get_world_positions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_cloths_bend_stiffnesses(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_cloths_dampings(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_cloths_shear_stiffnesses(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_cloths_stretch_stiffnesses(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_particle_groups(particle_groups : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_particle_masses(masses : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_pressures(pressures : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_self_collision_filters(self_collision_filters : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_self_collisions(self_collisions : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_spring_dampings(damping : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_stretch_stiffnesses(stiffness : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_velocities(velocities : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] set_world_positions(positions : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [property] property count : int
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property max_particles_per_cloth : int
- [property] property max_springs_per_cloth : int
- [property] property name : str
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

### DeformablePrim
- [class] class DeformablePrim(prim_paths_expr : str, deformable_materials : ndarray | Tensor | None = None, name : str = 'deformable_prim_view', reset_xform_properties : bool = True, positions : ndarray | Tensor | None = None, translations : ndarray | Tensor | None = None, orientations : ndarray | Tensor | None = None, scales : ndarray | Tensor | None = None, visibilities : ndarray | Tensor | None = None, vertex_velocity_dampings : ndarray | Tensor | None = None, sleep_dampings : ndarray | Tensor | None = None, sleep_thresholds : ndarray | Tensor | None = None, settling_thresholds : ndarray | Tensor | None = None, self_collisions : ndarray | Tensor | None = None, self_collision_filter_distances : ndarray | Tensor | None = None, solver_position_iteration_counts : ndarray | Tensor | None = None)
- [method] apply_deformable_materials(deformable_materials : DeformableMaterial | List [ DeformableMaterial ], indices : ndarray | list | Tensor | None = None)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] get_applied_deformable_materials(indices : ndarray | list | Tensor | None = None)
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_collision_mesh_element_deformation_gradients(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_collision_mesh_element_rest_poses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_collision_mesh_element_rotations(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_collision_mesh_element_stresses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_collision_mesh_indices(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_collision_mesh_nodal_positions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_self_collision_filter_distances(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_self_collisions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_settling_thresholds(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_element_deformation_gradients(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_element_rest_poses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_element_rotations(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_element_stresses(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_indices(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_kinematic_targets(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_nodal_positions(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_nodal_velocities(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_simulation_mesh_rest_points(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_sleep_dampings(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_sleep_thresholds(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_solver_position_iteration_counts(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_vertex_velocity_dampings(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_collision_mesh_indices(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_collision_mesh_rest_points(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_self_collision_filter_distances(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_self_collisions(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_settling_thresholds(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_simulation_mesh_indices(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_simulation_mesh_kinematic_targets(positions : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_simulation_mesh_nodal_positions(positions : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_simulation_mesh_nodal_velocities(velocities : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_simulation_mesh_rest_points(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_sleep_dampings(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_sleep_thresholds(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_solver_position_iteration_counts(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_vertex_velocity_dampings(values : ndarray | Tensor | None, indices : ndarray | list | Tensor | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [property] property count : int
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property max_collision_mesh_elements_per_body : int
- [property] property max_collision_mesh_vertices_per_body : int
- [property] property max_simulation_mesh_elements_per_body : int
- [property] property max_simulation_mesh_vertices_per_body : int
- [property] property name : str
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

### GeometryPrim
- [class] class GeometryPrim(prim_paths_expr : str, name : str = 'geometry_prim_view', positions : ndarray | Tensor | warp.array | None = None, translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, scales : ndarray | Tensor | warp.array | None = None, visibilities : ndarray | Tensor | warp.array | None = None, reset_xform_properties : bool = True, collisions : ndarray | Tensor | warp.array | None = None, track_contact_forces : bool = False, prepare_contact_sensors : bool = False, disable_stablization : bool = True, contact_filter_prim_paths_expr : List [ str ] | None = [], max_contact_count : int = 0)
- [method] apply_collision_apis(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] apply_physics_materials(physics_materials : PhysicsMaterial | List [ PhysicsMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] disable_collision(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] enable_collision(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_applied_physics_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_collision_approximations(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_contact_force_data(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_contact_force_matrix(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_contact_offsets(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_friction_data(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_min_torsional_patch_radii(indices : ndarray | list | Tensor | None = None)
- [method] get_net_contact_forces(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_rest_offsets(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_torsional_patch_radii(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_collision_enabled(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_collision_approximations(approximation_types : List [ str ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_contact_offsets(offsets : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_min_torsional_patch_radii(radii : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_rest_offsets(offsets : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_torsional_patch_radii(radii : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [property] property count : int
- [property] property geoms : List [ pxr.UsdGeom.Gprim ]
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property name : str
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

### ParticleSystem
- [class] class ParticleSystem(prim_paths_expr : str, name : str = 'particle_system_view', particle_systems_enabled : ndarray | Tensor | None = None, simulation_owners : Sequence [ str ] | None = None, contact_offsets : ndarray | Tensor | None = None, rest_offsets : ndarray | Tensor | None = None, particle_contact_offsets : ndarray | Tensor | None = None, solid_rest_offsets : ndarray | Tensor | None = None, fluid_rest_offsets : ndarray | Tensor | None = None, enable_ccds : ndarray | Tensor | None = None, solver_position_iteration_counts : ndarray | Tensor | None = None, max_depenetration_velocities : ndarray | Tensor | None = None, winds : ndarray | Tensor | None = None, max_neighborhoods : int | None = None, max_velocities : ndarray | Tensor | None = None, global_self_collisions_enabled : ndarray | Tensor | None = None)
- [method] apply_particle_materials(particle_materials : ParticleMaterial | List [ ParticleMaterial ], indices : ndarray | list | Tensor | None = None)
- [method] get_applied_particle_materials(indices : ndarray | list | Tensor | None = None)
- [method] get_contact_offsets(indices : ndarray | list | Tensor | None = None)
- [method] get_enable_ccds(indices : ndarray | list | Tensor | None = None)
- [method] get_fluid_rest_offsets(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_global_self_collisions_enabled(indices : ndarray | list | Tensor | None = None)
- [method] get_max_depenetration_velocities(indices : ndarray | list | Tensor | None = None)
- [method] get_max_neighborhoods(indices : ndarray | list | Tensor | None = None)
- [method] get_max_velocities(indices : ndarray | list | Tensor | None = None)
- [method] get_particle_contact_offsets(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_particle_systems_enabled(indices : ndarray | list | Tensor | None = None)
- [method] get_rest_offsets(indices : ndarray | list | Tensor | None = None)
- [method] get_simulation_owners(indices : ndarray | list | Tensor | None = None)
- [method] get_solid_rest_offsets(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] get_solver_position_iteration_counts(indices : ndarray | list | Tensor | None = None)
- [method] get_winds(indices : ndarray | list | Tensor | None = None, clone : bool = True)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | None = None)
- [method] post_reset ( ) → None
- [method] set_contact_offsets(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_enable_ccds(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_fluid_rest_offsets(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_global_self_collisions_enabled(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_max_depenetration_velocities(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_max_neighborhoods(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_max_velocities(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_particle_contact_offsets(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_particle_systems_enabled(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_rest_offsets(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_simulation_owners(values : Sequence [ str ], indices : ndarray | List | Tensor | None = None)
- [method] set_solid_rest_offsets(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_solver_position_iteration_counts(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_winds(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [property] property count : int
- [property] property name : str

### RigidPrim
- [class] class RigidPrim(prim_paths_expr : str | List [ str ], name : str = 'rigid_prim_view', positions : ndarray | Tensor | warp.array | None = None, translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, scales : ndarray | Tensor | warp.array | None = None, visibilities : ndarray | Tensor | warp.array | None = None, reset_xform_properties : bool = True, masses : ndarray | Tensor | warp.array | None = None, densities : ndarray | Tensor | warp.array | None = None, linear_velocities : ndarray | Tensor | warp.array | None = None, angular_velocities : ndarray | Tensor | warp.array | None = None, track_contact_forces : bool = False, prepare_contact_sensors : bool = True, disable_stablization : bool = True, contact_filter_prim_paths_expr : List [ str ] | None = [], max_contact_count : int = 0)
- [method] apply_forces(forces : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None, is_global : bool = True)
- [method] apply_forces_and_torques_at_pos(forces : ndarray | Tensor | warp.array | None = None, torques : ndarray | Tensor | warp.array | None = None, positions : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, is_global : bool = True)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] disable_gravities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] disable_rigid_body_physics(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] enable_gravities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] enable_rigid_body_physics(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_angular_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_coms(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_contact_force_data(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_contact_force_matrix(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_current_dynamic_state ( ) → DynamicsViewState
- [method] get_default_state ( ) → DynamicsViewState
- [method] get_densities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_friction_data(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_inertias(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_inv_inertias(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_inv_masses(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_linear_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_masses(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_net_contact_forces(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_sleep_thresholds(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_velocities(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, clone : bool = True, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_angular_velocities(velocities : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_coms(positions : ndarray | Tensor | warp.array = None, orientations : ndarray | Tensor | warp.array = None, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, linear_velocities : ndarray | Tensor | warp.array | None = None, angular_velocities : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_densities(densities : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_inertias(values : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_linear_velocities(velocities : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_masses(masses : ndarray | Tensor | warp.array, indices : ndarray | List | Tensor | warp.array | None = None)
- [method] set_sleep_thresholds(thresholds : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_velocities(velocities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [property] property count : int
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property name : str
- [property] property num_shapes : int
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

### SdfShapePrim
- [class] class SdfShapePrim(prim_paths_expr : str, num_query_points : int, prepare_sdf_schemas : bool = True, name : str = 'sdf_shape_view', positions : ndarray | Tensor | warp.array | None = None, translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, scales : ndarray | Tensor | warp.array | None = None, visibilities : ndarray | Tensor | warp.array | None = None, reset_xform_properties : bool = True, collisions : ndarray | Tensor | warp.array | None = None, track_contact_forces : bool = False, prepare_contact_sensors : bool = False, disable_stablization : bool = True, contact_filter_prim_paths_expr : List [ str ] | None = [])
- [method] apply_collision_apis(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] apply_physics_materials(physics_materials : PhysicsMaterial | List [ PhysicsMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] disable_collision(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] enable_collision(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_applied_physics_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_collision_approximations(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_contact_force_data(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_contact_force_matrix(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_contact_offsets(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_friction_data(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_min_torsional_patch_radii(indices : ndarray | list | Tensor | None = None)
- [method] get_net_contact_forces(indices : ndarray | List | Tensor | warp.array | None = None, clone : bool = True, dt : float = 1.0)
- [method] get_rest_offsets(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_sdf_and_gradients(points : ndarray | Tensor, indices : ndarray | Tensor | None = None, clone : bool = True)
- [method] get_sdf_margins(indices : ndarray | List | Tensor | None = None, clone : bool = True)
- [method] get_sdf_narrow_band_thickness(indices : ndarray | List | Tensor | None = None, clone : bool = True)
- [method] get_sdf_resolution(indices : ndarray | List | Tensor | None = None, clone : bool = True)
- [method] get_sdf_subgrid_resolution(indices : ndarray | List | Tensor | None = None, clone : bool = True)
- [method] get_torsional_patch_radii(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_collision_enabled(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_physics_handle_valid ( ) → bool
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_collision_approximations(approximation_types : List [ str ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_contact_offsets(offsets : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_min_torsional_patch_radii(radii : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_rest_offsets(offsets : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_sdf_margins(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_sdf_narrow_band_thickness(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_sdf_resolution(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_sdf_subgrid_resolution(values : ndarray | Tensor, indices : ndarray | List | Tensor | None = None)
- [method] set_torsional_patch_radii(radii : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [property] property count : int
- [property] property geoms : List [ pxr.UsdGeom.Gprim ]
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property name : str
- [property] property num_query_points : int
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

### SingleArticulation
- [class] class SingleArticulation(prim_path : str, name : str = 'articulation', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, reset_xform_properties : bool = True, articulation_controller : ArticulationController | None = None, enable_residual_reports : bool = False)
- [method] apply_action(control_actions : ArticulationAction)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_gravity ( ) → None
- [method] enable_gravity ( ) → None
- [method] get_angular_velocity ( ) → ndarray
- [method] get_applied_action ( ) → ArticulationAction
- [method] get_applied_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_articulation_body_count ( ) → int
- [method] get_articulation_controller ( ) → ArticulationController
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_enabled_self_collisions ( ) → int
- [method] get_joint_positions(joint_indices : List | ndarray | None = None)
- [method] get_joint_velocities(joint_indices : List | ndarray | None = None)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_measured_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_measured_joint_forces(joint_indices : List | ndarray | None = None)
- [method] get_position_residual(report_max : bool | None = True)
- [method] get_sleep_threshold ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_solver_velocity_iteration_count ( ) → int
- [method] get_stabilization_threshold ( ) → float
- [method] get_velocity_residual(report_max : bool | None = True)
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] get_world_velocity ( ) → ndarray
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity(velocity : ndarray)
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_enabled_self_collisions ( flag : bool ) → None
- [method] set_joint_efforts(efforts : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_positions(positions : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_velocities(velocities : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joints_default_state(positions : ndarray | None = None, velocities : ndarray | None = None, efforts : ndarray | None = None)
- [method] set_linear_velocity(velocity : ndarray)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_solver_position_iteration_count(count : int)
- [method] set_solver_velocity_iteration_count ( count : int )
- [method] set_stabilization_threshold(threshold : float)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_world_velocity ( velocity : ndarray )
- [property] property dof_names : List [ str ]
- [property] property dof_properties : ndarray
- [property] property handles_initialized : bool
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SingleClothPrim
- [class] class SingleClothPrim(prim_path : str, particle_system : SingleParticleSystem, particle_material : ParticleMaterial | None = None, name : str | None = 'cloth', position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, particle_mass : float | None = 0.01, pressure : float | None = None, particle_group : int | None = 0, self_collision : bool | None = True, self_collision_filter : bool | None = True, stretch_stiffness : float | None = None, bend_stiffness : float | None = None, shear_stiffness : float | None = None, spring_damping : float | None = None)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_cloth_bend_stiffness ( ) → float
- [method] get_cloth_damping ( ) → ndarray | Tensor
- [method] get_cloth_shear_stiffness ( ) → float
- [method] get_cloth_stretch_stiffness ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → XFormPrimState
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_particle_group ( ) → int
- [method] get_pressure ( ) → float
- [method] get_self_collision ( ) → bool
- [method] get_self_collision_filter ( ) → bool
- [method] get_spring_damping ( ) → ndarray | Tensor
- [method] get_stretch_stiffness ( ) → ndarray | Tensor
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_cloth_bend_stiffness ( stiffness : float ) → None
- [method] set_cloth_damping ( damping : float ) → None
- [method] set_cloth_shear_stiffness ( stiffness : float ) → None
- [method] set_cloth_stretch_stiffness(stiffness : ndarray | Tensor)
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_particle_group ( particle_group : int ) → None
- [method] set_pressure ( pressure : float ) → None
- [method] set_self_collision ( self_collision : bool ) → None
- [method] set_self_collision_filter(self_collision_filter : bool)
- [method] set_spring_damping(damping : ndarray | Tensor)
- [method] set_stretch_stiffness(stiffness : ndarray | Tensor)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property mesh : pxr.UsdGeom.Mesh
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SingleDeformablePrim
- [class] class SingleDeformablePrim(prim_path : str, deformable_material : DeformableMaterial | None = None, name : str | None = 'deformable', position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, vertex_velocity_damping : float | None = None, sleep_damping : float | None = None, sleep_threshold : float | None = None, settling_threshold : float | None = None, self_collision : bool | None = True, self_collision_filter_distance : float | None = None, solver_position_iteration_count : int | None = None, kinematic_enabled : bool | None = False, simulation_rest_points : Sequence [ float ] | None = None, simulation_indices : Sequence [ int ] | None = None, simulation_hexahedral_resolution : int | None = 10, collision_rest_points : Sequence [ float ] | None = None, collision_indices : Sequence [ int ] | None = None, collision_simplification : bool | None = True, collision_simplification_remeshing : bool | None = True, collision_simplification_remeshing_resolution : int | None = 0, collision_simplification_target_triangle_count : int | None = 0, collision_simplification_force_conforming : bool | None = False, embedding : Sequence [ int ] | None = None)
- [method] apply_deformable_material(deformable_materials : DeformableMaterial)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_deformable_material ( ) → DeformableMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_mesh_indices ( ) → ndarray | Tensor
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → XFormPrimState
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_self_collision ( ) → bool
- [method] get_self_collision_filter_distance ( ) → float
- [method] get_settling_threshold ( ) → float
- [method] get_simulation_mesh_indices ( ) → ndarray | Tensor
- [method] get_simulation_mesh_rest_points ( ) → ndarray | Tensor
- [method] get_sleep_damping ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_vertex_velocity_damping ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_self_collision ( self_collision : bool ) → None
- [method] set_self_collision_filter_distance(self_collision_filter_distance : float)
- [method] set_settling_threshold(settling_threshold : float)
- [method] set_sleep_damping ( sleep_damping : float ) → None
- [method] set_sleep_threshold(sleep_threshold : float)
- [method] set_solver_position_iteration_count(iterations : int)
- [method] set_vertex_velocity_damping(vertex_velocity_damping : float)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property mesh : pxr.UsdGeom.Mesh
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SingleGeometryPrim
- [class] class SingleGeometryPrim(prim_path : str, name : str = 'geometry_prim', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, reset_xform_properties : bool = True, collision : bool = False, track_contact_forces : bool = False, prepare_contact_sensor : bool = False, disable_stablization : bool = True, contact_filter_prim_paths_expr : List [ str ] | None = [])
- [method] apply_physics_material(physics_material : PhysicsMaterial, weaker_than_descendants : bool = False)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_physics_material ( ) → PhysicsMaterial
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_collision_approximation ( ) → str
- [method] get_collision_enabled ( ) → bool
- [method] get_contact_force_data(dt : float = 1.0)
- [method] get_contact_force_matrix(dt : float = 1.0)
- [method] get_contact_offset ( ) → float
- [method] get_default_state ( ) → XFormPrimState
- [method] get_friction_data(dt : float = 1.0)
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_min_torsional_patch_radius ( ) → float
- [method] get_net_contact_forces(dt : float = 1.0)
- [method] get_rest_offset ( ) → float
- [method] get_torsional_patch_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_collision_approximation(approximation_type : str)
- [method] set_collision_enabled ( enabled : bool ) → None
- [method] set_contact_offset ( offset : float ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_min_torsional_patch_radius(radius : float)
- [method] set_rest_offset ( offset : float ) → None
- [method] set_torsional_patch_radius ( radius : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property geom : pxr.UsdGeom.Gprim
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SingleParticleSystem
- [class] class SingleParticleSystem(prim_path : str, name : str | None = 'particle_system', particle_system_enabled : bool | None = None, simulation_owner : str | None = None, contact_offset : float | None = None, rest_offset : float | None = None, particle_contact_offset : float | None = None, solid_rest_offset : float | None = None, fluid_rest_offset : float | None = None, enable_ccd : bool | None = None, solver_position_iteration_count : float | None = None, max_depenetration_velocity : float | None = None, wind : Sequence [ float ] = None, max_neighborhood : int | None = None, max_velocity : float | None = None, global_self_collision_enabled : bool | None = None, non_particle_collision_enabled : bool | None = None)
- [method] apply_particle_anisotropy ( ) → pxr.PhysxSchema.PhysxParticleAnisotropyAPI
- [method] apply_particle_isotropy ( ) → pxr.PhysxSchema.PhysxParticleAnisotropyAPI
- [method] apply_particle_material(particle_materials : ParticleMaterial)
- [method] apply_particle_smoothing ( ) → pxr.PhysxSchema.PhysxParticleSmoothingAPI
- [method] get_applied_particle_material ( ) → ParticleMaterial
- [method] get_contact_offset ( ) → float
- [method] get_enable_ccd ( ) → bool
- [method] get_fluid_rest_offset ( ) → float
- [method] get_global_self_collision_enabled ( ) → bool
- [method] get_max_depenetration_velocity ( ) → None
- [method] get_max_neighborhood ( ) → int
- [method] get_max_velocity ( ) → float
- [method] get_particle_contact_offset ( ) → float
- [method] get_particle_system_enabled ( ) → bool
- [method] get_rest_offset ( ) → float
- [method] get_simulation_owner ( ) → pxr.Usd.Prim
- [method] get_solid_rest_offset ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_wind ( ) → Sequence [ float ]
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] post_reset ( ) → None
- [method] set_contact_offset ( value : float ) → None
- [method] set_enable_ccd ( value : bool ) → None
- [method] set_fluid_rest_offset ( value : float ) → None
- [method] set_global_self_collision_enabled(value : bool)
- [method] set_max_depenetration_velocity(value : float)
- [method] set_max_neighborhood ( value : int ) → None
- [method] set_max_velocity ( value : float ) → None
- [method] set_particle_contact_offset ( value : float ) → None
- [method] set_particle_system_enabled ( value : bool ) → None
- [method] set_rest_offset ( value : float ) → None
- [method] set_simulation_owner ( value : str ) → None
- [method] set_solid_rest_offset ( value : float ) → None
- [method] set_solver_position_iteration_count(value : int)
- [method] set_wind ( value : Sequence [ float ] ) → None
- [property] property name : str | None
- [property] property particle_system : pxr.PhysxSchema.PhysxParticleSystem
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SingleRigidPrim
- [class] class SingleRigidPrim(prim_path : str, name : str = 'rigid_prim', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, reset_xform_properties : bool = True, mass : float | None = None, density : float | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] get_angular_velocity ( )
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_com ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → DynamicState
- [method] get_density ( ) → float
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, linear_velocity : ndarray | None = None, angular_velocity : ndarray | None = None)
- [method] set_density ( density : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SingleXFormPrim
- [class] class SingleXFormPrim(prim_path : str, name : str = 'xform_prim', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, reset_xform_properties : bool = True)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_default_state ( ) → XFormPrimState
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### XFormPrim
- [class] class XFormPrim(prim_paths_expr : str | List [ str ], name : str = 'xform_prim_view', positions : ndarray | Tensor | None = None, translations : ndarray | Tensor | None = None, orientations : ndarray | Tensor | None = None, scales : ndarray | Tensor | None = None, visibilities : ndarray | Tensor | None = None, reset_xform_properties : bool = True, usd : bool = True)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( )
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, usd : bool = True)
- [property] property count : int
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property name : str
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

## isaacsim.core.simulation_manager

### IsaacEvents
- [class] class IsaacEvents(value, names = None, *, module = None, qualname = None, type = None, start = 1, boundary = None)
- [attribute] PHYSICS_READY = 'isaac.physics_ready'
- [attribute] PHYSICS_WARMUP = 'isaac.physics_warmup'
- [attribute] POST_PHYSICS_STEP = 'isaac.post_physics_step'
- [attribute] POST_RESET = 'isaac.post_reset'
- [attribute] PRE_PHYSICS_STEP = 'isaac.pre_physics_step'
- [attribute] PRIM_DELETION = 'isaac.prim_deletion'
- [attribute] SIMULATION_VIEW_CREATED = 'isaac.simulation_view_created'
- [attribute] TIMELINE_STOP = 'isaac.timeline_stop'

### SimulationManager
- [class] class SimulationManager
- [method] classmethod assets_loading ( ) → bool
- [method] classmethod deregister_callback ( callback_id )
- [method] classmethod enable_all_default_callbacks(enable : bool = True)
- [method] classmethod enable_ccd(flag : bool, physics_scene : str = None)
- [method] classmethod enable_fabric ( enable )
- [method] classmethod enable_fabric_usd_notice_handler ( stage_id , flag )
- [method] classmethod enable_gpu_dynamics(flag : bool, physics_scene : str = None)
- [method] classmethod enable_on_stop_callback ( enable : bool = True ) → None
- [method] classmethod enable_post_warm_start_callback(enable : bool = True)
- [method] classmethod enable_stablization(flag : bool, physics_scene : str = None)
- [method] classmethod enable_stage_open_callback(enable : bool = True)
- [method] classmethod enable_usd_notice_handler ( flag )
- [method] classmethod enable_warm_start_callback(enable : bool = True)
- [method] classmethod get_backend ( ) → str
- [method] classmethod get_broadphase_type(physics_scene : str = None)
- [method] classmethod get_default_callback_status ( ) → dict
- [method] classmethod get_default_physics_scene ( ) → str
- [method] classmethod get_num_physics_steps ( )
- [method] classmethod get_physics_dt ( physics_scene : str = None ) → str
- [method] classmethod get_physics_sim_device ( ) → str
- [method] classmethod get_physics_sim_view ( )
- [method] classmethod get_simulation_time ( )
- [method] classmethod get_solver_type ( physics_scene : str = None ) → str
- [method] classmethod initialize_physics ( ) → None
- [method] classmethod is_ccd_enabled ( physics_scene : str = None ) → bool
- [method] classmethod is_default_callback_enabled(callback_name : str)
- [method] classmethod is_fabric_enabled ( enable )
- [method] classmethod is_fabric_usd_notice_handler_enabled ( stage_id )
- [method] classmethod is_gpu_dynamics_enabled(physics_scene : str = None)
- [method] classmethod is_paused ( )
- [method] classmethod is_simulating ( )
- [method] classmethod is_stablization_enabled(physics_scene : str = None)
- [method] classmethod register_callback(callback : callable, event, order : int = 0, name : str = None)
- [method] classmethod set_backend ( val : str ) → None
- [method] classmethod set_broadphase_type(val : str, physics_scene : str = None)
- [method] classmethod set_default_physics_scene(physics_scene_prim_path : str)
- [method] set_physics_dt(dt : float = 0.016666666666666666, physics_scene : str = None)
- [method] classmethod set_physics_sim_device ( val ) → None
- [method] classmethod set_solver_type(solver_type : str, physics_scene : str = None)
- [method] classmethod step ( render : bool = False )

## isaacsim.core.utils._isaac_utils.math
- [function] add ( arg0: carb::Float3 , arg1: carb::Float3 ) → carb::Float3
- [function] cross ( arg0: carb::Float3 , arg1: carb::Float3 ) → carb::Float3
- [function] dot ( * args , ** kwargs )
- [function] get_basis_vector_x ( arg0: carb::Float4 ) → carb::Float3
- [function] get_basis_vector_y ( arg0: carb::Float4 ) → carb::Float3
- [function] get_basis_vector_z ( arg0: carb::Float4 ) → carb::Float3
- [function] inverse ( arg0: carb::Float4 ) → carb::Float4
- [function] lerp ( * args , ** kwargs )
- [function] mul ( * args , ** kwargs )
- [function] normalize ( * args , ** kwargs )
- [function] rotate ( arg0: carb::Float4 , arg1: carb::Float3 ) → carb::Float3
- [function] slerp(arg0: carb::Float4, arg1: carb::Float4, arg2: float)
- [function] transform_inv(arg0: pxrInternal_v0_24__pxrReserved__::GfTransform, arg1: pxrInternal_v0_24__pxrReserved__::GfTransform)

## isaacsim.core.utils._isaac_utils.transforms
- [function] set_scale ( arg0: int , arg1: str , arg2: carb::Float3 ) → None
- [function] set_transform(arg0: int, arg1: str, arg2: carb::Float3, arg3: carb::Float4)

## isaacsim.core.utils.articulations
- [function] add_articulation_root ( prim : pxr.Usd.Prim ) → None
- [function] find_all_articulation_base_paths ( ) → List
- [function] move_articulation_root(src_prim : pxr.Usd.Prim, dst_prim : pxr.Usd.Prim)
- [function] remove_articulation_root ( prim : pxr.Usd.Prim ) → None

## isaacsim.core.utils.bounds
- [function] compute_aabb(bbox_cache : pxr.UsdGeom.BBoxCache, prim_path : str, include_children : bool = False)
- [function] compute_combined_aabb(bbox_cache : pxr.UsdGeom.BBoxCache, prim_paths : List [ str ])
- [function] compute_obb(bbox_cache : pxr.UsdGeom.BBoxCache, prim_path : str)
- [function] compute_obb_corners(bbox_cache : pxr.UsdGeom.BBoxCache, prim_path : str)
- [function] create_bbox_cache(time : pxr.Usd.TimeCode = pxr.Usd.TimeCode.Default, use_extents_hint : bool = True)
- [function] get_obb_corners(centroid : ndarray, axes : ndarray, half_extent : ndarray)
- [function] recompute_extents(prim : pxr.UsdGeom.Boundable, time : pxr.Usd.TimeCode = pxr.Usd.TimeCode.Default, include_children : bool = False)

## isaacsim.core.utils.carb
- [function] get_carb_setting(carb_settings : carb.settings.ISettings, setting : str)
- [function] set_carb_setting(carb_settings : carb.settings.ISettings, setting : str, value : Any)

## isaacsim.core.utils.collisions
- [function] ray_cast(position : array, orientation : array, offset : array, max_dist : float = 100.0)

## isaacsim.core.utils.commands
- [function] get_current_stage(fabric : bool = False)
- [function] get_current_stage_id ( ) → int

### IsaacSimDestroyPrim
- [class] class IsaacSimDestroyPrim ( * args : Any , ** kwargs : Any )

### IsaacSimScalePrim
- [class] class IsaacSimScalePrim ( * args : Any , ** kwargs : Any )

### IsaacSimSpawnPrim
- [class] class IsaacSimSpawnPrim ( * args : Any , ** kwargs : Any )

### IsaacSimTeleportPrim
- [class] class IsaacSimTeleportPrim ( * args : Any , ** kwargs : Any )

## isaacsim.core.utils.constants

### AXES_INDICES
- [data] AXES_INDICES = {'X': 0, 'Y': 1, 'Z': 2, 'x': 0, 'y': 1, 'z': 2}

### AXES_TOKEN
- [data] AXES_TOKEN = {'X': pxr.UsdGeom.Tokens.x, 'Y': pxr.UsdGeom.Tokens.y, 'Z': pxr.UsdGeom.Tokens.z, 'x': pxr.UsdGeom.Tokens.x, 'y': pxr.UsdGeom.Tokens.y, 'z': pxr.UsdGeom.Tokens.z}

## isaacsim.core.utils.distance_metrics
- [function] rotational_distance_angle(r1 : ndarray | pxr.Gf.Matrix3d | pxr.Gf.Matrix4d, r2 : ndarray | pxr.Gf.Matrix3d | pxr.Gf.Matrix4d)
- [function] rotational_distance_identity_matrix_deviation(r1 : ndarray | pxr.Gf.Matrix4d | pxr.Gf.Matrix3d, r2 : ndarray | pxr.Gf.Matrix4d | pxr.Gf.Matrix3d)
- [function] rotational_distance_single_axis(r1 : ndarray | pxr.Gf.Matrix4d | pxr.Gf.Matrix3d, r2 : ndarray | pxr.Gf.Matrix4d | pxr.Gf.Matrix3d, axis : ndarray)
- [function] weighted_translational_distance(t1 : ndarray | pxr.Gf.Matrix4d, t2 : ndarray | pxr.Gf.Matrix4d, weight_matrix : ndarray = array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]))

## isaacsim.core.utils.extensions
- [function] disable_extension ( extension_name : str ) → bool
- [function] enable_extension ( extension_name : str ) → bool
- [function] get_extension_id ( extension_name : str ) → str
- [function] get_extension_path ( ext_id : str ) → str
- [function] get_extension_path_from_name ( extension_name : str ) → str

## isaacsim.core.utils.interops
- [function] jax2numpy ( array : jax.Array ) → numpy.ndarray
- [function] jax2tensorflow ( array : jax.Array ) → tensorflow.Tensor
- [function] jax2torch ( array : jax.Array ) → torch.Tensor
- [function] jax2warp ( array : jax.Array ) → warp.array
- [function] numpy2jax ( array : numpy.ndarray ) → jax.Array
- [function] numpy2tensorflow ( array : numpy.ndarray ) → tensorflow.Tensor
- [function] numpy2torch ( array : numpy.ndarray ) → torch.Tensor
- [function] numpy2warp ( array : numpy.ndarray ) → warp.array
- [function] tensorflow2jax ( tensor : tensorflow.Tensor ) → jax.Array
- [function] tensorflow2numpy ( tensor : tensorflow.Tensor ) → numpy.ndarray
- [function] tensorflow2torch ( tensor : tensorflow.Tensor ) → torch.Tensor
- [function] tensorflow2warp ( tensor : tensorflow.Tensor ) → warp.array
- [function] torch2jax ( tensor : torch.Tensor ) → jax.Array
- [function] torch2numpy ( tensor : torch.Tensor ) → numpy.ndarray
- [function] torch2tensorflow ( tensor : torch.Tensor ) → tensorflow.Tensor
- [function] torch2warp ( tensor : torch.Tensor ) → warp.array
- [function] warp2jax ( array : warp.array ) → jax.Array
- [function] warp2numpy ( array : warp.array ) → numpy.ndarray
- [function] warp2tensorflow ( array : warp.array ) → tensorflow.Tensor
- [function] warp2torch ( array : warp.array ) → torch.Tensor

## isaacsim.core.utils.math
- [function] cross ( a : ndarray | list , b : ndarray | list ) → list
- [function] normalize ( v )
- [function] normalized ( v )
- [function] radians_to_degrees ( rad_angles : ndarray ) → ndarray

## isaacsim.core.utils.mesh
- [function] get_mesh_vertices_relative_to(mesh_prim : pxr.UsdGeom.Mesh, coord_prim : pxr.Usd.Prim)

## isaacsim.core.utils.numpy.maths
- [function] cos ( data )
- [function] inverse ( data )
- [function] matmul ( matrix_a , matrix_b )
- [function] sin ( data )
- [function] transpose_2d ( data )

## isaacsim.core.utils.numpy.rotations
- [function] deg2rad ( degree_value : ndarray , device = None ) → ndarray
- [function] euler_angles_to_quats(euler_angles : ndarray, degrees : bool = False, extrinsic : bool = True, device = None)
- [function] gf_quat_to_tensor(orientation : pxr.Gf.Quatd | pxr.Gf.Quatf | pxr.Gf.Quaternion, device = None)
- [function] quats_to_euler_angles(quaternions : ndarray, degrees : bool = False, extrinsic : bool = True, device = None)
- [function] quats_to_rot_matrices(quaternions : ndarray, device = None)
- [function] quats_to_rotvecs(quaternions : ndarray, device = None)
- [function] rad2deg ( radian_value : ndarray , device = None ) → ndarray
- [function] rot_matrices_to_quats(rotation_matrices : ndarray, device = None)
- [function] rotvecs_to_quats(rotation_vectors : ndarray, degrees : bool = False, device = None)
- [function] wxyz2xyzw ( q , ret_torch = False )
- [function] xyzw2wxyz ( q , ret_torch = False )

## isaacsim.core.utils.numpy.tensor
- [function] as_type ( data , dtype )
- [function] assign ( src , dst , indices )
- [function] clone_tensor ( data , device = None )
- [function] convert ( data , device = None , dtype = 'float32' , indexed = None )
- [function] create_tensor_from_list ( data , dtype , device = None )
- [function] create_zeros_tensor ( shape , dtype , device = None )
- [function] expand_dims ( data , axis )
- [function] move_data ( data , device = None )
- [function] pad ( data , pad_width , mode = 'constant' , value = None )
- [function] resolve_indices ( indices , count , device = None )
- [function] tensor_cat ( data , device = None , dim = -1 )
- [function] tensor_stack ( data , dim = 0 )
- [function] to_list ( data )
- [function] to_numpy ( data )

## isaacsim.core.utils.numpy.transformations
- [function] assign_pose(current_positions, current_orientations, positions, orientations, indices, device = None, pose = None)
- [function] get_local_from_world(parent_transforms, positions, orientations, device = None)
- [function] get_pose ( positions , orientations , device = None )
- [function] get_world_from_local(parent_transforms, translations, orientations, device = None)
- [function] tf_matrices_from_poses(translations : ndarray, orientations : ndarray, device = None)

## isaacsim.core.utils.physics
- [function] get_rigid_body_enabled ( prim_path : str ) → bool | None
- [function] set_rigid_body_enabled ( _value , prim_path )
- [function] async simulate_async(seconds : float, steps_per_sec : int = 60, callback : Callable = None)

## isaacsim.core.utils.prims
- [function] create_prim(prim_path : str, prim_type : str = 'Xform', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, usd_path : str | None = None, semantic_label : str | None = None, semantic_type : str = 'class', attributes : dict | None = None)
- [function] define_prim(prim_path : str, prim_type : str = 'Xform', fabric : bool = False)
- [function] delete_prim ( prim_path : str ) → None
- [function] find_matching_prim_paths(prim_path_regex : str, prim_type : str | None = None)
- [function] get_all_matching_child_prims ( prim_path: str, predicate: ~typing.Callable[[str], bool] = <function <lambda>>, depth: int | None = None ) → List [ pxr.Usd.Prim ]
- [function] get_articulation_root_api_prim_path ( prim_path )
- [function] get_first_matching_child_prim(prim_path : str, predicate : Callable [ [ str ] , bool ], fabric : bool = False)
- [function] get_first_matching_parent_prim(prim_path : str, predicate : Callable [ [ str ] , bool ])
- [function] get_prim_at_path(prim_path : str, fabric : bool = False)
- [function] get_prim_attribute_names(prim_path : str, fabric : bool = False)
- [function] get_prim_attribute_value(prim_path : str, attribute_name : str, fabric : bool = False)
- [function] get_prim_children ( prim : pxr.Usd.Prim ) → List [ pxr.Usd.Prim ]
- [function] get_prim_object_type ( prim_path : str ) → str | None
- [function] get_prim_parent ( prim : pxr.Usd.Prim ) → pxr.Usd.Prim
- [function] get_prim_path ( prim : pxr.Usd.Prim ) → str
- [function] get_prim_property ( prim_path : str , property_name : str ) → Any
- [function] get_prim_type_name ( prim_path : str , fabric : bool = False ) → str
- [function] is_prim_ancestral ( prim_path : str ) → bool
- [function] is_prim_hidden_in_stage ( prim_path : str ) → bool
- [function] is_prim_no_delete ( prim_path : str ) → bool
- [function] is_prim_non_root_articulation_link ( prim_path : str ) → bool
- [function] is_prim_path_valid ( prim_path : str , fabric : bool = False ) → bool
- [function] is_prim_root_path ( prim_path : str ) → bool
- [function] move_prim ( path_from : str , path_to : str ) → None
- [function] query_parent_path(prim_path : str, predicate : Callable [ [ str ] , bool ])
- [function] set_prim_attribute_value(prim_path : str, attribute_name : str, value : Any, fabric : bool = False)
- [function] set_prim_hide_in_stage_window ( prim : pxr.Usd.Prim , hide : bool )
- [function] set_prim_no_delete ( prim : pxr.Usd.Prim , no_delete : bool )
- [function] set_prim_property(prim_path : str, property_name : str, property_value : Any)
- [function] set_prim_visibility ( prim : pxr.Usd.Prim , visible : bool ) → None
- [function] set_targets(prim : pxr.Usd.Prim, attribute : str, target_prim_paths : list)

## isaacsim.core.utils.random
- [function] get_random_translation_from_camera(min_distance : float, max_distance : float, fov_x : float, fov_y : float, fraction_to_screen_edge : float)
- [function] get_random_values_in_range(min_range : ndarray, max_range : ndarray)
- [function] get_random_world_pose_in_view(camera_prim : pxr.Usd.Prim, min_distance : float, max_distance : float, fov_x : float, fov_y : float, fraction_to_screen_edge : float, coord_prim : pxr.Usd.Prim, min_rotation_range : ndarray, max_rotation_range : ndarray)

## isaacsim.core.utils.render_product
- [function] add_aov ( render_product_path : str , aov_name : str )
- [function] create_hydra_texture(resolution : Tuple [ int ], camera_prim_path : str)
- [function] get_camera_prim_path ( render_product_path : str )
- [function] get_resolution ( render_product_path : str )
- [function] set_camera_prim_path ( render_product_path : str , camera_prim_path : str )
- [function] set_resolution(render_product_path : str, resolution : Tuple [ int ])

## isaacsim.core.utils.rotations
- [function] euler_angles_to_quat(euler_angles : ndarray, degrees : bool = False, extrinsic : bool = True)
- [function] euler_to_rot_matrix(euler_angles : ndarray, degrees : bool = False, extrinsic : bool = True)
- [function] gf_quat_to_np_array(orientation : pxr.Gf.Quatd | pxr.Gf.Quatf | pxr.Gf.Quaternion)
- [function] gf_rotation_to_np_array(orientation : pxr.Gf.Rotation)
- [function] lookat_to_quatf(camera : pxr.Gf.Vec3f, target : pxr.Gf.Vec3f, up : pxr.Gf.Vec3f)
- [function] matrix_to_euler_angles(mat : ndarray, degrees : bool = False, extrinsic : bool = True)
- [function] quat_to_euler_angles(quat : ndarray, degrees : bool = False, extrinsic : bool = True)
- [function] quat_to_rot_matrix ( quat : ndarray ) → ndarray
- [function] rot_matrix_to_quat ( mat : ndarray ) → ndarray

## isaacsim.core.utils.semantics
- [function] add_labels(prim : pxr.Usd.Prim, labels : list [ str ], instance_name : str = 'class', overwrite : bool = True)
- [function] add_update_semantics(prim : pxr.Usd.Prim, semantic_label : str, type_label : str = 'class', suffix = '')
- [function] check_incorrect_labels(prim_path : str | None = None)
- [function] check_incorrect_semantics(prim_path : str = None)
- [function] check_missing_labels ( prim_path : str | None = None ) → list [ str ]
- [function] check_missing_semantics ( prim_path : str = None ) → List [ str ]
- [function] count_labels_in_scene ( prim_path : str | None = None ) → dict [ str , int ]
- [function] count_semantics_in_scene(prim_path : str = None)
- [function] get_labels ( prim : pxr.Usd.Prim ) → dict [ str , list [ str ] ]
- [function] get_semantics(prim : pxr.Usd.Prim)
- [function] remove_all_semantics(prim : pxr.Usd.Prim, recursive : bool = False)
- [function] remove_labels(prim : pxr.Usd.Prim, instance_name : str | None = None, include_descendants : bool = False)
- [function] upgrade_prim_semantics_to_labels(prim : pxr.Usd.Prim, include_descendants : bool = False)

## isaacsim.core.utils.stage
- [function] add_reference_to_stage(usd_path : str, prim_path : str, prim_type : str = 'Xform')
- [function] clear_stage(predicate : Callable [ [ str ] , bool ] | None = None)
- [function] close_stage ( callback_fn : Callable = None ) → bool
- [function] create_new_stage ( ) → pxr.Usd.Stage
- [function] async create_new_stage_async ( ) → None
- [function] create_new_stage_in_memory ( ) → pxr.Usd.Stage
- [function] get_current_stage(fabric : bool = False)
- [function] get_current_stage_id ( ) → int
- [function] get_next_free_path ( path : str , parent : str = None ) → str
- [function] get_stage_units ( ) → float
- [function] get_stage_up_axis ( ) → str
- [function] is_stage_loading ( ) → bool
- [function] open_stage ( usd_path : str ) → bool
- [function] async open_stage_async ( usd_path : str ) → Tuple [ bool , int ]
- [function] print_stage_prim_paths ( fabric : bool = False ) → None
- [function] remove_deleted_references ( )
- [function] save_stage ( usd_path : str , save_and_reload_in_place = True ) → bool
- [function] set_livesync_stage ( usd_path : str , enable : bool ) → bool
- [function] set_stage_units ( stage_units_in_meters : float ) → None
- [function] set_stage_up_axis ( axis : str = 'z' ) → None
- [function] traverse_stage ( fabric = False ) → Iterable
- [function] update_stage ( ) → None
- [function] async update_stage_async ( ) → None
- [function] use_stage ( stage : pxr.Usd.Stage ) → None

## isaacsim.core.utils.string
- [function] find_root_prim_path_from_regex(prim_path_regex : str)
- [function] find_unique_string_name(initial_name : str, is_unique_fn : Callable [ [ str ] , bool ])

## isaacsim.core.utils.torch.maths
- [function] cos ( data )
- [function] inverse ( data )
- [function] matmul ( matrix_a , matrix_b )
- [function] set_seed ( seed , torch_deterministic = False )
- [function] sin ( data )
- [function] transpose_2d ( data )
- [function] unscale_np ( x , lower , upper )

## isaacsim.core.utils.torch.rotations
- [function] deg2rad ( degree_value : float , device = None ) → Tensor
- [function] euler_angles_to_quats(euler_angles : Tensor, degrees : bool = False, extrinsic : bool = True, device = None)
- [function] gf_quat_to_tensor(orientation : pxr.Gf.Quatd | pxr.Gf.Quatf | pxr.Gf.Quaternion, device = None)
- [function] normalise_quat_in_pose ( pose )
- [function] rad2deg ( radian_value : Tensor , device = None ) → Tensor
- [function] rot_matrices_to_quats(rotation_matrices : Tensor, device = None)
- [function] wxyz2xyzw ( q )
- [function] xyzw2wxyz ( q )

## isaacsim.core.utils.torch.tensor
- [function] as_type ( data , dtype )
- [function] assign ( src , dst , indices )
- [function] clone_tensor ( data , device )
- [function] convert ( data , device , dtype = 'float32' , indexed = None )
- [function] create_tensor_from_list ( data , dtype , device = None )
- [function] create_zeros_tensor ( shape , dtype , device = None )
- [function] expand_dims ( data , axis )
- [function] move_data ( data , device )
- [function] pad ( data , pad_width , mode = 'constant' , value = None )
- [function] resolve_indices ( indices , count , device )
- [function] tensor_cat ( data , device = None , dim = -1 )
- [function] tensor_stack ( data , dim = 0 )
- [function] to_list ( data )
- [function] to_numpy ( data )

## isaacsim.core.utils.torch.transformations
- [function] assign_pose(current_positions, current_orientations, positions, orientations, indices, device, pose = None)
- [function] get_local_from_world(parent_transforms, positions, orientations, device)
- [function] get_pose ( positions , orientations , device )
- [function] get_world_from_local(parent_transforms, translations, orientations, device)
- [function] normalise_quat_in_pose ( pose )
- [function] tf_matrices_from_poses(translations : Tensor, orientations : Tensor, device = None)

## isaacsim.core.utils.transformations
- [function] get_relative_transform(source_prim : pxr.Usd.Prim, target_prim : pxr.Usd.Prim)
- [function] get_transform_with_normalized_rotation(transform : ndarray)
- [function] get_translation_from_target(translation_from_source : ndarray, source_prim : pxr.Usd.Prim, target_prim : pxr.Usd.Prim)
- [function] get_world_pose_from_relative(coord_prim : pxr.Usd.Prim, relative_translation : ndarray, relative_orientation : ndarray)
- [function] pose_from_tf_matrix(transformation : ndarray)
- [function] tf_matrices_from_poses(translations : ndarray | Tensor, orientations : ndarray | Tensor)
- [function] tf_matrix_from_pose(translation : Sequence [ float ], orientation : Sequence [ float ])

## isaacsim.core.utils.types

### ArticulationAction
- [class] class ArticulationAction(joint_positions : List | ndarray | None = None, joint_velocities : List | ndarray | None = None, joint_efforts : List | ndarray | None = None, joint_indices : List | ndarray | None = None)
- [method] get_dict ( ) → dict
- [method] get_dof_action ( index : int ) → dict
- [method] get_length ( ) → int | None

### ArticulationActions
- [class] class ArticulationActions(joint_positions : List | ndarray | None = None, joint_velocities : List | ndarray | None = None, joint_efforts : List | ndarray | None = None, joint_indices : List | ndarray | None = None, joint_names : List [ str ] | None = None)

### DOFInfo
- [class] class DOFInfo ( prim_path : str , handle : int , prim : pxr.Usd.Prim , index : int )

### DataFrame
- [class] class DataFrame ( current_time_step : int , current_time : float , data : dict )
- [method] get_dict ( ) → dict
- [method] classmethod init_from_dict ( dict_representation : dict )

### DynamicState
- [class] class DynamicState(position : ndarray, orientation : ndarray, linear_velocity : ndarray, angular_velocity : ndarray)

### DynamicsViewState
- [class] class DynamicsViewState(positions : ndarray | Tensor, orientations : ndarray | Tensor, linear_velocities : ndarray | Tensor, angular_velocities : ndarray | Tensor)

### JointsState
- [class] class JointsState(positions : ndarray, velocities : ndarray, efforts : ndarray)

### XFormPrimState
- [class] class XFormPrimState ( position : ndarray , orientation : ndarray )

### XFormPrimViewState
- [class] class XFormPrimViewState(positions : ndarray | Tensor, orientations : ndarray | Tensor)

## isaacsim.core.utils.viewports
- [function] add_aov_to_viewport ( viewport_api , aov_name : str )
- [function] backproject_depth(depth_image : array, viewport_api : Any, max_clip_depth : float)
- [function] create_viewport_for_camera(viewport_name : str, camera_prim_path : str, width : int = 1280, height : int = 720, position_x : int = 0, position_y : int = 0)
- [function] destroy_all_viewports(usd_context_name : str = None, destroy_main_viewport = True)
- [function] get_id_from_index ( index )
- [function] get_intrinsics_matrix ( viewport_api : Any ) → ndarray
- [function] get_viewport_names ( usd_context_name : str = None ) → List [ str ]
- [function] get_window_from_id ( id , usd_context_name : str = None )
- [function] project_depth_to_worldspace(depth_image : array, viewport_api : Any, max_clip_depth : float)
- [function] set_active_viewport_camera ( camera_prim_path : str )
- [function] set_camera_view(eye : array, target : array, camera_prim_path : str = '/OmniverseKit_Persp', viewport_api = None)
- [function] set_intrinsics_matrix(viewport_api : Any, intrinsics_matrix : ndarray, focal_length : float = 1.0)

## isaacsim.core.utils.xforms
- [function] clear_xform_ops ( prim : pxr.Usd.Prim )
- [function] get_local_pose ( prim_path )
- [function] get_world_pose ( prim_path , fabric = False )
- [function] reset_and_set_xform_ops(prim : pxr.Usd.Prim, translation : pxr.Gf.Vec3d, orientation : pxr.Gf.Quatd, scale : pxr.Gf.Vec3d = pxr.Gf.Vec3d)
- [function] reset_xform_ops ( prim : pxr.Usd.Prim )

## isaacsim.core.version
- [function] get_version ( ) → Tuple [ str , str , str , str , str , str , str , str ]
- [function] parse_version(full_version : str)

### Version
- [class] class Version

## isaacsim.gui.components.element_wrappers.ui_widget_wrappers

### Button
- [class] class Button ( label : str , text : str , tooltip = '' , on_click_fn = None )
- [method] cleanup ( )
- [method] set_on_click_fn ( on_click_fn : Callable )
- [method] trigger_click ( )
- [property] property button : omni.ui.Button
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property label : omni.ui.Label
- [property] property visible : bool

### CheckBox
- [class] class CheckBox(label : str, default_value : bool = False, tooltip = '', on_click_fn = None)
- [method] cleanup ( )
- [method] get_value ( ) → bool
- [method] set_on_click_fn ( on_click_fn : Callable )
- [method] set_value ( val : bool )
- [property] property checkbox : omni.ui.CheckBox
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property label : omni.ui.Label
- [property] property visible : bool

### CollapsableFrame
- [class] class CollapsableFrame(title : str, collapsed : bool = True, enabled : bool = True, visible : bool = True, build_fn : Callable = None)
- [method] cleanup ( )
- [method] rebuild ( )
- [method] set_build_fn ( build_fn : Callable )
- [property] property collapsed : bool
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property frame : omni.ui.Frame
- [property] property title : str
- [property] property visible : bool

### ColorPicker
- [class] class ColorPicker(label : str, default_value : List [ float ] = [1.0, 1.0, 1.0, 1.0], tooltip : str = '', on_color_picked_fn : Callable = None)
- [method] cleanup ( )
- [method] get_color ( ) → List [ float ]
- [method] set_color ( color : List [ float ] )
- [method] set_on_color_picked_fn(on_color_picked_fn : Callable)
- [property] property color_picker : omni.ui.ColorWidget
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property label : omni.ui.Label
- [property] property visible : bool

### DropDown
- [class] class DropDown(label : str, tooltip : str = '', populate_fn : Callable = None, on_selection_fn : Callable = None, keep_old_selections : bool = False, add_flourish : bool = True)
- [method] cleanup ( )
- [method] get_items ( ) → List [ str ]
- [method] get_selection ( ) → str
- [method] get_selection_index ( ) → int
- [method] repopulate ( )
- [method] set_items ( items : List [ str ] , select_index : int = None )
- [method] set_keep_old_selection ( val : bool )
- [method] set_on_selection_fn ( on_selection_fn : Callable )
- [method] set_populate_fn(populate_fn : Callable, repopulate : bool = True)
- [method] set_populate_fn_to_find_all_usd_objects_of_type(object_type : str, repopulate = True)
- [method] set_selection ( selection : str )
- [method] set_selection_by_index ( select_index : int )
- [method] trigger_on_selection_fn_with_current_selection ( )
- [property] property combobox : omni.ui.ComboBox
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property label : omni.ui.Label
- [property] property visible : bool

### FloatField
- [class] class FloatField(label : str, tooltip : str = '', default_value : float = 0.0, step : float = 0.01, format : str = '%.2f', lower_limit : float = None, upper_limit : float = None, on_value_changed_fn : Callable = None, on_end_edit_fn : Callable = None)
- [method] cleanup ( )
- [method] get_lower_limit ( ) → float
- [method] get_upper_limit ( ) → float
- [method] get_value ( ) → float
- [method] set_lower_limit ( lower_limit : float )
- [method] set_on_end_edit_fn ( on_end_edit_fn : Callable )
- [method] set_on_value_changed_fn(on_value_changed_fn : Callable)
- [method] set_upper_limit ( upper_limit : float )
- [method] set_value ( val : float )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property float_field : omni.ui.FloatField
- [property] property label : omni.ui.Label
- [property] property visible : bool

### Frame
- [class] class Frame(enabled : bool = True, visible : bool = True, build_fn : Callable = None)
- [method] cleanup ( )
- [method] rebuild ( )
- [method] set_build_fn ( build_fn : Callable )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property frame : omni.ui.Frame
- [property] property visible : bool

### IntField
- [class] class IntField(label : str, tooltip : str = '', default_value : int = 0, lower_limit : int = None, upper_limit : int = None, on_value_changed_fn : Callable = None)
- [method] cleanup ( )
- [method] get_lower_limit ( ) → int
- [method] get_upper_limit ( ) → int
- [method] get_value ( ) → int
- [method] set_lower_limit ( lower_limit : int )
- [method] set_on_value_changed_fn(on_value_changed_fn : Callable)
- [method] set_upper_limit ( upper_limit : int )
- [method] set_value ( val : int )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property int_field : omni.ui.IntField
- [property] property label : omni.ui.Label
- [property] property visible : bool

### ScrollingFrame
- [class] class ScrollingFrame(num_lines = None, enabled : bool = True, visible : bool = True, build_fn : Callable = None)
- [method] cleanup ( )
- [method] rebuild ( )
- [method] set_build_fn ( build_fn : Callable )
- [method] set_num_lines ( num_lines : int )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property frame : omni.ui.Frame
- [property] property visible : bool

### StateButton
- [class] class StateButton(label : str, a_text : str, b_text : str, tooltip = '', on_a_click_fn : Callable = None, on_b_click_fn : Callable = None, physics_callback_fn : Callable = None)
- [method] cleanup ( )
- [method] get_current_text ( ) → str
- [method] is_in_a_state ( ) → bool
- [method] reset ( )
- [method] set_on_a_click_fn ( on_a_click_fn : Callable )
- [method] set_on_b_click_fn ( on_b_click_fn : Callable )
- [method] set_physics_callback_fn(physics_callback_fn : Callable)
- [method] trigger_click_if_a_state ( )
- [method] trigger_click_if_b_state ( )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property label : omni.ui.Label
- [property] property state_button : omni.ui.Button
- [property] property visible : bool

### StringField
- [class] class StringField(label : str, tooltip : str = '', default_value : str = '', read_only = False, multiline_okay = False, on_value_changed_fn : Callable = None, use_folder_picker = False, item_filter_fn = None, bookmark_label = None, bookmark_path = None, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder')
- [method] add_folder_picker_icon(on_click_fn, item_filter_fn = None, bookmark_label = None, bookmark_path = None, dialog_title = 'Select Output Folder', button_title = 'Select Folder')
- [method] cleanup ( )
- [method] get_value ( ) → str
- [method] set_item_filter_fn ( item_filter_fn : Callable )
- [method] set_multiline_okay ( multiline_okay : bool )
- [method] set_on_value_changed_fn(on_value_changed_fn : Callable)
- [method] set_read_only ( read_only : bool )
- [method] set_value ( val : str )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property file_picker_btn : omni.ui.Button
- [property] property file_picker_frame : omni.ui.Frame
- [property] property label : omni.ui.Label
- [property] property string_field : omni.ui.StringField
- [property] property visible : bool

### TextBlock
- [class] class TextBlock(label : str, text : str = '', tooltip : str = '', num_lines = 5, include_copy_button : bool = True)
- [method] cleanup ( )
- [method] get_text ( ) → str
- [method] set_num_lines ( num_lines : int )
- [method] set_text ( text : str )
- [property] property container_frame : omni.ui.Frame
- [property] property copy_btn : omni.ui.Button
- [property] property enabled : bool
- [property] property label : omni.ui.Label
- [property] property scrolling_frame : omni.ui.ScrollingFrame
- [property] property text_block : omni.ui.Label
- [property] property visible : bool

### XYPlot
- [class] class XYPlot(label : str, tooltip : str = '', x_data : List [ List ] | List = [], y_data : List [ List ] | List = [], x_min : float = None, x_max : float = None, y_min : float = None, y_max : float = None, x_label : str = 'X', y_label : str = 'Y', plot_height : int = 10, show_legend : bool = False, legends : List [ str ] = None, plot_colors : List [ List [ int ] ] = None)
- [method] cleanup ( )
- [method] get_legends ( ) → List [ str ]
- [method] get_plot_colors ( ) → List [ List [ int ] ]
- [method] get_plot_height ( ) → int
- [method] get_x_data ( ) → List [ List [ float ] ]
- [method] get_x_max ( ) → float
- [method] get_x_min ( ) → float
- [method] get_y_data ( ) → List [ List [ float ] ]
- [method] get_y_max ( ) → float
- [method] get_y_min ( ) → float
- [method] set_data(x_data : List [ List ] | List, y_data : List [ List ] | List)
- [method] set_legend_by_index ( idx : int , legend : str )
- [method] set_legends ( legends : List [ str ] )
- [method] set_plot_color_by_index ( index : int , r : int , g : int , b : int )
- [method] set_plot_colors ( plot_colors : List [ List [ int ] ] )
- [method] set_plot_height ( plot_height : int )
- [method] set_plot_visible_by_index ( index : int , visible : bool )
- [method] set_show_legend ( show_legend : bool )
- [method] set_x_max ( x_max : float )
- [method] set_x_min ( x_min : float )
- [method] set_y_max ( y_max : float )
- [method] set_y_min ( y_min : float )
- [property] property container_frame : omni.ui.Frame
- [property] property enabled : bool
- [property] property visible : bool

## isaacsim.gui.components.ui_utils
- [method] ui_utils. add_separator ( )
- [method] ui_utils. btn_builder(type = 'button', text = 'button', tooltip = '', on_clicked_fn = None)
- [method] ui_utils. cb_builder(type = 'checkbox', default_val = False, tooltip = '', on_clicked_fn = None)
- [method] ui_utils. color_picker_builder(type = 'color_picker', default_val = [1.0, 1.0, 1.0, 1.0], tooltip = 'Color Picker')
- [method] ui_utils. combo_cb_dropdown_builder ( type='checkbox_dropdown', default_val=[False, 0], items=['Option 1', 'Option 2', 'Option 3'], tooltip='', on_clicked_fn=[<function <lambda>>, None] )
- [method] ui_utils. combo_cb_plot_builder(default_val=False, on_clicked_fn=<function <lambda>>, data=None, min=-1, max=1, type=omni.ui.Type.LINE, value_stride=1, color=None, tooltip='')
- [method] ui_utils. combo_cb_scrolling_frame_builder ( type='cb_scrolling_frame', default_val=[False, 'No Data'], tooltip='', on_clicked_fn=<function <lambda>> )
- [method] ui_utils. combo_cb_str_builder ( type='checkbox_stringfield', default_val=[False, ' '], tooltip='', on_clicked_fn=<function <lambda>>, use_folder_picker=False, read_only=False, folder_dialog_title='Select Output Folder', folder_button_title='Select Folder' )
- [method] ui_utils. combo_cb_xyz_plot_builder(default_val=False, on_clicked_fn=<function <lambda>>, data=[], min=-1, max=1, type=omni.ui.Type.LINE, value_stride=1, tooltip='')
- [method] ui_utils. combo_floatfield_slider_builder(type = 'floatfield_stringfield', default_val = 0.5, min = 0, max = 1, step = 0.01, tooltip = ['', ''])
- [method] ui_utils. combo_intfield_slider_builder(type = 'intfield_stringfield', default_val = 0.5, min = 0, max = 1, step = 0.01, tooltip = ['', ''])
- [method] ui_utils. dropdown_builder(type = 'dropdown', default_val = 0, items = ['Option 1', 'Option 2', 'Option 3'], tooltip = '', on_clicked_fn = None)
- [method] ui_utils. float_builder(type = 'floatfield', default_val = 0, tooltip = '', min = -inf, max = inf, step = 0.1, format = '%.2f')
- [method] ui_utils. int_builder(type = 'intfield', default_val = 0, tooltip = '', min = -9223372036854775807, max = 9223372036854775807)
- [method] ui_utils. multi_btn_builder(type = 'multi_button', count = 2, text = ['button', 'button'], tooltip = ['', '', ''], on_clicked_fn = [None, None])
- [method] ui_utils. multi_cb_builder(type = 'multi_checkbox', count = 2, text = [' ', ' '], default_val = [False, False], tooltip = ['', '', ''], on_clicked_fn = [None, None])
- [method] ui_utils. multi_dropdown_builder(type = 'multi_dropdown', count = 2, default_val = [0, 0], items = [['Option 1', 'Option 2', 'Option 3'], ['Option A', 'Option B', 'Option C']], tooltip = '', on_clicked_fn = [None, None])
- [method] ui_utils. plot_builder(data = None, min = -1, max = 1, type = omni.ui.Type.LINE, value_stride = 1, color = None, tooltip = '')
- [method] ui_utils. progress_bar_builder(type = 'progress_bar', default_val = 0, tooltip = 'Progress')
- [method] ui_utils. scrolling_frame_builder(type = 'scrolling_frame', default_val = 'No Data', tooltip = '')
- [method] ui_utils. setup_ui_headers(file_path, title = 'My Custom Extension', doc_link = 'https://docs.isaacsim.omniverse.nvidia.com/latest/index.html', overview = '', info_collapsed = True)
- [method] ui_utils. state_btn_builder(type = 'state_button', a_text = 'STATE A', b_text = 'STATE B', tooltip = '', on_clicked_fn = None)
- [method] ui_utils. str_builder(type = 'stringfield', default_val = ' ', tooltip = '', on_clicked_fn = None, use_folder_picker = False, read_only = False, item_filter_fn = None, bookmark_label = None, bookmark_path = None, folder_dialog_title = 'Select Output Folder', folder_button_title = 'Select Folder')
- [method] ui_utils. xyz_builder(tooltip = '', axis_count = 3, default_val = [0.0, 0.0, 0.0, 0.0], min = -inf, max = inf, step = 0.001, on_value_changed_fn = [None, None, None, None])
- [method] ui_utils. xyz_plot_builder ( data = [] , min = -1 , max = 1 , tooltip = '' )

## isaacsim.replicator.domain_randomization.scripts.gate
- [function] on_env_reset ( )
- [function] on_interval ( interval )

## isaacsim.replicator.domain_randomization.scripts.physics_view
- [function] randomize_articulation_view(view_name : str, operation : str = 'direct', num_buckets : int = None, stiffness : omni.replicator.core.utils.ReplicatorItem = None, damping : omni.replicator.core.utils.ReplicatorItem = None, joint_friction : omni.replicator.core.utils.ReplicatorItem = None, position : omni.replicator.core.utils.ReplicatorItem = None, orientation : omni.replicator.core.utils.ReplicatorItem = None, linear_velocity : omni.replicator.core.utils.ReplicatorItem = None, angular_velocity : omni.replicator.core.utils.ReplicatorItem = None, velocity : omni.replicator.core.utils.ReplicatorItem = None, joint_positions : omni.replicator.core.utils.ReplicatorItem = None, joint_velocities : omni.replicator.core.utils.ReplicatorItem = None, lower_dof_limits : omni.replicator.core.utils.ReplicatorItem = None, upper_dof_limits : omni.replicator.core.utils.ReplicatorItem = None, max_efforts : omni.replicator.core.utils.ReplicatorItem = None, joint_armatures : omni.replicator.core.utils.ReplicatorItem = None, joint_max_velocities : omni.replicator.core.utils.ReplicatorItem = None, joint_efforts : omni.replicator.core.utils.ReplicatorItem = None, body_masses : omni.replicator.core.utils.ReplicatorItem = None, body_inertias : omni.replicator.core.utils.ReplicatorItem = None, material_properties : omni.replicator.core.utils.ReplicatorItem = None, tendon_stiffnesses : omni.replicator.core.utils.ReplicatorItem = None, tendon_dampings : omni.replicator.core.utils.ReplicatorItem = None, tendon_limit_stiffnesses : omni.replicator.core.utils.ReplicatorItem = None, tendon_lower_limits : omni.replicator.core.utils.ReplicatorItem = None, tendon_upper_limits : omni.replicator.core.utils.ReplicatorItem = None, tendon_rest_lengths : omni.replicator.core.utils.ReplicatorItem = None, tendon_offsets : omni.replicator.core.utils.ReplicatorItem = None)
- [function] randomize_rigid_prim_view(view_name : str, operation : str = 'direct', num_buckets : int = None, position : omni.replicator.core.utils.ReplicatorItem = None, orientation : omni.replicator.core.utils.ReplicatorItem = None, linear_velocity : omni.replicator.core.utils.ReplicatorItem = None, angular_velocity : omni.replicator.core.utils.ReplicatorItem = None, velocity : omni.replicator.core.utils.ReplicatorItem = None, force : omni.replicator.core.utils.ReplicatorItem = None, mass : omni.replicator.core.utils.ReplicatorItem = None, inertia : omni.replicator.core.utils.ReplicatorItem = None, material_properties : omni.replicator.core.utils.ReplicatorItem = None, contact_offset : omni.replicator.core.utils.ReplicatorItem = None, rest_offset : omni.replicator.core.utils.ReplicatorItem = None)
- [function] randomize_simulation_context(operation : str = 'direct', gravity : omni.replicator.core.utils.ReplicatorItem = None)
- [function] register_articulation_view(articulation_view : Articulation)
- [function] register_rigid_prim_view(rigid_prim_view : RigidPrim)
- [function] register_simulation_context(simulation_context : SimulationContext | World)
- [function] step_randomization(reset_inds : list | ndarray | Tensor | None = [])

## isaacsim.replicator.domain_randomization.scripts.trigger
- [function] on_rl_frame ( num_envs : int )

## isaacsim.replicator.domain_randomization.scripts.utils
- [function] calculate_truncation_ratio_simple ( corners , img_width , img_height )
- [function] get_distribution_params(distribution : omni.replicator.core.utils.ReplicatorItem, parameters : List [ str ])
- [function] get_image_space_points ( points , view_proj_matrix )
- [function] get_semantics(num_semantics, num_semantic_tokens, instance_semantic_map, min_semantic_idx, max_semantic_hierarchy_depth, semantic_token_map, required_semantic_types)
- [function] set_distribution_params(distribution : omni.replicator.core.utils.ReplicatorItem, parameters : Dict)

### NumpyEncoder
- [class] class NumpyEncoder(*, skipkeys = False, ensure_ascii = True, check_circular = True, allow_nan = True, sort_keys = False, indent = None, separators = None, default = None)
- [method] default ( obj )

## isaacsim.replicator.writers

### DOPEWriter
- [class] class DOPEWriter ( * args : Any , ** kwargs : Any )
- [method] is_last_frame_valid ( ) → bool
- [method] register_pose_annotator ( )
- [method] setup_writer ( writer_config : dict )
- [method] write ( data : dict )
- [attribute] image_output_format
- [attribute] output_dir
- [attribute] semantic_types
- [attribute] use_s3

### DataVisualizationWriter
- [class] class DataVisualizationWriter ( * args : Any , ** kwargs : Any )
- [method] detach ( )
- [method] write ( data : dict )
- [attribute] BB_2D_LOOSE = 'bounding_box_2d_loose_fast'
- [attribute] BB_2D_TIGHT = 'bounding_box_2d_tight_fast'
- [attribute] BB_3D = 'bounding_box_3d_fast'
- [attribute] SUPPORTED_BACKGROUNDS = ['rgb', 'normals']

### PoseWriter
- [class] class PoseWriter ( * args : Any , ** kwargs : Any )
- [method] detach ( )
- [method] get_current_frame_id ( )
- [method] write ( data : dict )
- [attribute] BB3D_ANNOT_NAME = 'bounding_box_3d_fast'
- [attribute] CAM_PARAMS_ANNOT_NAME = 'camera_params'
- [attribute] CUBOID_EDGE_COLORS = {'back': 'blue', 'connecting': 'green', 'front': 'red'}
- [attribute] CUBOID_KEYPOINTS_ORDER_DEFAULT = ['Center', 'LDB', 'LDF', 'LUB', 'LUF', 'RDB', 'RDF', 'RUB', 'RUF']
- [attribute] CUBOID_KEYPOINT_COLORS = ['white', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'purple']
- [attribute] CUBOID_KEYPOINT_ORDER_DOPE = ['LUF', 'RUF', 'RDF', 'LDF', 'LUB', 'RUB', 'RDB', 'LDB', 'Center']
- [attribute] RGB_ANNOT_NAME = 'rgb'
- [attribute] SUPPORTED_FORMATS = {'centerpose', 'dope'}

### PytorchListener
- [class] class PytorchListener
- [method] get_rgb_data ( ) → Tensor | None
- [method] write_data ( data : dict ) → None

### PytorchWriter
- [class] class PytorchWriter ( * args : Any , ** kwargs : Any )
- [method] write ( data : dict ) → None

### YCBVideoWriter
- [class] class YCBVideoWriter ( * args : Any , ** kwargs : Any )
- [method] is_last_frame_valid ( ) → bool
- [method] register_pose_annotator ( )
- [method] save_mesh_vertices(coord_prim : pxr.Usd.Prim, model_name : str, output_folder : str)
- [method] setup_writer ( writer_config : dict )
- [method] write ( data : dict )
- [attribute] bounding_box_2d_tight
- [attribute] class_name_to_index_map
- [attribute] distance_to_image_plane
- [attribute] factor_depth
- [attribute] image_output_format
- [attribute] intrinsic_matrix
- [attribute] num_frames
- [attribute] output_dir
- [attribute] pose
- [attribute] rgb
- [attribute] semantic_segmentation
- [attribute] semantic_types

## isaacsim.robot.manipulators.controllers

### PickPlaceController
- [class] class PickPlaceController(name : str, cspace_controller : BaseController, gripper : Gripper, end_effector_initial_height : float | None = None, events_dt : List [ float ] | None = None)
- [method] forward(picking_position : ndarray, placing_position : ndarray, current_joint_positions : ndarray, end_effector_offset : ndarray | None = None, end_effector_orientation : ndarray | None = None)
- [method] get_current_event ( ) → int
- [method] is_done ( ) → bool
- [method] is_paused ( ) → bool
- [method] pause ( ) → None
- [method] reset(end_effector_initial_height : float | None = None, events_dt : List [ float ] | None = None)
- [method] resume ( ) → None

### StackingController
- [class] class StackingController(name : str, pick_place_controller : PickPlaceController, picking_order_cube_names : List [ str ], robot_observation_name : str)
- [method] forward(observations : dict, end_effector_orientation : ndarray | None = None, end_effector_offset : ndarray | None = None)
- [method] is_done ( ) → bool
- [method] reset(picking_order_cube_names : List [ str ] | None = None)

## isaacsim.robot.manipulators.grippers

### Gripper
- [class] class Gripper ( end_effector_prim_path : str )
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] abstract close ( ) → None
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] abstract forward(* args, ** kwargs)
- [method] get_angular_velocity ( )
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_com ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] abstract get_default_state ( * args , ** kwargs )
- [method] get_density ( ) → float
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] abstract open ( ) → None
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] abstract set_default_state ( * args , ** kwargs )
- [method] set_density ( density : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale ( scale : Sequence [ float ] | None ) → None
- [method] set_mass ( mass : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### ParallelGripper
- [class] class ParallelGripper(end_effector_prim_path : str, joint_prim_names : List [ str ], joint_opened_positions : ndarray, joint_closed_positions : ndarray, action_deltas : ndarray = None, use_mimic_joints : bool = False)
- [method] apply_action(control_actions : ArticulationAction)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] close ( ) → None
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] forward(action : str)
- [method] get_action_deltas ( ) → ndarray
- [method] get_angular_velocity ( )
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_com ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → ndarray
- [method] get_density ( ) → float
- [method] get_joint_positions ( ) → ndarray
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize(articulation_apply_action_func : Callable, get_joint_positions_func : Callable, set_joint_positions_func : Callable, dof_names : List, physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] open ( ) → None
- [method] post_reset ( )
- [method] set_action_deltas ( value : ndarray ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_default_state(joint_positions : ndarray)
- [method] set_density ( density : float ) → None
- [method] set_joint_positions ( positions : ndarray ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property active_joint_count
- [property] property active_joint_indices
- [property] property joint_closed_positions : ndarray
- [property] property joint_dof_indicies : ndarray
- [property] property joint_opened_positions : ndarray
- [property] property joint_prim_names : List [ str ]
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### SurfaceGripper
- [class] class SurfaceGripper ( end_effector_prim_path : str , surface_gripper_path : str )
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] close ( ) → None
- [method] disable_rigid_body_physics ( ) → None
- [method] enable_rigid_body_physics ( ) → None
- [method] forward(action : str)
- [method] get_angular_velocity ( )
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_com ( ) → float
- [method] get_current_dynamic_state ( ) → DynamicState
- [method] get_default_state ( ) → dict
- [method] get_density ( ) → float
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_mass ( ) → float
- [method] get_sleep_threshold ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None, articulation_num_dofs : int = None)
- [method] is_closed ( ) → bool
- [method] is_open ( ) → bool
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] open ( ) → None
- [method] post_reset ( )
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_com(position : ndarray, orientation : ndarray)
- [method] set_default_state ( opened : bool )
- [method] set_density ( density : float ) → None
- [method] set_linear_velocity ( velocity : ndarray )
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_mass ( mass : float ) → None
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] update ( ) → None
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

## isaacsim.robot.manipulators.manipulators

### SingleManipulator
- [class] class SingleManipulator(prim_path : str, end_effector_prim_path : str, name : str = 'single_manipulator', position : Sequence [ float ] | None = None, translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, scale : Sequence [ float ] | None = None, visible : bool | None = None, gripper : Gripper = None)
- [method] apply_action(control_actions : ArticulationAction)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_gravity ( ) → None
- [method] enable_gravity ( ) → None
- [method] get_angular_velocity ( ) → ndarray
- [method] get_applied_action ( ) → ArticulationAction
- [method] get_applied_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_articulation_body_count ( ) → int
- [method] get_articulation_controller ( ) → ArticulationController
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_enabled_self_collisions ( ) → int
- [method] get_joint_positions(joint_indices : List | ndarray | None = None)
- [method] get_joint_velocities(joint_indices : List | ndarray | None = None)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_measured_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_measured_joint_forces(joint_indices : List | ndarray | None = None)
- [method] get_position_residual(report_max : bool | None = True)
- [method] get_sleep_threshold ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_solver_velocity_iteration_count ( ) → int
- [method] get_stabilization_threshold ( ) → float
- [method] get_velocity_residual(report_max : bool | None = True)
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] get_world_velocity ( ) → ndarray
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity(velocity : ndarray)
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_enabled_self_collisions ( flag : bool ) → None
- [method] set_joint_efforts(efforts : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_positions(positions : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_velocities(velocities : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joints_default_state(positions : ndarray | None = None, velocities : ndarray | None = None, efforts : ndarray | None = None)
- [method] set_linear_velocity(velocity : ndarray)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_solver_position_iteration_count(count : int)
- [method] set_solver_velocity_iteration_count ( count : int )
- [method] set_stabilization_threshold(threshold : float)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_world_velocity ( velocity : ndarray )
- [property] property dof_names : List [ str ]
- [property] property dof_properties : ndarray
- [property] property end_effector : SingleRigidPrim
- [property] property gripper : Gripper
- [property] property handles_initialized : bool
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

## isaacsim.robot.surface_gripper

### CreateSurfaceGripper
- [class] class CreateSurfaceGripper ( * args : Any , ** kwargs : Any )

### GripperView
- [class] class GripperView(paths : str = None, max_grip_distance : np.ndarray | wp.array | None = None, coaxial_force_limit : np.ndarray | wp.array | None = None, shear_force_limit : np.ndarray | wp.array | None = None, retry_interval : np.ndarray | wp.array | None = None, positions : np.ndarray | wp.array | None = None, translations : np.ndarray | wp.array | None = None, orientations : np.ndarray | wp.array | None = None, scales : np.ndarray | wp.array | None = None, reset_xform_op_properties : bool = True)
- [method] apply_gripper_action(values : list [ float ], indices : list | np.ndarray | wp.array | None = None)
- [method] apply_visual_materials(materials : type [ 'VisualMaterial' ] | list [ type [ 'VisualMaterial' ] ], *, weaker_than_descendants : bool | list | np.ndarray | wp.array | None = None, indices : int | list | np.ndarray | wp.array | None = None)
- [method] static ensure_api(prims : list [ Usd.Prim ], api : type, * args, ** kwargs)
- [method] get_applied_visual_materials(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_default_state(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_gripped_objects(indices : list | np.ndarray | wp.array | None = None)
- [method] get_local_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_local_scales(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_surface_gripper_properties(indices : list | np.ndarray | wp.array | None = None)
- [method] get_surface_gripper_status(indices : list | np.ndarray | wp.array | None = None)
- [method] get_visibilities(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] get_world_poses(*, indices : int | list | np.ndarray | wp.array | None = None)
- [method] reset_to_default_state(*, warn_on_non_default_state : bool = False)
- [method] reset_xform_op_properties ( ) → None
- [method] static resolve_paths(paths : str | list [ str ], raise_on_mixed_paths : bool = True)
- [method] set_default_state(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_poses(translations : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_local_scales(scales : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_surface_gripper_properties(max_grip_distance : list [ float ] | None = None, coaxial_force_limit : list [ float ] | None = None, shear_force_limit : list [ float ] | None = None, retry_interval : list [ float ] | None = None, indices : list | np.ndarray | wp.array | None = None)
- [method] set_visibilities(visibilities : bool | list | np.ndarray | wp.array, *, indices : int | list | np.ndarray | wp.array | None = None)
- [method] set_world_poses(positions : list | np.ndarray | wp.array | None = None, orientations : list | np.ndarray | wp.array | None = None, *, indices : int | list | np.ndarray | wp.array | None = None)
- [property] property is_non_root_articulation_link : bool
- [property] property paths : list [ str ]
- [property] property prims : list [ pxr.Usd.Prim ]
- [property] property valid : bool

## isaacsim.robot.surface_gripper._surface_gripper

### SurfaceGripperInterface
- [class] class SurfaceGripperInterface
- [method] close_gripper(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_path : str)
- [method] close_gripper_batch(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_paths : List [ str ])
- [method] get_gripped_objects(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_path : str)
- [method] get_gripped_objects_batch(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_paths : List [ str ])
- [method] get_gripper_status(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_path : str)
- [method] get_gripper_status_batch(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_paths : List [ str ])
- [method] open_gripper(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_path : str)
- [method] open_gripper_batch(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_paths : List [ str ])
- [method] set_gripper_action(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_path : str, action : float)
- [method] set_gripper_action_batch(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, prim_paths : List [ str ], actions : List [ float ])
- [method] set_write_to_usd(self : isaacsim.robot.surface_gripper._surface_gripper.SurfaceGripperInterface, write_to_usd : bool)

## isaacsim.robot.wheeled_robots.controllers
- [function] pid_control ( target , current , Kp = 0.1 )
- [function] quintic_polynomials_planner(sx, sy, syaw, sv, sa, gx, gy, gyaw, gv, ga, max_accel, max_jerk, dt)
- [function] stanley_control(state, cx, cy, cyaw, last_target_idx, p = 0.5, i = 0.01, d = 10, k = 0.5)

### DifferentialController
- [class] class DifferentialController(name : str, wheel_radius : float, wheel_base : float, max_linear_speed : float = 1e+20, max_angular_speed : float = 1e+20, max_wheel_speed : float = 1e+20)
- [method] forward(command : ndarray)
- [method] reset ( ) → None

### HolonomicController
- [class] class HolonomicController(name : str, wheel_radius : ndarray | None = None, wheel_positions : ndarray | None = None, wheel_orientations : ndarray | None = None, mecanum_angles : ndarray | None = None, wheel_axis : float = array([1, 0, 0]), up_axis : float = array([0, 0, 1]), max_linear_speed : float = 1e+20, max_angular_speed : float = 1e+20, max_wheel_speed : float = 1e+20, linear_gain : float = 1.0, angular_gain : float = 1.0)
- [method] build_base ( )
- [method] forward(command : ndarray)
- [method] reset ( ) → None

### QuinticPolynomial
- [class] class QuinticPolynomial ( xs , vxs , axs , xe , vxe , axe , time )
- [method] calc_first_derivative ( t )
- [method] calc_point ( t )
- [method] calc_second_derivative ( t )
- [method] calc_third_derivative ( t )

### WheelBasePoseController
- [class] class WheelBasePoseController(name : str, open_loop_wheel_controller : BaseController, is_holonomic : bool = False)
- [method] forward(start_position : ndarray, start_orientation : ndarray, goal_position : ndarray, lateral_velocity : float = 0.2, yaw_velocity : float = 0.5, heading_tol : float = 0.05, position_tol : float = 0.04)
- [method] reset ( ) → None

## isaacsim.robot.wheeled_robots.robots

### HolonomicRobotUsdSetup
- [class] class HolonomicRobotUsdSetup ( robot_prim_path : str , com_prim_path : str )
- [method] from_usd ( robot_prim_path , com_prim_path )
- [method] get_articulation_controller_params ( )
- [method] get_holonomic_controller_params ( )
- [property] property mecanum_angles
- [property] property up_axis
- [property] property wheel_axis
- [property] property wheel_dof_names
- [property] property wheel_orientations
- [property] property wheel_positions
- [property] property wheel_radius

### WheeledRobot
- [class] class WheeledRobot(prim_path : str, name : str = 'wheeled_robot', robot_path : str | None = None, wheel_dof_names : str | None = None, wheel_dof_indices : int | None = None, usd_path : str | None = None, create_robot : bool | None = False, position : ndarray | None = None, orientation : ndarray | None = None)
- [method] apply_action(control_actions : ArticulationAction)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] apply_wheel_actions(actions : ArticulationAction)
- [method] disable_gravity ( ) → None
- [method] enable_gravity ( ) → None
- [method] get_angular_velocity ( ) → ndarray
- [method] get_applied_action ( ) → ArticulationAction
- [method] get_applied_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_articulation_body_count ( ) → int
- [method] get_articulation_controller ( ) → ArticulationController
- [method] get_articulation_controller_properties ( )
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_enabled_self_collisions ( ) → int
- [method] get_joint_positions(joint_indices : List | ndarray | None = None)
- [method] get_joint_velocities(joint_indices : List | ndarray | None = None)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_measured_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_measured_joint_forces(joint_indices : List | ndarray | None = None)
- [method] get_position_residual(report_max : bool | None = True)
- [method] get_sleep_threshold ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_solver_velocity_iteration_count ( ) → int
- [method] get_stabilization_threshold ( ) → float
- [method] get_velocity_residual(report_max : bool | None = True)
- [method] get_visibility ( ) → bool
- [method] get_wheel_positions ( )
- [method] get_wheel_velocities ( )
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] get_world_velocity ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_enabled_self_collisions ( flag : bool ) → None
- [method] set_joint_efforts(efforts : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_positions(positions : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_velocities(velocities : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joints_default_state(positions : ndarray | None = None, velocities : ndarray | None = None, efforts : ndarray | None = None)
- [method] set_linear_velocity ( velocity : ndarray ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_solver_position_iteration_count ( count : int ) → None
- [method] set_solver_velocity_iteration_count ( count : int )
- [method] set_stabilization_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_wheel_positions ( positions ) → None
- [method] set_wheel_velocities ( velocities ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_world_velocity ( velocity : ndarray )
- [property] property dof_names : List [ str ]
- [property] property dof_properties : ndarray
- [property] property handles_initialized : bool
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property wheel_dof_indices

## isaacsim.robot_motion.motion_generation

### ArticulationKinematicsSolver
- [class] class ArticulationKinematicsSolver(robot_articulation : SingleArticulation, kinematics_solver : KinematicsSolver, end_effector_frame_name : str)
- [method] compute_end_effector_pose(position_only = False)
- [method] compute_inverse_kinematics(target_position : array, target_orientation : array | None = None, position_tolerance : float | None = None, orientation_tolerance : float | None = None)
- [method] get_end_effector_frame ( ) → str
- [method] get_joints_subset ( ) → ArticulationSubset
- [method] get_kinematics_solver ( ) → KinematicsSolver
- [method] set_end_effector_frame(end_effector_frame_name : str)

### ArticulationMotionPolicy
- [class] class ArticulationMotionPolicy(robot_articulation : SingleArticulation, motion_policy : MotionPolicy, default_physics_dt : float = 0.016666666666666666)
- [method] get_active_joints_subset ( ) → ArticulationSubset
- [method] get_default_physics_dt ( ) → float
- [method] get_motion_policy ( ) → MotionPolicy
- [method] get_next_articulation_action(physics_dt : float = None)
- [method] get_robot_articulation ( ) → SingleArticulation
- [method] get_watched_joints_subset ( ) → ArticulationSubset
- [method] move ( physics_dt : float = None ) → None
- [method] set_default_physics_dt(physics_dt : float)

### ArticulationTrajectory
- [class] class ArticulationTrajectory(robot_articulation : SingleArticulation, trajectory : Trajectory, physics_dt : float)
- [method] get_action_at_time(time : float)
- [method] get_action_sequence(timestep : float = None)
- [method] get_active_joints_subset ( ) → ArticulationSubset
- [method] get_robot_articulation ( ) → SingleArticulation
- [method] get_trajectory ( ) → Trajectory
- [method] get_trajectory_duration ( ) → float

### KinematicsSolver
- [class] class KinematicsSolver
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool | None = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] compute_forward_kinematics(frame_name : str, joint_positions : array, position_only : bool | None = False)
- [method] compute_inverse_kinematics(frame_name : str, target_positions : array, target_orientation : array | None = None, warm_start : array | None = None, position_tolerance : float | None = None, orientation_tolerance : float | None = None)
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] get_all_frame_names ( ) → List [ str ]
- [method] get_joint_names ( ) → List [ str ]
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] set_robot_base_pose(robot_positions : array, robot_orientation : array)
- [method] supports_collision_avoidance ( ) → bool
- [method] update_world(updated_obstacles : List | None = None)

### LulaKinematicsSolver
- [class] class LulaKinematicsSolver(robot_description_path : str, urdf_path : str, robot_description : RobotDescription | None = None)
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool | None = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] compute_forward_kinematics(frame_name : str, joint_positions : array, position_only : bool | None = False)
- [method] compute_inverse_kinematics(frame_name : str, target_position : array, target_orientation : array = None, warm_start : array = None, position_tolerance : float = None, orientation_tolerance : float = None)
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] get_all_frame_names ( ) → List [ str ]
- [method] get_cspace_acceleration_limits ( ) → array
- [method] get_cspace_jerk_limits ( ) → array
- [method] get_cspace_position_limits ( ) → Tuple [ array , array ]
- [method] get_cspace_velocity_limits ( ) → array
- [method] get_default_cspace_seeds ( ) → List [ array ]
- [method] get_default_orientation_tolerance ( ) → float
- [method] get_default_position_tolerance ( ) → float
- [method] get_joint_names ( ) → List [ str ]
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] set_default_cspace_seeds(seeds : array)
- [method] set_default_orientation_tolerance(tolerance : float)
- [method] set_default_position_tolerance(tolerance : float)
- [method] set_robot_base_pose(robot_position : array, robot_orientation : array)
- [method] supports_collision_avoidance ( ) → bool
- [method] update_world(updated_obstacles : List | None = None)
- [property] property bfgs_cspace_limit_biasing
- [property] property bfgs_cspace_limit_biasing_weight
- [property] property bfgs_cspace_limit_penalty_region
- [property] property bfgs_gradient_norm_termination
- [property] property bfgs_gradient_norm_termination_coarse_scale_factor
- [property] property bfgs_max_iterations
- [property] property bfgs_orientation_weight
- [property] property bfgs_position_weight
- [property] property ccd_bracket_search_num_uniform_samples
- [property] property ccd_descent_termination_delta
- [property] property ccd_max_iterations
- [property] property ccd_orientation_weight
- [property] property ccd_position_weight
- [property] property irwin_hall_sampling_order
- [property] property max_num_descents
- [property] property sampling_seed

### MotionPolicy
- [class] class MotionPolicy
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool | None = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] compute_joint_targets(active_joint_positions : array, active_joint_velocities : array, watched_joint_positions : array, watched_joint_velocities : array, frame_duration : float)
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] get_active_joints ( ) → List [ str ]
- [method] get_watched_joints ( ) → List [ str ]
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] set_cspace_target(active_joint_targets : array)
- [method] set_end_effector_target(target_translation = None, target_orientation = None)
- [method] set_robot_base_pose(robot_translation : array, robot_orientation : array)
- [method] update_world(updated_obstacles : List | None = None)

### MotionPolicyController
- [class] class MotionPolicyController(name : str, articulation_motion_policy : ArticulationMotionPolicy)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool = False)
- [method] forward(target_end_effector_position : ndarray, target_end_effector_orientation : ndarray | None = None)
- [method] get_articulation_motion_policy ( ) → ArticulationMotionPolicy
- [method] get_motion_policy ( ) → MotionPolicy
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None

### PathPlanner
- [class] class PathPlanner
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool | None = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] compute_path(active_joint_positions : array, watched_joint_positions : array)
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] get_active_joints ( ) → List [ str ]
- [method] get_watched_joints ( ) → List [ str ]
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] set_cspace_target(active_joint_targets : array)
- [method] set_end_effector_target(target_translation, target_orientation = None)
- [method] set_robot_base_pose(robot_translation : array, robot_orientation : array)
- [method] update_world(updated_obstacles : List | None = None)

### Trajectory
- [class] class Trajectory
- [method] get_active_joints ( ) → List [ str ]
- [method] get_joint_targets(time : float)
- [property] property end_time : float
- [property] property start_time : float

### WorldInterface
- [class] class WorldInterface
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool | None = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] update_world(updated_obstacles : List | None = None)

## isaacsim.robot_motion.motion_generation.lula

### LulaCSpaceTrajectoryGenerator
- [class] class LulaCSpaceTrajectoryGenerator(robot_description_path : str, urdf_path : str)
- [method] compute_c_space_trajectory(waypoint_positions : array)
- [method] compute_timestamped_c_space_trajectory(waypoint_positions : array, timestamps : array, interpolation_mode : str = 'cubic_spline')
- [method] get_active_joints ( ) → List [ str ]
- [method] get_c_space_acceleration_limits ( )
- [method] get_c_space_jerk_limits ( )
- [method] get_c_space_position_limits ( )
- [method] get_c_space_velocity_limits ( )
- [method] set_c_space_acceleration_limits(acceleration_limits : array)
- [method] set_c_space_jerk_limits(jerk_limits : array)
- [method] set_c_space_position_limits(lower_position_limits : array, upper_position_limits : array)
- [method] set_c_space_velocity_limits(velocity_limits : array)
- [method] set_solver_param(param_name : str, param_val : int | float | str)

### LulaTaskSpaceTrajectoryGenerator
- [class] class LulaTaskSpaceTrajectoryGenerator(robot_description_path : str, urdf_path : str)
- [method] compute_task_space_trajectory_from_path_spec(path_spec : CompositePathSpec | TaskSpacePathSpec, frame_name : str)
- [method] compute_task_space_trajectory_from_points(positions : array, orientations : array, frame_name : str)
- [method] get_active_joints ( ) → List [ str ]
- [method] get_all_frame_names ( ) → List [ str ]
- [method] get_c_space_acceleration_limits ( )
- [method] get_c_space_jerk_limits ( )
- [method] get_c_space_position_limits ( )
- [method] get_c_space_velocity_limits ( )
- [method] get_path_conversion_config ( ) → TaskSpacePathConversionConfig
- [method] set_c_space_acceleration_limits(acceleration_limits : array)
- [method] set_c_space_jerk_limits(jerk_limits : array)
- [method] set_c_space_position_limits(lower_position_limits : array, upper_position_limits : array)
- [method] set_c_space_trajectory_generator_solver_param(param_name : str, param_val : int | float | str)
- [method] set_c_space_velocity_limits(velocity_limits : array)

### LulaTrajectory
- [class] class LulaTrajectory ( trajectory , active_joints )
- [method] get_active_joints ( ) → List [ str ]
- [method] get_joint_targets(time)
- [property] property end_time : float
- [property] property start_time : float

### RRT
- [class] class RRT(robot_description_path : str, urdf_path : str, rrt_config_path : str, end_effector_frame_name : str)
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] compute_path(active_joint_positions, watched_joint_positions)
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] get_active_joints ( ) → List
- [method] get_end_effector_pose(active_joint_positions : array, frame_name : str)
- [method] get_watched_joints ( ) → List
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] set_cspace_target ( active_joint_targets : array ) → None
- [method] set_end_effector_target(target_translation, target_orientation = None)
- [method] set_max_iterations ( max_iter : int ) → None
- [method] set_param(param_name : str, value : array | float | int | str)
- [method] set_random_seed ( random_seed : int ) → None
- [method] set_robot_base_pose(robot_position : array, robot_orientation : array)
- [method] update_world ( updated_obstacles : List = None ) → None

## isaacsim.robot_motion.motion_generation.lula.motion_policies

### RmpFlow
- [class] class RmpFlow(robot_description_path : str, urdf_path : str, rmpflow_config_path : str, end_effector_frame_name : str, maximum_substep_size : float, ignore_robot_state_updates = False)
- [method] add_capsule(capsule : DynamicCapsule | VisualCapsule, static : bool = False)
- [method] add_cone(cone : DynamicCone | VisualCone, static : bool = False)
- [method] add_cuboid(cuboid : DynamicCuboid | FixedCuboid | VisualCuboid, static : bool = False)
- [method] add_cylinder(cylinder : DynamicCylinder | VisualCylinder, static : bool = False)
- [method] add_ground_plane(ground_plane : GroundPlane)
- [method] add_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>, static: bool = False)
- [method] add_sphere(sphere : DynamicSphere | VisualSphere, static : bool = False)
- [method] compute_joint_targets(active_joint_positions : array, active_joint_velocities : array, watched_joint_positions : array, watched_joint_velocities : array, frame_duration : float)
- [method] delete_collision_sphere_prims ( ) → None
- [method] delete_end_effector_prim ( ) → None
- [method] disable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] enable_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] get_active_joints ( ) → List [ str ]
- [method] get_collision_spheres_as_prims ( ) → List
- [method] get_default_cspace_position_target ( )
- [method] get_end_effector_as_prim ( ) → VisualCuboid
- [method] get_end_effector_pose(active_joint_positions : array)
- [method] get_internal_robot_joint_states ( ) → Tuple [ array , array , array , array ]
- [method] get_kinematics_solver ( ) → LulaKinematicsSolver
- [method] get_watched_joints ( ) → List [ str ]
- [method] remove_obstacle(obstacle: <module 'isaacsim.core.api.objects' from '/builds/omniverse/isaac/omni_isaac_sim/_build/linux-x86_64/release/exts/isaacsim.core.api/isaacsim/core/api/objects/__init__.py'>)
- [method] reset ( ) → None
- [method] set_cspace_target ( active_joint_targets ) → None
- [method] set_end_effector_target(target_position = None, target_orientation = None)
- [method] set_ignore_state_updates ( ignore_robot_state_updates ) → None
- [method] set_internal_robot_joint_states(active_joint_positions : array, active_joint_velocities : array, watched_joint_positions : array, watched_joint_velocities : array)
- [method] set_robot_base_pose(robot_position : array, robot_orientation : array)
- [method] stop_visualizing_collision_spheres ( ) → None
- [method] stop_visualizing_end_effector ( ) → None
- [method] update_world ( updated_obstacles : List = None ) → None
- [method] visualize_collision_spheres ( ) → None
- [method] visualize_end_effector_position ( ) → None

## isaacsim.robot_setup.assembler

### AssembledBodies
- [class] class AssembledBodies(base_path : str, attach_path : str, fixed_joint : pxr.UsdPhysics.FixedJoint, root_joints : List [ pxr.UsdPhysics.Joint ], attach_body_articulation_root : pxr.Usd.Prim, collision_mask = None)
- [property] property attach_body_articulation_root : pxr.Usd.Prim
- [property] property attach_path : str
- [property] property base_path : str
- [property] property collision_mask : pxr.Usd.Relationship
- [property] property fixed_joint : pxr.UsdPhysics.FixedJoint
- [property] property root_joints : List [ pxr.UsdPhysics.Joint ]

### AssembledRobot
- [class] class AssembledRobot(assembled_robots : AssembledBodies)
- [property] property attach_path : str
- [property] property base_path : str
- [property] property collision_mask : pxr.Usd.Relationship
- [property] property fixed_joint : pxr.UsdPhysics.FixedJoint
- [property] property root_joints : List [ pxr.UsdPhysics.Joint ]

### RobotAssembler
- [class] class RobotAssembler
- [method] assemble ( )
- [method] assemble_rigid_bodies(base_path : str, attach_path : str, base_mount_frame : str, attach_mount_frame : str, mask_all_collisions : bool = True, refresh_asset_paths : bool = False)
- [method] begin_assembly(stage, base_prim_path, base_mount_path, attachment_prim_path, attachment_mount_path, variant_set, variant_name)
- [method] cancel_assembly ( )
- [method] create_fixed_joint(prim_path : str, target0 : str = None, target1 : str = None)
- [method] finish_assemble ( )
- [method] is_root_joint ( prim ) → bool
- [method] mask_collisions(prim_path_a : str, prim_path_b : str)
- [method] reset ( )

## isaacsim.robot_setup.grasp_editor
- [function] import_grasps_from_file(file_path : str)

### GraspSpec
- [class] class GraspSpec ( imported_data : dict )
- [method] compute_gripper_pose_from_rigid_body_pose(grasp_name : str, rb_trans : array, rb_quat : array)
- [method] compute_rigid_body_pose_from_gripper_pose(grasp_name : str, gripper_trans : array, gripper_quat : array)
- [method] get_grasp_dict_by_name ( name : str ) → dict
- [method] get_grasp_dicts ( ) → dict
- [method] get_grasp_names ( ) → List [ str ]

## isaacsim.sensors.camera

### Camera
- [class] class Camera(prim_path : str, name : str = 'camera', frequency : int | None = None, dt : float | None = None, resolution : Tuple [ int , int ] | None = None, position : ndarray | None = None, orientation : ndarray | None = None, translation : ndarray | None = None, render_product_path : str = None, annotator_device : str = None)
- [method] add_bounding_box_2d_loose_to_frame(init_params : dict = {})
- [method] add_bounding_box_2d_tight_to_frame(init_params : dict = {})
- [method] add_bounding_box_3d_to_frame ( init_params : dict = {} ) → None
- [method] add_distance_to_camera_to_frame ( init_params : dict = {} ) → None
- [method] add_distance_to_image_plane_to_frame(init_params : dict = {})
- [method] add_instance_id_segmentation_to_frame(init_params : dict = {})
- [method] add_instance_segmentation_to_frame(init_params : dict = {})
- [method] add_motion_vectors_to_frame ( init_params : dict = {} ) → None
- [method] add_normals_to_frame ( init_params : dict = {} ) → None
- [method] add_occlusion_to_frame ( init_params : dict = {} ) → None
- [method] add_pointcloud_to_frame(include_unlabelled : bool = True, init_params : dict = {})
- [method] add_rgb_to_frame ( init_params : dict = {} ) → None
- [method] add_semantic_segmentation_to_frame(init_params : dict = {})
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] attach_annotator ( annotator_name : str , ** kwargs ) → None
- [method] destroy ( ) → None
- [method] detach_annotator ( annotator_name : str ) → None
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_aspect_ratio ( ) → float
- [method] get_camera_points_from_image_coords(points_2d, depth, device : str = None, backend_utils_cls : type = None)
- [method] get_clipping_range ( ) → Tuple [ float , float ]
- [method] get_current_frame ( clone = False ) → dict
- [method] get_default_state ( ) → XFormPrimState
- [method] get_depth ( device : str = None ) → np.ndarray | wp.types.array
- [method] get_dt ( ) → float
- [method] get_fisheye_polynomial_properties ( ) → Tuple [ float , float , float , float , float , List ]
- [method] get_focal_length ( ) → float
- [method] get_focus_distance ( ) → float
- [method] get_frequency ( ) → float
- [method] get_ftheta_properties ( ) → Tuple [ float , float , Tuple [ float , float ] , float , List [ float ] ]
- [method] get_horizontal_aperture ( ) → float
- [method] get_horizontal_fov ( ) → float
- [method] get_image_coords_from_world_points(points_3d : ndarray)
- [method] get_intrinsics_matrix(device : str = None, backend_utils_cls : type = None)
- [method] get_kannala_brandt_k3_properties ( ) → Tuple [ float , float , Tuple [ float , float ] , float , List [ float ] ]
- [method] get_lens_aperture ( ) → float
- [method] get_lens_distortion_model ( ) → str
- [method] get_local_pose ( camera_axes : str = 'world' ) → None
- [method] get_local_scale ( ) → ndarray
- [method] get_lut_properties ( ) → Tuple [ float , float , Tuple [ float , float ] , str , str ]
- [method] get_opencv_fisheye_properties ( ) → Tuple [ float , float , float , float , List ]
- [method] get_opencv_pinhole_properties ( ) → Tuple [ float , float , float , float , List ]
- [method] get_pointcloud(device : str = None, world_frame : bool = True)
- [method] get_projection_mode ( ) → str
- [method] get_projection_type ( ) → str
- [method] get_rad_tan_thin_prism_properties ( ) → Tuple [ float , float , Tuple [ float , float ] , float , List [ float ] ]
- [method] get_render_product_path ( ) → str
- [method] get_resolution ( ) → Tuple [ int , int ]
- [method] get_rgb ( device : str = None ) → np.ndarray | wp.types.array
- [method] get_rgba ( device : str = None ) → np.ndarray | wp.types.array
- [method] get_shutter_properties ( ) → Tuple [ float , float ]
- [method] get_stereo_role ( ) → str
- [method] get_vertical_aperture ( ) → float
- [method] get_vertical_fov ( ) → float
- [method] get_view_matrix_ros(device : str = None, backend_utils_cls : type = None)
- [method] get_visibility ( ) → bool
- [method] get_world_points_from_image_coords(points_2d, depth, device : str = None, backend_utils_cls : type = None)
- [method] get_world_pose(camera_axes : str = 'world')
- [method] get_world_scale ( ) → ndarray
- [method] initialize(physics_sim_view = None, attach_rgb_annotator = True)
- [method] is_paused ( ) → bool
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] pause ( ) → None
- [method] post_reset ( ) → None
- [method] remove_bounding_box_2d_loose_from_frame ( ) → None
- [method] remove_bounding_box_2d_tight_from_frame ( ) → None
- [method] remove_bounding_box_3d_from_frame ( ) → None
- [method] remove_distance_to_camera_from_frame ( ) → None
- [method] remove_distance_to_image_plane_from_frame ( ) → None
- [method] remove_instance_id_segmentation_from_frame ( ) → None
- [method] remove_instance_segmentation_from_frame ( ) → None
- [method] remove_motion_vectors_from_frame ( ) → None
- [method] remove_normals_from_frame ( ) → None
- [method] remove_occlusion_from_frame ( ) → None
- [method] remove_pointcloud_from_frame ( ) → None
- [method] remove_rgb_from_frame ( ) → None
- [method] remove_semantic_segmentation_from_frame ( ) → None
- [method] resume ( ) → None
- [method] set_clipping_range(near_distance : float | None = None, far_distance : float | None = None)
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_dt ( value : float ) → None
- [method] set_fisheye_polynomial_properties(nominal_width : float | None, nominal_height : float | None, optical_centre_x : float | None, optical_centre_y : float | None, max_fov : float | None, polynomial : Sequence [ float ] | None)
- [method] set_focal_length ( value : float )
- [method] set_focus_distance ( value : float )
- [method] set_frequency ( value : int ) → None
- [method] set_ftheta_properties(nominal_height : float | None = None, nominal_width : float | None = None, optical_center : Tuple [ float , float ] | None = None, max_fov : float | None = None, distortion_coefficients : Sequence [ float ] | None = None)
- [method] set_horizontal_aperture(value : float, maintain_square_pixels : bool = True)
- [method] set_kannala_brandt_k3_properties(nominal_height : float | None = None, nominal_width : float | None = None, optical_center : Tuple [ float , float ] | None = None, max_fov : float | None = None, distortion_coefficients : Sequence [ float ] | None = None)
- [method] set_kannala_brandt_properties(nominal_width : float, nominal_height : float, optical_centre_x : float, optical_centre_y : float, max_fov : float | None, distortion_model : Sequence [ float ])
- [method] set_lens_aperture ( value : float )
- [method] set_lens_distortion_model ( value : str ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, camera_axes : str = 'world')
- [method] set_local_scale ( scale : Sequence [ float ] | None ) → None
- [method] set_lut_properties(nominal_height : float | None = None, nominal_width : float | None = None, optical_center : Tuple [ float , float ] | None = None, ray_enter_direction_texture : str | None = None, ray_exit_position_texture : str | None = None)
- [method] set_matching_fisheye_polynomial_properties(nominal_width : float, nominal_height : float, optical_centre_x : float, optical_centre_y : float, max_fov : float | None, distortion_model : Sequence [ float ], distortion_fn : Callable)
- [method] set_opencv_fisheye_properties(cx : float | None = None, cy : float | None = None, fx : float | None = None, fy : float | None = None, fisheye : List [ float ] | None = None)
- [method] set_opencv_pinhole_properties(cx : float | None = None, cy : float | None = None, fx : float | None = None, fy : float | None = None, pinhole : List [ float ] | None = None)
- [method] set_projection_mode ( value : str ) → None
- [method] set_projection_type ( value : str ) → None
- [method] set_rad_tan_thin_prism_properties(nominal_height : float | None = None, nominal_width : float | None = None, optical_center : Tuple [ float , float ] | None = None, max_fov : float | None = None, distortion_coefficients : Sequence [ float ] | None = None)
- [method] set_rational_polynomial_properties(nominal_width : float, nominal_height : float, optical_centre_x : float, optical_centre_y : float, max_fov : float | None, distortion_model : Sequence [ float ])
- [method] set_resolution(value : Tuple [ int , int ], maintain_square_pixels : bool = True)
- [method] set_shutter_properties(delay_open : float | None = None, delay_close : float | None = None)
- [method] set_stereo_role ( value : str ) → None
- [method] set_vertical_aperture(value : float, maintain_square_pixels : bool = True)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None, camera_axes : str = 'world')
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str
- [property] property supported_annotators : List [ str ]

### CameraView
- [class] class CameraView(prim_paths_expr : str = None, name : str = 'camera_prim_view', camera_resolution : Tuple [ int , int ] = (256, 256), output_annotators : List [ str ] | None = ['rgb', 'depth'], positions : ndarray | Tensor | warp.array | None = None, translations : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, scales : ndarray | Tensor | warp.array | None = None, visibilities : ndarray | Tensor | warp.array | None = None, reset_xform_properties : bool = True)
- [method] apply_visual_materials(visual_materials : VisualMaterial | List [ VisualMaterial ], weaker_than_descendants : bool | List [ bool ] | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] destroy ( ) → None
- [method] get_applied_visual_materials(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_aspect_ratios ( ) → float
- [method] get_data(annotator_type : str, *, tiled : bool = False, out : warp.array | None = None)
- [method] get_default_state ( ) → XFormPrimViewState
- [method] get_depth ( out = None ) → Tensor
- [method] get_depth_tiled(out = None, device = 'cpu')
- [method] get_focal_lengths(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_focus_distances(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_horizontal_apertures(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_lens_apertures(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_local_poses(indices : ndarray | list | Tensor | warp.array | None = None, camera_axes : str = 'world')
- [method] get_local_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_projection_modes(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_projection_types(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_render_product_path ( ) → str
- [method] get_resolutions ( ) → Tuple [ int , int ]
- [method] get_rgb ( out = None ) → Tensor
- [method] get_rgb_tiled(out = None, device = 'cpu')
- [method] get_shutter_properties(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_stereo_roles(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_vertical_apertures(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_visibilities(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] get_world_poses(indices : ndarray | list | Tensor | warp.array | None = None, camera_axes : str = 'world', usd : bool = True)
- [method] get_world_scales(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] is_valid(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] is_visual_material_applied(indices : ndarray | list | Tensor | warp.array | None = None)
- [method] post_reset ( ) → None
- [method] set_default_state(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_focal_lengths(values : List [ float ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_focus_distances(values : List [ float ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_horizontal_apertures(values : List [ float ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_lens_apertures(values : List [ float ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_local_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, camera_axes : str = 'world')
- [method] set_local_scales(scales : ndarray | Tensor | warp.array | None, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_projection_modes(values : List [ str ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_projection_types(values : List [ str ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_resolutions(resolution : Tuple [ int , int ])
- [method] set_shutter_properties(values : List [ Tuple [ float , float ] ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_stereo_roles(values : List [ str ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_vertical_apertures(values : List [ float ], indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_visibilities(visibilities : ndarray | Tensor | warp.array, indices : ndarray | list | Tensor | warp.array | None = None)
- [method] set_world_poses(positions : ndarray | Tensor | warp.array | None = None, orientations : ndarray | Tensor | warp.array | None = None, indices : ndarray | list | Tensor | warp.array | None = None, camera_axes : str = 'world', usd : bool = True)
- [property] property count : int
- [property] property initialized : bool
- [property] property is_non_root_articulation_link : bool
- [property] property name : str
- [property] property prim_paths : List [ str ]
- [property] property prims : List [ pxr.Usd.Prim ]

## isaacsim.sensors.physics

### ContactSensor
- [class] class ContactSensor(prim_path : str, name : str | None = 'contact_sensor', frequency : int | None = None, dt : float | None = None, translation : ndarray | None = None, position : ndarray | None = None, min_threshold : float | None = None, max_threshold : float | None = None, radius : float | None = None)
- [method] add_raw_contact_data_to_frame ( ) → None
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_current_frame ( ) → None
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dt ( ) → float
- [method] get_frequency ( ) → int
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_max_threshold ( ) → float
- [method] get_min_threshold ( ) → float
- [method] get_radius ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_paused ( ) → bool
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] pause ( ) → None
- [method] post_reset ( ) → None
- [method] remove_raw_contact_data_from_frame ( ) → None
- [method] resume ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_dt ( value : float ) → None
- [method] set_frequency ( value : float ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_max_threshold ( value : float ) → None
- [method] set_min_threshold ( value : float ) → None
- [method] set_radius ( value : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### EffortSensor
- [class] class EffortSensor(prim_path : str, sensor_period : float = -1, use_latest_data : bool = False, enabled : bool = True)
- [method] apply_action(control_actions : ArticulationAction)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] change_buffer_size ( new_buffer_size : int ) → None
- [method] disable_gravity ( ) → None
- [method] enable_gravity ( ) → None
- [method] get_angular_velocity ( ) → ndarray
- [method] get_applied_action ( ) → ArticulationAction
- [method] get_applied_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_articulation_body_count ( ) → int
- [method] get_articulation_controller ( ) → ArticulationController
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dof_index ( dof_name : str ) → int
- [method] get_enabled_self_collisions ( ) → int
- [method] get_joint_positions(joint_indices : List | ndarray | None = None)
- [method] get_joint_velocities(joint_indices : List | ndarray | None = None)
- [method] get_joints_default_state ( ) → JointsState
- [method] get_joints_state ( ) → JointsState
- [method] get_linear_velocity ( ) → ndarray
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_measured_joint_efforts(joint_indices : List | ndarray | None = None)
- [method] get_measured_joint_forces(joint_indices : List | ndarray | None = None)
- [method] get_position_residual(report_max : bool | None = True)
- [method] get_sensor_reading(interpolation_function = None, use_latest_data = False)
- [method] get_sleep_threshold ( ) → float
- [method] get_solver_position_iteration_count ( ) → int
- [method] get_solver_velocity_iteration_count ( ) → int
- [method] get_stabilization_threshold ( ) → float
- [method] get_velocity_residual(report_max : bool | None = True)
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] get_world_velocity ( ) → ndarray
- [method] initialize(physics_sim_view : omni.physics.tensors.SimulationView = None)
- [method] initialize_callbacks ( ) → None
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] lerp ( start : float , end : float , time : float ) → float
- [method] post_reset ( ) → None
- [method] set_angular_velocity ( velocity : ndarray ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_enabled_self_collisions ( flag : bool ) → None
- [method] set_joint_efforts(efforts : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_positions(positions : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joint_velocities(velocities : ndarray, joint_indices : List | ndarray | None = None)
- [method] set_joints_default_state(positions : ndarray | None = None, velocities : ndarray | None = None, efforts : ndarray | None = None)
- [method] set_linear_velocity ( velocity : ndarray ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_sleep_threshold ( threshold : float ) → None
- [method] set_solver_position_iteration_count ( count : int ) → None
- [method] set_solver_velocity_iteration_count ( count : int )
- [method] set_stabilization_threshold ( threshold : float ) → None
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_world_velocity ( velocity : ndarray )
- [method] update_dof_name ( dof_name : str ) → None
- [property] property dof_names : List [ str ]
- [property] property dof_properties : ndarray
- [property] property handles_initialized : bool
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property num_bodies : int
- [property] property num_dof : int
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### EsSensorReading
- [class] class EsSensorReading(is_valid : bool = False, time : float = 0, value : float = 0)

### IMUSensor
- [class] class IMUSensor(prim_path : str, name : str | None = 'imu_sensor', frequency : int | None = None, dt : float | None = None, translation : ndarray | None = None, position : ndarray | None = None, orientation : ndarray | None = None, linear_acceleration_filter_size : int | None = 1, angular_velocity_filter_size : int | None = 1, orientation_filter_size : int | None = 1)
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_current_frame ( read_gravity = True ) → dict
- [method] get_default_state ( ) → XFormPrimState
- [method] get_dt ( ) → float
- [method] get_frequency ( ) → int
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_paused ( ) → bool
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] pause ( ) → None
- [method] post_reset ( ) → None
- [method] resume ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_dt ( value : float ) → None
- [method] set_frequency ( value : int ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

### IsaacSensorCreateContactSensor
- [class] class IsaacSensorCreateContactSensor ( * args : Any , ** kwargs : Any )

### IsaacSensorCreateImuSensor
- [class] class IsaacSensorCreateImuSensor ( * args : Any , ** kwargs : Any )

### IsaacSensorCreatePrim
- [class] class IsaacSensorCreatePrim ( * args : Any , ** kwargs : Any )

## isaacsim.sensors.physx

### IsaacSensorCreateLightBeamSensor
- [class] class IsaacSensorCreateLightBeamSensor ( * args : Any , ** kwargs : Any )

### ProximitySensor
- [class] class ProximitySensor(parent : pxr.Usd.Prim, callback_fns = [None, None, None], exclusions = [])
- [method] check_for_overlap ( )
- [method] get_active_zones ( ) → List [ str ]
- [method] get_data ( ) → Dict [ str , Dict [ str , float ] ]
- [method] get_entered_zones ( ) → List [ str ]
- [method] get_exited_zones ( ) → List [ str ]
- [method] is_overlapping ( )
- [method] report_hit ( hit )
- [method] reset ( )
- [method] status ( )
- [method] to_string ( )
- [method] update ( )

### RangeSensorCreateGeneric
- [class] class RangeSensorCreateGeneric ( * args : Any , ** kwargs : Any )

### RangeSensorCreateLidar
- [class] class RangeSensorCreateLidar ( * args : Any , ** kwargs : Any )

### RangeSensorCreatePrim
- [class] class RangeSensorCreatePrim ( * args : Any , ** kwargs : Any )

### RotatingLidarPhysX
- [class] class RotatingLidarPhysX(prim_path : str, name : str = 'rotating_lidar_physX', rotation_frequency : float | None = None, rotation_dt : float | None = None, position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, fov : Tuple [ float , float ] | None = None, resolution : Tuple [ float , float ] | None = None, valid_range : Tuple [ float , float ] | None = None)
- [method] add_azimuth_data_to_frame ( ) → None
- [method] add_depth_data_to_frame ( ) → None
- [method] add_intensity_data_to_frame ( ) → None
- [method] add_linear_depth_data_to_frame ( ) → None
- [method] add_point_cloud_data_to_frame ( ) → None
- [method] add_semantics_data_to_frame ( ) → None
- [method] add_zenith_data_to_frame ( ) → None
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] disable_semantics ( ) → None
- [method] disable_visualization ( ) → None
- [method] enable_semantics ( ) → None
- [method] enable_visualization(high_lod : bool = False, draw_points : bool = True, draw_lines : bool = True)
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_current_frame ( ) → dict
- [method] get_default_state ( ) → XFormPrimState
- [method] get_fov ( ) → Tuple [ float , float ]
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_num_cols ( ) → int
- [method] get_num_cols_in_last_step ( ) → int
- [method] get_num_rows ( ) → int
- [method] get_resolution ( ) → float
- [method] get_rotation_frequency ( ) → int
- [method] get_valid_range ( ) → Tuple [ float , float ]
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_paused ( ) → bool
- [method] is_semantics_enabled ( ) → bool
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] pause ( ) → None
- [method] post_reset ( ) → None
- [method] remove_azimuth_data_from_frame ( ) → None
- [method] remove_depth_data_from_frame ( ) → None
- [method] remove_intensity_data_from_frame ( ) → None
- [method] remove_linear_depth_data_from_frame ( ) → None
- [method] remove_point_cloud_data_from_frame ( ) → None
- [method] remove_semantics_data_from_frame ( ) → None
- [method] remove_zenith_data_from_frame ( ) → None
- [method] resume ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_fov ( value : Tuple [ float , float ] ) → None
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_resolution ( value : float ) → None
- [method] set_rotation_frequency ( value : int ) → None
- [method] set_valid_range(value : Tuple [ float , float ])
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

## isaacsim.sensors.rtx

### IsaacSensorCreateRtxIDS
- [class] class IsaacSensorCreateRtxIDS ( * args : Any , ** kwargs : Any )
- [attribute] _sensor_plugin_name
- [attribute] _sensor_type

### IsaacSensorCreateRtxLidar
- [class] class IsaacSensorCreateRtxLidar ( * args : Any , ** kwargs : Any )
- [attribute] _replicator_api
- [attribute] _schema
- [attribute] _sensor_plugin_name
- [attribute] _sensor_type
- [attribute] _supported_configs

### IsaacSensorCreateRtxRadar
- [class] class IsaacSensorCreateRtxRadar ( * args : Any , ** kwargs : Any )
- [attribute] _replicator_api
- [attribute] _schema
- [attribute] _sensor_plugin_name
- [attribute] _sensor_type

### LidarRtx
- [class] class LidarRtx(prim_path : str, name : str = 'lidar_rtx', position : ndarray | None = None, translation : ndarray | None = None, orientation : ndarray | None = None, config_file_name : str | None = None, ** kwargs)
- [method] add_azimuth_data_to_frame ( )
- [method] add_azimuth_range_to_frame ( )
- [method] add_elevation_data_to_frame ( )
- [method] add_horizontal_resolution_to_frame ( )
- [method] add_intensities_data_to_frame ( )
- [method] add_linear_depth_data_to_frame ( )
- [method] add_point_cloud_data_to_frame ( )
- [method] add_range_data_to_frame ( )
- [method] apply_visual_material(visual_material : VisualMaterial, weaker_than_descendants : bool = False)
- [method] attach_annotator(annotator_name : Literal [ 'IsaacComputeRTXLidarFlatScan' , 'IsaacExtractRTXSensorPointCloudNoAccumulator' , 'IsaacCreateRTXLidarScanBuffer' , 'StableIdMap' , 'GenericModelOutput' ], ** kwargs)
- [method] attach_writer ( writer_name : str , ** kwargs ) → None
- [method] static decode_stable_id_mapping ( stable_id_mapping_raw : bytes )
- [method] detach_all_annotators ( ) → None
- [method] detach_all_writers ( ) → None
- [method] detach_annotator ( annotator_name : str ) → None
- [method] detach_writer ( writer_name : str ) → None
- [method] disable_visualization ( )
- [method] enable_visualization ( )
- [method] get_annotators ( ) → dict
- [method] get_applied_visual_material ( ) → VisualMaterial
- [method] get_azimuth_range ( ) → Tuple [ float , float ]
- [method] get_current_frame ( ) → dict
- [method] get_default_state ( ) → XFormPrimState
- [method] get_depth_range ( ) → Tuple [ float , float ]
- [method] get_horizontal_fov ( ) → float
- [method] get_horizontal_resolution ( ) → float
- [method] get_local_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_local_scale ( ) → ndarray
- [method] get_num_cols ( ) → int
- [method] get_num_rows ( ) → int
- [method] static get_object_ids ( obj_ids : ndarray ) → List [ int ]
- [method] get_render_product_path ( ) → str
- [method] get_rotation_frequency ( ) → float
- [method] get_visibility ( ) → bool
- [method] get_world_pose ( ) → Tuple [ ndarray , ndarray ]
- [method] get_world_scale ( ) → ndarray
- [method] get_writers ( ) → dict
- [method] initialize ( physics_sim_view = None ) → None
- [method] is_paused ( ) → bool
- [method] is_valid ( ) → bool
- [method] is_visual_material_applied ( ) → bool
- [method] static make_add_remove_deprecated_attr ( deprecated_attr : str )
- [method] pause ( ) → None
- [method] post_reset ( ) → None
- [method] remove_azimuth_data_to_frame ( )
- [method] remove_azimuth_range_to_frame ( )
- [method] remove_elevation_data_to_frame ( )
- [method] remove_horizontal_resolution_to_frame ( )
- [method] remove_intensities_data_to_frame ( )
- [method] remove_linear_depth_data_to_frame ( )
- [method] remove_point_cloud_data_to_frame ( )
- [method] remove_range_data_to_frame ( )
- [method] resume ( ) → None
- [method] set_default_state(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_pose(translation : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [method] set_local_scale(scale : Sequence [ float ] | None)
- [method] set_visibility ( visible : bool ) → None
- [method] set_world_pose(position : Sequence [ float ] | None = None, orientation : Sequence [ float ] | None = None)
- [property] property name : str | None
- [property] property non_root_articulation_link : bool
- [property] property prim : pxr.Usd.Prim
- [property] property prim_path : str

## isaacsim.simulation_app

### AppFramework
- [class] class AppFramework ( name : str = 'kit' , argv = [] )
- [method] close ( )
- [method] update ( ) → None
- [property] property app : omni.kit.app.IApp
- [property] property framework : Any

### SimulationApp
- [class] class SimulationApp ( launch_config : dict = None , experience : str = '' )
- [method] close(wait_for_replicator = True, skip_cleanup = False)
- [method] is_exiting ( ) → bool
- [method] is_running ( ) → bool
- [method] reset_render_settings ( )
- [method] run_coroutine(coroutine : asyncio.Coroutine, run_until_complete : bool = True)
- [method] set_setting ( setting : str , value ) → None
- [method] update ( ) → None
- [property] property app : omni.kit.app.IApp
- [property] property context : omni.usd.UsdContext
- [attribute] DEFAULT_LAUNCHER_CONFIG = {'active_gpu': None, 'anti_aliasing': 3, 'create_new_stage': True, 'denoiser': True, 'disable_viewport_updates': False, 'display_options': 3094, 'enable_crashreporter': True, 'extra_args': [], 'fast_shutdown': True, 'headless': True, 'height': 720, 'hide_ui': None, 'limit_cpu_threads': 32, 'max_bounces': 4, 'max_gpu_count': None, 'max_specular_transmission_bounces': 6, 'max_volume_bounces': 4, 'multi_gpu': True, 'open_usd': None, 'physics_gpu': 0, 'profiler_backend': [], 'renderer': 'RaytracedLighting', 'samples_per_pixel_per_frame': 64, 'subdiv_refinement_level': 0, 'sync_loads': True, 'width': 1280, 'window_height': 900, 'window_width': 1440}

## isaacsim.storage.native.nucleus
- [function] build_server_list ( ) → List
- [function] check_server ( server : str , path : str , timeout : float = 10.0 ) → bool
- [function] async check_server_async(server : str, path : str, timeout : float = 10.0)
- [function] create_folder ( server : str , path : str ) → bool
- [function] delete_folder ( server : str , path : str ) → bool
- [function] async download_assets_async(src : str, dst : str, progress_callback, concurrency : int = 10, copy_behaviour : omni.client.CopyBehavior = omni.client.CopyBehavior.OVERWRITE, copy_after_delete : bool = True, timeout : float = 300.0)
- [function] find_nucleus_server ( suffix : str ) → Tuple [ bool , str ]
- [function] get_assets_root_path ( * , skip_check : bool = False ) → str
- [function] async get_assets_root_path_async ( * , skip_check : bool = False ) → str
- [function] get_assets_server ( ) → str | None
- [function] get_full_asset_path ( path : str ) → str | None
- [function] async get_full_asset_path_async ( path : str ) → str | None
- [function] get_isaac_asset_root_path ( ) → str | None
- [function] get_nvidia_asset_root_path ( ) → str | None
- [function] get_server_path ( suffix : str = '' ) → str | None
- [function] async get_server_path_async ( suffix : str = '' ) → str | None
- [function] get_url_root ( url : str ) → str
- [function] is_dir ( path : str ) → bool
- [function] async is_dir_async ( path : str ) → bool
- [function] is_file ( path : str ) → bool
- [function] async is_file_async ( path : str ) → bool
- [function] async list_folder ( path : str ) → Tuple [ List , List ]
- [function] async recursive_list_folder ( path : str ) → List
- [function] verify_asset_root_path(path : str)

### Version
- [class] class Version ( s )

## isaacsim.util.debug_draw._debug_draw
- [function] acquire_debug_draw_interface(plugin_name : str = None, library_path : str = None)
- [function] release_debug_draw_interface(arg0 : isaacsim.util.debug_draw._debug_draw.DebugDraw)

### DebugDraw
- [class] class DebugDraw
- [method] clear_lines(self : isaacsim.util.debug_draw._debug_draw.DebugDraw)
- [method] clear_points(self : isaacsim.util.debug_draw._debug_draw.DebugDraw)
- [method] draw_lines(self : isaacsim.util.debug_draw._debug_draw.DebugDraw, arg0 : List[carb::Float3], arg1 : List[carb::Float3], arg2 : List[carb::ColorRgba], arg3 : List [ float ])
- [method] draw_lines_spline ( self: isaacsim.util.debug_draw._debug_draw.DebugDraw, arg0: List[carb::Float3], arg1: carb::ColorRgba, arg2: float, arg3: bool ) → None
- [method] draw_points(self : isaacsim.util.debug_draw._debug_draw.DebugDraw, arg0 : List[carb::Float3], arg1 : List[carb::ColorRgba], arg2 : List [ float ])
- [method] get_num_lines(self : isaacsim.util.debug_draw._debug_draw.DebugDraw)
- [method] get_num_points(self : isaacsim.util.debug_draw._debug_draw.DebugDraw)

## lula
- [function] compute_ik_ccd(kinematics: lula::Kinematics, target_pose: lula::Pose3, target_frame: str, config: lula.CyclicCoordDescentIkConfig)
- [function] convert_composite_path_spec_to_c_space(composite_path_spec: lula.CompositePathSpec, kinematics: lula.Kinematics, control_frame: str, task_space_path_conversion_config: lula.TaskSpacePathConversionConfig = <lula.TaskSpacePathConversionConfig object at 0x7fd7436ed830>, ik_config: lula.CyclicCoordDescentIkConfig = <lula.CyclicCoordDescentIkConfig object at 0x7fd6a2e89530>)
- [function] convert_task_space_path_spec_to_c_space(task_space_path_spec: lula::TaskSpacePathSpec, kinematics: lula.Kinematics, control_frame: str, task_space_path_conversion_config: lula.TaskSpacePathConversionConfig = <lula.TaskSpacePathConversionConfig object at 0x7fd6a2d54870>, ik_config: lula.CyclicCoordDescentIkConfig = <lula.CyclicCoordDescentIkConfig object at 0x7fd8e8856db0>)
- [function] create_c_space_path_spec(initial_c_space_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [function] create_c_space_trajectory_generator ( * args , ** kwargs )
- [function] create_collision_sphere_generator(vertices : list [ numpy.ndarray [ numpy.float64 [ 3 , 1 ] ] ], triangles : list [ numpy.ndarray [ numpy.int32 [ 3 , 1 ] ] ])
- [function] create_composite_path_spec(initial_c_space_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [function] create_linear_c_space_path(c_space_path_spec : lula.CSpacePathSpec)
- [function] create_motion_planner ( * args , ** kwargs )
- [function] create_obstacle ( type : lula.Obstacle.Type ) → lula.Obstacle
- [function] create_rmpflow ( config : lula.RmpFlowConfig ) → lula.RmpFlow
- [function] create_rmpflow_config(rmpflow_config_file: str, robot_description: lula::RobotDescription, end_effector_frame: str, world_view: lula::WorldView)
- [function] create_rmpflow_config_from_memory(rmpflow_config: str, robot_description: lula::RobotDescription, end_effector_frame: str, world_view: lula::WorldView)
- [function] create_task_space_path_spec(initial_pose : lula.Pose3)
- [function] create_world ( ) → lula.World
- [function] export_c_space_path_spec_to_memory(c_space_path_spec : lula.CSpacePathSpec)
- [function] export_composite_path_spec_to_memory(composite_path_spec : lula.CompositePathSpec)
- [function] export_task_space_path_spec_to_memory(task_space_path_spec: lula::TaskSpacePathSpec)
- [function] load_c_space_path_spec_from_file(c_space_path_spec_file : str)
- [function] load_c_space_path_spec_from_memory(c_space_path_spec_yaml : str)
- [function] load_composite_path_spec_from_file(composite_path_spec_file : str)
- [function] load_composite_path_spec_from_memory(composite_path_spec_yaml : str)
- [function] load_robot(robot_description_file : str, robot_urdf : str)
- [function] load_robot_from_memory(robot_description : str, robot_urdf : str)
- [function] load_task_space_path_spec_from_file(task_space_path_spec_file : str)
- [function] load_task_space_path_spec_from_memory(task_space_path_spec_yaml : str)
- [function] set_log_level ( level: lula.LogLevel = <LogLevel.ERROR: 1> ) → None

### CSpacePath
- [class] class CSpacePath
- [class] class Domain
- [method] span ( self : lula.CSpacePath.Domain ) → float
- [method] domain ( self : lula.CSpacePath ) → lula.CSpacePath.Domain
- [method] eval(self : lula.CSpacePath, s : float)
- [method] max_position(self : lula.CSpacePath)
- [method] min_position(self : lula.CSpacePath)
- [method] num_c_space_coords ( self : lula.CSpacePath ) → int
- [method] path_length ( self : lula.CSpacePath ) → float
- [property] property lower
- [property] property upper

### CSpacePathSpec
- [class] class CSpacePathSpec
- [method] add_c_space_waypoint(self : lula.CSpacePathSpec, waypoint : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] num_c_space_coords ( self : lula.CSpacePathSpec ) → int

### CSpaceTrajectoryGenerator
- [class] class CSpaceTrajectoryGenerator
- [class] class InterpolationMode
- [class] class SolverParamValue
- [method] generate_time_stamped_trajectory ( self: lula.CSpaceTrajectoryGenerator, waypoints: list[numpy.ndarray[numpy.float64[m, 1]]], times: list[float], interpolation_mode: lula.CSpaceTrajectoryGenerator.InterpolationMode = <InterpolationMode.CUBIC_SPLINE: 1> ) → lula.Trajectory
- [method] generate_trajectory(self : lula.CSpaceTrajectoryGenerator, waypoints : list [ numpy.ndarray [ numpy.float64 [ m , 1 ] ] ])
- [method] num_c_space_coords(self : lula.CSpaceTrajectoryGenerator)
- [method] set_acceleration_limits(self : lula.CSpaceTrajectoryGenerator, max_acceleration : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] set_jerk_limits(self : lula.CSpaceTrajectoryGenerator, max_jerk : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] set_position_limits(self : lula.CSpaceTrajectoryGenerator, min_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], max_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] set_solver_param(self : lula.CSpaceTrajectoryGenerator, param_name : str, value : lula.CSpaceTrajectoryGenerator.SolverParamValue)
- [method] set_velocity_limits(self : lula.CSpaceTrajectoryGenerator, max_velocity : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [property] property name
- [property] property value
- [attribute] CUBIC_SPLINE = <InterpolationMode.CUBIC_SPLINE: 1>
- [attribute] LINEAR = <InterpolationMode.LINEAR: 0>

### CollisionSphereGenerator
- [class] class CollisionSphereGenerator
- [class] class ParamValue
- [class] class Sphere
- [method] generate_spheres(self : lula.CollisionSphereGenerator, num_spheres : int, radius_offset : float)
- [method] get_sampled_spheres(self : lula.CollisionSphereGenerator)
- [method] num_triangles(self : lula.CollisionSphereGenerator)
- [method] set_param(self : lula.CollisionSphereGenerator, param_name : str, value : lula.CollisionSphereGenerator.ParamValue)
- [property] property center
- [property] property radius

### CompositePathSpec
- [class] class CompositePathSpec
- [class] class PathSpecType
- [class] class TransitionMode
- [method] add_c_space_path_spec(self : lula.CompositePathSpec, path_spec : lula.CSpacePathSpec, transition_mode : lula.CompositePathSpec.TransitionMode)
- [method] add_task_space_path_spec(self: lula.CompositePathSpec, path_spec: lula::TaskSpacePathSpec, transition_mode: lula.CompositePathSpec.TransitionMode)
- [method] c_space_path_spec(self : lula.CompositePathSpec, path_spec_index : int)
- [method] num_c_space_coords(self : lula.CompositePathSpec)
- [method] num_path_specs ( self : lula.CompositePathSpec ) → int
- [method] path_spec_type(self : lula.CompositePathSpec, path_spec_index : int)
- [method] task_space_path_spec(self : lula.CompositePathSpec, path_spec_index : int)
- [property] property name
- [property] property value
- [property] property name
- [property] property value
- [attribute] CSPACE = <PathSpecType.CSPACE: 1>
- [attribute] TASK_SPACE = <PathSpecType.TASK_SPACE: 0>
- [attribute] FREE = <TransitionMode.FREE: 1>
- [attribute] LINEAR_TASK_SPACE = <TransitionMode.LINEAR_TASK_SPACE: 2>
- [attribute] SKIP = <TransitionMode.SKIP: 0>

### CyclicCoordDescentIkConfig
- [class] class CyclicCoordDescentIkConfig
- [class] class CSpaceLimitBiasing
- [property] property name
- [property] property value
- [property] property bfgs_cspace_limit_biasing
- [property] property bfgs_cspace_limit_biasing_weight
- [property] property bfgs_cspace_limit_penalty_region
- [property] property bfgs_gradient_norm_termination
- [property] property bfgs_gradient_norm_termination_coarse_scale_factor
- [property] property bfgs_max_iterations
- [property] property bfgs_orientation_weight
- [property] property bfgs_position_weight
- [property] property ccd_bracket_search_num_uniform_samples
- [property] property ccd_descent_termination_delta
- [property] property ccd_max_iterations
- [property] property ccd_orientation_weight
- [property] property ccd_position_weight
- [property] property cspace_seeds
- [property] property irwin_hall_sampling_order
- [property] property max_num_descents
- [property] property orientation_tolerance
- [property] property position_tolerance
- [property] property sampling_seed
- [attribute] AUTO = <CSpaceLimitBiasing.AUTO: 0>
- [attribute] DISABLE = <CSpaceLimitBiasing.DISABLE: 2>
- [attribute] ENABLE = <CSpaceLimitBiasing.ENABLE: 1>

### CyclicCoordDescentIkResults
- [class] class CyclicCoordDescentIkResults
- [property] property cspace_position
- [property] property num_descents
- [property] property position_error
- [property] property success
- [property] property x_axis_orientation_error
- [property] property y_axis_orientation_error
- [property] property z_axis_orientation_error

### Kinematics
- [class] class Kinematics
- [class] class Limits
- [method] base_frame_name ( self : lula.Kinematics ) → str
- [method] c_space_coord_acceleration_limit(self : lula.Kinematics, coord_index : int)
- [method] c_space_coord_jerk_limit(self : lula.Kinematics, coord_index : int)
- [method] c_space_coord_limits(self : lula.Kinematics, coord_index : int)
- [method] c_space_coord_name(self : lula.Kinematics, coord_index : int)
- [method] c_space_coord_velocity_limit(self : lula.Kinematics, coord_index : int)
- [method] frame_names ( self : lula.Kinematics ) → list [ str ]
- [method] has_c_space_acceleration_limit(self : lula.Kinematics, coord_index : int)
- [method] has_c_space_jerk_limit(self : lula.Kinematics, coord_index : int)
- [method] jacobian(self : lula.Kinematics, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], frame : str)
- [method] num_c_space_coords ( self : lula.Kinematics ) → int
- [method] orientation ( * args , ** kwargs )
- [method] orientation_jacobian(self : lula.Kinematics, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], frame : str)
- [method] pose ( * args , ** kwargs )
- [method] position ( * args , ** kwargs )
- [method] position_jacobian(self : lula.Kinematics, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], frame : str)
- [method] within_cspace_limits(self : lula.Kinematics, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], log_warnings : bool)
- [property] property lower
- [property] property upper

### LinearCSpacePath
- [class] class LinearCSpacePath
- [method] domain(self : lula.LinearCSpacePath)
- [method] eval(self : lula.LinearCSpacePath, s : float)
- [method] max_position(self : lula.LinearCSpacePath)
- [method] min_position(self : lula.LinearCSpacePath)
- [method] num_c_space_coords(self : lula.LinearCSpacePath)
- [method] path_length ( self : lula.LinearCSpacePath ) → float
- [method] waypoints(self : lula.LinearCSpacePath)

### LogLevel
- [class] class LogLevel
- [data] ERROR
- [data] FATAL
- [data] INFO
- [data] VERBOSE
- [data] WARNING

### MotionPlanner
- [class] class MotionPlanner
- [class] class Limit
- [class] class ParamValue
- [class] class Results
- [method] plan_to_cspace_target(self : lula.MotionPlanner, q_initial : numpy.ndarray [ numpy.float64 [ m , 1 ] ], q_target : numpy.ndarray [ numpy.float64 [ m , 1 ] ], generate_interpolated_path : bool = False)
- [method] plan_to_pose_target ( self: lula.MotionPlanner, q_initial: numpy.ndarray[numpy.float64[m, 1]], pose_target: lula::Pose3, generate_interpolated_path: bool = False ) → lula::MotionPlanner::Results
- [method] plan_to_task_space_target(self : lula.MotionPlanner, q_initial : numpy.ndarray [ numpy.float64 [ m , 1 ] ], x_target : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], generate_interpolated_path : bool = False)
- [method] plan_to_translation_target(self : lula.MotionPlanner, q_initial : numpy.ndarray [ numpy.float64 [ m , 1 ] ], translation_target : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], generate_interpolated_path : bool = False)
- [method] set_param ( * args , ** kwargs )
- [method] set_parame(self : lula.MotionPlanner, param_name : str, value : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ])
- [method] update_world_view ( self : lula.MotionPlanner ) → None
- [property] property lower
- [property] property upper
- [property] property interpolated_path
- [property] property path
- [property] property path_found

### Obstacle
- [class] class Obstacle
- [class] class Attribute
- [class] class AttributeValue
- [class] class Type
- [method] set_attribute(self: lula.Obstacle, attribute: lula::Obstacle::Attribute, value: lula::Obstacle::AttributeValue)
- [method] type ( self : lula.Obstacle ) → lula::Obstacle::Type
- [property] property name
- [property] property value
- [property] property name
- [property] property value
- [attribute] HEIGHT = <Attribute.HEIGHT: 0>
- [attribute] RADIUS = <Attribute.RADIUS: 1>
- [attribute] SIDE_LENGTHS = <Attribute.SIDE_LENGTHS: 2>
- [attribute] CUBE = <Type.CUBE: 0>
- [attribute] CYLINDER = <Type.CYLINDER: 1>
- [attribute] SPHERE = <Type.SPHERE: 2>

### Pose3
- [class] class Pose3
- [method] static from_rotation ( rotation: lula::Rotation3 ) → lula.Pose3
- [method] static from_translation(translation : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ])
- [method] static identity ( ) → lula.Pose3
- [method] inverse ( self : lula.Pose3 ) → lula.Pose3
- [method] matrix ( self : lula.Pose3 ) → numpy.ndarray [ numpy.float64 [ 4 , 4 ] ]
- [property] property rotation
- [property] property translation

### RmpFlow
- [class] class RmpFlow
- [method] clear_end_effector_orientation_attractor(self : lula.RmpFlow)
- [method] clear_end_effector_position_attractor(self : lula.RmpFlow)
- [method] collision_sphere_positions(self : lula.RmpFlow, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] collision_sphere_radii ( self : lula.RmpFlow ) → list [ float ]
- [method] distance_to_obstacle ( self: lula.RmpFlow, obstacle: lula::World::ObstacleHandle, collision_sphere_index: int, cspace_position: numpy.ndarray[numpy.float64[m, 1]] ) → float
- [method] eval_accel(self : lula.RmpFlow, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], cspace_velocity : numpy.ndarray [ numpy.float64 [ m , 1 ] ], cspace_accel : numpy.ndarray [ numpy.float64 [ m , 1 ] , flags.writeable ])
- [method] eval_force_and_metric(self : lula.RmpFlow, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ], cspace_velocity : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] in_collision_with_obstacle(self : lula.RmpFlow, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] num_collision_spheres ( self : lula.RmpFlow ) → int
- [method] set_cspace_attractor(self : lula.RmpFlow, cspace_position : numpy.ndarray [ numpy.float64 [ m , 1 ] ])
- [method] set_end_effector_orientation_attractor(self: lula.RmpFlow, orientation: lula::Rotation3)
- [method] set_end_effector_position_attractor(self : lula.RmpFlow, position : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ])
- [method] update_world_view ( self : lula.RmpFlow ) → None

### RmpFlowConfig
- [class] class RmpFlowConfig
- [method] get_all_params(self : lula.RmpFlowConfig, names : list [ str ], values : list [ float ])
- [method] get_param(self : lula.RmpFlowConfig, param_name : str)
- [method] set_all_params(self : lula.RmpFlowConfig, names : list [ str ], values : list [ float ])
- [method] set_param(self : lula.RmpFlowConfig, param_name : str, value : float)
- [method] set_world_view(self: lula.RmpFlowConfig, world_view: lula::WorldView)

### RobotDescription
- [class] class RobotDescription
- [method] c_space_coord_name(self : lula.RobotDescription, coord_index : int)
- [method] default_c_space_configuration(self : lula.RobotDescription)
- [method] kinematics(self : lula.RobotDescription)
- [method] num_c_space_coords(self : lula.RobotDescription)

### Rotation3
- [class] class Rotation3
- [method] static distance(rotation0 : lula.Rotation3, rotation1 : lula.Rotation3)
- [method] static from_scaled_axis(scaled_axis : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ])
- [method] static identity ( ) → lula.Rotation3
- [method] inverse ( self : lula.Rotation3 ) → lula.Rotation3
- [method] matrix(self : lula.Rotation3)
- [method] scaled_axis(self : lula.Rotation3)
- [method] static slerp(rotation0 : lula.Rotation3, rotation1 : lula.Rotation3, t : float)
- [method] w ( self : lula.Rotation3 ) → float
- [method] x ( self : lula.Rotation3 ) → float
- [method] y ( self : lula.Rotation3 ) → float
- [method] z ( self : lula.Rotation3 ) → float

### TaskSpacePath
- [class] class TaskSpacePath
- [class] class Domain
- [method] span ( self : lula.TaskSpacePath.Domain ) → float
- [method] accumulated_rotation ( self : lula.TaskSpacePath ) → float
- [method] domain(self : lula.TaskSpacePath)
- [method] eval ( self : lula.TaskSpacePath , s : float ) → lula.Pose3
- [method] max_position(self : lula.TaskSpacePath)
- [method] min_position(self : lula.TaskSpacePath)
- [method] path_length ( self : lula.TaskSpacePath ) → float
- [property] property lower
- [property] property upper

### TaskSpacePathConversionConfig
- [class] class TaskSpacePathConversionConfig
- [property] property alpha
- [property] property initial_s_step_size
- [property] property initial_s_step_size_delta
- [property] property max_iterations
- [property] property max_position_deviation
- [property] property min_position_deviation
- [property] property min_s_step_size
- [property] property min_s_step_size_delta

### TaskSpacePathSpec
- [class] class TaskSpacePathSpec
- [method] add_linear_path(self : lula.TaskSpacePathSpec, target_pose : lula.Pose3, blend_radius : float = 0.0)
- [method] add_rotation(self : lula.TaskSpacePathSpec, target_rotation : lula.Rotation3)
- [method] add_tangent_arc(self : lula.TaskSpacePathSpec, target_position : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], constant_orientation : bool = True)
- [method] add_tangent_arc_with_orientation_target(self : lula.TaskSpacePathSpec, target_pose : lula.Pose3)
- [method] add_three_point_arc(self : lula.TaskSpacePathSpec, target_position : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], intermediate_position : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], constant_orientation : bool = True)
- [method] add_three_point_arc_with_orientation_target(self : lula.TaskSpacePathSpec, target_pose : lula.Pose3, intermediate_position : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ])
- [method] add_translation(self : lula.TaskSpacePathSpec, target_position : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], blend_radius : float = 0.0)
- [method] generate_path(self : lula.TaskSpacePathSpec)

### Trajectory
- [class] class Trajectory
- [class] class Domain
- [method] span ( self : lula.Trajectory.Domain ) → float
- [method] domain ( self : lula.Trajectory ) → lula.Trajectory.Domain
- [method] eval(self : lula.Trajectory, time : float, derivative_order : int = 0)
- [method] eval_all(self : lula.Trajectory, arg0 : float)
- [method] max_acceleration_magnitude(self : lula.Trajectory)
- [method] max_jerk_magnitude(self : lula.Trajectory)
- [method] max_position(self : lula.Trajectory)
- [method] max_velocity_magnitude(self : lula.Trajectory)
- [method] min_position(self : lula.Trajectory)
- [method] num_c_space_coords ( self : lula.Trajectory ) → int
- [property] property lower
- [property] property upper

### World
- [class] class World
- [class] class ObstacleHandle
- [method] add_obstacle(self : lula.World, obstacle : lula.Obstacle, pose : lula.Pose3 | None = None)
- [method] add_world_view ( self : lula.World ) → lula::WorldView
- [method] disable_obstacle(self: lula.World, obstacle: lula::World::ObstacleHandle)
- [method] enable_obstacle(self: lula.World, obstacle: lula::World::ObstacleHandle)
- [method] remove_obstacle(self: lula.World, obstacle: lula::World::ObstacleHandle)
- [method] set_pose(self: lula.World, obstacle: lula::World::ObstacleHandle, pose: lula.Pose3)

### WorldView
- [class] class WorldView
- [method] distance_to(self : lula.WorldView, obstacle : lula.World.ObstacleHandle, point : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], gradient : numpy.ndarray [ numpy.float64 [ 3 , 1 ] , flags.writeable ] | None = None)
- [method] distances_to(self : lula.WorldView, point : numpy.ndarray [ numpy.float64 [ 3 , 1 ] ], compute_distance_gradients : bool = True)
- [method] in_collision ( * args , ** kwargs )
- [method] num_enabled_obstacles ( self : lula.WorldView ) → int
- [method] update ( self : lula.WorldView ) → None

## omni.kit.loop._loop
- [function] acquire_loop_interface(plugin_name : str = None, library_path : str = None)
- [function] release_loop_interface(arg0 : omni.kit.loop._loop.RunLoopRunner)

### RunLoopRunner
- [class] class RunLoopRunner
- [method] get_manual_mode(self : omni.kit.loop._loop.RunLoopRunner, name : str = '')
- [method] get_manual_step_size(self : omni.kit.loop._loop.RunLoopRunner, name : str = '')
- [method] set_manual_mode(self : omni.kit.loop._loop.RunLoopRunner, enabled : bool = 'True', name : str = '')
- [method] set_manual_step_size(self : omni.kit.loop._loop.RunLoopRunner, dt : float = '0.01667', name : str = '')
