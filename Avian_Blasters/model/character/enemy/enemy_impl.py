from typing import Optional

from enemy import Enemy
from Avian_Blasters.model.character.health_handler import HealthHandler
from Avian_Blasters.model.character.health_handler_impl import HealthHandlerImpl
from attack_handler import AttackHandler
from attack_handler_impl import AttackHandlerImpl
from item.projectile.projectile import Projectile


class EnemyImpl(Enemy):
    """ Base class for all enemies in the game. It provides basic movement, attack, and health handling. """
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        speed: int,
        max_health: int,
        attack_handler: Optional[AttackHandler] = None,
        health_handler: Optional[HealthHandler] = None,
    ) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._speed = speed
        self._health_handler: HealthHandler = health_handler or HealthHandlerImpl(
            max_health
        )
        self._attack_handler: AttackHandler = attack_handler or AttackHandlerImpl()

    @property
    def x(self) -> int:
        return self._x  

    @property
    def y(self) -> int:
        return self._y

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def move(self) -> None:
        self._y += self._speed

    def attack(self) -> Optional[Projectile]:
        return self._attack_handler.try_attack(self)

    def take_damage(self, damage: int) -> None:
        self._health_handler.take_damage(damage)

    def is_dead(self) -> bool:
        return self._health_handler.is_dead()

    @property
    def get_health(self) -> int:
        return self._health_handler.current_health

    def shoot(self) -> Optional[Projectile]:
        return self.attack()
