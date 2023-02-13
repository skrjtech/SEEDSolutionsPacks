#include <ros/ros.h>
#include <scan_sample/laser_callback.h>
#include <scan_sample/mover_callback.h>


static sensor_msgs::LaserScan _LaserScanStructer;

// Laser Scan CallBack
void LaserScanCallBack(const sensor_msgs::LaserScan::ConstPtr &msg) {
    _LaserScanStructer = *msg;
    
    float near;
    int index;
    float center;
    float direction;
    
    LaserScanNearObject(&near, &index);
    LaserSacnCenterDistance(&center);
    LaserScanDirection(&direction);

    ROS_INFO("NEAR: %3.4f CENTER: %3.4f DIRECTION: %3.4f", near, center, direction);

    MoverCallBack();

    // code here start


    // code end 
}
// Laser Scan NearObject 一番近い物体との距離
void LaserScanNearObject(float *result, int *index) {
    int i = 0, idx = 0;
    float min = _LaserScanStructer.ranges[0];
    for ( i = 1; i < _LaserScanStructer.ranges.size(); i++) {
        if (min > _LaserScanStructer.ranges[i]) {
            min = _LaserScanStructer.ranges[i];
            idx = i;
        } 
    }
    *result = min;
    *index = idx;
}
// Laser Scan Center Distance 中央
void LaserSacnCenterDistance(float *result) {
    *result = _LaserScanStructer.ranges[_LaserScanStructer.ranges.size()/2];
}
// Laser Scan Direction 方向
void LaserScanDirection(float *result) {
    int index;
    LaserScanNearObject(result, &index);
    *result = _LaserScanStructer.angle_min + index * _LaserScanStructer.angle_max / (float)_LaserScanStructer.ranges.size();
}
