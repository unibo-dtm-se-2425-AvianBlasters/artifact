import os
import pygame
import random
from typing import List
from Avian_Blasters.controller.game_controller import GameController
from Avian_Blasters.controller.input_handler import InputHandler
from Avian_Blasters.controller.input_handler_impl import InputHandlerImpl
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_factory import PowerUpFactory
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.sound_manager_impl import SoundManagerImpl
from Avian_Blasters.view.game_view import GameView
from Avian_Blasters.view.game_view_impl import GameViewImpl
from Avian_Blasters.model.world import WORLD_HEIGHT, World
from Avian_Blasters.model.world_impl import WorldImpl
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.player.player_impl import PlayerImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.enemy_factory import create_enemy_formation, handle_bird_formation_movement, can_bird_shoot, update_bat_spawning
from Avian_Blasters.menu.scoreboard_impl import ScoreboardImpl

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Avian Blasters: The Avians Strike Back"
TARGET_FPS = 60

class GameControllerImpl(GameController):
    """GameControllerImpl is the main implementation of GameController"""
    
    def __init__(self, difficulty : int, name : str, fps : int):
        self._world: World = None
        self._view: GameView = None
        self._input_handler: InputHandler = None
        self._clock = None
        self._running = False
        self._player: Player = None
        self._paused = False
        self._name = name.replace(',', ' ').lstrip().rstrip()
        self._difficulty = difficulty
        self._fps = fps
        self._scoreboard = ScoreboardImpl()
        self._power_up_factory = PowerUpFactory()
        self._sound_manager = SoundManagerImpl()
        sound_path = 'assets' + os.sep + 'sounds' + os.sep
        self._shoot_sound_path = sound_path + 'shoot.mp3'
        self._power_up_sound_path = sound_path + 'power_up.mp3'
        self._game_over_sound_path = sound_path + 'game_over.mp3'
        self._game_start_sound_path = sound_path + 'game_start.mp3'
        self._enemy_defeated_sound_path = sound_path + 'enemy_defeat.mp3'
        self._enemy_hit_sound_path = sound_path + 'enemy_hit.mp3'
        self._player_hit_sound_path = sound_path + 'player_hit.mp3'
    
    def initialize(self) -> bool:
        """Initialize the game controller and its dependencies"""
        try:
            # Initialize pygame clock
            self._clock = pygame.time.Clock()
            
            # Initialize view
            self._view = GameViewImpl(self._fps)
            if not self._view.initialize(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE):
                return False
            
            # Initialize input handler
            self._input_handler = InputHandlerImpl()

            # Initialize world with a test player
            self._player = PlayerImpl(
                x=60,  # Center of world width
                y=75,  # Better positioned - not so close to bottom
                width=8,  # Larger width for better visibility
                height=5, # Larger height for better visibility
                delta=2,  # Movement speed
                health=self._difficulty,
                initial_score=0,
                initial_multiplier=1,
                limit_right=115,  # Near right edge
                limit_left=5,     # Near left edge
                refresh_rate = 60
            )

            # Create enemies in formation (like Space Invaders)
            entities = [self._player]
            entities.extend(create_enemy_formation())
            
            # Create world with the player and enemies
            self._world = WorldImpl(entities)
            
            self._running = True
            return True
            
        except Exception as e:
            print(f"Failed to initialize game controller: {e}")
            return False
    
    def run(self) -> None:
        """Start and run the main game loop"""
        if not self._running:
            print("Game controller not initialized!")
            return
        
        print("Starting Avian Blasters...")
        print("Controls: Arrow keys or A/D to move, Space to shoot, Right Shift to pause, Escape to quit")
        
        self._sound_manager.play_sound_effect(self._game_start_sound_path, volume=0.5)

        while self._running:
            # Calculate delta time
            delta_time = self._clock.tick(TARGET_FPS) / 1000.0
            
            # Handle input
            actions = self._input_handler.handle_events()
            self.handle_input(actions)
            
            graph_update = 1 / self._fps
            if not self._paused:
                # Update game state
                self.update_game_state(delta_time)
                if graph_update >= 1 / self._fps:
                    graph_update = 0
                    self._view.render_world(self._world)
                    self._view.update_display()
                graph_update += delta_time
        
        if (self._name != ''):
            name = self._name
            points = self._world.get_players()[0].get_score().score
            difficulty = self._difficulty
            self._scoreboard.add_score([name, points, difficulty])
            print("Score saved!")
        else:
            print("The score has not been saved as no name was given!")
        self.cleanup()
    
    def update_game_state(self, delta_time: float) -> None:
        """Update the game world state based on elapsed time"""        
        self._update_player()
        self._update_enemies(delta_time)
        self._update_projectiles()
        self._update_power_ups()
        self._world.remove_destroyed_items()

    def _update_player(self) -> None:
        if self._player and hasattr(self._player, 'get_status'):
            status_handler = self._player.get_status()
            if hasattr(status_handler, 'update'):
                status_handler.update()

        if self._player and hasattr(self._player, 'get_player_attack_handler'):
            attack_handler = self._player.get_player_attack_handler()
            if hasattr(attack_handler, 'update'):
                attack_handler.update()
        
        if self._player.is_touched(self._world.get_projectiles() + self._world.get_enemies()):
            self._sound_manager.play_sound_effect(self._player_hit_sound_path, volume = 0.5)
        if self._player.get_health_handler().current_health <= 0:
            self._running = False
            print("Oh no! The Avians have reached the car. Maaaaan... Game Over!")

    def _update_projectiles(self) -> None:
        """Update the positions of all projectiles in the world"""
        if not self._world:
            return
        
        for projectile in self._world.get_projectiles():
            if projectile.get_area().get_position_y <= 0 or projectile.get_area().get_position_y >= SCREEN_HEIGHT:
                    projectile.destroy()
            else:
                if projectile.projectile_type == ProjectileType.LASER:
                    movement_x = self._player.get_area().get_position_x
                    movement_y = 0
                elif projectile.projectile_type in [ProjectileType.NORMAL, ProjectileType.SOUND_WAVE]:
                    if projectile.get_type == Entity.TypeArea.PLAYER_PROJECTILE:
                        movement_y = -1
                    else:
                        movement_y = 1
                    movement_x = 0
                projectile.move(movement_x, movement_y, projectile.get_area().width, projectile.get_area().height)

    def _update_power_ups(self) -> None:
        if not self._world:
            return
        
        if self._player and hasattr(self._player, 'get_power_up_handler'):
            power_up_handler = self._player.get_power_up_handler()
            for power_up in self._world.get_power_ups():
                if power_up.get_area().get_position_y > SCREEN_HEIGHT:
                    power_up.destroy()
                else:
                    power_up.move(0, 1, power_up.get_area().width, power_up.get_area().height)
                    if self._player.get_area().overlap(power_up.get_area()):
                        power_up_handler.collect_power_up(power_up, self._player)
                        self._sound_manager.play_sound_effect(self._power_up_sound_path, volume=0.5)
            if hasattr(power_up_handler, 'player_update'):
                    power_up_handler.player_update(self._player, self._paused)         

        if self._player and hasattr(self._player, 'get_player_attack_handler'):
            attack_handler = self._player.get_player_attack_handler()
            if hasattr(attack_handler, 'update'):
                attack_handler.update()         
    
    def _update_enemies(self, delta_time: float) -> None:
        """Update the positions and behavior of all enemies in the world"""
        if not self._world:
            return
    
        handle_bird_formation_movement(self._world.get_enemies())
        
        # Handle random bat spawning
        new_bat = update_bat_spawning(delta_time, self._world.get_enemies())
        if new_bat:
            print("New bat spawned")
            self._world.add_enemies([new_bat])
        
        # Update existing enemies
        enemies_to_remove = []
        for enemy in self._world.get_enemies():
            if enemy.get_area().get_position_y > WORLD_HEIGHT:
                enemies_to_remove.append(enemy)
            elif enemy.is_dead():
                enemies_to_remove.append(enemy)
            else:
                collision_occurred = enemy.is_touched(self._world.get_projectiles())
                
                if collision_occurred and self._player:
                    enemy_died = enemy.is_dead()
                    
                    sound = None
                    if enemy_died:
                        self._try_drop_power_up(enemy.get_area().get_position_x, enemy.get_area().get_position_y)
                        sound = self._enemy_defeated_sound_path
                    else:
                        sound = self._enemy_hit_sound_path
                    self._sound_manager.play_sound_effect(sound, volume=0.5)
                    
                    points = 10 if enemy_died else 5
                    self._player.get_score().add_points(points)
                
                from Avian_Blasters.model.character.enemy.bat import Bat
                players = self._world.get_players()
                if isinstance(enemy, Bat) and players:
                    player = players[0]
                    enemy.set_player_position(
                        player.get_area().get_position_x,
                        player.get_area().get_position_y
                    )
                    enemy._attack_handler.set_player_position(
                        player.get_area().get_position_x,
                        player.get_area().get_position_y
                    )
                
                enemy.move()
                
                # Only allow shooting if bird has clear shot (no bird in front)
                if can_bird_shoot(enemy, self._world.get_enemies()):
                    projectiles = enemy.shoot()
                    if projectiles:
                        self._world.add_projectiles(projectiles)
        
        for enemy in enemies_to_remove:
            self._world.remove_entity(enemy)
    
        # Respawn a new wave if all enemies have been cleared
        if not self._world.get_enemies():
            self._world.add_enemies(create_enemy_formation())
            
    def _try_drop_power_up(self, enemy_x: int, enemy_y: int) -> None:
        # 20% chance to drop a power-up
        if random.random() < 0.40:
            # Choose a random power-up type
            available_power_ups = [
                PowerUpType.LASER,
                PowerUpType.INVULNERABILITY, 
                PowerUpType.DOUBLE_FIRE,
                PowerUpType.HEALTH_RECOVERY
            ]
            power_up_type = random.choice(available_power_ups)
            
            # Create power-up at enemy's position
            power_up = self._power_up_factory.create_power_up(
                power_up_type=power_up_type,
                x=enemy_x,
                y=enemy_y, 
                width=5,
                height=5,
                type_area=Entity.TypeArea.POWERUP
            )
            
            # Add power-up to the world
            self._world.add_power_ups([power_up])
    
    def handle_input(self, actions: List[InputHandler.Action]) -> None:
        """Process input actions and update the game state accordingly"""
        for action in actions:
            if action == InputHandler.Action.QUIT:
                self._running = False
            elif action == InputHandler.Action.PAUSE:
                self._paused = not self._paused
                if self._paused:
                    print("Pause")
                else:
                    print("Resumed")
            elif action == InputHandler.Action.MOVE_LEFT and self._player and not self._paused:
                self._player.move(-1)  # Move left
            elif action == InputHandler.Action.MOVE_RIGHT and self._player and not self._paused:
                self._player.move(1)   # Move right
            elif action == InputHandler.Action.SHOOT and self._player and not self._paused:
                projectiles = self._player.shoot()
                if projectiles:
                    self._sound_manager.play_sound_effect(self._shoot_sound_path, volume=0.5)
                    self._world.add_projectiles(projectiles)
    
    def is_game_running(self) -> bool:
        """Check if the game should continue running"""
        return self._running
    
    def cleanup(self) -> None:
        """Cleanup resources when the game ends"""
        if self._view:
            self._sound_manager.play_sound_effect(self._game_over_sound_path, volume=0.5)
            self._view.cleanup()
        print("Game ended. Thanks for playing!")
    