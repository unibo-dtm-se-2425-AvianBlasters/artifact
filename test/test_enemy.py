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
        # Test the attack handler with a basic enemy
        enemy = EnemyImpl(x=80, y=150, width=18, height=14, speed=4, max_health=3)
        
        # Set player position close enough for bat to attack (within 10 units vertically)
        bat_handler.set_player_position(80, 155)  # Only 5 units away vertically
        
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
            projectiles = enemy.shoot()
            self.assertEqual([], projectiles)  # Should return empty list during cooldown
        
        projectiles = enemy.shoot()
        self.assertEqual(1, len(projectiles))  # Should return list with 1 projectile after cooldown
        
        for _ in range(20):
            projectiles = enemy.shoot()
            self.assertEqual([], projectiles)  # Should return empty list during cooldown again


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
        
        # Move several times and track horizontal movement
        positions = []
        for _ in range(10):
            self.bird.move()
            positions.append(self.bird.x)
        
        # Bird should move down consistently (using fractional accumulation now)
        # With default vertical_speed=0.3, after 10 moves: int(0.3 * 10) = int(3.0) = 3
        # But let's check the actual movement pattern
        actual_movement = self.bird.y - initial_y
        self.assertGreater(actual_movement, 0)  # Should move downward
        self.assertLessEqual(actual_movement, 10)  # Reasonable downward movement
        
        # Bird should move horizontally (bouncing pattern, not oscillating)
        max_x = max(positions)
        min_x = min(positions)
        self.assertGreater(max_x - min_x, 0)  # Should have horizontal movement

    def test_wave_pattern_is_bouncing(self):
        """Test that bird follows a proper bouncing pattern"""
        # Create bird near right edge to ensure bouncing behavior
        self.bird = Bird(x=750, y=80, width=16, height=12, speed=4, health=15, 
                        horizontal_speed=2.0, screen_width=800)
        
        positions = []
        directions = []
        
        # Collect many positions to see the bouncing pattern
        for i in range(30):
            old_x = self.bird.x
            self.bird.move()
            new_x = self.bird.x
            positions.append(new_x)
            
            # Track direction changes
            if i > 0:
                directions.append(new_x - old_x)
        
        # The movement should bounce - check for direction changes
        positive_moves = [d for d in directions if d > 0]
        negative_moves = [d for d in directions if d < 0]
        self.assertTrue(len(positive_moves) > 0 and len(negative_moves) > 0, 
                       "Bird should bounce and change direction")


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
        """Bat should only move down when in DESCENDING state (no player nearby)"""
        initial_x = self.bat.x
        initial_y = self.bat.y
        
        self.bat.move()
        
        self.assertEqual(initial_x, self.bat.x)  # No horizontal movement in DESCENDING state
        # With default vertical_speed=0.2, int(0.2) = 0, so no movement on first frame
        # But accumulator builds up, so after a few moves we should see movement
        expected_y = initial_y  # First move might not show movement due to fractional accumulation
        self.assertEqual(expected_y, self.bat.y)

    def test_homing_behavior_right(self):
        """Test bat moving right when in BIRD_LIKE state"""
        # Create bat with higher horizontal speed to ensure detectable movement
        self.bat = Bat(x=50, y=120, width=14, height=10, speed=5, health=8, 
                      horizontal_speed=2.0, screen_width=800)
        # Set player position to trigger BIRD_LIKE state
        self.bat.set_player_position(50, 125)  # Close to bat's position
        
        # Move multiple times to trigger state change and build up movement
        for _ in range(10):
            self.bat.move()
        
        initial_x = self.bat.x
        # Move several more times to accumulate detectable horizontal movement
        for _ in range(5):
            self.bat.move()
        
        # In BIRD_LIKE state, bat should move horizontally from left side
        self.assertGreater(self.bat.x, initial_x)  # Should move right from left side

    def test_homing_behavior_left(self):
        """Test bat can move left when in BIRD_LIKE state"""
        # Position bat near right edge with higher horizontal speed
        self.bat = Bat(x=780, y=120, width=14, height=10, speed=5, health=8, 
                      horizontal_speed=2.0, screen_width=800)
        self.bat.set_player_position(780, 125)  # Close to bat's position
        
        # Move to trigger state change to BIRD_LIKE and reach boundary
        for _ in range(10):
            self.bat.move()
        
        initial_x = self.bat.x
        # Move several times to accumulate detectable leftward movement
        for _ in range(5):
            self.bat.move()
        
        # Near right boundary, bat should move left in BIRD_LIKE state
        self.assertLess(self.bat.x, initial_x)  # Should move left from boundary

    def test_homing_with_multiple_moves(self):
        """Test that bat shows consistent movement pattern in BIRD_LIKE state"""
        # Set player position to trigger BIRD_LIKE state
        self.bat.set_player_position(150, 125)  # Close to bat's position
        
        positions = []
        for _ in range(15):
            positions.append(self.bat.x)
            self.bat.move()
        
        # After state change to BIRD_LIKE, bat should show horizontal movement
        # Check that positions change (showing movement capability)
        unique_positions = len(set(positions))
        self.assertGreater(unique_positions, 1, "Bat should move and change positions")

class TestEnemyFactory(unittest.TestCase):
    def test_create_enemy_formation(self):
        enemies = create_enemy_formation()
        # Factory now creates 1-2 random enemies per wave
        self.assertGreaterEqual(len(enemies), 1)  # At least 1 enemy
        self.assertLessEqual(len(enemies), 2)     # At most 2 enemies
        
        # All enemies should be either Bird or Bat
        for enemy in enemies:
            self.assertTrue(isinstance(enemy, Bird) or isinstance(enemy, Bat))
        
        # Test that enemies have reasonable health values
        for enemy in enemies:
            self.assertGreaterEqual(enemy.get_health, 1)
            self.assertLessEqual(enemy.get_health, 3)    

if __name__ == "__main__":
    unittest.main()
