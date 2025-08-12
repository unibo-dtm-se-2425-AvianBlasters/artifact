from Avian_Blasters.model.area_impl import AreaImpl
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
from Avian_Blasters.model.position import Position


class NormalProjectile(ProjectileImpl):
    def __init__(self, x : int , y : int, width: int, height: int, direction: Direction, delta : int):
        super().__init__(x, y, width, height, ProjectileType.NORMAL, direction, delta)
    
    def move(self, x: int, y: int):
        if self.active:
            super().move(x, y)