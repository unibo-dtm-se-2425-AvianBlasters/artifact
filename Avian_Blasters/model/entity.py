from enum import Enum
from Avian_Blasters.model.area import Area

class Entity():
    class TypeArea(Enum):
        PLAYER = 1
        ENEMY = 2
        PLAYER_PROJECTILE = 3
        ENEMY_PROJECTILE = 4
        POWERUP = 5

    def get_area(self) -> Area:
        ...
    
    @property
    def get_type(self) -> TypeArea:
        ...
    
    def move(self, movement_x : int, movement_y : int, width : int, height : int):
        ...
        
    #def move(self, movement_x : int, movement_y : int):
    #    ...

    def is_touched(self, other) -> bool:
        ...