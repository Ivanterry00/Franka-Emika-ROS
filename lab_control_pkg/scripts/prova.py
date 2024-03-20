#!/usr/bin/python3

import copy
import sys
import math
import rospy
import moveit_commander
import time

from geometry_msgs.msg import Pose, PoseStamped
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive

from tf.transformations import quaternion_from_euler

FRAME_ID = 'fr3_link0'
(X, Y, Z, W) = (0, 1, 2, 3)
OPEN = 0.9
CLOSE = 0.15
TARGET_POSITIONS = {'target_1': [0.45, 0.0, 0.15], 'target_2': [0.0, -0.65, 0.55]}
ORIENTATION_POSITIONS = {'target_1': [0.92, -0.38, 0.0, 0.0], 'target_2': [0.0, 0.0, 0.0, 1.0]}
PICK_ORIENTATION_EULER = [-math.pi / 2, 0, 0]
PLACE_ORIENTATION_EULER = [-math.pi / 2, 0, -math.pi / 2]
SCENE = moveit_commander.PlanningSceneInterface()


def create_collision_object(id, dimensions, pose):
    object = CollisionObject()
    object.id = id
    object.header.frame_id = FRAME_ID

    solid = SolidPrimitive()
    solid.type = solid.BOX
    solid.dimensions = dimensions
    object.primitives = [solid]

    object_pose = Pose()
    object_pose.position.x = pose[X]
    object_pose.position.y = pose[Y]
    object_pose.position.z = pose[Z]

    object.primitive_poses = [object_pose]
    object.operation = object.ADD
    return object

def add_visual_objects(id, dimensions, pose):
    box_pose = PoseStamped()
    box_pose.header.frame_id = FRAME_ID
    box_pose.pose.position.x = pose[X]
    box_pose.pose.position.y = pose[Y]
    box_pose.pose.position.z = pose[Z]
    box_pose.pose.orientation.w = 1.0

    SCENE.add_box(id, box_pose, dimensions)


def add_collision_and_visual_objects():
    # FLOOR COLLISION ONLY FOR RVIZ SIMULATION
    floor_limit_front = create_collision_object(id='floor_limit_front',
                                          dimensions=[0.9, 2, 0.02],
                                          pose=[0.55, 0, -0.01])
    floor_limit_back = create_collision_object(id='floor_limit_back',
                                          dimensions=[0.46, 2, 0.02],
                                          pose=[-0.42, 0, -0.01])
    floor_limit_left = create_collision_object(id='floor_limit_left',
                                          dimensions=[0.34, 0.9, 0.02],
                                          pose=[-0.02, -0.55, -0.01])
    floor_limit_right = create_collision_object(id='floor_limit_right',
                                          dimensions=[0.34, 0.9, 0.02], 
                                          pose=[-0.02, 0.55, -0.01])

    # FLOOR COLLISION FOR GAZEBO SIMULATION
    floor_limit = create_collision_object(id='floor_limit',
                                            dimensions=[1.65, 2, 0.02],
                                            pose=[0.175, 0, -0.0101])
   
    back_wall = create_collision_object(id='back_wall',
                                        dimensions=[0.2, 2, 1.5],
                                        pose=[-0.55, 0, 0.75])
    table_1 = create_collision_object(id='table_1',
                                        dimensions=[0.6, 0.8, 0.1],
                                        pose=[0.45, 0.0, 0.05],)
    table_2 = create_collision_object(id='table_2',
                                        dimensions=[0.7, 0.5, 0.4],
                                        pose=[0.0, -0.75, 0.2])

    # FLOOR COLLISION ONLY FOR RVIZ SIMULATION
    SCENE.add_object(floor_limit_back)
    SCENE.add_object(floor_limit_front)
    SCENE.add_object(floor_limit_left)
    SCENE.add_object(floor_limit_right)

    # FLOOR COLLISION FOR GAZEBO SIMULATION
    # SCENE.add_object(floor_limit)

    SCENE.add_object(back_wall)
    SCENE.add_object(table_1)
    SCENE.add_object(table_2)

