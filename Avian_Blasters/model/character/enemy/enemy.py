from abc import ABC, abstractmethod
from typing import Optional


from character import Character
from item.projectile.projectile import Projectile


class Enemy(Character, ABC):

    @property
    @abstractmethod
    def x(self) -> int:
        ...

    @property
    @abstractmethod
    def y(self) -> int:
        ...

    @property
    @abstractmethod
    def width(self) -> int:
        ...

    @property
    @abstractmethod
    def height(self) -> int:
        ...

    @abstractmethod
    def move(self) -> None:
        ...

    @abstractmethod
    def attack(self) -> Optional[Projectile]:
        ...

    @abstractmethod
    def take_damage(self, damage: int) -> None:
        ...

    @abstractmethod
    def is_dead(self) -> bool:
        ...