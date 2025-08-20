from abc import ABC, abstractmethod
from typing import Optional

from Avian_Blasters.model.item.projectile.projectile import Projectile


class AttackHandler(ABC):

    @abstractmethod
    def try_attack(self, enemy) -> Optional[Projectile]:
        ...
