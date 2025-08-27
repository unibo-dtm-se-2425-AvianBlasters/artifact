from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
from Avian_Blasters.model.cooldown_handler_impl import CoolDownHandlerImpl

class PlayerStatusImpl(PlayerStatus):
    """PlayerStatusImpl is an implementation of PlayerStatus"""

    def __init__(self, status : PlayerStatus.Status, refresh_rate : int):
        self.__check_instance(status)
        self._status = status
        self._cooldown = CoolDownHandlerImpl(0, refresh_rate)
    
    @property
    def status(self) -> PlayerStatus.Status:
        return self._status
    
    @status.setter
    def status(self, new_status : PlayerStatus.Status):
        self.__check_instance(new_status)
        self._status = new_status
    
    def invincibility(self, cooldown : int):
        self.__change_status(cooldown, PlayerStatus.Status.INVULNERABLE)
    
    def slow_down(self, cooldown : int):
        self.__change_status(cooldown, PlayerStatus.Status.SLOWED)
    
    def update(self):
        if self._status != PlayerStatus.Status.NORMAL:
            self._cooldown.update()
            if self._cooldown.is_over():
                self._status = PlayerStatus.Status.NORMAL
    
    def __change_status(self, cooldown : int, new_status : PlayerStatus.Status):
        if self._status == PlayerStatus.Status.NORMAL or self._status != PlayerStatus.Status.INVULNERABLE:
            self.status = new_status
            self._cooldown.cooldown = cooldown
        elif self._status == new_status:
            self._cooldown.cooldown = cooldown
    
    def __check_instance(self, status : PlayerStatus.Status):
        if not isinstance(status, PlayerStatus.Status):
            raise ValueError("A valid Status must be used!")