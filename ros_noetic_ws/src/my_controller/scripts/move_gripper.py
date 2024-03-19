#!/usr/bin/env python3

import rospy
import sys
from franka_gripper.msg import MoveActionGoal, MoveGoal

def move_gripper(width, speed):
    rospy.init_node('move_gripper_node', anonymous=True)
    
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

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: rosrun your_package_name move_gripper_node.py <width> <speed>")
        sys.exit(1)

    try:
        width = float(sys.argv[1])
        speed = float(sys.argv[2])
        move_gripper(width, speed)
    except ValueError:
        print("Error: Width and speed must be numeric values")
        sys.exit(1)
    except rospy.ROSInterruptException:
        pass