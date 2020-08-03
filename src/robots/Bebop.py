"""
Contains the necessary code to control bebop 2
"""
from robots.Robot import Robot
from robots.actions.move import execute_move
from robots.actions.camera import take_picture

# To control the bebop simulation the following topic is used
#   /bebop/command/trajectory

def create_msg(position):
    return {
        'points': [
            {
                'transforms': [
                    {
                        'translation': position
                    }
                ]
            }
        ]
    }

class Bebop(Robot):
    """
    Class that represents the Bebop 2 Power Drone
    """
    STEP_FOR_MOVEMENT = 0.20
    POSSIBLE_MOVES = []

    POSITION = {
        'x': 0.0,
        'y': 0.0,
        'z': 0.0
    }
    ANGULAR_POSITION = {
        'x': 0.0,
        'y': 0.0
    }
    MOVE_TOPIC = {
        'topic_name': '/bebop/command/trajectory',
        'msg_type': 'trajectory_msgs/MultiDOFJointTrajectory'
    }
    NUMBER_MOVEMENTS = 6

    def __init__(self, client):
        """
        Constructor of the class
        """
        super(Bebop, self).__init__(client, '/bebop/camera1', self.MOVE_TOPIC, self.POSSIBLE_MOVES)

    def takeoff(self):
        """
        With this we can takeoff the drone
        """
        self.POSITION['z'] = 1.0
        execute_move(create_msg(self.POSITION), self.move_topic)

    def move_robot(self, move):
        """
        Overwrite the move_robot function of super class Robot to adapt
        to the Bebop 2 drone simulation
        """
        if move == 0:
            # Move left
            self.POSITION['y'] += self.STEP_FOR_MOVEMENT
        elif move == 1:
            # Move right
            self.POSITION['y'] -= self.STEP_FOR_MOVEMENT
        elif move == 2:
            # Move foward
            self.POSITION['x'] -= self.STEP_FOR_MOVEMENT
        elif move == 3:
            # Move backward
            self.POSITION['x'] += self.STEP_FOR_MOVEMENT
        elif move == 4:
            # Move up
            self.POSITION['z'] += self.STEP_FOR_MOVEMENT
        elif move == 5:
            # Move down
            self.POSITION['z'] -= self.STEP_FOR_MOVEMENT
        execute_move(create_msg(self.POSITION), self.move_topic)
        take_picture(self.camera_topic)

    def land(self):
        """
        Land the dron in the ground
        """
        self.POSITION['z'] = 0
        execute_move(create_msg(self.POSITION), self.move_topic)