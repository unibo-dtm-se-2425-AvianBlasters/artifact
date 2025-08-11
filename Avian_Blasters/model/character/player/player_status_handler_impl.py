from player_status_handler import PlayerStatus

class PlayerStatusImpl(PlayerStatus):

    def __init__(self, status : PlayerStatus.Status):
        self._status = status
    
    @property
    def get_current_status(self) -> PlayerStatus.Status:
        return self._status
    
    def set_current_status(self, new_status : PlayerStatus.Status):
        self._status = new_status