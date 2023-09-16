import numpy as np

from env.renderer import Renderer

class World:
    def __init__(self):
        self.map = np.array([
            [0., 0.,   0.,  1.],
            [0., None, 0., -1.],
            [0., 0.,   0,  0.]
        ])

        self.goal = (0, 3)
        self.walls = [(1, 1)]
        self.start = (2, 0)
        self.agent = self.start

    @property
    def height(self):
        return self.map.shape[0]

    @property
    def width(self):
        return self.map.shape[1]

    @property
    def shape(self):
        return self.map.shape

    def states(self):
        for h in range(self.height):
            for w in range(self.width):
                yield (h, w)

    def iswall(self, coord):
        return coord in self.walls

    def isgoal(self, coord):
        return coord == self.goal

    def move(self, now, action):
        ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        d = ds[action]
        next = (now[0] + d[0], now[0] + d[1])
        ny, nx = next

        if ny < 0 or ny >= self.height or nx < 0 or nx >=self.width:
            return now
        if next in self.walls:
            return now

        return next

    def reward(self, state, action, next):
        return self.map[next]

    def reset(self):
        self.agent = self.start
        return self.agent

    def step(self, action):
        now  = self.agent
        next = self.move(now, action)

        reward = self.reward(now, action, next)
        done = next == self.goal

        self.agent = next
        return next, reward, done

    def render_v(self, v=None, policy=None, print=True):
        renderer = Renderer(self.map, self.goal, self.walls)
        renderer.render_v(v, policy, print)

    def render_q(self, q=None, print=True):
        renderer = Renderer(self.map, self.goal, self.walls)
        renderer.render_q(q, print)
