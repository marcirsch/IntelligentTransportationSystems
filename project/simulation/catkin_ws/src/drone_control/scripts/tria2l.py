#!/usr/bin/env python

import rospy
from mavros_msgs.srv import SetMode
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
import time

rospy.init_node('mavros_takeoff_python')
rate = rospy.Rate(10)

# Set Mode
print "\nSetting Mode"
rospy.wait_for_service('/mavros/set_mode')
try:
    change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
    response = change_mode(custom_mode="ALT_HOLD")
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Set mode failed: %s" %e)

# Arm
print "\nArming"
rospy.wait_for_service('/mavros/cmd/arming')
try:
    arming_cl = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
    response = arming_cl(value = True)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Arming failed: %s" %e)

print "\narming..."
time.sleep(4)

# Takeoff
print "\nTaking off"
rospy.wait_for_service('/mavros/cmd/takeoff')
try:
    takeoff_cl = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
    #response = takeoff_cl(x=0, y=0, z=0)
    response = takeoff_cl()
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Takeoff failed: %s" %e)
