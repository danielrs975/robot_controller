'''
Contains the necessary code to control bebop 2
'''
import roslibpy

class Bebop():
    '''
    Constructor
    '''
    def __init__(self, client):
        # This topic modify the angular speed of the rotors
        self.motors_speeds_topic = roslibpy.Topic(client, '/command/motor_speed', 'mav_msgs/Actuators')

    '''
    Method to take off the drone
    '''
    def takeoff(self):
        pass

    '''
    Method to land the drone
    '''
    def land(self):
        pass