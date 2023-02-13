import sys
import time
import rospy
##-- for smach
from smach import State,StateMachine
import smach_ros
##-- for navigation
import yaml
import tf
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
##-- for find pkg
import rospkg
##-- for moveit
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Pose, PoseStamped
import geometry_msgs.msg
##-- for hand control
from seed_r7_ros_controller.srv import*

import numpy as np

class NaviAction:
  def __init__(self):
    # rospack = rospkg.RosPack()
    # rospack.list() 
    # path = rospack.get_path('seed_r7_samples')
    # with open(path + '/config/waypoints.yaml') as f:
    #     self.config = yaml.load(f)
    rospy.on_shutdown(self.shutdown)
    self.ac = actionlib.SimpleActionClient('base_link', MoveBaseAction)
    while not self.ac.wait_for_server(rospy.Duration(5)):
      rospy.loginfo("Waiting for the move_base action server to come up")
    rospy.loginfo("The server comes up")
    self.goal = MoveBaseGoal()

  def set_goal(self, x, y, z=0., row=0., pich=0., yow=0.):
    rospy.on_shutdown(self.shutdown)

    # rev = dict(self.config[_number]) #List to Dictionary

    self.goal.target_pose.header.frame_id = 'map'
    self.goal.target_pose.header.stamp = 0
    self.goal.target_pose.header.stamp = rospy.Time.now()
    self.goal.target_pose.pose.position.x = x
    self.goal.target_pose.pose.position.y = y
    self.goal.target_pose.pose.position.z = z
    quat = tf.transformations.quaternion_from_euler(row, pich, yow)
    self.goal.target_pose.pose.orientation.x = quat[0]
    self.goal.target_pose.pose.orientation.y = quat[1]
    self.goal.target_pose.pose.orientation.z = quat[2]
    self.goal.target_pose.pose.orientation.w = quat[3]

    rospy.loginfo('Sending goal')
    self.ac.send_goal(self.goal)
    succeeded = self.ac.wait_for_result(rospy.Duration(60))
    state = self.ac.get_state()
    if succeeded:
      rospy.loginfo("Succeed")
      return 'succeeded'
    else:
      rospy.loginfo("Failed")
      return 'aborted'

  def shutdown(self):
    #rospy.loginfo("The robot was terminated")
    self.ac.cancel_goal()

rospy.init_node("sample_scan")
nv = NaviAction()
for x in np.arange(0., 5., 0.01):
  nv.set_goal(x, 0, 0, 0, 0, -1)

print(nv.ac.get_state())
print(nv.ac.get_result())