from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import Projectile
from typing import Optional

class Character(Entity):

    @property
    def get_health(self) -> int:
        ...
    
    def shoot(self) -> Optional[Projectile]:
        ...