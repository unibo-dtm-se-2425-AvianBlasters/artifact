from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.timed_power_up import TimedPowerUp


class ProjectilePowerUp(TimedPowerUp):

    """A power-up that affects the type of projectiles the player shoots, 
        and keeps track of the projectiles created while the power-up is active"""
    
    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, duration: float, is_timed: bool = True, delta: int = DEFAULT_DELTA):
        super().__init__(x, y, width, height, type, power_up_type, duration, is_timed, delta)
        self._projectiles = set()

    def add_projectile(self, projectile):
        """ Add a projectile created while the power-up is active """
        self._projectiles.add(projectile)
    
    def remove_effect(self, player : Player):
        """ Destroy all projectiles created while the power-up was active """
        for projectile in self._projectiles:
            projectile.destroy()
        self._projectiles.clear()
        
        