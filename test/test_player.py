import unittest
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
# from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
# from Avian_Blasters.model.item.item import Direction

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
        self.assertEqual(self.health, self.player.get_health)
        self.assertEqual(self.initial_score, self.player.get_score().get_score)
        self.assertEqual(self.initial_multiplier, self.player.get_score().get_multiplier)
        self.assertEqual(Entity.TypeArea.PLAYER, self.player.get_type)
        self.assertEqual(PlayerStatus.Status.NORMAL, self.player.get_status().get_current_status)

    def test_movement(self):
        movement_x = 10
        self.player.move(movement_x)
        self.assertEqual(movement_x * self.delta, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        movement_x_2 = -20
        self.player.move(movement_x_2)
        self.assertEqual(movement_x * self.delta + movement_x_2 * self.delta, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        self.player.move(movement_x)
        self.assertEqual(self.initial_x, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
    
    def test_going_against_wall(self):
        movement_x = 51
        self.player.move(movement_x)
        self.assertEqual(self.limit_right, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        movement_x2 = -50
        self.player.move(movement_x2)
        self.assertEqual(self.initial_x, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        self.player.move((-movement_x - 1)/2)
        self.assertEqual(-52, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        self.player.move(movement_x2)
        self.assertEqual(self.limit_left, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        self.player.move(300)
        self.assertEqual(self.limit_right, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)
        
    def test_add_points(self):
        self.assertEqual(self.initial_score, self.player.get_score().get_score)
        score_increment = 100
        self.player.get_score().add_points(score_increment)
        self.assertEqual(score_increment, self.player.get_score().get_score)
        self.assertNotEqual(self.initial_score, self.player.get_score().get_score)
    
    def test_damage(self):
        ...
    
    def test_shoot(self):
        self.assertEqual(ProjectileType.NORMAL, self.player.shoot().projectile_type)
        self.assertEqual(None, self.player.shoot())
        

