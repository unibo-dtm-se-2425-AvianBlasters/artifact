from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.timed_power_up import TimedPowerUp


class DoubleFirePowerUp(TimedPowerUp):
    def __init__(self, x: int, y: int, width: int, height: int, duration: float, delta: int):
        super().__init__(x, y, width, height, Entity.TypeArea.POWER_UP, PowerUpType.DOUBLE_FIRE, duration, delta)

    def apply_effect(self, player):
        player.player_attack_handler_get().set_number_of_projectiles(2)

    def remove_effect(self, player):
        player.player_attack_handler_get().set_number_of_projectiles(1)