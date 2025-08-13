from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.timed_power_up import TimedPowerUp
from Avian_Blasters.model.item.projectile.projectile import ProjectileType


class LaserPowerUp(TimedPowerUp):
    def __init__(self, x: int, y: int, width: int, height: int, duration: float, delta: int ):
        super().__init__(x, y, width, height, Entity.TypeArea.POWER_UP, PowerUpType.LASER, duration, delta)

    def apply_effect(self, player : Player):
        player.player_attack_handler_get().set_projectile_type(ProjectileType.LASER)

    def remove_effect(self, player: Player):
        player.player_attack_handler_get().set_projectile_type(ProjectileType.NORMAL)