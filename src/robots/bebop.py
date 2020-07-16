'''
Contains the necessary code to control bebop 2
'''
import roslibpy
import time
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
        iteration = 0
        step = 10
        msg = {
            'angular_velocities': [0, 0, 0, 0]
        }
        iter = 0
        while iter < 1000:
            self.motors_speeds_topic.publish(msg)
            time.sleep(1)
            idx = 0
            print('Increasing speed of rotors {}'.format(msg['angular_velocities']))
            for _ in enumerate(msg['angular_velocities']):
                msg['angular_velocities'][idx] += step
                idx += 1
            iter += 1

    '''
    Method to land the drone
    '''
    def land(self):
        pass