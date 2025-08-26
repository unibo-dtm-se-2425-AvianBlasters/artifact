from Avian_Blasters.model.cooldown_handler import CoolDownHandler

class CoolDownHandlerImpl(CoolDownHandler):
    """CoolDownHandlerImpl is the main implementation of the
    CoolDownHandler interface"""
    
    def __init__(self, cooldown : int, refresh_rate : int):
        if refresh_rate <= 0:
            raise ValueError("The refresh rate must be a postive integer!")
        self._refresh_rate = refresh_rate
        self._cooldown = cooldown
        self._actual_countdown = self._cooldown * self._refresh_rate

    @property
    def cooldown(self) -> int:
        return self._cooldown
    
    @cooldown.setter
    def cooldown(self, new_cooldown : int):
        if (new_cooldown < 0):
            raise ValueError("The cooldown must be a positive integer!")
        self._cooldown = max(self._cooldown, new_cooldown)
        self._actual_cooldown = self._cooldown * self._refresh_rate
    
    @property
    def refresh_rate(self) -> int:
        return self._refresh_rate
    
    def update(self):
        if not self.is_over():
            self._actual_cooldown -= 1
    
    def is_over(self) -> bool:
        return self._actual_cooldown <= 0