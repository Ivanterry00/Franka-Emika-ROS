#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def publish_desired_position(x, y, z, qx, qy, qz, qw):
    rospy.init_node('publish_desired_position_node', anonymous=True)
    
    # Creazione del publisher per pubblicare sulla posizione desiderata
    pub = rospy.Publisher('/cartesian_impedance_example_controller/equilibrium_pose', PoseStamped, queue_size=10)
    
    # Creazione di un messaggio PoseStamped
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "fr3_link0"  # Imposta il frame_id a "base_link" o a un altro valore appropriato
    
    # Assegna le coordinate alla posizione
    pose_msg.pose.position.x = x
    pose_msg.pose.position.y = y
    pose_msg.pose.position.z = z
    
    # Assegna gli angoli come quaternioni
    pose_msg.pose.orientation.x = qx
    pose_msg.pose.orientation.y = qy
    pose_msg.pose.orientation.z = qz
    pose_msg.pose.orientation.w = qw
    
    # Pubblica il messaggio
    pub.publish(pose_msg)
    
    rospy.loginfo(f"Pubblicata posizione desiderata su /cartesian_impedance_example_controller/equilibrium_pose: (x={x}, y={y}, z={z}), quaternioni=(x={qx}, y={qy}, z={qz}, w={qw})")

if __name__ == '__main__':
    try:
        # x = float(input("Inserisci la coordinata x: "))
        # y = float(input("Inserisci la coordinata y: "))
        # z = float(input("Inserisci la coordinata z: "))
        # qx = float(input("Inserisci il valore x del quaternione: "))
        # qy = float(input("Inserisci il valore y del quaternione: "))
        # qz = float(input("Inserisci il valore z del quaternione: "))
        # qw = float(input("Inserisci il valore w del quaternione: "))
        
        publish_desired_position(0.5, 0.5, 0.3, 0, 0, 0, 1)
    except ValueError:
        rospy.logerr("Errore: Assicurati di inserire coordinate e quaternioni validi (numeri)")
    except rospy.ROSInterruptException:
        pass
