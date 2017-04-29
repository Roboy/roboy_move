#!/usr/bin/python


from std_msgs.msg import String
from std_msgs.msg import Int32
from roboy_move.srv import Movement
from roboy_move.srv import Yaw

import os
import sys

import rospy

def yaw_callback(req):
	pub = rospy.Publisher('/roboy_move/yaw', Int32, queue_size=10)
	msg = Int32()
	msg.data = req.value;
	pub.publish(msg)
	return {'success':True}

def replay_callback(req):
	pub = rospy.Publisher('/roboy_move/replay', String, queue_size=10)
	msg = String()
	msg.data = req.value;
	pub.publish(msg)
	return {'success':True}


if __name__ == '__main__':
	rospy.init_node('roboy_move')
	rospy.Service('/roboy_move/yaw', Yaw, yaw_callback)
	rospy.Service('/roboy_move/replay', Movement, replay_callback)
	print "/roboy_move/ is ready"

	rospy.spin()