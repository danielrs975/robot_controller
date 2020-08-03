'''
The main of the program to control the robot. For now
this software only controls the simulation robot.
'''
import logging
import time
import roslibpy
import numpy as np
from gym_envs.RobotEnv import RobotEnv
from robots.Bebop import Bebop # Importing Bebop controller

# Print important information (Debug purpose only)
fmt = "%(asctime)s %(levelname)8s: %(message)s"
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

# Constants
PORT = 9090
HOST = 'localhost'

"""
Make connection to ROS Server
return client ----> it is the socket connection
"""
def connect_to_ros():
    client = roslibpy.Ros(host=HOST, port=PORT)
    return client

"""
Disconnect from the ROS Server
"""
def disconnect_of_ros(robot, client):
    robot.remove_subscribers()
    client.close()

if __name__ == '__main__':
    client = connect_to_ros()
    bebop_controller = Bebop(client)
    client.run()
    env = RobotEnv(bebop_controller)
    bebop_controller.takeoff()
    type_of_control = int(input('Introduce type of control for the robot (0.- Manual, 1.- Automatic): '))

    bebop_controller.takeoff()
    if (type_of_control == 0):
        while True:
            move_selected = input('Select a move (0-rotate right, 1-rotate left, 2-backward, 3-forward, 4-left, 5-right, 6-up, 7-down) and press enter or exit (e): ')
            if (move_selected == 'e'):
                bebop_controller.land()
                break
            move_selected = int(move_selected)
            bebop_controller.move_robot(move_selected)
            env.render()
    else:
        for i in range(100):
            env.step(np.random.randint(4))
            env.render()

    

    # disconnect_of_ros(bebop_controller, client)
    print('Exiting the robots controller')