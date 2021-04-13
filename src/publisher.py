#!/usr/bin/env python3

import rospy
from std_msgs.msg import String



if __name__ == '__main__':
    rospy.init_node('publisher_test')

    pub = rospy.Publisher("/number_count", String, queue_size=10)

    rate = rospy.Rate(2)
    counter = "test"
    while not rospy.is_shutdown():
        msg = String()
        msg.data = counter
        pub.publish(msg)

        rate.sleep()
