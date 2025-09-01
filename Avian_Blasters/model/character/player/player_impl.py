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
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

DEFAULT_COOLDOWN = 5

class PlayerImpl(CharacterImpl, Player):
    """PlayerImpl is an implementation of Player that takes advantage of
    the implementations present in CharacterImpl"""
    
    def __init__(self, x : int, y : int, width : int, height : int, delta : int, health : int, initial_score : int, initial_multiplier : int, limit_right : int, limit_left : int, fps : int):
        super().__init__(x, y, width, height, Entity.TypeArea.PLAYER, delta, health)
        self._power_up_handler = PowerUpHandlerImpl(None)
        self._score = ScoreImpl(initial_score, initial_multiplier)
        self._status_handler = PlayerStatusImpl(PlayerStatus.Status.NORMAL, fps)
        self._attack_handler = PlayerAttackHandler(ProjectileFactory(), PlayerAttackHandler.PLAYER_PROJECTILE_SPEED, ProjectileType.NORMAL, )
        if limit_right <= limit_left:
            raise ValueError("The right limit must be bigger than the left one!")
        self._limit_r = limit_right
        self._limit_l = limit_left
        self._default_speed = delta
        self._fps = fps
        self._is_hurt = False

    def get_power_up_handler(self) -> PowerUpHandler:
        return self._power_up_handler
    
    def get_player_attack_handler(self) -> PlayerAttackHandler:
        return self._attack_handler
    
    def move(self, x : int):
        if not isinstance(x, int):
            raise ValueError("X must be a positive integer!")
        effective_movement = self.__effective_movement(x)
        dx = 0
        dy = 0
        if self.__can_move(effective_movement):
            dx = effective_movement
        elif effective_movement > 0:
            dx = (self._limit_r - self.get_area().get_position_x) / self._delta
        elif effective_movement < 0:
            dx = (self._limit_l - self.get_area().get_position_x) / self._delta
        super().move(dx, dy, self.get_area().width, self.get_area().height)

    def __can_move(self, x : int) -> bool:
        if x > 0:
            return self._limit_r > (x * self._delta + self.get_area().get_position_x + self.get_area().width / 2)
        elif x < 0:
            return self._limit_l < (x * self._delta + self.get_area().get_position_x - self.get_area().width / 2)
        return True

    def __effective_movement(self, x : int) -> int:
        # Apply movement reduction if player is slowed by bat sound waves
        if self._status_handler.status == PlayerStatus.Status.SLOWED:
            # Reduce movement speed by 50% when slowed
            return int(x * 0.5)
        else:
            return x
                
    def get_score(self) -> Score:
        return self._score
    
    def is_touched(self, others: list[Entity]) -> bool:
        self.__update()
        if self._status_handler.status != PlayerStatus.Status.INVULNERABLE:
            for i in others:
                if not isinstance(i, Entity):
                    raise ValueError("A list of Entity objects must be used!")
                if i.get_type == Entity.TypeArea.ENEMY or i.get_type == Entity.TypeArea.ENEMY_PROJECTILE:
                    if super().is_touched(i):
                        # Check if it's a sound wave projectile from bats
                        if hasattr(i, 'projectile_type') and i.projectile_type == ProjectileType.SOUND_WAVE:
                            # Sound waves don't deal damage but slow the player
                            self._status_handler.slow_down(DEFAULT_COOLDOWN)
                        else:
                            # Regular damage from enemies or normal projectiles
                            damage = 3 if i.get_type == Entity.TypeArea.ENEMY else 1
                            self.get_health_handler().take_damage(damage)
                            if self.get_health_handler().current_health > 0:
                                self._status_handler.invincibility(DEFAULT_COOLDOWN)
                            self._is_hurt = True
                        return True
                    elif i.get_type == Entity.TypeArea.ENEMY and self.__check_if_enemy_crossed(i):
                        self.__instant_defeat()
                        return True
        else:
            self._status_handler.update()
            if self._status_handler.status != PlayerStatus.Status.INVULNERABLE:
                self._is_hurt = False
            for i in others:
                if not isinstance(i, Entity):
                    raise ValueError("A list of Entity objects must be used!")
                if i.get_type == Entity.TypeArea.ENEMY:
                    if self.__check_if_enemy_crossed(i):
                        self.__instant_defeat()
                        return True
        return False

    def __check_if_enemy_crossed(self, enemy : Enemy) -> bool:
        return enemy.get_area().get_position_y == self.get_area().get_position_y
    
    def __instant_defeat(self):
        damage = 3
        self.get_health_handler().take_damage(damage)
        print("Oh no! The Avians have reached the car. Maaaaan... Game Over!")
                        

    def get_status(self) -> PlayerStatus:
        return self._status_handler
    
    def shoot(self) -> list[Projectile]:
        return self._attack_handler.try_attack(self)
    
    def __update(self):
        if self.get_status().status == PlayerStatus.Status.SLOWED and self._delta != self._default_speed/2:
            self.delta = int (self._default_speed/2)
        elif self.get_status().status != PlayerStatus.Status.SLOWED and self._delta == self._default_speed/2:
            self.delta = self._default_speed

    def is_hurt(self) -> bool:
        return self._is_hurt
        