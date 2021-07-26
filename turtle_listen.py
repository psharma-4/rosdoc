#!/usr/bin/env python
import roslib
import rospy
import tf
from geometry_msgs.msg import Twist
import turtlesim.srv
import math
if __name__=="__main__":
    rospy.init_node("frame_listener")

    tf_list=tf.TransformListener()
    rospy.wait_for_service('spawn')
    spawner=rospy.ServiceProxy('spawn',turtlesim.srv.Spawn)
    spawner(4,2,0,'turtle2')
    
    pub=rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=10)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            translation,rotation= tf_list.lookupTransform('/turtle2_frame','/turtle1_frame',rospy.Time(0))
        except(tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
            continue

        angular=  math.atan2(translation[1],translation[0])
        linear=0.5 * math.sqrt(translation[0]**2 +translation[1]**2)
        cmd=Twist()
        cmd.angular.z=angular
        cmd.linear.x=linear
        pub.publish(cmd)
        rate.sleep()
