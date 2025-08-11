from Avian_Blasters.model.item.projectile.projectile_types.laser_projectile import LaserProjectile
from Avian_Blasters.model.item.projectile.projectile_types.normal_projectile import NormalProjectile
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.position import Position


class ProjectileFactory:
    def create_projectile(self, projectile_type: ProjectileType, position: Position) -> Projectile:
        ...