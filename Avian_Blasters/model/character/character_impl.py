from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.character.health_handler import HealthHandler
from Avian_Blasters.model.character.health_handler_impl import HealthHandlerImpl
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.entity_impl import EntityImpl
from Avian_Blasters.model.entity import Entity

class CharacterImpl(EntityImpl, Character):
    """CharacterImpl is an implementation of Character"""

    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, delta : int, health : int):
        super().__init__(x, y, width, height, type, delta)
        self._health_handler = HealthHandlerImpl(health)
        self._max_health = health
    
    def get_health_handler(self) -> HealthHandler:
        return self._health_handler
    
    def shoot(self) -> list[Projectile]:
        ...