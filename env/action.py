class Action:
    def __init__(self):
        self.set = [0, 1, 2, 3]
        self.data = None

    def __len__(self):
        return len(self.set)

    def __repr__(self):
        return self.to_stirng()

    def is_valid(self, action):
        return action in self.set

    def space(self):
        return self.set

    def to_stirng(self):
        if self.data == None:
            return 'None'
        if self.data == 0:
            return 'UP'
        if self.data == 1:
            return 'DOWN'
        if self.data == 2:
            return 'LEFT'
        if self.data == 3:
            return 'RIGHT'

