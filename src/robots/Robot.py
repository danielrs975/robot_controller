'''
Robot Class
It contains all the common functionality
between robots
'''
import roslibpy
import time
from robots.actions.camera import take_picture

class Robot():

    def __init__(self, client, camera_name):
        '''
        Constructor
        '''
        self.camera_topic = roslibpy.Topic(client, '{}/image_raw/compressed'.format(camera_name), 'sensor_msgs/CompressedImage')