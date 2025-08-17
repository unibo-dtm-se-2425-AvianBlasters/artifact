from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl
from Avian_Blasters.model.item.power_up.power_up_types.double_fire_power_up import DoubleFirePowerUp
from Avian_Blasters.model.item.power_up.power_up_types.invulnerability_power_up import InvulnerabilityPowerUp
from Avian_Blasters.model.item.power_up.power_up_types.laser_power_up import LaserPowerUp


class PowerUpFactory:

    _available_types = {
        PowerUpType.LASER: (LaserPowerUp, True, 10.0),
        PowerUpType.INVULNERABILITY: (InvulnerabilityPowerUp, True, 10.0),
        PowerUpType.DOUBLE_FIRE: (DoubleFirePowerUp, True, 7.0)
    } 

    def create_power_up(self, power_up_type: PowerUpType, x: int, y: int, width: int , height: int, type_area: Entity.TypeArea, delta: int = DEFAULT_DELTA) -> PowerUpImpl:
        
        if not isinstance(type_area, Entity.TypeArea):
            raise ValueError("Invalid type area")

        if not isinstance(power_up_type, PowerUpType):
            raise ValueError("Invalid projectile type")
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers")  

        _power_up_parameters = self._available_types.get(power_up_type)

        if _power_up_parameters is None:
            raise ValueError(f"Unsupported power-up type: {power_up_type}")
        
        _power_up_type, _is_timed, _duration = _power_up_parameters
        
        return _power_up_type(x, y, width, height, type_area, power_up_type, _is_timed, _duration, delta)