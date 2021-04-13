#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def calback_reciever(msg):
    rospy.loginfo(msg.data)

if __name__ == '__main__':
    rospy.init_node('subscriber_test')

    sub = rospy.Subscriber("/number_count", Int64, calback_reciever)

    rospy.spin()