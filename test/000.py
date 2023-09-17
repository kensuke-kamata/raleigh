from collections import defaultdict
import numpy as np
import env

def update(pi, V, world, gamma=0.9):
    for state in world.states():
        if world.isgoal(state):
            V[state] = 0
            continue

        actions = pi[state]
        value = 0
        for action, prob in actions.items():
            next = world.move(state, action)
            reward = world.reward(state, action, next)
            value += prob * (reward + gamma * V[next])
        V[state] = value

    return V

def evaluate(pi, V, world, gamma, threshold=0.001):
    while True:
        old = V.copy()
        V = update(pi, V, world, gamma)

        # Check how much updated
        delta = 0
        for state in V.keys():
            t = abs(V[state] - old[state])
            if delta < t:
                delta = t

        if delta < threshold:
            break

    return V

world = env.World()
gamma = 0.9

pi = defaultdict(lambda: {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25})
V = defaultdict(lambda: 0)

V = evaluate(pi, V, world, gamma)
print(V)
world.render_v(V)
