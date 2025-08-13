from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.entity_impl import EntityImpl
from Avian_Blasters.model.entity import Entity

class CharacterImpl(EntityImpl, Character):
    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, delta : int, health : int):
        super().__init__(x, y, width, height, type, delta)
        self._health = health
        self._max_health = health
    
    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, health : int):
        if (self._health + health) < self._max_health:
            self._health += health
        else:
            self._health = self._max_health
    
    def shoot(self):
        ...