from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl
from Avian_Blasters.model.item.power_up.timed_power_up import TimedPowerUp


class DoubleFirePowerUp(TimedPowerUp):
    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, is_timed: bool, duration: float, delta: int):
        super().__init__(x, y, width, height, type, power_up_type, is_timed, duration, delta)

    def apply_effect(self, player):
        player.player_attack_handler_get().set_number_of_projectiles(2)

    def remove_effect(self, player):
        player.player_attack_handler_get().set_number_of_projectiles(1)