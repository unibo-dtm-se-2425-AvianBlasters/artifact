from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus

class PlayerStatusImpl(PlayerStatus):

    def __init__(self, status : PlayerStatus.Status):
        self._status = status
    
    @property
    def status(self) -> PlayerStatus.Status:
        return self._status
    
    @status.setter
    def status(self, new_status : PlayerStatus.Status):
        self._status = new_status