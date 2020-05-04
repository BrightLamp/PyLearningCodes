# encoding=utf-8

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

pos = 0


def talker():
    global pos
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10)  # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['front_caster_joint']
    hello_str.position = [3]
    hello_str.velocity = []
    hello_str.effort = []

    while not rospy.is_shutdown():
        pos += 1
        hello_str.position = [pos]
        hello_str.header.stamp = rospy.Time.now()
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
