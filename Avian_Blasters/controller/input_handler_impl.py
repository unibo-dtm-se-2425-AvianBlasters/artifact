import pygame
from typing import List
from Avian_Blasters.controller.input_handler import InputHandler

class InputHandlerImpl(InputHandler):
    """InputHandlerImpl is a pygame implementation of InputHandler"""
    
    def __init__(self):
        self._keys_pressed = {}
    
    def handle_events(self) -> List[InputHandler.Action]:
        """Process pygame events and return list of actions"""
        actions = []
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actions.append(InputHandler.Action.QUIT)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    actions.append(InputHandler.Action.SHOOT)
                elif event.key == pygame.K_RSHIFT:
                    actions.append(InputHandler.Action.PAUSE)
                elif event.key == pygame.K_ESCAPE:
                    actions.append(InputHandler.Action.QUIT)
        
        # Add continuous actions (held keys)
        actions.extend(self.get_continuous_actions())
        
        return actions
    
    def is_key_pressed(self, key: int) -> bool:
        """Check if a specific key is currently pressed"""
        keys = pygame.key.get_pressed()
        return keys[key]
    
    def get_continuous_actions(self) -> List[InputHandler.Action]:
        """Get actions for keys that are held down (like movement)"""
        actions = []
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            actions.append(InputHandler.Action.MOVE_LEFT)
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            actions.append(InputHandler.Action.MOVE_RIGHT)
        
        return actions
