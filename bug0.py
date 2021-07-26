#!/usr/bin/env python
import rospy
import roslib
#from sensor_msgs import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import tf
import math

curr_x=0.0
curr_y=0.0
curr_theta=0.0
final_goal=[6.0,4.0]
#prev_time=0.0
#time=rospy.Time.now()
global cmd

cmd=Twist()
cmd.linear.x=0.0
cmd.linear.y=0.0
cmd.linear.z=0.0
cmd.angular.x=0.0
cmd.angular.y=0.0
cmd.angular.z=0.0

def odom_callback(msg):
    #rospy.loginfo(msg.pose.pose.orientation)
    global curr_x
    global curr_y
    global curr_theta
    curr_x=msg.pose.pose.position.x
    curr_y=msg.pose.pose.position.y
    orient=msg.pose.pose.orientation
    (roll,pitch,yaw)=tf.transformations.euler_from_quaternion([orient.x,orient.y,orient.z,orient.w])
    curr_theta=yaw
    rospy.loginfo('x')
    rospy.loginfo(curr_x)
    rospy.loginfo('y')
    rospy.loginfo(curr_y)
    rospy.loginfo('theta')
    rospy.loginfo(curr_theta)

def to_goal():
    target_angle =math.atan2(final_goal[1]-curr_y,final_goal[0]-curr_x)
    rospy.loginfo(target_angle)
    rospy.loginfo(curr_theta-target_angle)
    dist=math.sqrt((final_goal[0]-curr_x)**2 +(final_goal[1]-curr_y)**2)
    if(abs(curr_theta-target_angle)>5*0.0174):
        cmd.linear.x=0.0
        cmd.angular.z=0.1 *(curr_theta-target_angle/abs(curr_theta-target_angle))
        rospy.loginfo('rotate')
    # elif(dist>0.001):
    #     cmd.linear.x=0.1
    #     cmd.angular.z=0.0
    #     rospy.loginfo('straight')
    else:
        cmd.linear.x=0.0
        cmd.angular.z=0.0
        exit()
        rospy.loginfo('reached')


if __name__=="__main__":
    rospy.init_node("bug0")
    cmd_pub=rospy.Publisher("/cmd_vel",Twist,queue_size=1)
    Odom_sub=rospy.Subscriber('/odom',Odometry,odom_callback)
    cmd_pub.publish(cmd)
    rospy.spin()
    # rate=rospy.Rate(10.0)
    # while not rospy.is_shutdown():
    #     #prev_time=time
    #     #time=rospy.Time.now()
    #     to_goal()
    #     cmd_pub.publish(cmd)
    #     rospy.loginfo("publishing...")
    #     rate.sleep()

