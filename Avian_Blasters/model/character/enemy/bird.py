import math

from enemy_impl import EnemyImpl
from attack_handler_impl import BirdAttackHandler


class Bird(EnemyImpl):

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        speed: int,
        health: int,
        wave_amplitude: int = 20,
        wave_frequency: float = 0.15,
    ) -> None:
        super().__init__(x, y, width, height, speed, health, attack_handler=BirdAttackHandler())
        self._base_x = x
        self._wave_amplitude = max(0, wave_amplitude)
        self._wave_frequency = max(0.0, wave_frequency)
        self._phase = 0.0

    def move(self) -> None:
        super().move()
        self._phase += self._wave_frequency
        offset = int(self._wave_amplitude * math.sin(self._phase))
        self._x = self._base_x + offset
