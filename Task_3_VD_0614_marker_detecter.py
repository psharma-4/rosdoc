#!/usr/bin/env python

import cv2
from cv_bridge import CvBridge, CvBridgeError
import rospy
from sensor_msgs.msg import Image
import math
from std_msgs.msg import String




class image_proc():

	# Initialise everything
	def __init__(self):
		rospy.init_node('detect_marker') #Initialise rosnode 
                self.logo_cascade = cv2.CascadeClassifier('/home/pranav/catkin_ws/src/vitarana_drone/scripts/cascade.xml')

                 
                              
                self.coord=String()
                self.coord.data="NO MARKER" # When no marker is detected


                #SUBSCRIBER
		self.image_sub = rospy.Subscriber("/edrone/camera/image_raw", Image, self.image_callback) #Subscribing to the camera topic
                
                #PUBLISHER
                self.coord_pub = rospy.Publisher("pixel_coord", String, queue_size=1)

		self.bridge = CvBridge() 


	# Callback function of camera topic
	def image_callback(self, data):
		try:
			cv_img = self.bridge.imgmsg_to_cv2(data, "bgr8") # Converting the image to OpenCV standard image
                 
               	except CvBridgeError as e:
			print(e)

                
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)                   # Converting image to grayscale
                logo = self.logo_cascade.detectMultiScale(gray, scaleFactor=1.05) # Detecting the marker
                self.coord.data="NO MARKER"
                for (x, y, w, h) in logo:
                    if(w>=27 and w<=34): # These values are selected so that only marker is detectd while searching for it
                        cv_img=cv2.rectangle(cv_img,(x,y),(x+w,y+h),(0,0,255),5)
                        X=(x+x+w)//2  # Getting x coordinate of centre of marker
                        Y=(y+y+h)//2  # Getting y coordinate of centre of marker
                        self.coord.data=str(X)+","+str(Y)
                        
                    else:
                        self.coord.data="NO MARKER" 
                         
                    #print(w)   
                    
                #cv2.imshow("j",cv_img)
                #cv2.waitKey(1)    
                self.coord_pub.publish(self.coord)
                    
if __name__ == '__main__':
    image_proc_obj = image_proc()
    rospy.loginfo("started")
    
    
    rospy.spin()




