import gym
from gym import spaces
from gym.utils import seeding

class Environment(gym.Env):
    
    def __init__(self):
        """__init__ Constructor for the class

        Defines the action and observation space, 
        and the variables required by the environment.
        Also, resets the environment so that it can be used.

        """

    def step(self, action):
        """step Simulates one step of the environment

        Parameters
        ----------
        action : Can be Integer or any Real Value
            The action to take place in this step.

        Returns
        -------
        Observation, reward, done
            By done we mean, whether the episode has terminated or not.
        """

    def _get_obs(self):
        """_get_obs Returns the observation for the environment at the current timestep

        Returns
        -------
        Observation

        """

    def reset(self):
        """reset Resets the environment

        Returns
        -------
        Returns the observation after resetting the environment

        """
