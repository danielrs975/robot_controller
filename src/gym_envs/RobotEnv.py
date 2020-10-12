'''
Gym environment for the Teresa robot
ToDo: 
    - Define what are the states/observations
'''
import cv2
import gym
from gym import spaces
import numpy as np
import os
import time
from src.utils.global_variables import OBSERVATION_FILE, 
from src.utils.useful_functions import is_modified


import time

class RobotEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    IMAGE_SIZE = (800, 800)
    ERROR = 150
    SPACE_REWARD_X = IMAGE_SIZE[0] // 2 - ERROR
    SPACE_REWARD_Y = IMAGE_SIZE[1] // 2 + ERROR

    SQUARE_SIZE_X = 225 # This is the step in the X axis
    SQUARE_SIZE_Y = 470 +25 # This is the step in the Y axis

    STEP_X = 1 # It moves the square 20 pixeles in the X axis
    STEP_Y = 1 # It moves the square 40 pixeles in the Y axis

    MAX_X = int(((IMAGE_SIZE[0] - SQUARE_SIZE_X) / STEP_X) + 1)
    MAX_Y = int(((IMAGE_SIZE[1] - SQUARE_SIZE_Y) / STEP_Y) + 1)
    NB_STATES = MAX_X*MAX_Y
    
    '''
    Explanation of the observation space
    It consists of four important values
    Type: Box(4)
                            
            Graphical Representation of the
                    Observation Space
                           800
                 ________________________
                |           | top        |
                |          _|_           |
                |_________|   |__________|
            800 |    left |___|    right |
                |           |            |
                |           | bottom     |
                |           |            |
                |           |            |
                |___________|____________|
    '''
    def __init__(self, robot):
        super(RobotEnv, self).__init__()
        self.robot = robot
        self.state = 0
        self.action_space = spaces.Discrete(robot.NUMBER_MOVEMENTS)

        if os.path.exists(OBSERVATION_FILE):
            self.old_file = os.stat(OBSERVATION_FILE).st_mtime
        else:
            self.old_file = -1

    def pos_to_state(self, x, y):
        new_col = int(x / self.STEP_X)
        new_row = int(y / self.STEP_Y)
        return int(new_col + new_row*self.MAX_X)

    def state_to_pos(self):
        state = self.state
        return int(self.STEP_Y*(state // self.MAX_X)), int(self.STEP_X*(state % self.MAX_X))

    def face_in_place(self, x, y, w, h):
        '''
        Method that calculates if the object is in the desire position
        Parameters:
        -   x (Float) --> x coordinate of the object position
        -   y (Float) --> y coordinate of the object position
        Returns
        -   True  --> if the face is in place
        -   False --> otherwise
        '''
        point_a = (x, y)
        point_b = (x + w, y + h)
        if (point_a[0] >= self.SPACE_REWARD_X and point_a[0] <= self.SPACE_REWARD_Y):
            return True
        return False

    def step(self, action):
        reward = 0 # Reward of the state
        done = 0 # Boolean that indicates that an episode has finished

        # Execute move
        self.robot.move_robot(action)
        
        '''
        In here we identify if the object we want to follow is in sight or no. This is
        used to calculate the reward
        '''
        time_passed = 0
        while not os.path.exists(OBSERVATION_FILE) or not is_modified(self.old_file, os.stat(OBSERVATION_FILE).st_mtime): # Wait until the file exists
            time.sleep(1)
            if time_passed == 30:
                break
            time_passed += 1

        self.old_file = os.stat(OBSERVATION_FILE).st_mtime # In here we get the time we got the picture

        # image = face_recognition.load_image_file(OBSERVATION_FILE) # TODO: This part executes before an image is saved. Think how to correct it.
        # face_locations = face_recognition.face_locations(image)
        body_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_fullbody.xml')
        image = cv2.imread(OBSERVATION_FILE)
        face_locations = body_classifier.detectMultiScale(image, 1.2, 3)
        if len(face_locations) > 0:
            x, y, w, h = face_locations[0]
            # self.SQUARE_SIZE_X = w
            # self.SQUARE_SIZE_Y = h

            # self.encode_pos(x, y)
            # self.state = self.encode_pos(x, y, w, h)

            self.state = self.pos_to_state(x, y)

            print("State is: " + str(self.state))
            print("Coordinates image: " + str(x) + " " + str(y))

            #-------------The code below will change
            if self.face_in_place(x, y, w, h):
                reward = 1
                done = 1
            else:
                reward = 0
            #----------------------------------------
        else:
            self.state = self.pos_to_state(0, 0)
            done = 1
            reward = 0
        return self.state, reward, done, {}

    def reset(self):
        self.robot.reset_simulation()
        self.state = self.pos_to_state(0, 0)
        self.last_u = None

        return self.state

    def render(self, mode='human'):
        image = cv2.imread(OBSERVATION_FILE)
        window_name = 'image'
        # x, y = self.decode_pos() # Replace this by the actual square position
        
        # (x, y, w, h) = self.decode_pos()
        x, y = self.state_to_pos()
        w = self.SQUARE_SIZE_X
        h = self.SQUARE_SIZE_Y

        cv2.rectangle(image, (x, y), (x+w, y+h), (25, 125, 225), 5)
        
        # color = (255, 0, 0)

        # thickness = 2

        # Replace 800 with size of the image and 50 with range you want
        #           height width
        error = 150
        # space_reward = (self.SPACE_REWARD_X, self.SPACE_REWARD_Y)

        # cv2.rectangle(image, (space_reward[0], 0), (space_reward[1], 800), (255, 0, 0), 5)
        # image = cv2.rectangle(image, space_reward, (space_reward[0] + 50, space_reward[1] + 50), (0, 0, 255), thickness)

        cv2.imshow(window_name, image)
        value = 5
        imgcpy = image.copy()

        img = cv2.resize(imgcpy, None, fx=0.5, fy=0.5)
        cv2.imshow(window_name, image)
        
        cv2.waitKey(1)
        # cv2.destroyAllWindows()
        return 0

    def close(self):
        pass
