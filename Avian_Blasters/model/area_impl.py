from position import Position
from area import Area
from pygame import Rect

class AreaImpl(Area):
    def __init__(self, x : int, y : int, width : int, height : int):
        self._position = Position(x, y)
        self._width = width
        self._height = height
        self._figure = self.__position_adjustment(x, y, width, height)
    
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
    
    def overlap(self, other : Area) -> bool:
        return self.get_area().colliderect(other.get_area())
    
    def get_area(self) -> Rect:
        return self._figure

    def __position_adjustment(x : int, y : int, width : int, height : int) -> Rect:
        return Rect((x-width/2, y-height/2), (x-width/2, y+height/2),
                    width, height)