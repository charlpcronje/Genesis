# emergent/transformations.py

class Transformation:
    def __init__(self, id, func, base_cost=10.0):
        self.id = id
        self.func = func
        self.base_cost = base_cost
        self.usage_count = 0

    def get_cost(self, entity):
        decay = max(1.0, 10 - self.usage_count)
        return self.base_cost * (1.0 / (1 + self.usage_count)) + decay

    def apply(self, value, *args):
        self.usage_count += 1
        return self.func(value, *args)
