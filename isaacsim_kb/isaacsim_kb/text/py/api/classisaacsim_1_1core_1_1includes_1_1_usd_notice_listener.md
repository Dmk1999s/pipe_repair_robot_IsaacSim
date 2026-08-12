<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_usd_notice_listener.html | title: UsdNoticeListener — Isaac Sim -->

# UsdNoticeListener
Fully qualified name: `isaacsim::core::includes::UsdNoticeListener`
template<typenameT>
classUsdNoticeListener:publicpxr ::TfWeakBase

Helper base class to subscribe to pxr::TfNotice.
Provides a convenient base class for listening to USD notices with automatic cleanup and weak pointer management. Template parameter T specifies the notice type to listen for.
Note
Inherits from pxr::TfWeakBase to enable weak pointer management
Warning
Always call revokeListener() before destruction to avoid memory leaks
Template Parameters:
T – The type of USD notice to listen for (e.g., pxr::UsdNotice::ObjectsChanged)

Public Functions
inlinevirtual~UsdNoticeListener()

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

virtualvoidhandleNotice(constT &objectsChanged)=0

Pure virtual function to handle received notices.
Derived classes must implement this function to process the received USD notices. Called automatically when a notice of type T is received.
Note
This function is called from the USD notice system thread
Parameters:
objectsChanged – [in] The notice object containing change information
