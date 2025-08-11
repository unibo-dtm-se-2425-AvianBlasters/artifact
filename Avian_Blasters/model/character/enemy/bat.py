from typing import Optional

from enemy_impl import EnemyImpl
from attack_handler_impl import BatAttackHandler


class Bat(EnemyImpl):

    def __init__(self, x: int, y: int, width: int, height: int, speed: int, health: int) -> None:
        super().__init__(x, y, width, height, speed, health, attack_handler=BatAttackHandler())
        self._target_x: Optional[int] = None

    def set_target_x(self, player_x: int) -> None:
        self._target_x = player_x

    def move(self) -> None:
        if self._target_x is not None:
            if self._x < self._target_x:
                self._x += self._speed
            elif self._x > self._target_x:
                self._x -= self._speed
        self._y += max(1, self._speed // 2)
