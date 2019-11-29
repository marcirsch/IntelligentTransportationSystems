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
from std_msgs.msg import String
from sensor_msgs.msg import Image
from mavros_msgs.srv import *
from cv_bridge import CvBridge


## Constants
ARUCO_CODE_ID = 70
INPUT_IMG = 'img9.jpg'
mode = ScalingMode.NO

class Imagerecognition:
    def __init__(self):
        rospy.Subscriber("/iris/usb_cam/image_raw", Image, self.markerRecognitionCallback)
        self._cv_bridge = CvBridge()
    
    def markerRecognitionCallback(self, image_msg):
        #rospy.loginfo(image_msg.header)
        
        cv_img = self._cv_bridge.imgmsg_to_cv2(image_msg, "bgr8")
        print("before recoginition")
        ids, corners = marker_recognition(cv_img, mode)
        targetCorners = select_target(ids, corners, ARUCO_CODE_ID)
        turning_dir()
        moving_dir()

    def main(self):
        rospy.spin()

if __name__ == "__main__":
    rospy.init_node('image_process', anonymous=True)
    img_proc = Imagerecognition()
    img_proc.main()
     