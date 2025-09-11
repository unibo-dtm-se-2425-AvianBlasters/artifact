from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl


class TimedPowerUp(PowerUpImpl):
    """ TimedPowerUp is a class that represents a power-up that has a duration"""
    
    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, duration: float, is_timed: bool = True, delta: int = DEFAULT_DELTA):
        super().__init__(x, y, width, height, type, power_up_type, is_timed, duration, delta)

    def remove_effect(self, player : Player):
        """ Remove the effect of the power-up from the player """
        ...
        
      
