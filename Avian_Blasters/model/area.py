from pygame import Rect

class Area:
    
    @property
    def get_position_x(self) -> int:
        ...

    @property
    def get_position_y(self) -> int:
        ...

    @property
    def width(self) -> int:
        ...
    
    @width.setter
    def width(self, new_width : int):
        ...
    
    @property
    def height(self) -> int:
        ...
    
    @height.setter
    def height(self, new_height : int):
        ...
    
    def overlap(self, other) -> bool:
        ...
    
    def get_area(self) -> Rect:
        ...