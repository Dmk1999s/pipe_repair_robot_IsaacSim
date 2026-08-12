<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_prim_manager_usd_notice_listener.html | title: PrimManagerUsdNoticeListener — Isaac Sim -->

# PrimManagerUsdNoticeListener
Fully qualified name: `isaacsim::core::includes::PrimManagerUsdNoticeListener`
classPrimManagerUsdNoticeListener:publicisaacsim ::core ::includes ::UsdNoticeListener <pxr ::UsdNotice::ObjectsChanged>

Custom USD notice listener for handling object changes in the stage.
Implements a specialized listener for USD object change notifications, specifically handling prim additions, removals, and modifications. This listener is essential for maintaining synchronization between the USD stage and component management system.
Public Functions
inlinePrimManagerUsdNoticeListener(ComponentManager *manager)

Constructs a new USD notice listener.
Parameters:
manager – [in] Pointer to the component manager that will handle notifications

inlinevirtualvoidhandleNotice(
constpxr ::UsdNotice::ObjectsChanged&objectsChanged,
)override
Handles USD object change notifications.
Processes notifications about changes to USD objects, including prim additions, removals, and modifications. Triggers appropriate component manager callbacks.
Parameters:
objectsChanged – [in] The notification containing information about changed objects

inlinevoidregisterListener()

Registers this listener to receive USD notices of type T.
Sets up the notice listener using weak pointers to avoid circular references. Automatically revokes any existing listener registration to prevent leaks.
Note
Safe to call multiple times - will revoke previous registration first

inlinevoidrevokeListener()

Revokes the notice listener registration.
Safely unregisters the notice listener if it was previously registered. Safe to call multiple times or when no listener is registered.
Note
Automatically called in destructor
