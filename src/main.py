'''
The main of the program to control the robot. For now
this software only controls the simulation robot.
'''
import roslibpy
import logging
import time
from robots.giraff import Giraff # Importing giraff

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
    giraff_controller = Giraff(client)

    client.run() # Running the main loop
    while client.is_connected:
        '''
        Accept input from the user
        '''
        move_selected = input('Select a move (l-left, r-right, b-backward, f-forward) and press enter or exit (e): ')
        if move_selected == 'e':
            break
        elif move_selected == 'l':
            giraff_controller.move_left()
        elif move_selected == 'r':
            giraff_controller.move_right()
        elif move_selected == 'b':
            giraff_controller.move_backward()
        elif move_selected == 'f':
            giraff_controller.move_forward()
        else:
            print('Invalid movement try again')

    disconnect_of_ros(giraff_controller, client)
    print('Exiting the robots controller')
    