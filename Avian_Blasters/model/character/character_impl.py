from character import Character
from entity_impl import EntityImpl
from entity import Entity

class CharacterImpl(EntityImpl, Character):

    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, delta : int, health : int):
        super().__init__(self, x, y, width, height, type, delta)
        self._health = health
    
    @property
    def get_health(self) -> int:
        return self._health
    
    def shoot(self):
        ...