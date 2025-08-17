from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.character.health_handler import HealthHandler
from typing import Optional

class Character(Entity):
    """Character is a type of Entity posessing health and being
    able to attack by shooting a Projectile"""

    def get_health_handler(self) -> HealthHandler:
        """Returns the HealthHandler of the character"""
        ...
    
    def shoot(self) -> Optional[Projectile]:
        """The Character will shoot a projectile and will
        return it if it does. If the recoil/cooldown is not
        yet done, it will return nothing"""
        ...