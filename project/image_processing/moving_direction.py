import numpy as np
from geometry_msgs.msg import TwistStamped, PoseStamped

#https://github.com/PX4/Firmware/blob/master/integrationtests/python_src/px4_it/mavros/mavros_offboard_posctl_test.py
#ez alapjan kene megcsinalni jora



def moving_dir(my_destination, ids,corners):
    print(ids)
    print(ids[0][0])


"""  
    if my_destination == 0:
        pos.pose.position.x = starting_x
        pos.pose.position.z = starting_y 
        pos.pose.position.z = starting_z
        set_point.pub(message)
    
    else:
        id = ids[0]
        #message = TwistStamped()
        pos = PoseStamped()
        if id != my_destination:
            row_error = (my_destination-id)/10
            column_error = (my_destination-id)%10
            pos.pose.position.x = local_position.pose.position.x + column_error*6 
            pos.pose.position.z = local_position.pose.position.z + row_error*6 
            set_point.pub(message)
"""
