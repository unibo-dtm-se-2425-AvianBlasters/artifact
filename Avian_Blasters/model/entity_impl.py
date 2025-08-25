from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.area_impl import AreaImpl
from Avian_Blasters.model.area import Area

class EntityImpl(Entity):
    """EntityImpl is an implementation of Entity"""

    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, delta : int):
        self._area = AreaImpl(x, y, width, height)
        self._type = type
        self._delta = delta
    
    def get_area(self) -> Area:
        return self._area
    
    @property
    def get_type(self) -> Entity.TypeArea:
        return self._type
    
    def move(self, movement_x : int, movement_y : int, width : int, height : int):
        self._area = AreaImpl(self._area.get_position_x + movement_x * self._delta,
                          self._area.get_position_y + movement_y * self._delta,
                          width,
                          height)
        
    # def move(self, movement_x : int, movement_y : int):
    #    self.move(self, movement_x * self._delta, movement_y * self._delta, self._area.get_width, self._area.get_height)
    
    def is_touched(self, other : Entity) -> bool:
        return self._area.overlap(other.get_area())
    
    @property
    def delta(self) -> int:
        return self._delta
    
    @delta.setter
    def delta(self, new_delta : int):
        self._delta = new_delta