#!/usr/bin/env python3

import rospy
from navigation_tools.nav_tool_lib import nav_module

#from hsrlib.hsrif import HSRInterfaces
import hsrb_interface
import dynamic_reconfigure.client as reconf_client

from std_msgs.msg import Bool

robot = hsrb_interface.Robot()
whole_body = robot.get("whole_body")
omnibase = robot.get("omni_base")
omni_base = nav_module("hsr")


def callback(msg):
    print(msg)
    if msg.status == 3:
        rospy.loginfo('success')
    else: 
        rospy.loginfo('retry')


#omni_base.go_abs(2.0, 0.8, 0, 30,"pumas")
#omni_base.go_rel(-0.3, 0, 0, 30,"pumas")
reconf_base = reconf_client.Client('tmc_map_merger/inputs/base_scan/obstacle_circle')
reconf_head = reconf_client.Client('tmc_map_merger/inputs/head_rgbd_sensor/obstacle_circle')
reconf_laser_obstacle_enable = reconf_client.Client('/tmc_map_merger/inputs/head_rgbd_sensor')
reconf_depth_obstacle_enable = reconf_client.Client('/tmc_map_merger/inputs/base_scan')
reconf_laser_obstacle_enable.update_configuration({"enable": True})
reconf_depth_obstacle_enable.update_configuration({"enable": True})
state = rospy.Subscriber('/navigation/status',Bool,callback)
omni_base.go_abs(1, 0, 0, 30,"pumas")


# OBSTACLE RECONFIGURE SETTINGS
reconf_depth_obstacle_enable.update_configuration({"enable": False})
#omni_base.go_rel(0, 0, 2.0, 30, "pumas") #TODO
#omni_base.go_abs(1, 0, 2.0, 30, "pumas")
#omni_base.go_abs(1, 0, 2.0, 30, "pumas")
reconf_depth_obstacle_enable.update_configuration({"enable": True})
