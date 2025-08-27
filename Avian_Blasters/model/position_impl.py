from Avian_Blasters.model.position import Position

class PositionImpl(Position):
    """PositionImpl is an implementation of Position"""

    def __init__(self, x : int, y : int):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("X and Y must be integer values!")
        self._x = x
        self._y = y

    @property
    def get_x(self) -> int:
        return self._x
    
    @property
    def get_y(self) -> int:
        return self._y