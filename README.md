# SCRB_Software_IntroTask
# Your First Task: GitHub + ROS2 Packages

To help you get hands-on and reinforce the basics, we’d like you to complete this
introductory task. It will give you practice with ROS2, GitHub, and both C++ and Python
development. Feel free to use any of the videos/documentation found above!

## Here’s what you need to do:

**1.​ Create a new GitHub repository​**
     This is where you’ll upload your code for this task and future personal practice.
     Make it public or private — up to you!
     
**2.​ Set up a new ROS2 workspace​**
     Use either your virtual machine or your local Linux setup (Ubuntu 22.04). Make
     sure the workspace builds and sources correctly.
     
**3.​ Inside that workspace, create two packages:**
       ○​ A Python package (using ament_python)
       ○​ A C++ package (using ament_cmake)
       
**4.​ Implement a simple publisher and subscriber in each package**
       ○​ You could do anything you'd like! For example: have the publisher send a
       string like "Hello from ROS2!" and have the subscriber print it to the
       terminal.
       
**5.​ Build your workspace and test your nodes​**
     Make sure they work using ros2 run or by launching them together.
     
**6.​ Push everything to your GitHub repo​**
     Be sure to commit your src/, CMakeLists.txt, package.xml, and any
     launch or config files you make.

If you're ever unsure about anything, don’t hesitate to ask questions — everyone here
started somewhere, and we're all learning together.

*SOURCE: [SCRB Software Intro Task Guideline](SCRB_Software_Intro%20Task%20Guideline.pdf)*

<a href="https://spaceconcordia.ca/robotics">
  <img src="Robotics_logo_SCRB.webp" width="150" alt="Space Concordia Robotics Logo">
</a>

---

## How to Launch the Publisher/Subscriber Nodes in C++

1. Clone the repository into a workspace, you can name it *IntroTask*.

2. Open a linux terminal, head towards the root workspace *IntroTask* and check for missing 																	dependencies by typing:
	'rosdep install -i --from-path src --rosdistro humble -y'
3. On the same terminal and same workspace 'IntroTask', build the new package by typing:
	'colcon build --packages-select cpp_task'
4. Open 2 new terminals, both navigate into 'IntroTask' and for each new terminal, source the setup files by typing:
	'. install/setup.bash' or 'source install/setup.bash'
5. Run the talker node on the first new terminal by typing:
	'ros2 run cpp_task talker'
6. Run the listener node on the second new terminal by typing:
	'ros2 run cpp_task listener'
7. Voila! The Publisher and Subscriber have been implemented.

---

## How to Launch the Publisher/Subscriber Nodes in Python 🐍

1. Clone the repository into a workspace, you can name it *IntroTask*.

2. Open a linux terminal, head towards the root workspace *IntroTask* and check for missing 																	dependencies by typing:
	'rosdep install -i --from-path src --rosdistro humble -y'
3. On the same terminal and same workspace 'IntroTask', build the new package by typing:
	'colcon build --packages-select py_task'
4. Open 2 new terminals, both navigate into 'IntroTask' and for each new terminal, source the setup files by typing:
	'. install/setup.bash' or 'source install/setup.bash'
5. Run the talker node on the first new terminal by typing:
	'ros2 run py_task talker'
6. Run the listener node on the second new terminal by typing:
	'ros2 run py_task listener'
7. Voila! The Publisher and Subscriber have been implemented.




