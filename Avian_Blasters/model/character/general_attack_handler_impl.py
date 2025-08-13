from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.character.general_attack_handler import GeneralAttackHandler
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

PROJECTILE_TYPE_DEFAULT = ProjectileType.NORMAL
COOLDOWN_STEPS_DEFAULT = 20

class GeneralAttackHandlerImpl(GeneralAttackHandler):
    def __init__(self, projectile_factory : ProjectileFactory, projectile_speed : int, projectile_type : ProjectileType = PROJECTILE_TYPE_DEFAULT, cooldown_steps : int = COOLDOWN_STEPS_DEFAULT):
        self._projectile_type = projectile_type
        self._projectile_speed = projectile_speed
        self._projectile_factory = projectile_factory
        self._cooldown_steps = max(0, cooldown_steps)
        self._cooldown = 0

    @property
    def projectile_type(self) -> str:
        return self._projectile_type
    
    def _can_attack(self, character : Character) -> bool:
        if self._cooldown > 0:
            self._cooldown -= 1
            return False
        return True
        
    def _reset_cooldown(self):
        self._cooldown = self._cooldown_steps
