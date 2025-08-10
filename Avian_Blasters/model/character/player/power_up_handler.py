from player import Player
from item.power_up.power_up import PowerUp

class PowerUpHandler():

    def collect_power_up(self, power_up : PowerUp, player : Player):
        ...
    
    def player_update(self, player : Player):
        ...
    
    def get_current_power_up(self) -> PowerUp | None:
        ...