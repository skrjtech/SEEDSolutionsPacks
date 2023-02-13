#!/usr/bin/python

import sys
import time
import rospy
##-- for smach
from smach import State,StateMachine
import smach_ros
##-- for navigation
# import yaml
import tf
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
##-- for find pkg
import rospkg
##-- for moveit
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Pose, PoseStamped, Twist
import geometry_msgs.msg
##-- for hand control
from seed_r7_ros_controller.srv import*

rospy.init_node('scenario_node')
pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)

for i in range(10):
    pose = Twist()
    pose.linear.x = -1
    pose.linear.y = 0.
    pose.linear.z = 0.
    pose.angular.x = 0.
    pose.angular.y = 0.
    pose.angular.z = 0.
    pub.publish(pose)
    rate.sleep()