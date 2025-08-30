from typing import Optional

from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BatAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class Bat(EnemyImpl):

    """ Bat is an enemy that moves horizontally and attacks by firing sound waves. """

    def __init__(
        self, 
        x: int, 
        y: int, 
        width: int, 
        height: int, 
        speed: int, 
        health: int,
        horizontal_speed: float = 0.3,
        vertical_speed: float = 0.2
    ) -> None:
        super().__init__(x, y, width, height, speed, health, attack_handler=BatAttackHandler(ProjectileFactory()))
        self._target_x: Optional[int] = None
        self._horizontal_speed = max(0.0, horizontal_speed)
        self._vertical_speed = max(0.0, vertical_speed)
        # Accumulate fractional movement for sub-pixel speeds
        self._horizontal_accumulator = 0.0
        self._vertical_accumulator = 0.0

    def set_target_x(self, player_x: int) -> None:
        self._target_x = player_x

    def move(self) -> None:
        # Calculate horizontal movement direction based on target
        horizontal_direction = 0
        if self._target_x is not None:
            if self.x < self._target_x:
                horizontal_direction = 1  # Move right toward target
            elif self.x > self._target_x:
                horizontal_direction = -1  # Move left toward target
        
        # Accumulate fractional movement for smooth sub-pixel speeds
        self._horizontal_accumulator += self._horizontal_speed * horizontal_direction
        self._vertical_accumulator += self._vertical_speed
        
        # Extract integer movement and keep fractional part
        dx = int(self._horizontal_accumulator)
        dy = int(self._vertical_accumulator)
        
        # Keep the fractional parts for next frame
        self._horizontal_accumulator -= dx
        self._vertical_accumulator -= dy
        
        # Only move if there's actual movement to apply
        if dx != 0 or dy != 0:
            from Avian_Blasters.model.entity_impl import EntityImpl
            EntityImpl.move(self, dx, dy, self.get_area().width, self.get_area().height)
