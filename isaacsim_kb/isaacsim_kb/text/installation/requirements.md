<!-- source: installation/requirements.html | title: Isaac Sim Requirements — Isaac Sim Documentation -->

# Isaac Sim Requirements
Hint
By installing Isaac Sim, you can run the Isaac Sim Compatibility Checker lightweight app to check if your machine meets the system requirements and compatibility.

## System Requirements
Requirements for x86_64
[TABLE]
Element | Minimum Spec | Good | Ideal
OS | Ubuntu 22.04/24.04 Windows 10/11 | Ubuntu 22.04/24.04 Windows 10/11 | Ubuntu 22.04/24.04 Windows 10/11
CPU | Intel Core i7 (7th Generation) AMD Ryzen 5 | Intel Core i7 (9th Generation) AMD Ryzen 7 | Intel Core i9, X-series or higher AMD Ryzen 9, Threadripper or higher
Cores | 4 | 8 | 16
RAM [ 1 ] | 32GB | 64GB | 64GB
Storage | 50GB SSD | 500GB SSD | 1TB NVMe SSD
GPU | GeForce RTX 4080 | GeForce RTX 5080 | RTX PRO 6000 Blackwell
VRAM [ 1 ] | 16GB [ 2 ] | 16GB | 48GB
Driver [ 3 ] | Linux: 580.65.06 Windows: 580.88 | Linux: 580.65.06 Windows: 580.88 | Linux: 580.65.06 Windows: 580.88
[/TABLE]
[1](1 ,2 )More RAM and VRAM is recommended for advanced usage of Isaac Sim. Isaac Lab usage will require additional RAM and VRAM for training.
[2 ]GPUs with less than 16GB VRAM may be insufficient to run a complex scene rendering more than 16MP per frame. Consider upgrading to a higher spec if that is your use case.
[3 ]Isaac Sim was tested on these driver versions. See Technical Requirements for recommended driver versions.
Note

- The Isaac Sim container is only supported on Linux.

- An Internet connection is required to access the Isaac Sim assets online and to run some extensions.

- GPUs without RT Cores (A100, H100) are not supported.

- Due to VRAM constraints, some tutorials and benchmarks may not run on GPU below the minimum specifications. Workflows leveraging a large number of sensors are particularly affected.

- See Linux Troubleshooting to resolve driver installation issues on Linux.

- We recommend installing the Latest Production Branch Version drivers from the Unix Driver Archive using the `.run` installer on Linux if you are on a new GPU or experiencing issues with the current drivers.

- Windows 10 support ends on October 14, 2025. After this date, Microsoft will no longer provide free security, feature, or technical updates for Windows 10. As a result, we will be dropping support for Windows 10 in future releases of Isaac Sim to ensure the security and functionality of our software.

Requirements for aarch64
[TABLE]
Element | Specifications
Device | NVIDIA DGX™ Spark
OS | NVIDIA DGX OS 7.2.3
Driver [ 4 ] | 580.95.05
[/TABLE]
[4 ]Isaac Sim was tested on these driver versions. See Technical Requirements for recommended driver versions.
Note

- Isaac Sim aarch64 builds are currently only supported on DGX Spark system.

- The Isaac Sim container is only supported on Linux.

- An Internet connection is required to access the Isaac Sim assets online and to run some extensions.

Limitations
Warning
Here are the limitations of running Isaac Sim 5.1 on DGX Spark:

- Hub Workstation Cache is not supported.

- Livestreaming is not supported.

- Importing OBJ files is not supported. This impacts the ability to use the urdf importer for assets that contain OBJ meshes.

- Application Template is not supported.

- cuRobo and cuMotion is not supported.

- Isaac Sim App Selector is not supported.
