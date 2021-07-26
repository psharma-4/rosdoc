#!/usr/bin/env python
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Float32
import random
a=60
def call_back(msg):
    rospy.loginfo("RECIEVED")
    global a
    rospy.loginfo(msg.data)
    if(msg.data>100):
        a=127
    else:
        a=1

pub =rospy.Publisher('ros_t',Int8, queue_size=10)
sub=rospy.Subscriber('ard_t',Float32,call_back)
rospy.init_node('ros_end',anonymous=True)
rate =rospy.Rate(1)

while not rospy.is_shutdown():
    rospy.loginfo(a)
    pub.publish(a)
    rate.sleep()

