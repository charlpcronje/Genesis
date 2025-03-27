# Combined Project Files

## c:\dev\ailogs\2nd Try\emergent_system\main.py
```py
# main.py

from emergent.engine import run_simulation

if __name__ == "__main__":
    logs = run_simulation()
    for log in logs:
        print(log)

```

## c:\dev\ailogs\2nd Try\emergent_system\emergent\engine.py
```py
# emergent/engine.py

from emergent.entities import Entity
from emergent.transformations import Transformation
from emergent.memory import Memory

def run_simulation():
    memory = Memory()

    # Example transformations
    def plus_one(x): return x + 1
    def times_two(x): return x * 2

    t1 = Transformation("plus_one", plus_one, base_cost=5.0)
    t2 = Transformation("times_two", times_two, base_cost=8.0)

    e = Entity("e1", 1)

    for _ in range(5):
        result = e.apply_transformation(t1)
        if result:
            memory.record(e, t1, result)
            e = result

    for _ in range(3):
        result = e.apply_transformation(t2)
        if result:
            memory.record(e, t2, result)
            e = result

    return memory.logs

```

## c:\dev\ailogs\2nd Try\emergent_system\emergent\entities.py
```py
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

```

## c:\dev\ailogs\2nd Try\emergent_system\emergent\memory.py
```py
# emergent/memory.py

class Memory:
    def __init__(self):
        self.logs = []

    def record(self, entity, transformation, result):
        self.logs.append({
            "entity": entity.id,
            "transformation": transformation.id,
            "before": entity.value,
            "after": result.value if result else None,
            "energy_before": entity.energy,
            "energy_after": result.energy if result else None
        })

```

## c:\dev\ailogs\2nd Try\emergent_system\emergent\transformations.py
```py
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

```

## c:\dev\ailogs\2nd Try\emergent_system\README.md
```md
# Emergent System

This system simulates an emergent, self-improving logic engine with Entities, Transformations, Memory, Cost, and Improvement.

## How to Run

```bash
python main.py
```

## Structure

- `entities.py`: Entity class
- `transformations.py`: Transformation logic
- `memory.py`: Memory and cost tracker
- `engine.py`: Simulation engine
- `main.py`: Entry point

```

