from typing import Optional

from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BatAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class Bat(EnemyImpl):

    """ Bat is an enemy that moves horizontally and attacks by firing sound waves. """

    def __init__(self, x: int, y: int, width: int, height: int, speed: int, health: int) -> None:
        super().__init__(x, y, width, height, speed, health, attack_handler=BatAttackHandler(ProjectileFactory()))
        self._target_x: Optional[int] = None

    def set_target_x(self, player_x: int) -> None:
        self._target_x = player_x

    def move(self) -> None:
        # Calculate horizontal movement based on target
        x_movement = 0
        if self._target_x is not None:
            if self.x < self._target_x:
                x_movement = self._speed
            elif self.x > self._target_x:
                x_movement = -self._speed
        
        # Calculate vertical movement
        y_movement = max(1, self._speed // 2)
        
        # Use the parent class's move method to update position
        super().move(x_movement, y_movement, self.width, self.height)
