import random
from dataclasses import dataclass
from typing import Optional

from attack_handler import AttackHandler
from item.projectile.projectile import Projectile


@dataclass
class _SimpleProjectile(Projectile):

    x: int
    y: int
    speed_y: int
    damage: int = 1
    kind: str = "bullet"  # e.g. "bullet" or "sound_wave"
    slow_factor: float = 1.0  # 1.0 means no slow; < 1 slows the target
    slow_duration_steps: int = 0

    def step(self) -> None:
        self.y += self.speed_y


class AttackHandlerImpl(AttackHandler):

    def __init__(self, fire_chance: float = 0.05, cooldown_steps: int = 20, projectile_speed: int = 4) -> None:
        if not 0.0 <= fire_chance <= 1.0:
            raise ValueError("fire_chance must be within [0, 1]")
        self._fire_chance = fire_chance
        self._cooldown_steps = max(0, cooldown_steps)
        self._cooldown = 0
        self._projectile_speed = projectile_speed

    def _ready_and_roll(self) -> bool:
        if self._cooldown > 0:
            self._cooldown -= 1
            return False
        if random.random() <= self._fire_chance:
            self._cooldown = self._cooldown_steps
            return True
        return False

    def try_attack(self, enemy) -> Optional[Projectile]:  # type: ignore[override]
        if not self._ready_and_roll():
            return None
        # Default projectile is a small downward bullet
        return _SimpleProjectile(
            x=enemy.x,
            y=enemy.y + max(1, enemy.height // 2),
            speed_y=self._projectile_speed,
            damage=1,
            kind="bullet",
        )


class BirdAttackHandler(AttackHandlerImpl):
    """Birds drop standard bullets downward."""

    def __init__(self, fire_chance: float = 0.06, cooldown_steps: int = 18, projectile_speed: int = 5) -> None:
        super().__init__(fire_chance, cooldown_steps, projectile_speed)

    def try_attack(self, enemy) -> Optional[Projectile]:  # type: ignore[override]
        if not self._ready_and_roll():
            return None
        return _SimpleProjectile(
            x=enemy.x,
            y=enemy.y + max(1, enemy.height // 2),
            speed_y=self._projectile_speed,
            damage=1,
            kind="bullet",
        )


class BatAttackHandler(AttackHandler):

    def __init__(self, fire_chance: float = 0.04, cooldown_steps: int = 30, wave_speed: int = 2, slow_factor: float = 0.6, slow_duration_steps: int = 45) -> None:
        if not 0.0 <= fire_chance <= 1.0:
            raise ValueError("fire_chance must be within [0, 1]")
        self._fire_chance = fire_chance
        self._cooldown_steps = max(0, cooldown_steps)
        self._cooldown = 0
        self._wave_speed = wave_speed
        self._slow_factor = slow_factor
        self._slow_duration_steps = slow_duration_steps

    def try_attack(self, enemy) -> Optional[Projectile]:  # type: ignore[override]
        if self._cooldown > 0:
            self._cooldown -= 1
            return None
        if random.random() > self._fire_chance:
            return None
        self._cooldown = self._cooldown_steps
        return _SimpleProjectile(
            x=enemy.x,
            y=enemy.y + max(1, enemy.height // 2),
            speed_y=self._wave_speed,
            damage=0,  # sound wave does not deal direct damage
            kind="sound_wave",
            slow_factor=self._slow_factor,
            slow_duration_steps=self._slow_duration_steps,
        )
