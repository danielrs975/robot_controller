"""
In here we store the constants for configuration of the Robot or the
virtual environment
"""

from src.utils.useful_functions import calculate_center

EXECUTION_TIME = 0.4 # Time that the robot takes to execute an action
OBSERVATION_FILE = 'env_observation' # Name of the file where we get the response of the simulation


"""
Training Configuration data
"""
IMAGE_SIZE = (800, 800)
SQUARE_SIZE_X = 225
SQUARE_SIZE_Y = 470 + 25

SPACE_REWARD_POINT_1 = (194, 123)
SPACE_REWARD_POINT_2 = (614, 700)

STEP_X = 10
STEP_Y = 20
ERROR = 100
MAX_X = int(((IMAGE_SIZE[0] - SQUARE_SIZE_X) / STEP_X) + 1)
MAX_Y = int(((IMAGE_SIZE[1] - SQUARE_SIZE_Y) / STEP_Y) + 1)
NB_STATES = MAX_X*MAX_Y

def pos_to_state(x, y):
        """Transform a coordinate into a single integer

        Args:
            x (Integer): X coordinate
            y (Integer): Y coordinate

        Returns:
            Integer: Representation of the position
        """
        new_col = int(x / STEP_X)
        new_row = int(y / STEP_Y)
        return int(new_col + new_row*MAX_X)

def state_to_pos(state):
        """Tranform the single integer into the original coordinates
        x and y

        Returns:
            List: a list containing the two coordinates
        """
        return int(STEP_X*(state % MAX_X)), int(STEP_Y*(state // MAX_X))

def in_range(x,y,z):
        if x>y-z and x<y+z:  
            return True
        return False


def show_parameters():
    print(f'STEP_X={STEP_X}\n'\
            f'STEP_Y={STEP_Y}\n'\
            f'MAX_X={MAX_X}\n'\
            f'MAX_Y={MAX_Y}\n'\
            f'NB_STATES={NB_STATES}')


FINAL_X, FINAL_Y = calculate_center(IMAGE_SIZE, SQUARE_SIZE_X, SQUARE_SIZE_Y)