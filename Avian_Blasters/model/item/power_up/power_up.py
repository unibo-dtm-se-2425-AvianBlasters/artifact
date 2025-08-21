from enum import Enum
from typing import TYPE_CHECKING

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.item.item import Item
from Avian_Blasters.model.item.item_impl import ItemImpl
if TYPE_CHECKING:
    from Avian_Blasters.model.character.player.player import Player

class PowerUpType(Enum):
    DOUBLE_FIRE = 1
    LASER = 2
    INVULNERABILITY = 3
    HEALTH_RECOVERY = 4

class PowerUp(ItemImpl):

    @property
    def power_up_type(self) -> PowerUpType:
        ...

    @property
    def is_timed(self) -> bool:
        ...

    @property
    def duration(self) -> float | None:
        ...
    
    def is_collected(self, player_area: Area) -> bool:
        ...

    def apply_effect(self, player : "Player"): 
        ...

    def remove_effect(self, player : "Player"):
        ...
