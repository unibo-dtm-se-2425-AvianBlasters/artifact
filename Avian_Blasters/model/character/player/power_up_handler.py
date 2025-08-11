from Avian_Blasters.model.item.power_up.power_up import PowerUp

class PowerUpHandler():

    def collect_power_up(self, power_up : PowerUp):
        ...
    
    def player_update(self):
        ...
    
    def get_current_power_up(self) -> PowerUp | None:
        ...