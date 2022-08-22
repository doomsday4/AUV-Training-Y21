Assignment 2

1. Created a workspace for working, catkin_ws.
2. Created a package "demo-gazebo" using the catkin_make command.
3. Used the roslaunch command to launch an empty world in gazebo.
4. Created a launch folder within the package to add the launch and the world files.
5. We create a test.launch file within the launch folder, name the our world as "world".
6. We now create a world folder within the package and create a test.world file within this folder.
7. We can edit this world file to include our requirements.
8. We then create a custom model by creating a folder named "models" in the package, then further adding the model folder in it, which contains the .sdf and the .config files.
9. We then edit the .launch and the .world files accordingly to add the custom model.
10. Then use the catkin_make command to compile the codes.
11. To add the custom physics solver, we edit the world file and add the 'world' solver. I've also added some constraints and the max_step_size parameters.
12. To spawn the robot, we first git clone the package of the robot. Here, i've used the Two-wheeled robot, 'm2wr'.
13. We then modify the launch file to include the robot model node.
14. Then we compile the files using catkin_make, source the code and spawn the robot in our world.
15. The .xacro file in the udrf folder allows us to use topics and msgs to move our robot.
16. We then use the cmd/vel method to move the robot.
17. Then we use the teleop method to configure the robot through the keyboard.

To Run the code:
1. roslaunch demo-gazebo test.launch
2. Then on a new terminal, use the cmd/vel command to move the robot, eg- rostopic pub /cmd_vel geometry_msgs/Twist -- '[1.0,0.0,0.0]' '[0.0,0.0,0.0]'
3. Now, use the teleop command to use the keyboard to steer the robot, rosrun teleop_twist_keyboard teleop_twist_keyboard.py

Assignment 3

1. First, we create a new package in the same directory, by the name 'navigation'. For the dependencies, i've used std_msgs, rospy and roscpp.
2. Then we use the catkin_make command and source the generated setup file to add the package to our environment.
3. Now we add the laser sensor to our robot, by adding a link in the .xacro file and also a joint. I also added a macro in the macros.xacro file of the robot. 
4. I then launched the robot on rviz, adjusted the robot model and then created the rviz folder in the launch folder of the robot.
5. Then we add the camera sensors, creating the links and the joints in the xacro file for 2 cameras in the front and 1 in the rear side. I've used rectangular boxes as the cameras here.
6. I then edit the names and the orientation of the cameras so that i can get all the views that i want. Camera1(rear view), Camera2(front-left[pi/8] view) and Camera3(front-right[-pi/8] view).
7. Add the plugins in .gazebo files as three separate cameras by adjusting the references and simulate on gazebo and rviz simultaneously to get the image. We can see all the 3 views in different windows.
8. Now, I added the IMU sensor using a similar process.
9. Added the gmapping node in the rviz launch file of the robot and used the laser to visualise the world using the map.

Video Link- https://www.youtube.com/watch?v=b3E1uNyxU4E
