# NavGuide
## About

NavGuide is a device that primarily aims to assist visually challenged people while navigating through new and dynamic environments. Our project focuses on road-crossing scenarios since visually challenged individuals find it the most difficult to cope with. Unlike existing solutions in the literature which use resource-demanding SLAM-based techniques, our algorithm is computationally efficient and fast. NavGuide works based on a framework which depends on a stereo camera for perception of the surroundings. The device contains haptic actuators to give the required feedback to the user. 

## Framework
### Methodology
<p align="center">
<img src="img/methodology.png" style="height: 600px; width: 300px;"/>
</p>

#### Step 1
First step is to detect the crosswalk. We do it by training a Haar Cascade classifier. The crosswalk is detected in the image frame along with its four corner points. 

#### Step 2
The second step is to orthorectify the image in which the crosswalk was detected. It can be done by applying a homography transformation. The homography transformation matrix is automatically computed by OpenCV given the points (and the location to which the points must be transformed) which need to be transformed from the perspective image plane to orthogonal world plane. Generally, a homography transformation matrix is the product of camera intrinsic and extrinsic matrices. The equation below shows the equation of transformation. 
<p align="center">
<img src="img/homography_equation.png" style="height: 100px; width: 185px;"/>
</p>
Here s is the scaling, H is the homography matrix, x' and y' are transformed points, x and y are points that need to be transformed. Once H has been computed, it can be appled to the entire image frame to produce a new orthorectified image plane. The image below illustrates the same. 
\
&nbsp;

![1](img/1.png)





