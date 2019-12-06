from __future__ import division


import rospy
import math
import numpy as np
from geometry_msgs.msg import PoseStamped, Quaternion
from mavros_test_common import MavrosTestCommon
from pymavlink import mavutil
from std_msgs.msg import Header
from tf.transformations import quaternion_from_euler


class MavrosOffboardPosctlTest(MavrosTestCommon):

    def listener():
        x=10
        y=10
        z=5
        offset = 1
        
        self.pos = PoseStamped() #pozcionk
        self.radius = 1
        rate = rospy.Rate(10)  # Hz

        self.pos.pose.position.x = x
        self.pos.pose.position.y = y
        self.pos.pose.position.z = z
        rospy.loginfo(
            "attempting to reach position | x: {0}, y: {1}, z: {2} | current position x: {3:.2f}, y: {4:.2f}, z: {5:.2f}".
            format(x, y, z, self.local_position.pose.position.x,
                   self.local_position.pose.position.y,
                   self.local_position.pose.position.z))
       
        desired = np.array((x, y, z))
        pos = np.array((self.local_position.pose.position.x,
                        self.local_position.pose.position.y,
                        self.local_position.pose.position.z))
        setpoint_pub.pub(pos)
        #while np.linalg.norm(desired - pos) > offset
        sleep(1000)



if __name__ == '__main__':
    rospy.init_node('control_node', anonymous=True)
    setpoint_pub = rospy.Publisher('mavros/setpoint_position/local', PoseStamped, queue_size=1)
    MavrosOffboardPosctlTest()
