from Avian_Blasters.model.character.character_impl import CharacterImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
from Avian_Blasters.model.character.player.player_status_handler_impl import PlayerStatusImpl
from Avian_Blasters.model.character.player.power_up_handler import PowerUpHandler
from Avian_Blasters.model.character.player.power_up_handler_impl import PowerUpHandlerImpl
from Avian_Blasters.model.character.player.score import Score
from Avian_Blasters.model.character.player.score_impl import ScoreImpl

class PlayerImpl(CharacterImpl, Player):
    
    def __init__(self, x : int, y : int, width : int, height : int, delta : int, health : int, initial_score : int, initial_multiplier : int, limit_right : int, limit_left : int):
        super().__init__(x, y, width, height, Entity.TypeArea.PLAYER, delta, health)
        self._power_up_handler = PowerUpHandlerImpl(None)
        self._score = ScoreImpl(initial_score, initial_multiplier)
        self._status_handler = PlayerStatusImpl(PlayerStatus.Status.NORMAL)
        self._limit_r = limit_right
        self._limit_l = limit_left

    def power_up_handler_get(self) -> PowerUpHandler:
        return self._power_up_handler
    
    def move(self, x : int):
        if self.__can_move(x):
            super().move(x, self.get_area().get_position_y, self.get_area().get_width, self.get_area().get_height)
    
    def __can_move(self, x : int) -> bool:
        return (x != (self._limit_r - self.get_area().get_width/2) and x != (self._limit_l + self.get_area().get_height))
                
    def get_score(self) -> Score:
        return self._score
    
    def is_touched(self, others: list[Entity]):
        if self._status_handler.get_current_status != PlayerStatus.Status.INVULNERABLE:
            for i in others:
                if i.get_type == Entity.TypeArea.ENEMY or Entity.TypeArea.ENEMY_PROJECTILE:
                    if super().is_touched(i):
                        damage = 3 if i.get_type == Entity.TypeArea.ENEMY else 1
                        self._health -= damage
                        if self.get_health <= 0:
                            pass
                        else:
                            self._status_handler.set_current_status(PlayerStatus.Status.INVULNERABLE)
    
    def get_status(self) -> PlayerStatus:
        return self._status_handler
