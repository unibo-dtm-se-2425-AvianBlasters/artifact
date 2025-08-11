from Avian_Blasters.model.item.power_up.power_up import PowerUp

class PowerUpHandlerImpl():
    
    def __init__(self, power_up_active : PowerUp | None):
       self._power_up_active = power_up_active
    
    def collect_power_up(self, power_up : PowerUp):
        ...
    
    def player_update(self):
        ...
    
    def get_current_power_up(self) -> PowerUp | None:
        return self._power_up_active