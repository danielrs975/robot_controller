'''
Contains the necesary code to move a robot
in a 2D space
'''
import roslibpy
import time

EXECUTION_TIME = 1 # Time between each command (seconds)

'''
Array that contains all the posible movements of the robot, now it is only 4

           y  ^ 3
              |
              |
              |
    0         |          1
    --------------------->
              |         x
              |
              |
              | 2
            
These are the posible movements: (The numbers representes the index in the array)
    0 left
    1 right
    2 backwards
    3 forward
'''
POSSIBLE_MOVES = [
    {
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
    },
    {
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
    },
    {
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
    },
    {
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