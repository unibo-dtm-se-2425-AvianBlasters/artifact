from player import Player
from item.power_up.power_up import PowerUp

class PowerUpHandlerImpl():
    
    def __init__(self, power_up_active : PowerUp | None):
       self._power_up_active = power_up_active
    
    def collect_power_up(self, power_up : PowerUp, player : Player):
        ...
    
    def player_update(self, player : Player):
        ...
    
    def get_current_power_up(self) -> PowerUp | None:
        return self._power_up_active