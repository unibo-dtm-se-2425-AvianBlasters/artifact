import unittest
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import EnemyAttackHandler, BirdAttackHandler, BatAttackHandler
from Avian_Blasters.model.character.health_handler_impl import HealthHandlerImpl
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory
from Avian_Blasters.model.character.enemy.enemy_factory import create_enemy_formation



class TestEnemyHealthHandler(unittest.TestCase):
    def setUp(self):
        self.health_handler = HealthHandlerImpl(max_health=100)

    def test_initial_health(self):
        self.assertEqual(100, self.health_handler.max_health)
        self.assertEqual(100, self.health_handler.current_health)
        self.assertFalse(self.health_handler.is_dead())

    def test_take_damage(self):
        self.health_handler.take_damage(30)
        self.assertEqual(70, self.health_handler.current_health)
        self.assertFalse(self.health_handler.is_dead())

    def test_take_fatal_damage(self):
        self.health_handler.take_damage(150)  # More than max health
        self.assertEqual(0, self.health_handler.current_health)
        self.assertTrue(self.health_handler.is_dead())

    def test_heal(self):
        self.health_handler.take_damage(40)
        self.health_handler.heal(20)
        self.assertEqual(80, self.health_handler.current_health)

    def test_heal_over_max(self):
        self.health_handler.take_damage(10)
        self.health_handler.heal(50)  # More than needed
        self.assertEqual(100, self.health_handler.current_health)  # Capped at max

    def test_invalid_health(self):
        with self.assertRaises(ValueError):
            HealthHandlerImpl(max_health=0)


class TestAttackHandlers(unittest.TestCase):
    def setUp(self):
        self.factory = ProjectileFactory()
        self.always_attack_handler = EnemyAttackHandler(self.factory, fire_chance=1.0, cooldown_steps=20)
        self.never_attack_handler = EnemyAttackHandler(self.factory, fire_chance=0.0, cooldown_steps=20)
        self.cooldown_handler = EnemyAttackHandler(self.factory, fire_chance=1.0, cooldown_steps=3)

    def test_always_attack(self):
        enemy = EnemyImpl(x=50, y=60, width=16, height=12, speed=2, max_health=10)
        projectiles = self.always_attack_handler.try_attack(enemy)
        self.assertEqual(1, len(projectiles))
        projectile = projectiles[0]
        self.assertEqual(50, projectile.get_area().get_position_x)

    def test_never_attack(self):
        enemy = EnemyImpl(x=50, y=60, width=16, height=12, speed=2, max_health=10)
        projectiles = self.never_attack_handler.try_attack(enemy)
        self.assertEqual(0, len(projectiles))

    def test_cooldown_behavior(self):
        enemy = EnemyImpl(x=50, y=60, width=16, height=12, speed=2, max_health=10)
        
        # First attack should succeed
        projectiles1 = self.cooldown_handler.try_attack(enemy)
        self.assertEqual(1, len(projectiles1))
        
        # Next 3 attacks should fail due to cooldown
        for _ in range(3):
            projectiles = self.cooldown_handler.try_attack(enemy)
            self.assertEqual(0, len(projectiles))
        
        # After cooldown, should succeed again
        projectiles2 = self.cooldown_handler.try_attack(enemy)
        self.assertEqual(1, len(projectiles2))

    def test_bird_attack_handler(self):
        bird_handler = BirdAttackHandler(self.factory, fire_chance=1.0, cooldown_steps=20)
        enemy = EnemyImpl(x=100, y=200, width=20, height=16, speed=3, max_health=5)
        
        projectiles = bird_handler.try_attack(enemy)
        self.assertEqual(1, len(projectiles))

    def test_bat_attack_handler(self):
        bat_handler = BatAttackHandler(self.factory, fire_chance=1.0, cooldown_steps=20)
        enemy = EnemyImpl(x=80, y=150, width=18, height=14, speed=4, max_health=3)
        
        projectiles = bat_handler.try_attack(enemy)
        self.assertEqual(1, len(projectiles))
        
        # Verify that bat creates sound wave projectiles
        projectile = projectiles[0]
        from Avian_Blasters.model.item.projectile.projectile import ProjectileType
        self.assertEqual(ProjectileType.SOUND_WAVE, projectile.projectile_type)


