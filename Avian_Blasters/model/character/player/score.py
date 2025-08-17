class Score:
    """This class handles how points are collected by the player"""

    
    def add_points(self, points : int):
        """Add a certain amount of points to the score"""
        ...
    
    @property
    def score(self) -> int:
        """Access the current value of the score"""
        ...
    
    @property
    def multiplier(self) -> int:
        """Access the current score multiplier"""
        ...
    
    @multiplier.setter
    def multiplier(self, multiplier : int):
        ...
    
