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

### Set up
1) Clone this repository.
2) Enter the folder with the project and create a folder inside called ```venv```
3) Create a virtual environment with the ```virtualenv``` command. Example: ```virtualenv --python=python3 venv/```
4) Activate the environment. ```source venv/bin/activate```
5) Install ```roslibpy```. ```pip install roslibpy```

## Author
- Daniel Rodriguez