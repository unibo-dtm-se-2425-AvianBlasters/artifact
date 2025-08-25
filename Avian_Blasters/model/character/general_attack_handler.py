from abc import abstractmethod
from ast import List
from typing import Optional

from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.cooldown_handler import CoolDownHandler
from Avian_Blasters.model.item.projectile.projectile import Projectile


class GeneralAttackHandler:

    @property
    def projectile_type(self) -> str:
        ...

    @property
    def cooldown_handler(self) -> CoolDownHandler:
        ...
    
    @abstractmethod
    def try_attack(self, character) -> list[Projectile]:
        ...

    @abstractmethod
    def _reset_cooldown(self):
        ...

    @abstractmethod
    def update(self):
        ...

    