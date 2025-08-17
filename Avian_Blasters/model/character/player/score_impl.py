from Avian_Blasters.model.character.player.score import Score

class ScoreImpl(Score):
    """ScoreImpl is an implementation of Score"""
    
    def __init__(self, initial_score : int, initial_multiplier : int):
        self._score = initial_score
        self._multiplier = initial_multiplier

    def add_points(self, points : int):
        self._score += points * self._multiplier
    
    @property
    def score(self) -> int:
        return self._score
    
    @property
    def multiplier(self) -> int:
        return self._multiplier
    
    @multiplier.setter
    def multiplier(self, multiplier : int):
        self._multiplier = multiplier
    
