#!/usr/bin/env python
# coding: utf-8
import rospy
from math import pi
from time import sleep
import moveit_commander
from geometry_msgs.msg import Pose, PoseStamped
from moveit_commander import MoveGroupCommander,PlanningSceneInterface
from tf.transformations import quaternion_from_euler


DE2RA = pi / 180

if __name__ == '__main__':

    rospy.init_node("abb_motion_plan_py")

    abb = MoveGroupCommander("arm")

    abb.set_named_target("down")
    abb.go()
    sleep(2)

    abb.allow_replanning(True)
    abb.set_planning_time(5)

    abb.set_num_planning_attempts(10)

    abb.set_goal_position_tolerance(0.01)

    abb.set_goal_orientation_tolerance(0.01)

    abb.set_goal_tolerance(0.01)

    abb.set_max_velocity_scaling_factor(1.0)

    abb.set_max_acceleration_scaling_factor(1.0)
   
    target_joints2 = [90, 90, 90, 90, 90]
    

    while 1:
        # abb.set_joint_value_target(target_joints1)
        # abb.go()
        # sleep(2)


        # abb.set_joint_value_target(target_joints2)
        # abb.go()
   
        # sleep(2)
        abb.set_named_target("down")
        abb.go()
        sleep(2)

        abb.set_named_target("random")
        abb.go()
        sleep(2)

