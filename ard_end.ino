#include <ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/Float32.h>
ros::NodeHandle nh;


void call_back(const std_msgs::Int8 &msg){
  int a=(int)msg.data;
  digitalWrite(LED_BUILTIN,HIGH); 
  delay(a*3);
  digitalWrite(LED_BUILTIN,LOW);
  delay(a*3);
  //Serial.print(a);
}
std_msgs::Float32 f;
ros::Publisher pub("ard_t",&f);
ros::Subscriber<std_msgs::Int8> sub("ros_t",&call_back);
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // put your setup code here, to run once:
  //Serial.begin(9600);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(pub);
  randomSeed(analogRead(0));
}

void loop() {
  // put your main code here, to run repeatedly:
  f.data=random(1,200);
  pub.publish(&f);
  nh.spinOnce();
  delay(1);
}
