import gym
import universe

env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1) # creats a local docker container

observation_n = env.reset()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
