"""
In here we store the constants for configuration of the Robot or the
virtual environment
"""

EXECUTION_TIME = 0.4 # Time that the robot takes to execute an action
OBSERVATION_FILE = 'env_observation' # Name of the file where we get the response of the simulation


"""
Training Configuration data
"""
IMAGE_SIZE = (800, 800)
SQUARE_SIZE_X = 225
SQUARE_SIZE_Y = 470 + 25

STEP_X = 10
STEP_Y = 20
ERROR = 150
MAX_X = int(((IMAGE_SIZE[0] - SQUARE_SIZE_X) / STEP_X) + 1)
MAX_Y = int(((IMAGE_SIZE[1] - SQUARE_SIZE_Y) / STEP_Y) + 1)
NB_STATES = MAX_X*MAX_Y

def show_parameters():
    print(f'STEP_X={STEP_X}\n'\
            f'STEP_Y={STEP_Y}\n'\
            f'MAX_X={MAX_X}\n'\
            f'MAX_Y={MAX_Y}\n'\
            f'NB_STATES={NB_STATES}')