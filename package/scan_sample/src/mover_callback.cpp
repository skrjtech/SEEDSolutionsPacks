#include "scan_sample/mover_callback.h"
#include <tf/transform_listener.h>

void MoverCallBack(void) {
    tf::TransformListener listener;
    tf::StampedTransform transform;
    listener.waitForTransform("/odom", "/base_link", ros::Time(0), ros::Duration(0.5));
    listener.lookupTransform("/odom", "/base_link", ros::Time(0), transform);
    ROS_INFO("ROBOT X %3.4f Y %3.4f YOW %3.4f", transform.getOrigin().x(), transform.getOrigin().y(), tf::getYaw(transform.getRotation()));
}