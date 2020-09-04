'''
Gym environment for the Teresa robot
ToDo: 
    - Define what are the states/observations
'''
import cv2
import face_recognition
import gym
from gym import spaces
import os
from src.utils.useful_functions import is_modified

class RobotEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, robot):
        super(RobotEnv, self).__init__()
        self.robot = robot
        self.state = 0
        self.action_space = spaces.Discrete(robot.NUMBER_MOVEMENTS)
        if os.path.exists('env_observation'):
            self.old_file = os.stat('env_observation').st_mtime
        else:
            self.old_file = -1

    def encode_pos(self, x, y):
        image_size = 800
        self.state = x*image_size + y

    def decode_pos(self):
        image_size = 800
        x = self.state / image_size
        y = self.state % image_size
        return int(x), int(y)

    def step(self, action):
        reward = 0 # Reward of the state
        done = 0 # Boolean that indicates that an episode has finished

        # Execute move
        self.robot.move_robot(action)
        
        '''
        In here we identify if the object we want to follow is in sight or no. This is
        used to calculate the reward
        '''
        while not os.path.exists('env_observation') or not is_modified(self.old_file, os.stat('env_observation').st_mtime): # Wait until the file exists
            continue

        self.old_file = os.stat("env_observation").st_mtime # In here we get the time we got the picture
        
        image = face_recognition.load_image_file("env_observation") # TODO: This part executes before an image is saved. Think how to correct it.
        face_locations = face_recognition.face_locations(image)
        face_locations = [(1, 2, 3, 4)]
        if len(face_locations) > 0:
            y, _, _, x = face_locations[0]
            self.encode_pos(x, y)
        else:
            done = 1
            reward = 0

        return self.state, reward, done, {}

    def reset(self):
        self.robot.reset_simulation()
        self.state = 0
        self.last_u = None

        return self.state

    def render(self, mode='human'):
        image = cv2.imread('./env_observation')
        window_name = 'image'
        x, y = self.decode_pos() # Replace this by the actual square position

        start_point = (x, y)
        end_point = (x + 40, y + 40)

        color = (255, 0, 0)

        thickness = 2
        # center = 800 // 2
        # error = 50
        # range = center - error / 2
        # Replace 800 with size of the image and 50 with range you want
        space_reward = (375, 200)
        image = cv2.rectangle(image, start_point, end_point, color, thickness)

        image = cv2.rectangle(image, space_reward, (space_reward[0] + 50, space_reward[1] + 50), (0, 0, 255), thickness)

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
