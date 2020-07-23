'''
The main of the program to control the robot. For now
this software only controls the simulation robot.
'''
import roslibpy
import logging
import time
import numpy as np
from robots.Teresa import Teresa # Importing Teresa
from gym_envs.teresa_env import TeresaEnv

# Print important information (Debug purpose only)
fmt = "%(asctime)s %(levelname)8s: %(message)s"
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

# Constants
PORT = 9090
HOST = 'localhost'

'''
Make connection to ROS Server
return client ----> it is the socket connection
'''
def connect_to_ros():
    client = roslibpy.Ros(host=HOST, port=PORT)
    return client

'''
Disconnect from the ROS Server
'''
def disconnect_of_ros(robot, client):
    robot.remove_subscribers()
    client.close()

if __name__ == '__main__':
    client = connect_to_ros()
    teresa_controller = Teresa(client)
    client.run() # Running the main loop
    env = TeresaEnv(teresa_controller)
    
    for i in range(100):
        env.step(np.random.randint(4))
        env.render()

    disconnect_of_ros(teresa_controller, client)
    print('Exiting the robots controller')
    