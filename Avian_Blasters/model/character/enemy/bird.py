import math

from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BirdAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class Bird(EnemyImpl):
    """ Bird is an enemy that moves in a wave-like pattern and drops bullets downward. """
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
        super().__init__(x, y, width, height, speed, health, attack_handler=BirdAttackHandler(ProjectileFactory()))
        self._base_x = x
        self._wave_amplitude = max(0, wave_amplitude)
        self._wave_frequency = max(0.0, wave_frequency)
        self._phase = 0.0

    def move(self) -> None:
        # Call parent move method first to update y position
        super().move()
        # Then handle wave-like horizontal movement
        self._phase += self._wave_frequency
        offset = int(self._wave_amplitude * math.sin(self._phase))
        # Update position using area's position
        new_x = self._base_x + offset
        super().move(new_x - self.x, 0, self.width, self.height)
