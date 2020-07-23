'''
Contains the necesary code to move a robot
in a 2D space
'''
import roslibpy
import time

EXECUTION_TIME = 1.5 # Time between each command (seconds)
LINEAR_SPEED = 0.5
ROTATION_SPEED = 1.0

'''
Array that contains all the posible movements of the robot, now it is only 4

           y  ^ 3
              |
              |
              |
    1         |          0
    --------------------->
              |         x
              |
              |
              | 2
            
These are the posible movements: (The numbers representes the index in the array)
    0 rotate right
    1 rotate left
    2 backwards
    3 forward
'''
POSSIBLE_MOVES = [
    # Rotate Right
    {
        'linear': {
            'y': 0.0, 
            'x': 0.0, 
            'z': 0.0
        }, 
        'angular': {
            'y': ROTATION_SPEED, 
            'x': ROTATION_SPEED, 
            'z': ROTATION_SPEED
        }
    },
    # Rotate Left
    {
        'linear': {
            'y': 0.0, 
            'x': 0.0, 
            'z': 0.0
        }, 
        'angular': {
            'y': -ROTATION_SPEED, 
            'x': -ROTATION_SPEED, 
            'z': -ROTATION_SPEED
        }
    },
    # Move Backward
    {
        'linear': {
            'y': 0.0, 
            'x': -LINEAR_SPEED, 
            'z': 0.0
        }, 
        'angular': {
            'y': 0.0, 
            'x': 0.0, 
            'z': 0.0
        }
    },
    # Move Forward
    {
        'linear': {
            'y': 0.0, 
            'x': LINEAR_SPEED, 
            'z': 0.0
        }, 
        'angular': {
            'y': 0.0, 
            'x': 0.0, 
            'z': 0.0
        }
    }
]

STOP_ROBOT = {
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
Tranform the command receives through user input into a ROS msg. Specifically
to a message of type geometry_msgs/Twist
'''
def get_move_msg(move):
    return POSSIBLE_MOVES[move]

'''
Publish the move to the ros topic to execute it
'''
def execute_move(move, move_topic):
    move_msg = get_move_msg(move) # Get the ROS message for the move selected

    # Execute the move
    move_topic.publish(roslibpy.Message(move_msg))
    time.sleep(EXECUTION_TIME)
    move_topic.publish(roslibpy.Message(STOP_ROBOT))
    time.sleep(EXECUTION_TIME)