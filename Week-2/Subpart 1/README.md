## Introduction to Reinforcement Learning Algorithms

A Robot Learning setup is primarily composed of two components, an agent and an environment. Then environment refers to the object that the agent is acting on, while the agent represents the RL algorithm. The environment starts by sending a state to the agent, which then based on its knowledge tries to take an action in response to that state. After that, the environment sends a pair of next state and reward back to the agent. The agent will update its knowledge with the reward returned by the environment to evaluate its last action. The loop keeps going on until the environment sends a terminal state, which results in termination or end of the episode.

### Types of RL Algorithms

**1. Model-based vs Model-free** : The model stands for the simulation of the dynamics of the environment. That is, the model learns the transition probability T(s1|(s0, a)) from the pair of current state s0 and action a to the next state s1. (This is the probability that given that the agent in a state s0, and it takes an action a0, then what is the probability that it ends up in state s1). If the transition probability is successfully learned, the agent will know how likely it is to enter a specific state, given current state and action.
If you know this transition probaility matrix, then you can easily use it to plan your policy.
   On the other hand, model-free algorithms rely on trial-and-error to update its knowledge. As a result, it does not require space to store all the combination of states and actions. You will be working on model-free algorithms in this track as model-based algorithms, tend to become impractical as the State and Action spaces grow, since learning the state transition probabilities becomes very difficult. Think of it in terms of robotics - If we consider a certain angle to be a state, then it can have infinite values since angle can be any real value in  a given range.

**2. Off Policy vs On policy** : An on-policy agent learns the value based on its current action(a) derived from the current policy, whereas its off-policy counter part learns it based on the action(a\*) obtained from another policy.

<p align="center">
   <img src="https://github.com/Terabyte17/Robot-Learning/blob/main/Week-2/Subpart%201/assets/types-of-algos.png" alt="Types of RL algos"></img>
</p>

### Q-Learning

Q-Learning is an off-policy model-free RL algorithm, which forms the building blocks for Deep Q Network. So, lets go thorugh some basic terminologies before diving deep into Q-Learning.
<br/>
**Value(V)**: It is the expected long-term return with discount from the current state, as opposed to the short-term reward R. Vπ(s) is the expected long-term return of the current state under policy π. It is a function of the current state only. It represents the average reward the agent can get from this state to the end of episode considering all actions.
<br/>
**Action Value or Q-value** : Q-value is a function of both the state and the current action a. Qπ(s, a) refers to the long-term return of the current state s, taking action a under policy π.
<br/>
**Discount(Gamma)** : This is a paramter having a value between 0 and 1, and basically decides whether the agent should try to maxiise the immediate reward(R) or the reward it collects in a long time.

Methods in Q-Learning family learn an approximator Q_theta(s,a) for the optimal action-value function, Q*(s,a). Typically they use an objective function based on the [Bellman equation](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html). This optimization is almost always performed off-policy, which means that each update can use data collected at any point during training, regardless of how the agent was choosing to explore the environment when the data was obtained. The corresponding policy is obtained via the connection between Q* and pi*: the actions taken by the Q-learning agent are given by

<p align="center">
   <img src="https://github.com/Terabyte17/Robot-Learning/blob/main/Week-2/Subpart%201/assets/q-update.png" alt="optimal policy"></img>
</p>

### DQN
DQN(Deep Q-Network) is one of the most commonly used RL algorithms and uses the Q-update step to get to the optimal Action Value function. Since, the the number of states and state transitions are extremely large, even in simple environements we use a deep neural network as a function approximator in Deep Q-Network. This neural network learns a very good approximation of the actual Q-function by interacting with the environment and getting performing the Q update at every step as mentioned below:

<p align="center">
   <img src="https://github.com/Terabyte17/Robot-Learning/blob/main/Week-2/Subpart%201/assets/q-learning.png" alt="q-update"></img>
</p>

Since we are using neural networks as approximators, and the target network is same as the learning network and is getting constatntly updated, this might lead to unstable learning at times, so DQN has some variants which tackle these problems by introducing the following improvements:
* **Target Network** : Use a different target network, that gets updated less frequently as compared to the learning network, i.e. set the target network paramters equal to the learning network parameters every 100(say) steps. This is done in Double DQN. 
* **Experience Replay** :  Experience Replay stores experiences including state transitions, rewards and actions, which are necessary data to perform Q learning, and makes mini-batches to update neural networks. This reduces correlations between experiences as they are sampled from the experience replay and increases learning speed.
* **Clipping Rewards** : Clipping large rewards and mapping them to a normalized value between +1 and -1 has often lead to faster and more stable training.

<p align="center">
   <img src="https://github.com/Terabyte17/Robot-Learning/blob/main/Week-2/Subpart%201/assets/5go13e.jpg" alt="meme"></img>
 </p>
