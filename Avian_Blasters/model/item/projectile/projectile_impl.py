from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.position import Position

DEFAULT_SPEED = 1

class ProjectileImpl(Projectile):
    def __init__(self, projectile_type, position, direction, speed=DEFAULT_SPEED):
        self._type = projectile_type
        self._position = position
        self._active = True
        self._direction = direction
        self._speed = speed

    @property
    def position(self) -> Position:
        return self._position
    
    @property
    def active(self) -> bool:
        return self._active
    
    @property
    def type(self) -> ProjectileType:
        return self._type
    
    @property
    def direction(self) -> int:
        return self._direction
    
    @property
    def speed(self) -> int:
        return self._speed

    def destroy(self):
        self._active = False