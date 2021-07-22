### Creating a custom gym environment

This week's task includes creating a full fleged OpenAI gym environment, which can be directly installed as a PIP package from the terminal. OpenAI gym already has a lot of environments ranging from classic control ones to Atari games like Breakout, Pacman, Pong etc. However, you will be creating your own environment from scratch and training a robot in that using the algorithms learnt this week.

Before diving into the environment description, lets see the basic components in any gym enironment. So, every gym environment has the following file structure:

```
gym-robotics/
  setup.py
  gym_robot/
    __init__.py
    envs/
      __init__.py
      robot_env.py
```
Note: Here the names can be anything you which but make sure that you use consistent names in the files given below, otherwise it will give an error.

`setup.py` contains our environment details like name,version and its dependencies:

```
from setuptools import setup

setup(name='gym_name',
      version='0.0.1',
      install_requires=['gym', 'pybullet']
)
```

`gym_robot/__init__.py` contains the package registry information given below:

```
from gym.envs.registration import register

register(id='packagename-v0', entry_point='gym_robot.envs:RoBots')
```
`envs/__init__.py` will contain the following import statement:
```
from gym_robot.envs.robot_env import Robots
```

The main environment is defined in `envs/robot_env.py`.

### Environment Description

You will be creating an environment for training a 2 wheeled bot, known as Turtle Bot to balance for as long as possible without falling. You need to formulate this problem as Markov Decision Process and make an environment to train your bot. Tinker with the urdf, see what commands you give and what happens, and then accordingly try to build an environment which can make the robot self balance on its own. Here, you yourself don't have to code how to self balance the bot. You just have to define the state space, action space, reward, and the functions given below, so that on, seeing all this the algorithm can train your bot.

Below is the starter code, stating the methods that shoud be there in your env and loads the turtle bot URDF provided:

```
import gym
from gym import error, spaces, utils
import pybullet as p
import pybullet_data

class RoBots(gym.Env):

  def __init__(self):
    self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    ...

  def step(self, action):
    ...

  def reset(self):
    p.resetSimulation()
    p.setGravity(0, 0, -9.8)
    p.setTimeStep(0.01)
    planeId = p.loadURDF("plane.urdf")
    cubeStartPos = [0, 0, 0.001]
    cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
    path = os.path.abspath(os.path.dirname(__file__))
    self.botId = p.loadURDF(os.path.join(path, "balancebot_simple.urdf"), cubeStartPos, cubeStartOrientation)
    ...

  def render(self, mode='human'):
    pass
```

The main task of creating the environment can be further broken down as:

- Defining an appropriate observation space that provides the information required to make a decision(take a certain action). Hint: The robot's orientation can be a crucial factor to determine its state for balancing.
- Defining an action space for the robot
- Defining a reward function, that gives the robot appropriate feedback of its performance and helps it acheive the target behaviour of balancing. Make it an episodic task with each episode lasting 200s.
- Implementing the actions in your action space, using `p.setJointMotorControl2(...)`

After creating you environment, go to the main directory of the environment and run the following command in the terminal to install the package:
~~~
pip install -e package_name
~~~

The last stage involves testing out your environment using the `gym_test.py` which would send random actions to the agent, so that you can observe its behaviour and the reward. You can modify the file based on your action space so that its sends legitimate actions to the robot.
