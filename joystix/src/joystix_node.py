#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32

def callback(data):
	leftPub.publish(data.axes[1] * 100)
	rightPub.publish(data.axes[4] * 100)

def start():

	global leftPub
	global rightPub
	leftPub = rospy.Publisher('leftJoystick', Float32, queue_size = 10)
	rightPub = rospy.Publisher('rightJoystick', Float32, queue_size = 10)

	rospy.Subscriber('joy', Joy, callback)
	rospy.init_node('twin_sticks')
	rospy.spin()

if __name__ == '__main__':
	start()
