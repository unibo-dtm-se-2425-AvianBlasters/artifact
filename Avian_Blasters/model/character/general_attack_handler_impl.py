from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.character.general_attack_handler import GeneralAttackHandler
from Avian_Blasters.model.cooldown_handler import CoolDownHandler
from Avian_Blasters.model.cooldown_handler_impl import CoolDownHandlerImpl
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

PROJECTILE_TYPE_DEFAULT = ProjectileType.NORMAL
COOLDOWN_STEPS_DEFAULT = 20
PROJECTILE_SPEED_DEFAULT = 1

class GeneralAttackHandlerImpl(GeneralAttackHandler):
    """ GeneralAttackHandlerImpl is an implementation of GeneralAttackHandler interface 
        that provides basic functionality for handling attacks of a character"""

    def __init__(self, projectile_factory : ProjectileFactory, projectile_speed : int = PROJECTILE_SPEED_DEFAULT, cooldown_steps: int = COOLDOWN_STEPS_DEFAULT):
        self._projectile_type = PROJECTILE_TYPE_DEFAULT
        self._projectile_speed = projectile_speed
        self._projectile_factory = projectile_factory
        self._cooldown_handler = CoolDownHandlerImpl(cooldown = 0, refresh_rate = cooldown_steps)

    @property
    def projectile_type(self) -> str:
        return self._projectile_type
    
    @property
    def cooldown_handler(self) -> CoolDownHandler:
        return self._cooldown_handler

    def set_projectile_type(self, projectile_type: ProjectileType):
        self._projectile_type = projectile_type
        
    def try_attack(self, character : Character):
        #Base implementation - should be overridden by subclasses
        return []
        
    def _reset_cooldown(self):
        self._cooldown_handler.cooldown = 1

    def update(self):
        self._cooldown_handler.update()
