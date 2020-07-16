'''
Gym environment for the Giraff robot
ToDo: 
    - Define what are the states/observations
'''
import cv2
import gym
from gym import spaces

N_DISCRETE_ACTIONS = 4

class GiraffEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, giraff):
        super(GiraffEnv, self).__init__()
        self.giraff = giraff
        self.state = 0
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
    
    def step(self, action):
        reward = 0 # Reward of the state
        done = 0 # Boolean that indicates that an episode has finished

        # Execute move
        self.giraff.move_robot(action)
        
        '''
        In here we identify if the object we want to follow is in sight or no. This is
        used to calculate the reward
        '''

        return self.state, reward, done, {}

    def reset(self):
        self.state = ''
        self.last_u = None

        return self.state

    def render(self, mode='human'):
        image = cv2.imread('./env_observation', 0)
        window_name = 'image'

        cv2.imshow(window_name, image)
        cv2.waitKey(1)
        # cv2.destroyAllWindows()
        return 0

    def close(self):
        pass
