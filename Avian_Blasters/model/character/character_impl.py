from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.entity_impl import EntityImpl
from Avian_Blasters.model.entity import Entity

class CharacterImpl(EntityImpl, Character):

    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, delta : int, health : int):
        super().__init__(x, y, width, height, type, delta)
        self._health = health
    
    @property
    def get_health(self) -> int:
        return self._health
    
    def shoot(self):
        ...