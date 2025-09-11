from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.timed_power_up import TimedPowerUp


class DoubleFirePowerUp(TimedPowerUp):

    """ DoubleFirePowerUp is a timed power-up that makes the player shoot two projectiles at once for a duration """

    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, is_timed: bool, duration: float, delta: int):
        super().__init__(x, y, width, height, type, power_up_type, duration, is_timed, delta)

    def apply_effect(self, player):
        player.get_player_attack_handler().set_number_of_projectiles(2)

    def remove_effect(self, player):
        player.get_player_attack_handler().set_number_of_projectiles(1)