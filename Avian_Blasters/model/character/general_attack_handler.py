from abc import abstractmethod
from ast import List
from typing import Optional

from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.item.projectile.projectile import Projectile


class GeneralAttackHandler:

    @property
    def projectile_type(self) -> str:
        ...
    
    @abstractmethod
    def try_attack(self, character) -> List[Projectile]:
        ...

    @abstractmethod
    def _reset_cooldown(self):
        ...

    @abstractmethod
    def _can_attack(self, character : Character) -> bool:
        ...

    