class CoolDownHandler():
    """CoolDownHandler is a class that automatises operations
    needing a timer"""
    
    @property
    def cooldown(self) -> int:
        """Gives access to the current cooldown"""
        ...
    
    @cooldown.setter
    def cooldown(self, new_cooldown : int):
        ...
    
    @property
    def refresh_rate(self) -> int:
        """Returns the refresh rate that will multiply the
        countdown to fit the one of the visual representation"""
        ...
    
    def update(self):
        """Automatically decreases the cooldown by one unit"""
        ...
    
    def is_over(self) -> bool:
        """Returns True if the cooldown is over"""
        ...