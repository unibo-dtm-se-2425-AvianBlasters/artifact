from Avian_Blasters.model.character.player.score import Score

class ScoreImpl(Score):
    """ScoreImpl is an implementation of Score"""
    
    def __init__(self, initial_score : int, initial_multiplier : int):
        if initial_score < 0:
            raise ValueError("The score must be at least zero!")
        self._score = initial_score
        if initial_multiplier <= 0:
            raise ValueError("The multiplier must be a postive integer!")
        self._multiplier = initial_multiplier

    def add_points(self, points : int):
        addition = points * self.multiplier
        if addition < 0 and abs(addition) > abs(self._score): 
            self._score = 0
        else:
            self._score += points * self._multiplier
    
    @property
    def score(self) -> int:
        return self._score
    
    @property
    def multiplier(self) -> int:
        return self._multiplier
    
    @multiplier.setter
    def multiplier(self, multiplier : int):
        if isinstance(multiplier, int) and multiplier >= 1:
            self._multiplier = multiplier
        else:
            raise Exception("The multiplier must be a postive integer!")
    
