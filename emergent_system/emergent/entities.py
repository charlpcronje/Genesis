# emergent/entities.py

class Entity:
    def __init__(self, id, value, energy=100.0):
        self.id = id
        self.value = value
        self.energy = energy
        self.history = {}

    def apply_transformation(self, transformation, *args):
        cost = transformation.get_cost(self)
        if self.energy >= cost:
            new_value = transformation.apply(self.value, *args)
            self.energy -= cost
            self.history[transformation.id] = self.history.get(transformation.id, 0) + 1
            return Entity(self.id, new_value, self.energy)
        else:
            return None
