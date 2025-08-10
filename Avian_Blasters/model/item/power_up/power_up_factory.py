from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType
from Avian_Blasters.model.position import Position


class PowerUpFactory:
    def create_power_up(self, power_up_type: PowerUpType, position: Position) -> PowerUp:
        ...