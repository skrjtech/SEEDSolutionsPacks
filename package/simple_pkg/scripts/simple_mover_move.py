#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
import actionlib
import tf
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class NaviAction:
  def __init__(self):
    rospy.on_shutdown(self.shutdown)
    self.ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    while not self.ac.wait_for_server(rospy.Duration(5)):
      rospy.loginfo("Waiting for the move_base action server to come up")
    rospy.loginfo("The server comes up")
    self.goal = MoveBaseGoal()

  def set_goal(self, x, y, z=0., row=0., pich=0., yow=0.):
    rospy.on_shutdown(self.shutdown)

    self.goal.target_pose.header.frame_id = 'map'
    self.goal.target_pose.header.stamp = rospy.Time.now()
    self.goal.target_pose.pose.position.x = x
    self.goal.target_pose.pose.position.y = y
    self.goal.target_pose.pose.position.z = z
    quat = tf.transformations.quaternion_from_euler(row, pich, yow)
    self.goal.target_pose.pose.orientation.x = quat[0]
    self.goal.target_pose.pose.orientation.y = quat[1]
    self.goal.target_pose.pose.orientation.z = quat[2]
    self.goal.target_pose.pose.orientation.w = quat[3]

    self.ac.send_goal(self.goal)
    succeeded = self.ac.wait_for_result(rospy.Duration(60))
    state = self.ac.get_state()
    if succeeded:
      return 'succeeded'
    else:
      return 'aborted'

  def shutdown(self):
    self.ac.cancel_goal()

if __name__ == "__main__":
	rospy.init_node("simple_mover_move")
	# mover = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	# rospy.on_shutdown(mover.cancel_goal)
	# goal = MoveBaseGoal()
	# # 初期値からX方向に1[m]移動
	# goal.target_pose.header.frame_id = 'map'
	# goal.target_pose.header.stamp = rospy.Time.now()
	# goal.target_pose.pose.position.x = 1
	# goal.target_pose.pose.position.y = 0
	# goal.target_pose.pose.position.z = 0
	# quat =  tf.transformations.quaternion_from_euler(0,0,1)
	# goal.target_pose.pose.orientation.x = quat[0]
	# goal.target_pose.pose.orientation.y = quat[1]
	# goal.target_pose.pose.orientation.z = quat[2]
	# goal.target_pose.pose.orientation.w = quat[3]
	# mover.send_goal(goal)
	# mover.wait_for_result(rospy.Duration(60))

	na = NaviAction()
	na.set_goal(1, 0, 0, 0, 0, 0)
	na.set_goal(1, 1, 0, 0, 0, 0)
	na.set_goal(0, 1, 0, 0, 0, 0)