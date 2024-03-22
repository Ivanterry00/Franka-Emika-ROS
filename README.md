# Franka-Emika-ROS

This repository provides resources and tools for controlling Franka Emika robots using the Robot Operating System (ROS). 

## Getting Started
### Prerequisites

Before getting started with controlling Franka Emika robots using ROS, ensure that you have the following prerequisites installed, from the following sources:

- [Ubuntu 20.04.6 LTS (Focal Fossa)](https://releases.ubuntu.com/focal/)  
- [ROS Noetic](https://wiki.ros.org/noetic/Installation/Ubuntu)

and follow the instructions provided in the links to install them.

You also will need to install the following packages:

- [libfranka](https://github.com/frankaemika/libfranka) (recommended version 0.13.3)
- [franka_ros](https://github.com/frankaemika/franka_ros) (recommended version 0.10.1)

following the instructions provided in this [Franka Control Interface (FCI)](https://frankaemika.github.io/docs/installation_linux.html).

Moreover, you will need to install the MoveIt! package for motion planning and manipulation. You can install it by following the instructions provided with this link [MoveIt!](https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html).

### Installation

To install the Franka Emika ROS package, clone the repository into your catkin workspace and build it using the following commands:

```bash
cd ~/your_catkin_ws/src
git clone https://github.com/Ivanterry00/Franka-Emika-ROS.git
cd ~/your_catkin_ws
catkin_make
```

## Usage

To do... 


## Notes
- In franka_ros, even if you use fr3 as robot, the names of links and joints are always panda_link and panda_joint
- When installing a live kernel, create a new Ubuntu group and use it to edit /etc/security/limits.conf as written at the end of the Linux installation section in the Franka Control interface documentation
- Remember that there are different planner to use on RViz (omp, chomp etc...)
- 

## Useful Commands for franka_ros Testing
To implements the franka_gripper_node for interfacing a gripper from ROS.
```bash
roslaunch franka_gripper franka_gripper.launch robot_ip:=172.16.0.2
```
To connect to a robot and publish the robot and gripper joint states for visualization in RViz.
This is purely for visualization - no commands are sent to the robot. It can be useful to check the connection to the robot.
```bash
roslaunch franka_visualization franka_visualization.launch robot_ip:=172.16.0.2 load_gripper:=true robot:=fr3
```
To launch the joint impedance example, execute the following command.
```bash
roslaunch franka_example_controllers joint_impedance_example_controller.launch robot_ip:=172.16.0.2 load_gripper:=true robot:=fr3
```
To launch the franka_control_node.
```bash
roslaunch franka_control franka_control.launch robot_ip:=172.16.0.2 load_gripper:=true robot:=fr3
```