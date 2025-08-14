from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.character.health_handler import HealthHandler
from typing import Optional

class Character(Entity):

    def get_health_handler(self) -> HealthHandler:
        ...
    
    def shoot(self) -> Optional[Projectile]:
        ...