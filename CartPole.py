import sys
sys.path.append('/Users/doomsday69/opt/miniconda3/lib/python3.9/site-packages') #location of the package

import gym
import pygame

env = gym.make("CartPole-v1")
obs = env.reset()

k_p = 4.7
k_d = 7.2
k_i = 3.5
F = 0
integral = 0
f = 0

for i in range(200):
    env.render()
    obs, reward, done , info = env.step(f)
    angle = obs[2]
    omega = obs[3]

    integral += angle
    F = k_p*angle + k_i*integral + k_d*omega

    f = 0
    if F > 0:
        f = 1

    if done:
        obs = env.reset()
        integral = 0

env.close()