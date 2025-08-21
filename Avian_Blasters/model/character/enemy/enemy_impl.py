from typing import Optional

from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.character.health_handler import HealthHandler
from Avian_Blasters.model.character.health_handler_impl import HealthHandlerImpl
from Avian_Blasters.model.character.general_attack_handler import GeneralAttackHandler
from Avian_Blasters.model.character.enemy.attack_handler_impl import EnemyAttackHandler
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


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
        attack_handler: Optional[GeneralAttackHandler] = None,
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
        self._attack_handler: GeneralAttackHandler = attack_handler or EnemyAttackHandler(ProjectileFactory())

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
        projectiles = self._attack_handler.try_attack(self)
        return projectiles[0] if projectiles else None

    def take_damage(self, damage: int) -> None:
        self._health_handler.take_damage(damage)

    def is_dead(self) -> bool:
        return self._health_handler.is_dead()

    @property
    def get_health(self) -> int:
        return self._health_handler.current_health

    def shoot(self) -> Optional[Projectile]:
        return self.attack()

    def shoot_all(self) -> list[Projectile]:
        """New method that returns all projectiles from an attack"""
        return self._attack_handler.try_attack(self)
