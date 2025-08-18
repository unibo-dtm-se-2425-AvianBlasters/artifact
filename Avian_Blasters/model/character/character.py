from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.character.health_handler import HealthHandler

class Character(Entity):
    """Character is a type of Entity posessing health and being
    able to attack by shooting a Projectile"""

    def get_health_handler(self) -> HealthHandler:
        """Returns the HealthHandler of the character"""
        ...
    
    def shoot(self) -> list[Projectile]:
        """The Character will shoot one or more projectiles and will
        return it/them if it does. If the recoil/cooldown phase is not
        over yet, the method will return nothing"""
        ...