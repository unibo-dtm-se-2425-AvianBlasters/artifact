from enum import Enum

from Avian_Blasters.model.area import Area
from Avian_Blasters.model.position import Position

class ProjectileType(Enum):
    NORMAL = 1
    LASER = 2

class Projectile:

    @property
    def position(self) -> Position:
        ...

    @property
    def area(self) -> Area:
        ...
    
    @property
    def active(self) -> bool:
        ...
    
    @property
    def type(self) -> ProjectileType:
        ...

    @property
    def direction(self) -> int:
        ...

    @property
    def speed(self) -> int:
        ...

    def move(self):
        ...

    def destroy(self):
        ...
        