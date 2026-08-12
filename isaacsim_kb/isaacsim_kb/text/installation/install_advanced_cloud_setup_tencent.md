<!-- source: installation/install_advanced_cloud_setup_tencent.html | title: Tencent Cloud Deployment — Isaac Sim Documentation -->

# Tencent Cloud Deployment

## Requirements
Here are the requirements for running NVIDIA Isaac Sim on Tencent Cloud:

- A Tencent Cloud account with Computing Instance access that is able to create a Virtual Machine with GPU support.

- An Cloud Virtual Machine with the following recommended specifications:

- GPU: NVIDIA Tesla T4

- Machine type: GN7

- Image: Ubuntu Server 18.04.1 LTS

## Setup
To log in to Tencent Cloud, use the following steps:

- Go to the Tencent Cloud homepage .
[image: Tencent Cloud homepage]

- Click Log in.
[image: Tencent Cloud log in]

- Select enterprise user login, click CAM user sign in.
[image: CAM user sign in]

- Enter Root account ID, Sub-user name, and Password. Then click Sign in.
[image: Enterprise sign in]

- Enter the following page:
[image: Log in interface]

To launch the Tencent Cloud Virtual Machine, use the following steps:

- In the Products drop-down tab, click 04 Cloud Virtual Machine.
[image: Select Cloud Virtual Machine]

- Click Get Started.
[image: Cloud Virtual Machine]

- Enter the Cloud Virtual Machine page, select Instances in the leftmost column, you can create a new instance through the Create button, or start an existing instance by using the Start Up button. Here, use the Create button to create a new instance.
[image: Create instance]

- Enter the Cloud Virtual Machine (CVM) interface as follows, and create a cloud service instance.
[image: CVM]

- For Basic configurations, choose Spot instances for T4 graphics card. China, Guangzhou are selected for the region, Random is selected for the Availability Zone. You can also choose according to your needs.
[image: Basic configuration]
- For Instance configurations, choose GPU-based, GPU Compute GN7 (that is, T4 graphics card). For the operating system of the instance, select Ubuntu, 18.04 version. Do not check Install GPU driver automatically. Select 500GB or larger capacity for Storage.
[image: Instance configuration]

- After Select basic configurations is completed, click Next: Configure network and host, and click Confirm.

- To create a network, click create a VPC and a subnet respectively to create a private network and a subnet. Then follow the prompts. For network Bandwidth, select 20Mbps.
Note

- When creating a subnet, the region selection of Availability zone must be the same as Availability zone of Instance configurations in Select basic configurations section.

[image: CVM network][image: CVM VPC]

- Mandatory. Select Security Group to ensure that all the ports required for Isaac Sim remote connection are open. For simplicity, you can choose Open all ports. During actual operation, to ensure security, you must select a port that is open to the outside world.
Note

- Pay special attention here, you must ensure that all the ports required by Isaac Sim are opened and secure.

- For details, see Isaac Sim WebRTC Streaming Client .

[image: CVM network security][image: CVM create security group][image: CVM configure security group][image: CVM select security group]

- For Other Settings, create a key for ssh connections. You can select an existing secret key or create a new secret key. The secret key is a file in *.pem format.
[image: CVM create key]

- After Config network and host is complete, click Next: Confirm configuration.
[image: CVM confirm configuration]

- After the instance has been created successfully, you can start the instance, and access the instance through the public network IP.

- See Container Installation to install NVIDIA Drivers and other dependencies on the VM.

- Proceed to Container Deployment .
