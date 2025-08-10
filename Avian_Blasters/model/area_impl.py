from position import Position
from area import Area

class AreaImpl(Area):
    def __init__(self, x : int, y : int, width : int, height : int):
        self._position = Position(x, y)
        self._width = width
        self._height = height
    
    @property
    def get_position_x(self) -> int:
        return self._position.get_x()

    @property
    def get_position_y(self) -> int:
        return self._position.get_y()

    @property
    def get_width(self) -> int:
        return self._width
    
    @property
    def get_height(self) -> int:
        return self._height
    
    def overlap(self, other) -> bool:
        return NotImplemented

    def __position_adjustment(x,y,width,height):
        return NotImplemented