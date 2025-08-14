class Score:
    
    def add_points(self, points : int):
        ...
    
    @property
    def score(self) -> int:
        ...
    
    @property
    def multiplier(self) -> int:
        ...
    
    @multiplier.setter
    def multiplier(self, multiplier : int):
        ...
    
