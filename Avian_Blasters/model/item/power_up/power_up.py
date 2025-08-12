from enum import Enum

from Avian_Blasters.model.item.item import Item


class PowerUpType(Enum):
    DOUBLE_FIRE = 1
    LASER = 2
    INVULNERABILITY = 3

class PowerUp(Item):
    
    def is_collected(self, player_position) -> bool:
        ...

    def effect_on_player(self, player): 
        ...
