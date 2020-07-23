'''
These script contains several functions to move the robot
around
NOTE: Needs to be adapted after to the physical robot way to move (In process)
'''
import roslibpy
import time

from robots.Robot import Robot
from robots.actions.move import execute_move
from robots.actions.camera import take_picture

class Teresa(Robot):
    NUMBER_MOVEMENTS = 4 # Movements that the robot can made
    '''
    Class that represents the robot Teresa. This is the version 1.
    '''
    def __init__(self, client):
        '''
        Constructor of Giraff
        '''
        super(Teresa, self).__init__(client, '/teresa_robot/head_camera')
        self.move_topic = roslibpy.Topic(client, '/cmd_vel', 'geometry_msgs/Twist')

    def move_robot(self, move):
        '''
        Move the robot in the given direction
        '''
        execute_move(move, self.move_topic)
        take_picture(self.camera_topic)

    def remove_subscribers(self):
        '''
        Remove the listeners to the topics of the robot
        '''
        self.move_topic.unadvertise()