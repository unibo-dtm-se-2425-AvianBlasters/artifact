from Avian_Blasters.model.position_impl import PositionImpl
from Avian_Blasters.model.area import Area
from pygame import Rect

class AreaImpl(Area):
    """AreaImpl is an implementation of Area"""

    def __init__(self, x : int, y : int, width : int, height : int):
        self._position = PositionImpl(int(x), int(y))
        if not (isinstance(width, int) and isinstance(height, int)) or (width < 0 or height < 0):
            raise ValueError("Width and Height must be positive integers!")
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
        if isinstance(new_width, int) and new_width > 0:
            self._width = new_width
        else:
            raise Exception("Width must be a positive integer!")
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, new_height : int):
        if isinstance(new_height, int) and new_height > 0:
            self._height = new_height
        else:
            raise Exception("Height must be a positive integer!")
    
    
    def overlap(self, other : Area) -> bool:
        if not isinstance(other, Area):
            raise ValueError("An Area object must be used here!")
        return self.get_area().colliderect(other.get_area())
    
    def get_area(self) -> Rect:
        return self._figure

    def __position_adjustment(self, x : int, y : int, width : int, height : int) -> Rect:
        return Rect(int(x-width/2), int(y-height/2), width, height)