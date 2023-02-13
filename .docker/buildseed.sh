#!/bin/bash

# sudo apt update && sudo apt -y upgrade
sudo apt install -y cmake

source /opt/ros/melodic/setup.bash

sudo rm -f /etc/ros/rosdep/sources.list.d/20-default.list
sudo rosdep init
rosdep update

sudo apt-get install python-wstool python-catkin-tools

# catkin config --extend /opt/ros/$ROS_DISTRO

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin init
catkin build
cd ~/catkin_ws/src

git clone https://github.com/seed-solutions/seed_smartactuator_sdk
git clone https://github.com/seed-solutions/seed_r7_ros_pkg.git
git clone https://github.com/seed-solutions/task_programmer.git
# git clone https://github.com/seed-solutions/motion_tracer.git

cd ~/catkin_ws
rosdep install -y -r --from-paths src --ignore-src
catkin build seed_r7_ros_pkg

source ~/catkin_ws/devel/setup.bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

mkdir -p ~/catkin_ws/src/public