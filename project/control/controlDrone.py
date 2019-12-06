import rospy
import mavros
import math
import numpy as np
from std_msgs.msg import Header, Int32
from mavros_msgs.msg import PositionTarget
from mavros_msgs.srv import CommandBool, CommandTOL, SetMode
from geometry_msgs.msg import PoseStamped
import enum
from calculateCoordinates import calculateWindowCoordinates
import time


mavros.set_namespace()
offb_set_mode = SetMode


# SET THE WINDOW NUMBER HERE, WHERE YOU WANT THE DRONE TO BE MOVED (11..16,21..26, etc.)
targetWindowCode = 44

startWindowCode = 11

set_mode_client = rospy.ServiceProxy(mavros.get_topic('set_mode'), SetMode) 


DISTANCE_BEETWEEN_WINDOWS = 6
save_image_counter = 0



class ControlState(enum.Enum):
    INIT = 1   
    CODE_RECOGNITION = 2
    SLEEP1 = 3
    MOVE = 4
    SLEEP2 = 5

# INIT: The drone should fly to an aruco code on startup
# CODE_RECOGNITION: The drone recognizeses the actual code, which is seen by camera
# MOVE: after direction & distance calculations, the drone should fly to targetWindow
# NO_OP: stand-by

class DroneControl():

    def __init__(self):
        rospy.Subscriber('/pizzadelivery/window/id', Int32, self.receiveRecognizedIdCallback)
        #rospy.Subscriber('/mavros/setpoint_raw/local', PositionTarget, self.saveActualDronePosition)
        self.controlPublisher = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size=100)
        self.controlState = ControlState.INIT
        self.x = 0
        self.y = 0
        self.z = 17
        self.theta = 180
    
    def to_pose_stamped(self):
        pose = PoseStamped()
        pose.header.frame_id = ''
        pose.pose.position.x = self.x
        pose.pose.position.y = self.y
        pose.pose.position.z = self.z
        print("Filled PoseStamped object: ", pose)
        print("Filled PoseStamped objectheader: ", pose.header)

        #quaternion = tf.transformations.quaternion_from_euler(0, 0, self.theta)
        pose.pose.orientation.x = 0
        pose.pose.orientation.y = 0.8
        pose.pose.orientation.z = 0
        pose.pose.orientation.w = 0
        print("Filled PoseStamped object pose: ", pose.pose)


        return pose 

    def receiveRecognizedIdCallback(self, id_msg):
        print('The received aruco ID is:', id_msg)

        # Implement state machine here
        if self.controlState == ControlState.INIT:
            #fly to a specified position which is in front of an aruco code!!!!!!!
            #rate = rospy.Rate(10)
                           
            self.controlPublisher.publish(self.to_pose_stamped())
            #arm
            print(1)
            rospy.wait_for_service('/mavros/cmd/arming')
            print(2)
            try:
                print(3)
                armService = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
                print(4)
                armService(True)                    
                print(6)
            except rospy.ServiceException, e:
                print "Service arm call failed: %s"%e    
            
            print(5)
            set_mode_client(base_mode=0, custom_mode="OFFBOARD")
            print("id_msg: ", id_msg)
            print("startWindowCode: ", startWindowCode)

            if id_msg.data == startWindowCode:
                self.controlState = ControlState.CODE_RECOGNITION

        if self.controlState == ControlState.CODE_RECOGNITION:
            # code verification
            # if not at target window--> calc
            print("recognition")
            moveX, moveY = calculateWindowCoordinates(targetWindowCode, id_msg.data)
            self.y += moveX
            self.z += moveY

            self.controlState = ControlState.SLEEP1

        if self.controlState == ControlState.SLEEP1:
            time.sleep(2)
            self.controlState = ControlState.MOVE

        if self.controlState == ControlState.MOVE:
            # move

            self.controlPublisher.publish(self.to_pose_stamped())
            #arm
            print(1)
            rospy.wait_for_service('/mavros/cmd/arming')
            print(2)
            try:
                print(3)
                armService = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
                print(4)
                armService(True)                    
                print(6)
            except rospy.ServiceException, e:
                print "Service arm call failed: %s"%e    
            
            print(5)
            set_mode_client(base_mode=0, custom_mode="OFFBOARD")
            print("id_msg: ", id_msg)
            print("startWindowCode: ", startWindowCode)

            if id_msg.data == targetWindowCode:
                self.controlState = ControlState.SLEEP2

        if self.controlState == ControlState.SLEEP2:

            print("sleeping..")

    def saveActualDronePosition(self, position):
        print(position)        


    def main(self):
        rospy.spin()



if __name__ == "__main__":
    rospy.init_node('control_node', anonymous=True)
    drone_ctrl = DroneControl()
    drone_ctrl.main()

