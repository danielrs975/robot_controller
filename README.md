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
#### Prerequisites
Before running this environment we have to install all the controllers of the Teresa Robot, executes ```./install_teresa.sh```. 

IMPORTANT: 
- Be sure to have the packages ```teresa-driver``` and ```teresa_gazebo``` in your home directory.
- Activate the environment that contains teresa with ```source ~/teresa_ws/devel/setup.bash```


#### Executing the simulation
This has to be in 4 different terminals (Wait until each of the first 3 commands finish to execute the last one):
1) First terminal ```roscore```
2) Second terminal: ```roslaunch teresa_gazebo teresa_gazebo_mopomdp.launch```
3) Third terminal: ```roslaunch rosbridge_server rosbridge_websocket.launch```
4) Fourth terminal: ```python src/main_giraff.py```

## Author
- Daniel Rodriguez