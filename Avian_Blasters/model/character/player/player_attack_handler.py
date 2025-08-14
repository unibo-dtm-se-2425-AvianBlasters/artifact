import pygame
from Avian_Blasters.model.character.general_attack_handler_impl import GeneralAttackHandlerImpl
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
        self._number_of_projectiles = 1
        self._shots_interval = 100
        self._last_shot_time = 0
        self._remaining_shots = 0
        self._projectile_factory = projectile_factory

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
        current_time = pygame.time.get_ticks()
        if self._remaining_shots == 0:
            self._remaining_shots = self._number_of_projectiles
            self._last_shot_time = current_time
        projectiles = []
        if self._remaining_shots > 0 and (current_time - self._last_shot_time) >= self._shots_interval:
            projectiles.append(self.__projectile_factory.create_projectile(
                self._projectile_type,
                player.get_area().get_position_x + player.get_area().width // 2,
                player.get_area().get_position_y + player.get_area().height // 2,
                Direction.UP,
                PLAYER_PROJECTILE_WIDTH,
                PLAYER_PROJECTILE_HEIGHT,
                Entity.TypeArea.PLAYER_PROJECTILE,
                self._projectile_speed)
            )
            self._remaining_shots -= 1
            self._last_shot_time = current_time
            if self._remaining_shots <= 0:
                self._reset_cooldown()
        return projectiles
