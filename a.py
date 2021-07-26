
while():
    self.drone_orientation.rcRoll = 1500 
    self.drone_orientation.rcPitch = 1500 
    self.drone_orientation.rcYaw = 1500
    self.drone_orientation.rcThrottle = 1500
    self.rc_pub.publish(self.drone_orientation)
