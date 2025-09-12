import random
from Avian_Blasters.model.character.general_attack_handler_impl import GeneralAttackHandlerImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

ENEMY_PROJECTILE_WIDTH = 5
ENEMY_PROJECTILE_HEIGHT = 5

class EnemyAttackHandler(GeneralAttackHandlerImpl):
    """Base enemy attack handler that extends the general attack handler"""
    
    def __init__(self, projectile_factory: ProjectileFactory, fire_chance: float = 0.05, 
                 cooldown_steps: int = 20, projectile_speed: int = 4):
        super().__init__(projectile_factory, projectile_speed, cooldown_steps)
        if not 0.0 <= fire_chance <= 1.0:
            raise ValueError("fire_chance must be within [0, 1]")
        self._fire_chance = fire_chance
        self._projectile_type = ProjectileType.NORMAL
        
    def _can_attack(self) -> bool:
        """Check if the handler is ready to attack and roll for fire chance"""
        if not self._cooldown_handler.is_over():
            self._cooldown_handler.update()
            return False
        return random.random() <= self._fire_chance
        
    def try_attack(self, enemy : Character):
        if not self._can_attack():
            return []
        else:    
            projectile = self._projectile_factory.create_projectile(
                projectile_type=self._projectile_type,
                x=enemy.x,
                y=enemy.y + max(1, enemy.height // 2),
                type_area=Entity.TypeArea.ENEMY_PROJECTILE,
                delta=self._projectile_speed
            )
            self._reset_cooldown()
            return [projectile]


class BirdAttackHandler(EnemyAttackHandler):
    """Birds drop standard bullets downward"""
    
    def __init__(self, projectile_factory: ProjectileFactory, fire_chance: float = 0.008, 
                 cooldown_steps: int = 60, projectile_speed: int = 1):
        super().__init__(projectile_factory, fire_chance, cooldown_steps, projectile_speed)


class BatAttackHandler(EnemyAttackHandler):
    """Bats fire sound waves that slow down the player when close enough"""
    
    def __init__(self, projectile_factory: ProjectileFactory, fire_chance: float = 0.08, 
                 cooldown_steps: int = 30, projectile_speed: int = 2):
        super().__init__(projectile_factory, fire_chance, cooldown_steps, projectile_speed)
        # Use sound wave projectiles that disrupt player movement
        self._projectile_type = ProjectileType.SOUND_WAVE
        self._player_position = None
        
    def set_player_position(self, player_x: int, player_y: int):
        """Set the current player position for distance checking"""
        self._player_position = (player_x, player_y)
        
    def _can_attack(self, enemy) -> bool:
        """Check if the handler is ready to attack and if close enough to player"""
        if not self._cooldown_handler.is_over():
            self._cooldown_handler.update()
            return False
            
        # Check if we have player position information
        if self._player_position is None:
            return False
            
        # Calculate vertical distance to player
        player_x, player_y = self._player_position
        vertical_distance = abs(enemy.y - player_y)
        
        # Only attack if within 10 units vertically and pass random chance
        if vertical_distance <= 10:
            return random.random() <= self._fire_chance
        return False
        
    def try_attack(self, enemy):
        if not self._can_attack(enemy):
            return []
        else:    
            projectile = self._projectile_factory.create_projectile(
                projectile_type=self._projectile_type,
                x=enemy.x,
                y=enemy.y + max(1, enemy.height // 2),
                type_area=Entity.TypeArea.ENEMY_PROJECTILE,
                delta=self._projectile_speed
            )
            self._reset_cooldown()
            return [projectile]