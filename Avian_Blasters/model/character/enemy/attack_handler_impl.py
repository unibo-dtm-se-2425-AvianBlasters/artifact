import random
from typing import Optional

from Avian_Blasters.model.character.general_attack_handler_impl import GeneralAttackHandlerImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


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
        if self._cooldown > 0:
            self._cooldown -= 1
            return False
        return random.random() <= self._fire_chance
        
    def try_attack(self, enemy):
        """Try to attack and return a list of projectiles"""
        if not self._can_attack():
            return []
            
        projectile = self._projectile_factory.create_projectile(
            projectile_type=self._projectile_type,
            x=enemy.x,
            y=enemy.y + max(1, enemy.height // 2),
            direction=Direction.DOWN,
            width=5,
            height=5,
            type_area=Entity.TypeArea.ENEMY_PROJECTILE,
            delta=self._projectile_speed
        )
        
        self._reset_cooldown()
        return [projectile]


class BirdAttackHandler(EnemyAttackHandler):
    """Birds drop standard bullets downward"""
    
    def __init__(self, projectile_factory: ProjectileFactory, fire_chance: float = 0.06, 
                 cooldown_steps: int = 18, projectile_speed: int = 5):
        super().__init__(projectile_factory, fire_chance, cooldown_steps, projectile_speed)


class BatAttackHandler(EnemyAttackHandler):
    """Bats fire sound waves that slow down the player"""
    
    def __init__(self, projectile_factory: ProjectileFactory, fire_chance: float = 0.04, 
                 cooldown_steps: int = 30, projectile_speed: int = 2):
        super().__init__(projectile_factory, fire_chance, cooldown_steps, projectile_speed)
        # Use sound wave projectiles that disrupt player movement
        self._projectile_type = ProjectileType.SOUND_WAVE
