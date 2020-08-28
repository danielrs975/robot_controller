# Robot Controller written in Python
## Description
It is a simple robot controller that allows to send commands to a set of robots and also extract information about the sensors. For now it only works with Gazebo simulator.
### Tools used
One library it is used to connect with the ROS Server, ```roslibpy``` ([See docs here](https://roslibpy.readthedocs.io/en/latest/reference/index.html)).
## Setting up the environment
### Prerequisites
You must have installed:
- Python 3
- ROS Melodic
- Gazebo 9
- Virtual Environment command
- Ubuntu 18.04

### Set up
1) Clone this repository.
2) Change the permissions of the ```setup_env.sh``` with the following command ```chmod +x setup_env.sh```
3) After the installation, enter the folder with the project and create a folder inside called ```venv```
4) Create a virtual environment with the ```virtualenv``` command. Example: ```virtualenv --python=python3 venv/```
5) Activate the environment. ```source venv/bin/activate```
6) Install python dependecies. ```pip install -r requirements.txt```

## Running the environments
### For the Teresa Robot
#### Prerequisites (This part is not necessary if you are running the world inside the folder gazebo_envs/)
Before running this environment we have to install all the controllers of the Teresa Robot, executes ```./install_teresa.sh```. 

IMPORTANT: 
- Be sure to have the packages ```teresa-driver``` and ```teresa_gazebo``` in your home directory.
- Activate the environment that contains teresa with ```source ~/teresa_ws/devel/setup.bash```


#### Executing the simulation
This has to be in 3 different terminals (Wait until each of the first 3 commands finish to execute the last one):
1) First terminal ```roscore```
2) Second terminal: ```rosrun gazebo_ros gazebo ./gazebo/envs/Teresa_Lightweight.world```
3) Third terminal: ```roslaunch rosbridge_server rosbridge_websocket.launch```
### For the Bebop 2 Power Drone
#### Prerequisites
To run this environment you need to install some programs:
- Sphinx Parrot-Simulator. [See instructions here](https://developer.parrot.com/docs/sphinx/installation.html)
- Bebop autonomy ros package. [See instructions here](https://bebop-autonomy.readthedocs.io/en/latest/installation.html)
- Nvidia drivers (Version 435, this is important for the simulation)

IMPORTANT:
- Be sure that you are using your nvidia graphic card. Run the command ```nvidia-settings```

#### Executing the simulation
This has to be in 5 different terminals in this order:
1) First terminal: ```roscore```
2) Second terminal: ```sudo firmwared```
3) Third terminal: ```sphinx /opt/parrot-sphinx/usr/share/sphinx/drones/bebop2.drone::with_front_cam=true::stolen_interface=```
4) Fourth terminal: ```roslaunch rosbridge_server rosbridge_websocket.launch```
5) Fifth terminal: ```roslaunch bebop_driver bebop_node.launch```

After you run these commands, execute the python script ```python src/main_bebop.py```

## Author
- Daniel Rodriguez