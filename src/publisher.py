#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64



if __name__ == '__main__':
    rospy.init_node('publisher_test')

    pub = rospy.Publisher("/number_count", Int64, queue_size=10)

    rate = rospy.Rate(2)
    counter = 1
    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = counter
        counter += 1
        pub.publish(msg)

        rate.sleep()
