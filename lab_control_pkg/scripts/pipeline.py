#!/usr/bin/env python3

# Import for MoveIt! and ROS
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi, tau, dist, fabs, cos
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

# Import for collision objects
from geometry_msgs.msg import Pose, PoseStamped
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive

# Import for gripper control
from franka_gripper.msg import MoveActionGoal, MoveGoal
import time

# Constants
GROUP_NAME = "fr3_arm"
FRAME_ID = "fr3_link0"
(X, Y, Z, W) = (0, 1, 2, 3)
TARGET_POSITIONS = {'target_1': [0.45, 0.0, 0.15], 'target_2': [0.0, -0.65, 0.55]}
ORIENTATION_POSITIONS = {'target_1': [0.92, -0.38, 0.0, 0.0], 'target_2': [0.0, 0.0, 0.0, 1.0]}
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


def add_collision_objects():
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

def moveGripper(width, speed):
    # Create publisher to publish to the /franka_gripper/move/goal topic
    pub = rospy.Publisher('/franka_gripper/move/goal', MoveActionGoal, queue_size=10)
    
    # Wait for publisher to be registered
    rospy.sleep(1.0)
    
    # Create a MoveActionGoal message
    move_goal_msg = MoveActionGoal()
    move_goal_msg.goal = MoveGoal()
    
    # Set width and speed values from command-line arguments
    move_goal_msg.goal.width = width
    move_goal_msg.goal.speed = speed
    
    # Publish the message once
    pub.publish(move_goal_msg)
    
    rospy.loginfo(f"Published MoveActionGoal message to /franka_gripper/move/goal with width: {width}, speed: {speed}")

    time.sleep(4.0)

def planCartesianPath(move_group, x, y, z):
    waypoints = []
    wpose = move_group.get_current_pose().pose
    wpose.position.x += x
    wpose.position.y += y
    wpose.position.z += z
    waypoints.append(copy.deepcopy(wpose))

    (plan, fraction) = move_group.compute_cartesian_path(
                                       waypoints,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold

    # waypoints = []
    # wpose = move_group.get_current_pose().pose
    # wpose.position.x += 0.2
    # wpose.position.z -= 0.2
    # waypoints.append(copy.deepcopy(wpose))

    # wpose.position.z -= 0.1
    # waypoints.append(copy.deepcopy(wpose))
 
    # wpose.position.z += 0.3
    # waypoints.append(copy.deepcopy(wpose))
 
    # wpose.position.x -= 0.2
    # waypoints.append(copy.deepcopy(wpose))
 
    # wpose.position.x -= 0.3
    # wpose.position.y -= 0.7
    # wpose.position.z += 0.1
    # waypoints.append(copy.deepcopy(wpose))

    return plan, fraction

def displayTrajectory(plan, robot):
    print("============ Visualizing plan")
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)

    display_trajectory_publisher = rospy.Publisher(
        "/move_group/display_planned_path",
        moveit_msgs.msg.DisplayTrajectory,
        queue_size=20,
    )

    display_trajectory_publisher.publish(display_trajectory)

def executePlan(move_group, robot, x, y, z):
    while(True):
        # Planning a cartesian path
        plan, fraction = planCartesianPath(move_group, x, y, z)

        # Display the trajectory
        displayTrajectory(plan, robot)

        print("If the plan is good ress 'y' to continue")
        key = input()
        if key == 'y':
            break
        elif key == 'n':
            print("Planning a new path")
        
    # Execute the plan
    move_group.execute(plan, wait=True)

def getBasicRobotData(move_group, robot):
    print("==== Reference frame: %s" % move_group.get_planning_frame())

    print("==== End effector link: %s" % move_group.get_end_effector_link())

    print("==== Printing current robot state")
    print(robot.get_current_state())
    print("")

    print("==== Available Planning Groups:", robot.get_group_names())
    print("")

    print("==== Printing current robot pose")
    print(move_group.get_current_pose().pose)
    print("")

    
def main():
    try:
        print("")
        print("----------------------------------------------------------")
        print("Franka Control Interface and MoveIt! Demo")
        print("----------------------------------------------------------")
        print("Press Ctrl-D to exit at any time")
        print("")
        
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('pipeline', anonymous=True)
        robot = moveit_commander.RobotCommander()
        move_group = moveit_commander.MoveGroupCommander(GROUP_NAME)

        # Get basic information
        getBasicRobotData(move_group, robot)

        # Create a scene  adding collision objects
        add_collision_objects()
        
        # Move the gripper
        moveGripper(0.08, 0.3)
        # Execute the plan
        executePlan(move_group, robot, 0.2, 0.0, -0.2)
        # Execute the plan
        executePlan(move_group, robot, 0.0, 0.0, -0.1)
        # Move the gripper
        moveGripper(0.0, 0.3)
        # Execute the plan
        executePlan(move_group, robot, 0.0, 0.0, 0.3)
        # Execute the plan
        executePlan(move_group, robot, -0.3, -0.7, 0.1)
        # Move the gripper
        moveGripper(0.08, 0.3)
        

        print("Demo complete!")
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()