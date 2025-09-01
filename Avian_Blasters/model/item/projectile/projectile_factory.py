from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl


class ProjectileFactory:

    DEFAULT_SIZES = {
        ProjectileType.NORMAL: (2, 4),
        ProjectileType.LASER: (2, 90),
        ProjectileType.SOUND_WAVE: (2, 5)
    }

    def create_projectile(self, projectile_type: ProjectileType, x: int, y: int, width: int , height: int, type_area: Entity.TypeArea, delta: int = DEFAULT_DELTA):
        
        if not isinstance(type_area, Entity.TypeArea):
            raise ValueError("Invalid type area")

        if not isinstance(projectile_type, ProjectileType):
            raise ValueError("Invalid projectile type")
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers")

        if projectile_type in self.DEFAULT_SIZES:
                width, height = self.DEFAULT_SIZES[projectile_type]
        else:
            raise ValueError("Unsupported projectile type")
        
        return ProjectileImpl(x, y, width, height, type_area, projectile_type, delta)