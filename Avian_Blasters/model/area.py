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
    
    @property
    def height(self) -> int:
        ...
    
    def overlap(self, other) -> bool:
        ...
    
    def get_area(self) -> Rect:
        ...