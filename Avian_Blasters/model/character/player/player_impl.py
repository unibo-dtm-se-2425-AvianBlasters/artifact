from character_impl import CharacterImpl
from entity import Entity
from power_up_handler import PowerUpHandler
from power_up_handler_impl import PowerUpHandlerImpl
from score import Score
from score_impl import ScoreImpl
from player import Player

class PlayerImpl(CharacterImpl, Player):
    
    def __init__(self, x : int, y : int, width : int, height : int, delta : int, health : int, initial_score : int, initial_multiplier : int):
        super().__init__(x, y, width, height, Entity.TypeArea.PLAYER, delta, health)
        self._power_up_handler = PowerUpHandlerImpl(None)
        self._score = ScoreImpl(initial_score, initial_multiplier)

    def power_up_handler_get(self) -> PowerUpHandler:
        return self._power_up_handler
    
    def move(self, x : int, y : int):
        if self.__can_move():
            super().move(x, y)
    
    def __can_move() -> bool:
        ...
    
    def get_score(self) -> Score:
        return self._score