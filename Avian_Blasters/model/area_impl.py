from Avian_Blasters.model.position_impl import PositionImpl
from Avian_Blasters.model.area import Area
from pygame import Rect

class AreaImpl(Area):
    """AreaImpl is an implementation of Area"""

    def __init__(self, x : int, y : int, width : int, height : int):
        self._position = PositionImpl(x, y)
        if width < 0 or height < 0:
            raise ValueError("Width and Height must be bigger than zero")
        self._width = width
        self._height = height
        self._figure = self.__position_adjustment(x, y, width, height)
    
    @property
    def get_position_x(self) -> int:
        return self._position.get_x

    @property
    def get_position_y(self) -> int:
        return self._position.get_y

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, new_width : int):
        self._width = new_width
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, new_height : int):
        self._height = new_height
    
    def overlap(self, other : Area) -> bool:
        return self.get_area().colliderect(other.get_area())
    
    def get_area(self) -> Rect:
        return self._figure

    def __position_adjustment(self, x : int, y : int, width : int, height : int) -> Rect:
        return Rect(int(x-width/2), int(y-height/2), width, height)