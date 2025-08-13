from enum import Enum

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.item.item import Item


class PowerUpType(Enum):
    DOUBLE_FIRE = 1
    LASER = 2
    INVULNERABILITY = 3

class PowerUp(Item):
    
    def is_collected(self, player_area: Area) -> bool:
        ...

    def effect_on_player(self, player : Player): 
        ...

    def remove_effect(self, player : Player):
        ...
