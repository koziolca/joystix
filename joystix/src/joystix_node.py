import rospy
from sensor_msgs.msg import Joy

def callback(data):
	leftPub.publish(data.axes[1] * 100)
	rightPub.publish(data.axes[4] * 100)

def start():

	global leftPub
	global rightPub
	leftPub = rospy.Publisher('leftJoystick')
	rightPub = rospy.Publisher('rightJoystick')

	rospy.Subscriber('joy', Joy, callback)
	rospy.init_node('twin_sticks')
	rospy.spin()

if __name__ == '__main__':
	start()
