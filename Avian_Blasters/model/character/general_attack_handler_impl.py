from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.character.general_attack_handler import GeneralAttackHandler
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

PROJECTILE_TYPE_DEFAULT = ProjectileType.NORMAL
COOLDOWN_STEPS_DEFAULT = 20
PROJECTILE_SPEED_DEFAULT = 1

class GeneralAttackHandlerImpl(GeneralAttackHandler):
    def __init__(self, projectile_factory : ProjectileFactory):
        self._projectile_type = PROJECTILE_TYPE_DEFAULT
        self._projectile_speed = PROJECTILE_SPEED_DEFAULT
        self._projectile_factory = projectile_factory
        self._cooldown_steps = max(0, COOLDOWN_STEPS_DEFAULT)
        self._cooldown = 0

    @property
    def projectile_type(self) -> str:
        return self._projectile_type

    def set_projectile_type(self, projectile_type: ProjectileType):
        self._projectile_type = projectile_type
        
    def _reset_cooldown(self):
        self._cooldown = self._cooldown_steps
