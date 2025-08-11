from Avian_Blasters.model.area_impl import AreaImpl
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import DEFAULT_SPEED, ProjectileImpl
from Avian_Blasters.model.position import Position

DEFAULT_WIDTH = 2
DEFAULT_HEIGHT = 2


class NormalProjectile(ProjectileImpl):
    def __init__(self, position: Position, direction: int, speed: int = DEFAULT_SPEED, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        super().__init__(ProjectileType.NORMAL, position, direction, speed)
        self._width = width
        self._height = height
        self._area = AreaImpl(position.get_x(), position.get_y(), width, height)

    @property
    def area(self) -> AreaImpl:
        return self._area
    
    def move(self):
        if self.active:
            new_x = self.position.get_x()
            new_y = self.position.get_y() + self.direction * self.speed
            self._position = Position(new_x, new_y)
            self._update_area()

    def _update_area(self):
        self._area = AreaImpl(self.position.get_x(), self.position.get_y(), self._width, self._height)