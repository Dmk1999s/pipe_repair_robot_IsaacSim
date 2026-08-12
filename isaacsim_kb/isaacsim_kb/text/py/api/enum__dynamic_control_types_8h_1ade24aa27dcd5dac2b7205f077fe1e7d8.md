<!-- source: py/api/enum__dynamic_control_types_8h_1ade24aa27dcd5dac2b7205f077fe1e7d8.html | title: DcDriveMode — Isaac Sim -->

# DcDriveMode
Fully qualified name: `omni::isaac::dynamic_control::DcDriveMode`
enumclassomni ::isaac ::dynamic_control ::DcDriveMode:int32_t

Drive modes for degrees-of-freedom.
Drive modes for degrees-of-freedom
A DoF that is set on a specific drive mode will ignore drive target commands sent for a different mode. Joint limits, if they exist, will still be enforced.
Values:
enumeratoreForce

The output of the implicit spring drive controller is a force/torque.

enumeratoreAcceleration

The output of the implicit spring drive controller is a joint acceleration (use this to get (spatial)-inertia-invariant behavior of the drive).
