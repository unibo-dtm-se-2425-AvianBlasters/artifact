from enum import Enum
from Avian_Blasters.model.area import Area

class Entity():
    """Entity defines the base elements and actions that characterise
    all the elements of the game"""
    
    class TypeArea(Enum):
        """TypeArea defines the possible types of area an Entity
        can have"""
        PLAYER = 1
        ENEMY = 2
        PLAYER_PROJECTILE = 3
        ENEMY_PROJECTILE = 4
        POWERUP = 5

    def get_area(self) -> Area:
        """Returns the area the Entity to be able to get information
        about its position, width and height"""
        ...
    
    @property
    def get_type(self) -> TypeArea:
        """Returns the TypeArea the entity has"""
        ...
    
    def move(self, movement_x : int, movement_y : int, width : int, height : int):
        """Moves the entity by a certain x and y axis movement. It allows
        for a redefinition of its width and height"""
        ...

    def is_touched(self, other : "Entity") -> bool:
        """Checks whether an Entity is touching another"""
        ...
    
    @property
    def delta(self) -> int:
        """Gives access to the movement delta property of the Entity"""
        ...
    
    @delta.setter
    def delta(self, new_delta : int):
        ...