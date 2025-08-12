from abc import ABC, abstractmethod


class HealthHandler(ABC):

    @property
    @abstractmethod
    def max_health(self) -> int:
        ...

    @property
    @abstractmethod
    def current_health(self) -> int:
        ...

    @abstractmethod
    def take_damage(self, damage: int) -> None:
        ...

    @abstractmethod
    def heal(self, amount: int) -> None:
        ...

    @abstractmethod
    def is_dead(self) -> bool:
        ...
