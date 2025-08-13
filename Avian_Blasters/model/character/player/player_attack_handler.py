from Avian_Blasters.model.character.general_attack_handler import GeneralAttackHandler
from Avian_Blasters.model.character.general_attack_handler_impl import GeneralAttackHandlerImpl
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

PLAYER_COOLDOWN_STEPS = 15
PLAYER_PROJECTILE_WIDTH = 5
PLAYER_PROJECTILE_HEIGHT = 5

class PlayerAttackHandler(GeneralAttackHandlerImpl):
    PLAYER_PROJECTILE_SPEED = 3

    def __init__(self, projectile_factory : ProjectileFactory, projectile_speed : int, projectile_type : ProjectileType, cooldown_steps: int = PLAYER_COOLDOWN_STEPS):
        super().__init__(projectile_factory, projectile_speed, projectile_type, cooldown_steps)
        

    def try_attack(self, player : Player):
        if not self._can_attack(player):
            return None 
        projectile = self._projectile_factory.create_projectile(
            self._projectile_type,
            player.get_area().get_position_x + player.get_area().get_width // 2,
            player.get_area().get_position_y + player.get_area().get_height // 2,
            Direction.UP,
            PLAYER_PROJECTILE_WIDTH,
            PLAYER_PROJECTILE_HEIGHT,
            Entity.TypeArea.PLAYER_PROJECTILE,
            self._projectile_speed)
        self._reset_cooldown()
        return projectile
