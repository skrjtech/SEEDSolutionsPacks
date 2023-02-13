#ifndef __LASERCALLBACK_H_
#define __LASERCALLBACK_H_

#include <nav_msgs/Odometry.h>
#include <sensor_msgs/LaserScan.h>


void OdomRobotXYCallBack(const nav_msgs::Odometry::ConstPtr &msg);
// Laser Scan CallBack
void LaserScanCallBack(const sensor_msgs::LaserScan::ConstPtr &msg);
// Laser Scan NearObject 一番近い物体との距離
void LaserScanNearObject(float *result, int *index);
// Laser Scan Center Distance 中央
void LaserSacnCenterDistance(float *result);
// Laser Scan Direction 方向
void LaserScanDirection(float *result);

#endif