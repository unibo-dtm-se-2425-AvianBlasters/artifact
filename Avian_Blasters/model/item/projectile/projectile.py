from enum import Enum
from Avian_Blasters.model.item.item_impl import ItemImpl

class ProjectileType(Enum):
    NORMAL = 1
    LASER = 2

class Projectile(ItemImpl):
    
    @property
    def projectile_type(self) -> ProjectileType:
        ...

        