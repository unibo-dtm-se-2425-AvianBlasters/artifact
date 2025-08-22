from __future__ import annotations

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType


class PowerUpImpl(PowerUp):
    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, is_timed: bool = False, duration: float | None = None, delta: int = DEFAULT_DELTA):
        super().__init__(x, y, width, height, type, delta)
        self._power_up_type = power_up_type
        self._collected = False
        self._is_timed = is_timed
        self._duration = duration

    @property
    def is_timed(self) -> bool:
        return self._is_timed
    
    @property
    def duration(self) -> float | None:
        return self._duration

    @property
    def power_up_type(self) -> PowerUpType:
        return self._power_up_type
    
    def is_collected(self, player_area : Area) -> bool:
        if self._collected:
            return True
        if self.get_area().overlap(player_area):
            self._collected = True 
            return True
        return False
    
    def apply_effect(self, player : Player):
        ...