from Avian_Blasters.model.character.player.score import Score

class ScoreImpl(Score):
    
    def __init__(self, initial_score : int, initial_multiplier : int):
        self._score = initial_score
        self._multiplier = initial_multiplier

    def add_points(self, points : int):
        self._score += points
    
    @property
    def get_score(self) -> int:
        return self._score
    
    @property
    def get_multiplier(self) -> int:
        return self._multiplier
    
    def set_multiplier(self, multiplier : int):
        self._multiplier = multiplier
    
