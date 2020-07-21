#!/bin/bash


sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -


sudo apt update -y
echo 'Installing packages'
sudo apt install -y ros-melodic-desktop-full

echo 'Configuring environment'
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

echo 'Installing python dependecies'
sudo apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

echo 'Configuring ROS'
sudo rosdep init
rosdep update

echo 'Installing ROS Bridge'
sudo apt-get install ros-melodic-rosbridge-suite -y

echo 'Installing Gazebo'

sudo apt-get install gazebo9 libgazebo9-dev -y

echo 'Connecting gazebo with ros'
sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control -y

echo 'Removing unnecessary files'
sudo apt autoremove -y

echo 'Installation finished'

echo 'Activating environment'
source ~/.bashrc
