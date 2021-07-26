#!/usr/bin/env python
import rospy
import roslib
from turtlesim.msg import Pose 
import tf

def call_back(msg,t_name):
    tf_cast=tf.TransformBroadcaster()
    translation= (msg.x,msg.y,0)
    rotation=tf.transformations.quaternion_from_euler(0,0,msg.theta)
    current_time=rospy.Time.now()
    tf_cast.sendTransform(translation,rotation,current_time,"%s_frame" %t_name,"world")


if __name__=="__main__":
    rospy.init_node("frame_broadcaster")
    t_name=rospy.get_param('~turtle')
    sub=rospy.Subscriber("/%s/pose" %t_name,Pose,call_back,t_name)
    rospy.spin()
