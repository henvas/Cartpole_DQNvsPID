import numpy as np
import gym
import math


env = gym.make('CartPole-v0')


def pd_control(s):
    errors = [-s[0], -s[1], -s[2], -s[3]]

    # Position gains
    p_pos = 0.5
    d_pos = 0.5

    # Angular gains
    p_ang = 1
    d_ang = 1

    u_pos = p_pos*errors[0] + d_pos*errors[1]
    u_ang = p_ang*errors[2] + d_ang*errors[3]

    u = u_pos + u_ang

    return 0 if u > 0 else 1


env.reset()
rewards = []
state, _, _, _ = env.step(env.action_space.sample())

for _ in range(600):
    env.render()
    action = pd_control(state)
    state, reward, done, _ = env.step(action)
    rewards.append(reward)
    if done:
        if np.sum(rewards) >= 199:
            print("Success!")
        else:
            print("Fail, score:", np.sum(rewards))
        rewards = []
        env.reset()


env.close()
