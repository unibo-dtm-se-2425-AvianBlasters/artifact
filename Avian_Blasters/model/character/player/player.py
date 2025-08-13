from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.character.player.power_up_handler import PowerUpHandler
from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
from Avian_Blasters.model.character.player.score import Score

class Player(Character):
    
    def get_power_up_handler(self) -> PowerUpHandler:
        ...

    def get_score(self) -> Score:
        ...
    
    def get_status(self) -> PlayerStatus:
        ...