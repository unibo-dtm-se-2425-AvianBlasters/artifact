import unittest
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.entity import Entity

class TestPlayer(unittest.TestCase):
    initial_x = 0
    initial_y = 0
    width = 10
    height = 10
    delta = 2
    health = 3
    initial_score = 0
    initial_multiplier = 1
    limit_right = 100
    limit_left = -100

    def setUp(self):
        self.player = PlayerImpl(self.initial_x, self.initial_y,
                                self.width, self.width,self.delta,
                                self.health,self.initial_score, self.initial_multiplier, 
                                self.limit_right, self.limit_left)
    
    def test_inital_status(self):
        self.assertEqual(3, self.player.get_health)
        self.assertEqual(0, self.player.get_score().get_score)
        self.assertEqual(1, self.player.get_score().get_multiplier)
        self.assertEqual(Entity.TypeArea.PLAYER, self.player.get_type)
        self.assertEqual(PlayerStatus.Status.NORMAL, self.player.get_status().get_current_status)

    def test_movement(self):
        ...
    
    def test_going_against_wall(self):
        ...
    
    def test_add_points(self):
        self.assertEqual(0, self.player.get_score().get_score)
        score_increment = 100
        self.player.get_score().add_points(score_increment)
        self.assertEqual(score_increment, self.player.get_score().get_score)
        ...
    
    def test_damage(self):
        ...
    
    def test_shoot(self):
        ...

