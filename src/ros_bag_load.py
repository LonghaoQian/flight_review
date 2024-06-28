import rosbag
from bagpy import bagreader
import csv
from nav_msgs.msg import Odometry
import pandas as pd
import os
import sys

if __name__ == "__main__":
    bagfileName = "yaw_test2.bag"
    bagfileDir = "data/"
    fileName = os.path.dirname(os.path.abspath(sys.argv[0])) + "/../" + bagfileDir + bagfileName
    # read odometry info
    with rosbag.Bag(fileName, 'r') as bag:
        info = bag.get_type_and_topic_info()
        numOfInfo = len(info)
        # topic in info 0
        topic0 = list(info[0].keys())
        topic1 = list(info[1].keys())
        print("------message types-------")
        for x in topic0:
            print(x)
        print("------topics-------")
        for x in topic1:
            print(x)
        bag2 = bagreader(bagfileDir + bagfileName)

    topicList = ['/mavros/imu/data',
                 '/state_estimator/local_position/odom/UAV0',
                 '/tracking_controller/output_data',
                 '/tracking_controller/setpoint_pos_error',
                 '/tracking_controller/setpoint_vel_error',
                 '/tracking_controller/target',
                 '/tracking_controller/acc_setpoint',
                 '/mocap/UAV0',
                 '/tracking_controller/ude_estimate']
    for topic in topicList:
        bag2.message_by_topic(topic)
