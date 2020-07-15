'''
The main of the program to control the robot. For now
this software only controls the simulation robot.
'''
import roslibpy
import logging
import time
from robots.bebop import Bebop # Importing giraff

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
    bebop_controller = Bebop(client)

    client.run() # Running the main loop
    while client.is_connected:
        '''
        Accept input from the user
        '''
        print('Running bebop controller')
        # move_selected = int(input('Select a move (0-left, 1-right, 2-backward, 3-forward) and press enter or exit (e): '))
        # bebop_controller.move_robot(move_selected)

    disconnect_of_ros(bebop_controller, client)
    print('Exiting the robots controller')