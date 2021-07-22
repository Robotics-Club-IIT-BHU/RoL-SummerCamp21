import numpy 
import gym
import gym_robot
import time

if __name__=="__main__":
    env = gym.make("gym_robot-v0")
    env.reset()
    while True:
        # action= select random action from your action space
        env.step(action)