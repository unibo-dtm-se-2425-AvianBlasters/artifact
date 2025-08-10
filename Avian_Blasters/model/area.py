from position import Position

class Area:
    
    @property
    def get_position_x(self) -> int:
        ...

    @property
    def get_position_y(self) -> int:
        ...

    @property
    def get_width(self) -> int:
        ...
    
    @property
    def get_height(self) -> int:
        ...
    
    def overlap(self, other) -> bool:
        ...