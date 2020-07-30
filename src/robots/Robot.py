'''
Robot Class
It contains all the common functionality
between robots
'''
import roslibpy
import time
from robots.actions.camera import take_picture
from robots.actions.move import execute_move

class Robot():
    '''
    From here all the robots are generated. This robots are caracterized for
    having a camera and a set of movements
    '''
    def __init__(self, client, camera_name, move_topic, movements):
        '''
        Constructor
        '''
        self.movements = movements
        self.camera_topic = roslibpy.Topic(client, '{}/image_raw/compressed'.format(camera_name), 'sensor_msgs/CompressedImage')
        self.move_topic = roslibpy.Topic(client, move_topic['topic_name'], move_topic['msg_type'])

    def move_robot(self, move):
        '''
        Move the robot in the given direction
        - move (type: Integer) ----> Integer define from 0 to the number of movements - 1
        '''
        execute_move(self.movements[move], self.move_topic)
        take_picture(self.camera_topic)

    def remove_subscribers(self):
        '''
        Remove the listeners to the topics of the robot
        '''
        self.move_topic.unadvertise()