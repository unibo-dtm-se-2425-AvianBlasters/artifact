from __future__ import annotations
from typing import TYPE_CHECKING
from Avian_Blasters.model.item.power_up.power_up import PowerUp

if TYPE_CHECKING:
    from Avian_Blasters.model.character.player.player import Player

class PowerUpHandler():

    """ PowerUpHandler is a class that handles the power-ups of a player"""

    def collect_power_up(self, power_up : PowerUp, player: "Player"):
        """ Collects a power-up and applies its effect to the player """
        ...
    
    def player_update(self, player: "Player", paused: bool):
        """ Updates the power-up handler, checking for expiration of timed power-ups """
        ...
    
    def get_current_power_up(self) -> PowerUp | None:
        """ Returns the current active power-up, or None if there is no active power-up """
        ...