def reach_named_position(arm, target):
    arm.set_named_target(target)
    arm.go(wait=True)
    arm.stop()
    arm.clear_pose_targets()

def reach_pose(arm, pose, tolerance=0.001):
    arm.set_pose_target(pose)
    arm.set_goal_position_tolerance(tolerance)
    success = arm.go(wait=True) # `go()` returns a boolean indicating whether the planning and execution was successful.
    print(success)
    arm.stop()  # Calling `stop()` ensures that there is no residual movement
    arm.clear_pose_targets()    # It is always good to clear your targets after planning with poses.   

def open_gripper(gripper):
    return gripper.move(gripper.max_bound() * OPEN, True)


def close_gripper(gripper):
    gripper.move(gripper.max_bound() * CLOSE, True)


def pick_object(name, arm, gripper, actual_pose):
    pose = Pose()
    pose.position.x = TARGET_POSITIONS[name][X]
    pose.position.y = TARGET_POSITIONS[name][Y] 
    pose.position.z = TARGET_POSITIONS[name][Z] + 0.2
    # orientation = quaternion_from_euler(*PICK_ORIENTATION_EULER)
    # pose.orientation.x = orientation[X]
    # pose.orientation.y = orientation[Y]
    # pose.orientation.z = orientation[Z]
    # pose.orientation.w = orientation[W]
    pose.orientation.x = actual_pose.orientation.x
    pose.orientation.y = actual_pose.orientation.y
    pose.orientation.z = actual_pose.orientation.z
    pose.orientation.w = actual_pose.orientation.w
    
    reach_pose(arm, pose)
    open_gripper(gripper=gripper)
    pose.position.z -= 0.1
    reach_pose(arm, pose)
    close_gripper(gripper=gripper)
    # arm.attach_object(name)
    pose.position.z += 0.3
    reach_pose(arm, pose)


def place_object(name, arm, gripper, actual_pose):
    pose = Pose()
    pose.position.x = TARGET_POSITIONS[name][X]
    pose.position.y = TARGET_POSITIONS[name][Y]
    pose.position.z = TARGET_POSITIONS[name][Z]
    # orientation = quaternion_from_euler(*PLACE_ORIENTATION_EULER)
    # pose.orientation.x = orientation[X]
    # pose.orientation.y = orientation[Y]
    # pose.orientation.z = orientation[Z]
    # pose.orientation.w = orientation[W]
    pose.orientation.x = actual_pose.orientation.x
    pose.orientation.y = actual_pose.orientation.y
    pose.orientation.z = actual_pose.orientation.z 
    pose.orientation.w = actual_pose.orientation.w

    reach_pose(arm, pose)
    open_gripper(gripper=gripper)
    # arm.detach_object(name)

def cartesian_path(arm, waypoints):
    (plan, fraction) = arm.compute_cartesian_path(waypoints, 0.01, 0.0)
    return plan, fraction

# Function to print data about the robot's actual state
def print_data(arm):
    print("==== Reference frame: %s" % arm.get_planning_frame())

    print("==== End effector link: %s" % arm.get_end_effector_link())

    print("==== Printing current robot state")
    print(arm.get_current_state())
    print("")

    print("==== Printing current robot pose")
    print(arm.get_current_pose())
    print("")

    print("==== Available Planning Groups:", arm.get_group_names())
    print("")

def main():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('fr3_pick_place')
    rospy.sleep(2)

    arm = moveit_commander.MoveGroupCommander('fr3_arm')
    robot = moveit_commander.RobotCommander()
    gripper = robot.get_joint('fr3_finger_joint1')

    actual_pose = arm.get_current_pose().pose

    arm.set_num_planning_attempts(45)

    add_collision_and_visual_objects()
    open_gripper(gripper)
    pick_object(name='target_1', arm=arm, gripper=gripper, actual_pose=actual_pose)   
    place_object(name='target_2', arm=arm, gripper=gripper, actual_pose=actual_pose)
    reach_named_position(arm=arm, target='ready')

if __name__ == '__main__':
    main()