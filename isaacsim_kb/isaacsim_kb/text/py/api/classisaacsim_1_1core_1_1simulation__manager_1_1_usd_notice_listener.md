<!-- source: py/api/classisaacsim_1_1core_1_1simulation__manager_1_1_usd_notice_listener.html | title: UsdNoticeListener — Isaac Sim -->

# UsdNoticeListener
Fully qualified name: `isaacsim::core::simulation_manager::UsdNoticeListener`
classUsdNoticeListener:publicpxr ::TfWeakBase

Listener class for USD object change notifications.
This class listens for changes to USD objects and manages callbacks for deletion and physics scene addition events. It inherits from pxr::TfWeakBase to support the USD notification system.
Public Functions
UsdNoticeListener()

voidhandle(constpxr ::UsdNotice::ObjectsChanged&objectsChanged)

Handles USD object change notifications.
Parameters:
objectsChanged – [in] The notification containing information about changed objects.

voidenable(constbool&flag)

Enables or disables the listener.
Parameters:
flag – [in] True to enable the listener, false to disable.

boolisEnabled()

Checks if the listener is enabled.
Returns:
True if the listener is enabled, false otherwise.

std ::map<int,std ::function<void(conststd ::string&)>>&getDeletionCallbacks(
)
Gets the map of deletion callbacks.
Returns:
Reference to the map of deletion callbacks, keyed by callback ID.

std ::map<int,std ::function<void(conststd ::string&)>>&getPhysicsSceneAdditionCallbacks(
)
Gets the map of physics scene addition callbacks.
Returns:
Reference to the map of physics scene addition callbacks, keyed by callback ID.

std ::map<pxr ::SdfPath,pxr ::PhysxSchemaPhysxSceneAPI>&getPhysicsScenes(
)
Gets the map of physics scenes.
Returns:
Reference to the map of physics scenes, keyed by their USD paths.

int&getCallbackIter()

Gets the callback iteration counter.
Returns:
Reference to the current callback iteration counter.
