from __future__ import annotations

import pygame
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.player.power_up_handler import PowerUpHandler
from Avian_Blasters.model.item.power_up.power_up import PowerUp


class PowerUpHandlerImpl(PowerUpHandler):
    
    def __init__(self, power_up_active : PowerUp | None):
       self._power_up_active = power_up_active
       self._start_time = None
    
    def collect_power_up(self, power_up : PowerUp, player: Player):
        if not power_up.collected:
            if self._power_up_active:
                self._power_up_active.remove_effect(player)
                self._power_up_active.collected = False

            self._power_up_active = power_up
            self._power_up_active.collected = True
            self._power_up_active.apply_effect(player)
            if power_up.is_timed:
                self._start_time = pygame.time.get_ticks()
            self._power_up_active.destroy() #it destroys the item after applying the effect

    
    def player_update(self, player: Player):
        if self._power_up_active and self._power_up_active.is_timed:
            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - self._start_time) / 1000.0
            if time_elapsed >= self._power_up_active.duration:
                self._power_up_active.remove_effect(player)
                self._power_up_active = None
                self._start_time = None
    
    def get_current_power_up(self) -> PowerUp | None:
        return self._power_up_active