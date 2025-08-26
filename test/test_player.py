import unittest
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.entity_impl import EntityImpl
from Avian_Blasters.model.item.projectile.projectile import ProjectileType

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
    fps = 60

    def setUp(self):
        self.player = PlayerImpl(self.initial_x, self.initial_y,
                                self.width, self.width,self.delta,
                                self.health,self.initial_score, self.initial_multiplier, 
                                self.limit_right, self.limit_left, self.fps)
    
    def test_inital_status(self):
        self.assertEqual(self.health, self.player.get_health_handler().current_health)
        self.assertEqual(self.initial_score, self.player.get_score().score)
        self.assertEqual(self.initial_multiplier, self.player.get_score().multiplier)
        self.assertEqual(Entity.TypeArea.PLAYER, self.player.get_type)
        self.assertEqual(PlayerStatus.Status.NORMAL, self.player.get_status().status)

    def verify_movement(self, movement_x, check):
        self.player.move(movement_x)
        if (movement_x * self.delta > self.limit_right or movement_x * self.delta < self.limit_left) and check not in [self.limit_left, self.limit_right]:
            self.assertNotEqual(check, self.player.get_area().get_position_x)
        else:    
            self.assertEqual(check, self.player.get_area().get_position_x)
        self.assertEqual(self.initial_y, self.player.get_area().get_position_y)

    def test_movement(self):
        self.verify_movement(0, self.initial_x)
        movement_x = 10
        self.verify_movement(movement_x, movement_x * self.delta)
        movement_x_2 = -20
        self.verify_movement(movement_x_2, (movement_x + movement_x_2) * self.delta)
        self.verify_movement(movement_x, self.initial_x)
    
    def test_going_against_wall(self):
        movement_x = int (100 / self.delta) + 1
        self.verify_movement(movement_x, self.limit_right)
        movement_x2 = - int (100 / self.delta)
        self.verify_movement(movement_x2, self.initial_x)
        self.verify_movement((-movement_x - 1)/2, (-movement_x - 1)/2 * self.delta)
        self.verify_movement(movement_x2, self.limit_left)
        movement_x3 = 300
        self.verify_movement(movement_x3, self.limit_right)
        
    def test_add_points(self):
        self.assertEqual(self.initial_score, self.player.get_score().score)
        score_increment = 100
        self.player.get_score().add_points(score_increment)
        self.assertEqual(score_increment, self.player.get_score().score)
        self.assertNotEqual(self.initial_score, self.player.get_score().score)
    
    def test_damage(self):
        test_enemy_projectile = EntityImpl(x = 0, y = 0, width = self.width, height = self.height, type = Entity.TypeArea.ENEMY_PROJECTILE, delta = self.delta)
        test_enemy = EntityImpl(x = 0, y = 30, width = self.width, height = self.height, type = Entity.TypeArea.ENEMY, delta = self.delta)
        self.assertTrue(self.player.is_touched([test_enemy_projectile]))
        self.assertEqual(self.health - 1, self.player.get_health_handler().current_health)
        i = 0
        while (i < 5 * self.fps):
            self.assertFalse(self.player.is_touched([test_enemy_projectile]))
            i += 1
        self.assertFalse(self.player.is_touched([test_enemy]))
        test_enemy.move(0,-test_enemy.get_area().get_position_y/self.delta, self.width, self.height)
        self.assertTrue(self.player.is_touched([test_enemy]))
        self.assertEqual(0, self.player.get_health_handler().current_health)
    
    def test_shoot(self):
        shots = self.player.shoot()
        for i in shots:
            self.assertEqual(ProjectileType.NORMAL, i.projectile_type)
        i=0
        while (i < 5):
            shots = self.player.shoot()
            for i in shots:
                self.assertEqual(None, i)
            i += 1
        shots = self.player.shoot()
        for i in shots:
            self.assertEqual(ProjectileType.NORMAL, i.projectile_type)

        
class TestPlayerStatusHandler(unittest.TestCase):
    fps = 60

    def setUp(self):
        self.status_handler = PlayerStatusImpl(PlayerStatus.Status.NORMAL, self.fps)

    def test_set_up(self):
        self.assertEqual(PlayerStatus.Status.NORMAL, self.status_handler.status)

    def test_invulnerability(self):
        cooldown = 15
        self.status_handler.invincibility(cooldown)
        i = 0
        while (i < cooldown * self.fps):
            self.assertEqual(PlayerStatus.Status.INVULNERABLE, self.status_handler.status)
            self.status_handler.update()
            i += 1
        self.assertEqual(PlayerStatus.Status.NORMAL, self.status_handler.status)

    def test_slowing_effect(self):      
        cooldown = 10
        self.status_handler.slow_down(cooldown)
        self.assertEqual(PlayerStatus.Status.SLOWED, self.status_handler.status)
        
        # Update several times and check that it eventually goes back to normal
        i = 0
        while (i < cooldown * self.fps):
            self.assertEqual(PlayerStatus.Status.SLOWED, self.status_handler.status)
            self.status_handler.update()
            i += 1
        
        # After cooldown * fps updates, should be back to normal
        self.assertEqual(PlayerStatus.Status.NORMAL, self.status_handler.status)

    def test_change(self):
        cooldown = 5
        self.status_handler.slow_down(cooldown)
        self.assertEqual(PlayerStatus.Status.SLOWED, self.status_handler.status)
        self.status_handler.invincibility(cooldown)
        self.assertEqual(PlayerStatus.Status.INVULNERABLE, self.status_handler.status)
        print(self.status_handler._cooldown.cooldown)
        i = 0
        while (i < cooldown * self.fps):
            self.status_handler.slow_down(cooldown)
            print(self.status_handler._cooldown.cooldown)
            self.assertEqual(PlayerStatus.Status.INVULNERABLE, self.status_handler.status)
            self.status_handler.update()
            i += 1
        self.assertEqual(PlayerStatus.Status.NORMAL, self.status_handler.status)


class TestScore(unittest.TestCase):
    def setUp(self):
        self.score = ScoreImpl(0,1)
    
    def test_set_up(self):
        self.assertEqual(0, self.score.score)
        self.assertEqual(1, self.score.multiplier)
    
    def test_add_points(self):
        self.addition(1000)
    
    def test_multiplier_change(self):
        initial_multiplier = self.score._multiplier
        new_multiplier = 2
        self.score.multiplier = new_multiplier
        self.assertEqual(new_multiplier, self.score.multiplier)
        self.addition(1000)
        self.score.multiplier = initial_multiplier
        self.assertNotEqual(new_multiplier, self.score.multiplier)
        self.addition(1000)
        
    def addition(self, addition : int):
        initial_score = self.score.score
        self.score.add_points(addition)
        self.assertEqual(initial_score + addition * self.score.multiplier, self.score.score)
    