from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.character.health_handler import HealthHandler
from Avian_Blasters.model.character.player.player_attack_handler import PlayerAttackHandler
from Avian_Blasters.model.character.player.power_up_handler import PowerUpHandler
from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
from Avian_Blasters.model.character.player.score import Score

class Player(Character):
    """This class defines the actions and characteristics of the player character"""
    
    def get_health_handler(self) -> HealthHandler:
        """This is a getter for the HealthHandler of the player"""
        ...
    
    def get_power_up_handler(self) -> PowerUpHandler:
        """This is a getter for the PowerUpHandler of the player
        which allows for opeartions linked to PowerUps"""
        ...

    def player_attack_handler_get(self) -> PlayerAttackHandler:
        ...

    def get_score(self) -> Score:
        """This is a getter to be able to see and/or modify the score
        and the score multiplier"""
        ...
    
    def get_status(self) -> PlayerStatus:
        """This getter returns the handler for PlayerStatus"""
        ...
    
    def move(self, x : int):
        """This method is used to move the player character.
        As the Player can only move from left to right, only the
        variation of its position on the x axis has to be set"""
        ...
    
    def is_touched(self, others : list[Entity]) -> bool:
        """Checks if Player is touching other entities and
        handles damage/status changes related to the
        interactions with enemies and enemy projectiles"""
        ...