class TestEnemyImpl(unittest.TestCase):
    def setUp(self):
        self.enemy = EnemyImpl(x=100, y=50, width=20, height=16, speed=3, max_health=25)

    def test_initial_state(self):
        self.assertEqual(100, self.enemy.x)
        self.assertEqual(50, self.enemy.y)
        self.assertEqual(20, self.enemy.width)
        self.assertEqual(16, self.enemy.height)
        self.assertEqual(25, self.enemy.get_health)
        self.assertFalse(self.enemy.is_dead())

    def test_movement(self):
        initial_y = self.enemy.y
        self.enemy.move()
        self.assertEqual(initial_y + 3, self.enemy.y)  # Should move down by speed

    def test_damage_and_death(self):
        self.enemy.take_damage(10)
        self.assertEqual(15, self.enemy.get_health)
        self.assertFalse(self.enemy.is_dead())
        
        self.enemy.take_damage(15)
        self.assertEqual(0, self.enemy.get_health)
        self.assertTrue(self.enemy.is_dead())

    def test_attack_delegation(self):
        # Set up enemy with guaranteed attack
        factory = ProjectileFactory()
        always_attack = EnemyAttackHandler(factory, fire_chance=1.0, cooldown_steps=20)
        enemy = EnemyImpl(
            x=75, y=100, width=16, height=12, speed=2, max_health=10,
            attack_handler=always_attack
        )
        
        projectile = enemy.attack()
        self.assertIsNotNone(projectile)
        
        for _ in range(20):
            projectile2 = enemy.shoot()
            self.assertIsNone(projectile2)
        
        projectile2 = enemy.shoot()
        self.assertIsNotNone(projectile2)
        
        for _ in range(20):
            projectile2 = enemy.shoot()
            self.assertIsNone(projectile2)
        
        # Test shoot_all() method
        projectiles = enemy.shoot_all()
        self.assertEqual(1, len(projectiles))


class TestBird(unittest.TestCase):
    def setUp(self):
        self.bird = Bird(x=200, y=80, width=16, height=12, speed=4, health=15)

    def test_initial_state(self):
        self.assertEqual(200, self.bird.x)
        self.assertEqual(80, self.bird.y)
        self.assertEqual(16, self.bird.width)
        self.assertEqual(12, self.bird.height)
        self.assertEqual(15, self.bird.get_health)

    def test_wave_movement(self):
        initial_x = self.bird.x
        initial_y = self.bird.y
        
        # Move several times and track horizontal oscillation
        positions = []
        for _ in range(10):
            self.bird.move()
            positions.append(self.bird.x)
        
        # Bird should move down consistently
        self.assertEqual(initial_y + 4 * 10, self.bird.y)
        
        # Bird should oscillate horizontally around its base position
        max_x = max(positions)
        min_x = min(positions)
        self.assertGreater(max_x - min_x, 0)  # Should have horizontal movement

    def test_wave_pattern_is_sinusoidal(self):
        """Test that bird follows a proper wave pattern"""
        base_x = self.bird.x
        positions = []
        
        # Collect many positions to see the wave pattern
        for i in range(50):
            self.bird.move()
            offset = self.bird.x - base_x
            positions.append(offset)
        
        # The movement should be roughly sinusoidal
        # Check that it oscillates between positive and negative values
        has_positive = any(pos > 5 for pos in positions)
        has_negative = any(pos < -5 for pos in positions)
        self.assertTrue(has_positive and has_negative, "Bird should oscillate horizontally")


class TestBat(unittest.TestCase):
    def setUp(self):
        self.bat = Bat(x=150, y=120, width=14, height=10, speed=5, health=8)

    def test_initial_state(self):
        self.assertEqual(150, self.bat.x)
        self.assertEqual(120, self.bat.y)
        self.assertEqual(14, self.bat.width)
        self.assertEqual(10, self.bat.height)
        self.assertEqual(8, self.bat.get_health)

    def test_no_target_movement(self):
        """Bat should only move down when no target is set"""
        initial_x = self.bat.x
        initial_y = self.bat.y
        
        self.bat.move()
        
        self.assertEqual(initial_x, self.bat.x)  # No horizontal movement
        self.assertEqual(initial_y + max(1, 5 // 2), self.bat.y)  # Slow descent

    def test_homing_behavior_right(self):
        """Test bat homing towards a target to the right"""
        self.bat.set_target_x(300)  # Target to the right
        initial_x = self.bat.x
        
        self.bat.move()
        
        self.assertGreater(self.bat.x, initial_x)  # Should move right

    def test_homing_behavior_left(self):
        """Test bat homing towards a target to the left"""
        self.bat.set_target_x(50)  # Target to the left
        initial_x = self.bat.x
        
        self.bat.move()
        
        self.assertLess(self.bat.x, initial_x)  # Should move left

    def test_homing_with_multiple_moves(self):
        """Test that bat approaches target over multiple moves"""
        target_x = 300
        self.bat.set_target_x(target_x)
        
        distances = []
        for _ in range(10):
            distance = abs(self.bat.x - target_x)
            distances.append(distance)
            self.bat.move()
        
        # Distance should generally decrease (bat approaches target)
        final_distance = abs(self.bat.x - target_x)
        self.assertLess(final_distance, distances[0])

class TestEnemyFactory(unittest.TestCase):
    def test_create_enemy_formation(self):
        enemies = create_enemy_formation()
        self.assertEqual(len(enemies), 30)  # Total number of enemies
        self.assertIsInstance(enemies[0], Bird)
        self.assertIsInstance(enemies[-1], Bat)    

if __name__ == "__main__":
    unittest.main()
