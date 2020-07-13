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
    Move to the left the robot for 2 seconds and then stop
    '''
    def move_left(self):
        left = {
            'linear': {
                'y': 1.0, 
                'x': 0.0, 
                'z': 0.0
            }, 
            'angular': {
                'y': 0.0, 
                'x': 0.0, 
                'z': 0.0
            }
        }
        self.move_topic.publish(roslibpy.Message(left))
        time.sleep(2)
        self.move_topic.publish(roslibpy.Message(self.STOP))
        time.sleep(2)

    '''
    Move the robot to the right
    '''
    def move_right(self):
        right = {
            'linear': {
                'y': -1.0, 
                'x': 0.0, 
                'z': 0.0
            }, 
            'angular': {
                'y': 0.0, 
                'x': 0.0, 
                'z': 0.0
            }
        }
        self.move_topic.publish(roslibpy.Message(right))
        time.sleep(2)
        self.move_topic.publish(roslibpy.Message(self.STOP))
        time.sleep(2)

    '''
    Move the robot backwards
    '''
    def move_backward(self):
        backward = {
            'linear': {
                'y': 0.0, 
                'x': -1.0, 
                'z': 0.0
            }, 
            'angular': {
                'y': 0.0, 
                'x': 0.0, 
                'z': 0.0
            }
        }
        self.move_topic.publish(roslibpy.Message(backward))
        time.sleep(2)
        self.move_topic.publish(roslibpy.Message(self.STOP))
        time.sleep(2)

    '''
    Move the robot forward
    '''
    def move_forward(self):
        forward = {
            'linear': {
                'y': 0.0, 
                'x': 1.0, 
                'z': 0.0
            }, 
            'angular': {
                'y': 0.0, 
                'x': 0.0, 
                'z': 0.0
            }
        }
        self.move_topic.publish(roslibpy.Message(forward))
        time.sleep(2)
        self.move_topic.publish(roslibpy.Message(self.STOP))
        time.sleep(2)

    '''
    Remove the listeners to the topics of the robot
    '''
    def remove_subscribers(self):
        self.move_topic.unadvertise()