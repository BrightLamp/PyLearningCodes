# encoding=utf-8

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('py_tf_broadcaster')
    br = tf.TransformBroadcaster()

    x = 0.0
    y = 0.0
    z = 0.0
    roll = 0
    pitch = 0
    yaw = 1.57
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        yaw = yaw + 0.1
        roll = roll + 0.1
        br.sendTransform((x, y, z),
                         tf.transformations.quaternion_from_euler(roll, pitch, yaw),
                         rospy.Time.now(),
                         "base_link",
                         "front_caster")  # 发布base_link到link1的平移和翻转
        rate.sleep()
