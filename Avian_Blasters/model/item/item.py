from enum import Enum
from Avian_Blasters.model.entity import Entity

class Item(Entity):
    @property
    def active(self) -> bool:
        ...

    def destroy(self):
        ...