from Avian_Blasters.model.character.character_impl import CharacterImpl
from Avian_Blasters.model.character.player.player_attack_handler import PlayerAttackHandler
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
from Avian_Blasters.model.character.player.player_status_handler_impl import PlayerStatusImpl
from Avian_Blasters.model.character.player.power_up_handler import PowerUpHandler
from Avian_Blasters.model.character.player.power_up_handler_impl import PowerUpHandlerImpl
from Avian_Blasters.model.character.player.score import Score
from Avian_Blasters.model.character.player.score_impl import ScoreImpl
from Avian_Blasters.model.character.player.player_attack_handler import PlayerAttackHandler
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

DEFAULT_COOLDOWN = 30

class PlayerImpl(CharacterImpl, Player):
    """PlayerImpl is an implementation of Player that takes advantage of
    the implementations present in CharacterImpl"""
    
    def __init__(self, x : int, y : int, width : int, height : int, delta : int, health : int, initial_score : int, initial_multiplier : int, limit_right : int, limit_left : int):
        super().__init__(x, y, width, height, Entity.TypeArea.PLAYER, delta, health)
        self._power_up_handler = PowerUpHandlerImpl(None)
        self._attack_handler = PlayerAttackHandler(ProjectileFactory(), 3, ProjectileType.NORMAL, ) # Needs a projectile factory
        self._score = ScoreImpl(initial_score, initial_multiplier)
        self._status_handler = PlayerStatusImpl(PlayerStatus.Status.NORMAL)
        self._attack_handler = PlayerAttackHandler(ProjectileFactory(), PlayerAttackHandler.PLAYER_PROJECTILE_SPEED, ProjectileType.NORMAL, )
        self._limit_r = limit_right
        self._limit_l = limit_left

    def get_power_up_handler(self) -> PowerUpHandler:
        return self._power_up_handler
    
    def player_attack_handler_get(self) -> PlayerAttackHandler:
        return self._attack_handler
    
    def move(self, x : int):
        if self.__can_move(x):
            super().move(x, self.get_area().get_position_y, self.get_area().width, self.get_area().height)
        elif x>=0:
            super().move((self._limit_r - self.get_area().get_position_x)/self._delta, self.get_area().get_position_y, self.get_area().width, self.get_area().height)
        else:
            super().move((self._limit_l - self.get_area().get_position_x)/self._delta, self.get_area().get_position_y, self.get_area().width, self.get_area().height)
    
    def __can_move(self, x : int) -> bool:
        return abs(self._limit_r) > abs(x * self._delta + self.get_area().get_position_x + self.get_area().width/2) and abs(self._limit_l) > abs(x * self._delta + self.get_area().get_position_x - self.get_area().width/2)
        #(abs(x*self._delta) <= abs(self._limit_r - self.get_area().get_width/2 - self.get_area().get_position_x) and abs(x*self._delta) <= abs(self._limit_l - self.get_area().get_width/2) - self.get_area().get_position_x)        
                
    def get_score(self) -> Score:
        return self._score
    
    def is_touched(self, others: list[Entity]) -> bool:
        if self._status_handler.status != PlayerStatus.Status.INVULNERABLE:
            for i in others:
                if i.get_type == Entity.TypeArea.ENEMY or Entity.TypeArea.ENEMY_PROJECTILE:
                    if super().is_touched(i):
                        damage = 3 if i.get_type == Entity.TypeArea.ENEMY else 1
                        self.get_health_handler().take_damage(damage)
                        if self.get_health_handler().current_health > 0:
                            self._status_handler.invincibility(DEFAULT_COOLDOWN)
                        return True
        else:
            self._status_handler.update()
            return False
        return False


    
    def get_status(self) -> PlayerStatus:
        return self._status_handler
    
    def shoot(self) -> list[Projectile]:
        return self._attack_handler.try_attack(self)