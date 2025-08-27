import pygame
from enum import Enum

class InputHandler:
    """InputHandler defines the interface for handling user input"""
    
    class Action(Enum):
        """Actions that can be triggered by user input"""
        MOVE_LEFT = 1
        MOVE_RIGHT = 2
        SHOOT = 3
        QUIT = 4
        NONE = 5
        PAUSE = 6
    
    def handle_events(self) -> list['Action']:
        """Process pygame events and return list of actions"""
        ...
    
    def is_key_pressed(self, key: int) -> bool:
        """Check if a specific key is currently pressed"""
        ...
    
    def get_continuous_actions(self) -> list['Action']:
        """Get actions for keys that are held down (like movement)"""
        ...
