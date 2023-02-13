#!/usr/bin/python
#-*- coding: utf-8 -*-
import rospy
import math
import copy
import tf
import time
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Quaternion, Pose, PoseStamped, Vector3
from seed_r7_ros_controller.srv import*

def Hello():
    robot = moveit_commander.RobotCommander()
    upper_body = moveit_commander.MoveGroupCommander("upper_body")
    lifter = moveit_commander.MoveGroupCommander("lifter")
    rarm_with_torso = moveit_commander.MoveGroupCommander("rarm_with_torso")

    upper_body.set_max_velocity_scaling_factor(1)
    lifter.set_max_velocity_scaling_factor(1)

    rospy.wait_for_service('/seed_r7_ros_controller/hand_control')
    service = rospy.ServiceProxy('/seed_r7_ros_controller/hand_control', HandControl)

    def initPose(lifter=True,top=True):
        joint_length = len(upper_body.get_current_joint_values())
        upper_body.set_joint_value_target(joint_length * [0]) #all joints are initialized at 0
        upper_body.set_joint_value_target('r_elbow_joint',-2.8)
        upper_body.set_joint_value_target('l_elbow_joint',-2.8)
        upper_body.go(wait=True)    
        
        if(lifter and top):
          lifter.set_joint_value_target('ankle_joint',0)
          lifter.set_joint_value_target('knee_joint',0)
          lifter.go(wait=True)

        elif(lifter and not top):
          lifter.set_joint_value_target('ankle_joint',1.4)
          lifter.set_joint_value_target('knee_joint',-1.4)
          lifter.go(wait=True)
        
    def Run():
        upper_body.set_joint_value_target('r_elbow_joint',-2.0)
        upper_body.set_joint_value_target('l_elbow_joint',-2.8)
        upper_body.set_joint_value_target('r_shoulder_p_joint',-0.9)
        upper_body.set_joint_value_target('r_shoulder_r_joint',0)
        upper_body.set_joint_value_target('r_shoulder_y_joint',-0.5)
        upper_body.go(wait=True)

        upper_body.set_joint_value_target('waist_y_joint',0.5)
        upper_body.go(wait=True)
        for i in range(0,2):
            upper_body.set_joint_value_target('r_shoulder_y_joint',0.3)
            upper_body.go(wait=True) 
            upper_body.set_joint_value_target('r_shoulder_y_joint',-0.3)
            upper_body.go(wait=True) 

        upper_body.set_joint_value_target('waist_y_joint',-0.5)
        upper_body.go(wait=True)
        for i in range(0,2):
            upper_body.set_joint_value_target('r_shoulder_y_joint',0.3)
            upper_body.go(wait=True) 
            upper_body.set_joint_value_target('r_shoulder_y_joint',-0.3)
            upper_body.go(wait=True)

        init_pose(lifter=False)

    initPose()
    Run()

if __name__ == '__main__':
  rospy.init_node('motion_node')
  Hello()