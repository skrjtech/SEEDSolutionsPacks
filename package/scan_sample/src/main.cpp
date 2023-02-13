#include <stdio.h>
#include <ros/ros.h>
#include <scan_sample/laser_callback.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "scan_sample");
    ros::NodeHandle nh;
    ros::Subscriber sub1 = nh.subscribe("/scan", 1000, LaserScanCallBack);
    ros::spin();
    return 0;
}