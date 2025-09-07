from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl
from Avian_Blasters.model.item.power_up.projectile_power_up import ProjectilePowerUp
from Avian_Blasters.model.item.power_up.timed_power_up import TimedPowerUp
from Avian_Blasters.model.item.projectile.projectile import ProjectileType


class LaserPowerUp(ProjectilePowerUp):

    """ LaserPowerUp is a timed power-up that changes the player's projectile type to laser for a duration """

    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, is_timed: bool, duration: float, delta: int):
        super().__init__(x, y, width, height, type, power_up_type, duration, is_timed, delta)

    def apply_effect(self, player : Player):
        player.get_player_attack_handler().set_projectile_type(ProjectileType.LASER)

    def remove_effect(self, player: Player):
        player.get_player_attack_handler().set_projectile_type(ProjectileType.NORMAL)
        super().remove_effect(player)