import unittest
from Avian_Blasters.model.character.player.player_impl import PlayerImpl
from Avian_Blasters.model.entity import Entity

class testPlayer(unittest.TestCase):
    initial_x = 0
    initial_y = 0
    width = 10
    height = 10
    delta = 2
    health = 3
    initial_score = 0
    initial_multiplier = 1

    def setUp(self):
        self.player = PlayerImpl(self.initial_x, self.initial_y,
                                self.width, self.width,self.delta,
                                self.health,self.initial_score, self.initial_multiplier)
    
    def test_inital_status(self):
        self.assertEqual
        self.assertEqual(3, self.player.get_health())
        self.assertEqual(0, self.player.get_score().get_score())
        self.assertEqual(0, self.player.get_score().get_multiplier())
        self.assertEqual(Entity.TypeArea.PLAYER, self.player.get_type())

    def test_movement(self):
        ...
    
    def test_going_against_wall(self):
        ...
    
    def test_add_points(self):
        self.assertEqual(0, self.player.get_score().get_score())
        score_increment = 100
        self.player.get_score().add_points(score_increment)
        self.assertEqual(score_increment, self.player.get_score().get_score())
        ...
    
    def test_damage(self):
        ...
    
    def test_shoot(self):
        ...

