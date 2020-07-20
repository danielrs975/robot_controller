'''
The main of the program to control the robot. For now
this software only controls the simulation robot.
'''
import olympe
import logging
import time
from robots.bebop import Bebop # Importing Bebop controller

# Print important information (Debug purpose only)
fmt = "%(asctime)s %(levelname)8s: %(message)s"
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

# Constants
DRONE_IP = "10.202.0.1"

if __name__ == '__main__':
    client = olympe.Drone(DRONE_IP)
    bebop_controller = Bebop(client)
    

    bebop_controller.takeoff()
    bebop_controller.take_photo()
    bebop_controller.land()
    # move_selected = int(input('Select a move (0-left, 1-right, 2-backward, 3-forward) and press enter or exit (e): '))
    # bebop_controller.move_robot(move_selected)

    # disconnect_of_ros(bebop_controller, client)
    print('Exiting the robots controller')