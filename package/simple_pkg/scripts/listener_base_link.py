#!/usr/bin/python
import rospy
import tf
import geometry_msgs.msg
from nav_msgs.msg import Odometry  

def callback(msg):
    print(msg)

if __name__ == '__main__':
    rospy.init_node('tf_base_link_node')

    # t = tf.Transformer(True, rospy.Duration(10.0))
    # t.getFrameStrings()
    # m = geometry_msgs.msg.TransformStamped()
    # m.header.frame_id = 'odom'
    # m.child_frame_id = 'base_link'
    # m.transform.translation.x = 2.71828183
    # m.transform.rotation.w = 1.0
    # t.setTransform(m)
    # t.getFrameStrings()
    # t.lookupTransform('/odom', '/base_link', rospy.Time(0))
    # t.lookupTransform('/odom', '/base_link', rospy.Time(0))
    # print(m)

    # rate = rospy.Rate(10.0)
    # listener = tf.TransformListener()
    # while not rospy.is_shutdown():
    #     (transfromer,rot) = listener.lookupTransform('/odom', '/base_link', rospy.Time(0))
    #     print(transfromer, rot)

    odom_subscriber = rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

