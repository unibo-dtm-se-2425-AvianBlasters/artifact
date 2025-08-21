from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus

class PlayerStatusImpl(PlayerStatus):
    """PlayerStatusImpl is an implementation of PlayerStatus"""

    def __init__(self, status : PlayerStatus.Status):
        self._status = status
        self._cooldown = 0
    
    @property
    def status(self) -> PlayerStatus.Status:
        return self._status
    
    @status.setter
    def status(self, new_status : PlayerStatus.Status):
        self._status = new_status
    
    def invincibility(self, cooldown):
        if self._status != PlayerStatus.Status.INVULNERABLE:
            self._status = PlayerStatus.Status.INVULNERABLE
            self._cooldown = cooldown
    
    def slow_down(self, cooldown):
        """Apply slowing effect from bat sound wave attack"""
        if self._status == PlayerStatus.Status.NORMAL:
            self._status = PlayerStatus.Status.SLOWED
            self._cooldown = cooldown
        elif self._status == PlayerStatus.Status.SLOWED:
            # Extend the slowing effect if already slowed
            self._cooldown = max(self._cooldown, cooldown)
    
    def update(self):
        if self._status != PlayerStatus.Status.NORMAL:
            self._cooldown -= 1
            if self._cooldown == 0:
                self._status = PlayerStatus.Status.NORMAL