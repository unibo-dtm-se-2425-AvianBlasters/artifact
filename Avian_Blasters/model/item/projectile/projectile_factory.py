from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl


class ProjectileFactory:

    def create_projectile(self, projectile_type: ProjectileType, x: int, y: int, width: int , height: int, type_area: Entity.TypeArea, delta: int = DEFAULT_DELTA):
        
        if not isinstance(type_area, Entity.TypeArea):
            raise ValueError("Invalid type area")

        if not isinstance(projectile_type, ProjectileType):
            raise ValueError("Invalid projectile type")
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers")
        
        return ProjectileImpl(x, y, width, height, type_area, projectile_type, delta)