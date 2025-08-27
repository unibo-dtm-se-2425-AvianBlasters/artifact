import pygame
import time
from typing import List
from Avian_Blasters.controller.game_controller import GameController
from Avian_Blasters.controller.input_handler import InputHandler
from Avian_Blasters.controller.input_handler_impl import InputHandlerImpl
from Avian_Blasters.view.game_view import GameView
from Avian_Blasters.view.game_view_impl import GameViewImpl
from Avian_Blasters.model.world import World
from Avian_Blasters.model.world_impl import WorldImpl
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.player.player_impl import PlayerImpl
from Avian_Blasters.model.entity import Entity

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Avian Blasters: The Avians Strike Back"
TARGET_FPS = 60

class GameControllerImpl(GameController):
    """GameControllerImpl is the main implementation of GameController"""
    
    def __init__(self):
        self._world: World = None
        self._view: GameView = None
        self._input_handler: InputHandler = None
        self._clock = None
        self._running = False
        self._player: Player = None
        self._paused = False
    
    def initialize(self) -> bool:
        """Initialize the game controller and its dependencies"""
        try:
            # Initialize pygame clock
            self._clock = pygame.time.Clock()
            
            # Initialize view
            self._view = GameViewImpl()
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
                health=3,
                initial_score=0,
                initial_multiplier=1,
                limit_right=115,  # Near right edge
                limit_left=5,     # Near left edge
                fps = TARGET_FPS
            )
            
            # Create enemies in formation (like Space Invaders)
            entities = [self._player]
            entities.extend(self._create_enemy_formation())
            
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
        print("Controls: Arrow keys or A/D to move, Space to shoot, Escape to quit")
        
        while self._running:
            # Calculate delta time
            delta_time = self._clock.tick(TARGET_FPS) / 1000.0
            
            # Handle input
            actions = self._input_handler.handle_events()
            self.handle_input(actions)
            
            if not self._paused:
                # Update game state
                self.update_game_state(delta_time)
                self._view.render_world(self._world)
                self._view.update_display()
        
        self.cleanup()
    
    def update_game_state(self, delta_time: float) -> None:
        """Update the game world state based on elapsed time"""
        # Basic game state updates would go here
        # For now, just update player status if needed
        if self._player and hasattr(self._player, 'get_status'):
            status_handler = self._player.get_status()
            if hasattr(status_handler, 'update'):
                status_handler.update()
    
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
                    self._world.add_projectiles(projectiles)
    
    def is_game_running(self) -> bool:
        """Check if the game should continue running"""
        return self._running
    
    def cleanup(self) -> None:
        """Cleanup resources when the game ends"""
        if self._view:
            self._view.cleanup()
        print("Game ended. Thanks for playing!")
    
    def _create_enemy_formation(self) -> List[Entity]:
        """Create a formation of enemies like in the reference UI"""
        from Avian_Blasters.model.entity_impl import EntityImpl
        
        enemies = []
        
        # Create a simple enemy formation
        # Top row: Green birds
        for i in range(11):
            x = 10 + i * 10
            y = 10
            enemy = EntityImpl(x, y, 4, 4, Entity.TypeArea.ENEMY, 1)
            enemies.append(enemy)
        
        # Second row: More green birds  
        for i in range(9):
            x = 15 + i * 10
            y = 20
            enemy = EntityImpl(x, y, 4, 4, Entity.TypeArea.ENEMY, 1)
            enemies.append(enemy)
        
        # Middle rows: Mixed birds
        for row in range(2):
            for i in range(3):
                x = 30 + i * 15
                y = 30 + row * 10
                enemy = EntityImpl(x, y, 4, 4, Entity.TypeArea.ENEMY, 1)
                enemies.append(enemy)
        
        # Add some scattered enemies
        scattered_positions = [(15, 45), (60, 35), (90, 25), (45, 50)]
        for x, y in scattered_positions:
            enemy = EntityImpl(x, y, 4, 4, Entity.TypeArea.ENEMY, 1)
            enemies.append(enemy)
        
        return enemies
