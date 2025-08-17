class Position:
    """Position defines the central x and y placement of game
    elements"""

    @property
    def get_x(self) -> int:
        """Gives access to the x axis position"""
        ...
    
    @property
    def get_y(self) -> int:
        """Gives access to the y axis position"""
        ...