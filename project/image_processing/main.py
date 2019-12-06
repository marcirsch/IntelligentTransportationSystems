from marker_creation import marker_creation
from marker_recognition import marker_recognition
from marker_recognition import ScalingMode
from select_target import select_target
from moving_direction import moving_dir
from turning_direction import turning_dir

import rospy
import cv2
#import cv2.aruco as aruco
import sys
from std_msgs.msg import String,Int32
from sensor_msgs.msg import Image
from mavros_msgs.srv import *
from cv_bridge import CvBridge
from geometry_msgs.msg import TwistStamped, PoseStamped


## Constants
ARUCO_CODE_ID = 70
my_destination = 23
INPUT_IMG = 'img10.jpg'
mode = ScalingMode.NO


class Imagerecognition:
    def __init__(self):
        rospy.Subscriber("/iris/usb_cam/image_raw", Image, self.markerRecognitionCallback)
        self.seenId_pub = rospy.Publisher('/pizzadelivery/window/id', Int32, queue_size=1)
        self._cv_bridge = CvBridge()
    
    def markerRecognitionCallback(self, image_msg):
        cv_img = self._cv_bridge.imgmsg_to_cv2(image_msg, "bgr8")
        print("before recoginition")
        ids, corners = marker_recognition(cv_img, mode)
        print("publishing recognized aruco id")
        if ids is not None:
            self.seenId_pub.publish(ids[0][0])
        else:
            self.seenId_pub.publish(-1)


    def main(self):
        rospy.spin()

if __name__ == "__main__":
    rospy.init_node('image_process', anonymous=True)
    img_proc = Imagerecognition()
    img_proc.main()
     