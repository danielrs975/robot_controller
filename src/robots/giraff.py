'''
These script contains several functions to move the robot
around
NOTE: Needs to be adapted after to the physical robot way to move
'''
import roslibpy
import time

from robots.actions.move import execute_move
'''
Class that represents the robot Giraff. This is the version 1.
'''
class Giraff():
    STOP = {
        'linear': {
            'y': 0.0, 
            'x': 0.0, 
            'z': 0.0
        }, 
        'angular': {
            'y': 0.0, 
            'x': 0.0, 
            'z': 0.0
        }
    }

    '''
    Constructor of Giraff
    '''
    def __init__(self, client):
        self.move_topic = roslibpy.Topic(client, '/cmd_vel', 'geometry_msgs/Twist')

    '''
    Move the robot in the given direction
    '''
    def move_robot(self, move):
        execute_move(move, self.move_topic)

    '''
    Remove the listeners to the topics of the robot
    '''
    def remove_subscribers(self):
        self.move_topic.unadvertise()