from __future__ import annotations

from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl

DEFAULT_HEALTH_RECOVERY_AMOUNT = 10

class HealthRecoveryPowerUp(PowerUpImpl):
    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, is_timed: bool, duration: float | None, delta: int):
        super().__init__(x, y, width, height, type, power_up_type, is_timed, duration, delta)

    def apply_effect(self, player):
        player.get_health_handler().heal(DEFAULT_HEALTH_RECOVERY_AMOUNT)