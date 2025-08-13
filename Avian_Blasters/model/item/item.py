from enum import Enum
from Avian_Blasters.model.entity import Entity

class Direction(Enum):
    UP = 1
    DOWN = -1

class Item(Entity):
    @property
    def active(self) -> bool:
        ...

    def destroy(self):
        ...