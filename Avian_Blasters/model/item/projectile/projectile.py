from enum import Enum
from Avian_Blasters.model.item.item_impl import ItemImpl

class ProjectileType(Enum):
    NORMAL = 1
    LASER = 2
    SOUND_WAVE = 3

class Projectile(ItemImpl):

    """ Projectile is a class that represents a projectile item in the game."""
    
    @property
    def projectile_type(self) -> ProjectileType:
        """ Returns the type of the projectile """
        ...

        