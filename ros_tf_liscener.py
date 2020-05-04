# encoding=utf-8

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('py_tf_turtle')
    listener = tf.TransformListener()

    listener.waitForTransform("/base_link", "/front_caster", rospy.Time(), rospy.Duration(4))

    (trans, rot) = listener.lookupTransform('/base_link', '/front_caster', rospy.Time(0))

    rospy.loginfo('距离原点的位置: x=%f, y=%f, z=%f', trans[0], trans[1], trans[2])
    rospy.loginfo('旋转四元数: w=%f, x=%f, y=%f, z=%f', rot[0], rot[1], rot[2], rot[3])
    canTransform = listener.canTransform('/base_link', '/front_caster', rospy.Time(0))
    print canTransform
