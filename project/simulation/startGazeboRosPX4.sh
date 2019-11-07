#source ros location
source /opt/ros/melodic/setup.bash

#Run Firmware with gazebo_ros
source ../Firmware/Tools/setup_gazebo.bash $(pwd) ..//Firmware/build/px4_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:../Firmware
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:../Firmware/Tools/sitl_gazebo

#Start simulation
roslaunch px4 posix_sitl.launch