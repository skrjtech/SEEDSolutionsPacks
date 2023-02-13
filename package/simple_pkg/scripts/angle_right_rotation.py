#!/usr/bin/python
import rospy
from geometry_msgs.msg import Pose, PoseStamped, Twist

if __name__ == '__main__':
    
    rospy.init_node('angle_right_rotation_node')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(1)

    # Angle Right Rotation
    for _ in range(10):
        rospy.loginfo("Rotation iter: %d" % (_ + 1))
        pose = Twist()
        pose.linear.x = 0.
        pose.linear.y = 0.
        pose.linear.z = 0.
        pose.angular.x = 0.
        pose.angular.y = 0.
        pose.angular.z = -0.1
        pub.publish(pose)
        rate.sleep()