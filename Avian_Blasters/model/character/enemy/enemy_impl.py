from typing import Optional

from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.character.health_handler import HealthHandler
from Avian_Blasters.model.character.health_handler_impl import HealthHandlerImpl
from Avian_Blasters.model.character.general_attack_handler import GeneralAttackHandler
from Avian_Blasters.model.character.enemy.attack_handler_impl import EnemyAttackHandler
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory
from Avian_Blasters.model.character.character_impl import CharacterImpl
from Avian_Blasters.model.entity import Entity


class EnemyImpl(CharacterImpl, Enemy):
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
        # Initialize parent class with proper Entity.TypeArea
        super().__init__(x, y, width, height, Entity.TypeArea.ENEMY, speed, max_health)
        # Override health_handler if provided
        if health_handler:
            self._health_handler = health_handler
        # Set up attack handler
        self._attack_handler: GeneralAttackHandler = attack_handler or EnemyAttackHandler(ProjectileFactory())

    @property
    def x(self) -> int:
        return self.get_area().get_position_x

    @property
    def y(self) -> int:
        return self.get_area().get_position_y

    @property
    def width(self) -> int:
        return self.get_area().width

    @property
    def height(self) -> int:
        return self.get_area().height

    def move(self) -> None:
        # Call the EntityImpl's move method with appropriate parameters
        super().move(0, 1, self.width, self.height)

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

    def shoot(self) -> list[Projectile]:
        # Override Character's shoot method to use our attack handler
        return self._attack_handler.try_attack(self)
