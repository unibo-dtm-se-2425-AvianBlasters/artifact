from model.character.character import Character
from power_up_handler import PowerUpHandler
from player_status_handler import PlayerStatus
from score import Score

class Player(Character):
    
    def power_up_handler_get(self) -> PowerUpHandler:
        ...

    def get_score(self) -> Score:
        ...
    
    def get_status(self) -> PlayerStatus:
        ...