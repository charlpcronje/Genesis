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
