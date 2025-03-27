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
