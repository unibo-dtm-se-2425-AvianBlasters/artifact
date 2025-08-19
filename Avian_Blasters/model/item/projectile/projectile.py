from enum import Enum

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.item.item import Direction, Item
from Avian_Blasters.model.item.item_impl import ItemImpl
from Avian_Blasters.model.position import Position

class ProjectileType(Enum):
    NORMAL = 1
    LASER = 2

class Projectile(ItemImpl):
    
    @property
    def projectile_type(self) -> ProjectileType:
        ...

        