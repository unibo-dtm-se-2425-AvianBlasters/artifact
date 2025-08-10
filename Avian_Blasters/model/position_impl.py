from position import Position

class PositionImpl(Position):

    def __init__(self, x : int, y : int):
        self._x = x
        self._y = y

    @property
    def get_x(self) -> int:
        return self._x
    
    @property
    def get_y(self) -> int:
        return self._y