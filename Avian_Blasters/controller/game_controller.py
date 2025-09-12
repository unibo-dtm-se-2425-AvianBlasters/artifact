from Avian_Blasters.controller.input_handler import InputHandler

class GameController:
    """GameController defines the interface for managing the game loop and coordination between model and view"""
    
    def initialize(self) -> bool:
        """Initialize the game controller and its dependencies"""
        ...
    
    def run(self) -> None:
        """Start and run the main game loop"""
        ...
    
    def update_game_state(self, delta_time: float) -> None:
        """Update the game world state based on elapsed time"""
        ...
    
    def handle_input(self, actions: list[InputHandler.Action]) -> None:
        """Process input actions and update the game state accordingly"""
        ...
    
    def is_game_running(self) -> bool:
        """Check if the game should continue running"""
        ...
    
    def cleanup(self) -> None:
        """Cleanup resources when the game ends"""
        ...
