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

    def __init__(self, projectile_factory : ProjectileFactory, projectile_speed : int, projectile_type : ProjectileType, cooldown_steps: int = PLAYER_COOLDOWN_STEPS):
        super().__init__(projectile_factory, projectile_speed, projectile_type, cooldown_steps)
        

    def try_attack(self, player : Player):
        if not self._can_attack(player):
            return None 
        projectile = self.projectile_factory.create_projectile(
            projectile_type=self.projectile_type,
            x=player.get_area().get_position_x + player.get_area().get_width // 2,
            y=player.get_area().get_position_y + player.get_area().get_height // 2,
            direction= Direction.UP,
            width=PLAYER_PROJECTILE_WIDTH,
            height=PLAYER_PROJECTILE_HEIGHT,
            type= Entity.TypeArea.PLAYER_PROJECTILE,
            delta=self.projectile_speed)
        self._reset_cooldown()
        return projectile
    
    # The Player should have a PlayerAttackHandler and it should use try_attack method in the shoot() method