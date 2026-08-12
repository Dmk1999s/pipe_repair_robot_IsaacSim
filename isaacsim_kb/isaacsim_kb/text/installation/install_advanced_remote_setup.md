<!-- source: installation/install_advanced_remote_setup.html | title: Remote Workstation Deployment — Isaac Sim Documentation -->

# Remote Workstation Deployment

## Requirements
The requirements for running NVIDIA Isaac Sim on a headless remote workstation are:

- See System Requirements .

- See Container Installation .

## Setup
Follow these steps to access a remote Ubuntu workstation:

- If you have access to the remote workstation physically, install an SSH server to allow remote access:

```
$ sudo apt update
$ sudo apt install openssh-server
```

- Run the following command to get the remote workstation IP address:

```
$ ifconfig
```

- Run the following command to access the remote workstation:

```
$ ssh <remote_workstation_username>@<remote_workstation_ip_address>
<remote_workstation_username>@<remote_workstation_ip_address>'s password:
```

- Proceed to Container Deployment .
