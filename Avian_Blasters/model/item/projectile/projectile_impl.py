from Avian_Blasters.model.area_impl import AreaImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import ItemImpl
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.position import Position

class ProjectileImpl(Projectile):
    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, projectile_type : ProjectileType, delta : int):
        super().__init__(x, y, width, height, type, delta)
        self._projectile_type = projectile_type
    
    @property
    def projectile_type(self) -> ProjectileType:
        return self._projectile_type
    
    def move(self, movement_x, movement_y, width, height):
        if self.active:
            if self._projectile_type == ProjectileType.LASER:
                self._area = AreaImpl(movement_x, self.get_area().get_position_y, width, height)
            else:
                super().move(movement_x, movement_y, width, height)
