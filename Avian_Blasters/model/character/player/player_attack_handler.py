import pygame
from Avian_Blasters.model.character.general_attack_handler_impl import GeneralAttackHandlerImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

PLAYER_COOLDOWN_STEPS = 5
PLAYER_PROJECTILE_WIDTH = 5
PLAYER_PROJECTILE_HEIGHT = 5

class PlayerAttackHandler(GeneralAttackHandlerImpl):
    PLAYER_PROJECTILE_SPEED = 3

    def __init__(self, projectile_factory : ProjectileFactory, projectile_speed : int, projectile_type : ProjectileType, cooldown_steps: int = PLAYER_COOLDOWN_STEPS):
        super().__init__(projectile_factory, projectile_speed, cooldown_steps)
        self._number_of_projectiles = 1
        self._projectile_factory = projectile_factory
        self._projectile_type = projectile_type

    def set_number_of_projectiles(self, number_of_projectiles: int):
        if number_of_projectiles < 1:
            raise ValueError("Number of projectiles must be at least 1")
        self._number_of_projectiles = number_of_projectiles

    def _can_attack(self) -> bool:
        if self._cooldown > 0:
            self._cooldown -= 1
            return False
        return True

    def try_attack(self, player):
        if not self._can_attack():
            return []
        projectiles = []
        player_center_x = player.get_area().get_position_x 
        player_center_y = player.get_area().get_position_y 
        offset = 20
        total_width = (self._number_of_projectiles - 1) * offset
        start_x = player_center_x - total_width // 2 
        for i in range(self._number_of_projectiles):
            if self._number_of_projectiles == 1:
                projectile_x = player_center_x
            else:
                projectile_x = start_x + i * offset
            projectile = self._projectile_factory.create_projectile(
                projectile_type=self._projectile_type,
                x=projectile_x,
                y=player_center_y,
                direction=Direction.UP,
                width=PLAYER_PROJECTILE_WIDTH, 
                height=PLAYER_PROJECTILE_HEIGHT,
                type_area=Entity.TypeArea.PLAYER_PROJECTILE,
                delta=self.PLAYER_PROJECTILE_SPEED
            )
            projectiles.append(projectile)
        self._reset_cooldown()
        return projectiles
                
                
