from enum import Enum

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.item.item import Direction, Item
from Avian_Blasters.model.position import Position

class ProjectileType(Enum):
    NORMAL = 1
    LASER = 2

class Projectile(Item):
    
    @property
    def projectile_type(self) -> ProjectileType:
        ...

    @property
    def direction(self) -> Direction:
        ...
        