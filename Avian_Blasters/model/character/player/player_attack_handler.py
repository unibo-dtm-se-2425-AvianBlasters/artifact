import pygame
from Avian_Blasters.model.character.general_attack_handler_impl import GeneralAttackHandlerImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

PLAYER_COOLDOWN_STEPS = 30
PLAYER_PROJECTILE_WIDTH = 5
PLAYER_PROJECTILE_HEIGHT = 5

class PlayerAttackHandler(GeneralAttackHandlerImpl):
    """PlayerAttackHandler is an implementation of GeneralAttackHandler used to handle
    the attacks that have to be performed by the player character"""
    PLAYER_PROJECTILE_SPEED = 3

    def __init__(self, projectile_factory : ProjectileFactory, projectile_speed : int, projectile_type : ProjectileType, cooldown_steps: int = PLAYER_COOLDOWN_STEPS):
        super().__init__(projectile_factory, projectile_speed, cooldown_steps)
        self._number_of_projectiles = 1
        self._projectile_type = projectile_type

    @property
    def number_of_projectiles(self):
        return self._number_of_projectiles

    def set_number_of_projectiles(self, number_of_projectiles: int):
        if number_of_projectiles < 1:
            raise ValueError("Number of projectiles must be at least 1")
        self._number_of_projectiles = number_of_projectiles

    def try_attack(self, player):
        if not self._cooldown_handler.is_over():
            return []
        else:
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
                if self._projectile_type == ProjectileType.LASER:
                    projectile_y = player_center_y - (90 // 2) - player.get_area().height // 2
                else: 
                    projectile_y = player_center_y
                projectile = self._projectile_factory.create_projectile(
                    projectile_type=self._projectile_type,
                    x=projectile_x,
                    y=projectile_y,
                    width=PLAYER_PROJECTILE_WIDTH, 
                    height=PLAYER_PROJECTILE_HEIGHT,
                    type_area=Entity.TypeArea.PLAYER_PROJECTILE,
                    delta=self.PLAYER_PROJECTILE_SPEED
                )
                projectiles.append(projectile)
            self._reset_cooldown()
            return projectiles
                
                
