from Avian_Blasters.model.character.health_handler import HealthHandler


class HealthHandlerImpl(HealthHandler):
    def __init__(self, max_health: int) -> None:
        if max_health <= 0:
            raise ValueError("max_health must be positive")
        self._max_health = max_health
        self._current_health = max_health

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def current_health(self) -> int:
        return self._current_health

    def take_damage(self, damage: int) -> None:
        if damage <= 0:
            return
        self._current_health = max(0, self._current_health - damage)

    def heal(self, amount: int) -> None:  
        if amount <= 0:
            return
        self._current_health = min(self._max_health, self._current_health + amount)
    
    def is_dead(self) -> bool:
        return self._current_health <= 0
