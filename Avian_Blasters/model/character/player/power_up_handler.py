from __future__ import annotations
from typing import TYPE_CHECKING
from Avian_Blasters.model.item.power_up.power_up import PowerUp

if TYPE_CHECKING:
    from Avian_Blasters.model.character.player.player import Player

class PowerUpHandler():

    def collect_power_up(self, power_up : PowerUp, player: "Player"):
        ...
    
    def player_update(self, player: "Player", paused: bool):
        ...
    
    def get_current_power_up(self) -> PowerUp | None:
        ...

    def is_expired(self) -> bool:
        ...