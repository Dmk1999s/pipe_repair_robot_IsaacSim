<!-- source: installation/install_advanced_cloud_setup_volcano.html | title: Volcano Engine Deployment — Isaac Sim Documentation -->

# Volcano Engine Deployment

## Requirements
Volcano Engine provides veOmniverse services which are fully equipped with Isaac Sim, Isaac Lab, and Isaac Sim assets, all integrated with Nucleus. Additionally, Volcano Engine offers a wealth of ready-to-use USD assets, enabling to leverage high-quality resources for realistic simulations. The requirements for running Omniverse Isaac Sim on Volcano Engine simply are :

- A Volcano Engine account with access to the veOmniverse, which can create a launcher service with GPU support.

- A GPU-accelerated compute-optimized instance with the following recommended specifications:

- GPU: NVIDIA L40

- Service specification: 仿真计算ls1n2.1x

- Image: Ubuntu Server 22.04 LTS

## Setup
To launch veOmniverse Server, use the following steps:

- Go to the Volcano Engine homepage. Follow the path in the image to select the veOmniverse product.
[image: Volcano Engine homepage]

- Click the login （登陆）button in the top right corner to log in to Volcano Engine.

- If you haven’t applied for veOmniverse access yet, you will see the interface below. Click the “Apply for Experience”（申请体验）button as shown in the image to request service access from the Volcano team.
[image: Apply for access]

- Once you have applied for the access and received approval, you can directly log in to the veOmniverse console and be directed to the launcher page.

- On the launcher page, as shown in the image below, you can create and manage launcher services that can run NVIDIA Isaac Sim and Omniverse Nucleus.
[image: Launcher page]

- Creating a launcher is a simple process. Click the “Create” button in the top left corner to enter the creation page. Fill in the basic information, select the simulation computing service “仿真计算Is1n2.1x” and proceed to create it with payment.
[image: Creating a launcher]

- Once the creation is completed, you can manage the launcher services on the list page. Simply copy the IP address and login credentials to access remotely via VDI.
[image: Launcher services]

- After logging into the launcher, the system comes pre-installed with commonly used tools such as Isaac Sim and Isaac Lab. These tools are continuously updated and ready for direct use.
