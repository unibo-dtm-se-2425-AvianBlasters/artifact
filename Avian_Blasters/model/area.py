from pygame import Rect

class Area:
    """Area defines the area that game elements occupy and how
    to handle overlap with other ones"""
    
    @property
    def get_position_x(self) -> int:
        """Gives access to the central x position of the entity"""
        ...

    @property
    def get_position_y(self) -> int:
        """Gives access to the central y position of the entity"""
        ...

    @property
    def width(self) -> int:
        """Gives access to the width property"""
        ...
    
    @width.setter
    def width(self, new_width : int):
        ...
    
    @property
    def height(self) -> int:
        """Gives access to the height property"""
        ...
    
    @height.setter
    def height(self, new_height : int):
        ...
    
    def overlap(self, other) -> bool:
        """Checks whether another area is overlapping with
        the one that is calling this method"""
        ...
    
    def get_area(self) -> Rect:
        """Returns the area as a pygame Rect"""
        ...