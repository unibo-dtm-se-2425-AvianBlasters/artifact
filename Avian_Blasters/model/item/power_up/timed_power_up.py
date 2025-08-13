from abc import abstractmethod
import pygame
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item_impl import DEFAULT_DELTA
from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl


class TimedPowerUp(PowerUpImpl):
    def __init__(self, x: int, y: int, width: int, height: int, type: Entity.TypeArea, power_up_type: PowerUpType, duration: float, delta: int = DEFAULT_DELTA):
        super().__init__(x, y, width, height, type, power_up_type, delta)
        self._duration = duration
        self._start_time = None
        self._activated = False

    def effect_on_player(self, player : Player):
        if not self._activated:
            self._start_time = pygame.time.get_ticks()
            self._activated = True
            self.apply_effect(player)
            #The PowerUpHandler should handle the removal of the collected item once the effect is applied

    def update(self, player: Player):
        if self._activated:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self._start_time) / 1000.0
            if elapsed_time >= self._duration:
                self.disable(player)

    def disable(self, player: Player):
        self._activated = False
        self._start_time = None
        self.remove_effect(player)