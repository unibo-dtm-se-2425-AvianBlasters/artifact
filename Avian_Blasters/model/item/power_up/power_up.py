from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.item.item_impl import ItemImpl
if TYPE_CHECKING:
    from Avian_Blasters.model.character.player.player import Player

class PowerUpType(Enum):
    DOUBLE_FIRE = 1
    LASER = 2
    INVULNERABILITY = 3
    HEALTH_RECOVERY = 4

class PowerUp(ItemImpl):

    """ PowerUp is a class that represents a power-up item in the game, 
        which can be collected by the player to gain temporary or permanent enhancements. """

    @property
    def power_up_type(self) -> PowerUpType:
        """ Returns the type of the power-up """
        ...

    @property
    def is_timed(self) -> bool:
        """ Returns True if the power-up is timed, False otherwise """
        ...

    @property
    def duration(self) -> float | None:
        """ Returns the duration of the power-up effect in seconds, or None if it is not timed """
        ...
    
    def is_collected(self, player_area: Area) -> bool:
        """ Returns True if the power-up has been collected by the player"""
        ...

    def apply_effect(self, player : "Player"): 
        """ Apply the effect of the power-up to the player"""
        ...

