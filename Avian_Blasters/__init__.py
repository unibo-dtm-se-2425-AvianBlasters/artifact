import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Avian_Blasters')

# this is the initial module of your app
# this is executed whenever some client-code is calling `import Avian_Blasters` or `from Avian_Blasters import ...`
# put your main classes here, eg:
class MyClass:
    def my_method(self):
        return "Hello World"

#Enemy class for the game
class Enemy:
    def __init__(self,x, y, speed,health):

       """ 
       Initialize an enemy with position and speed.
       :param x: Initial x-coordinate of the enemy
       :param y: Initial y-coordinate of the enemy
       :param speed: Speed of the enemy
       """ 
       self.x = x
       self.y = y
       self.speed = speed
       self.health = health
       self.color = self.get_color()
       logger.debug(f"Enemy created at ({self.x}, {self.y}) with speed {self.speed}")
       
    def get_color(self):
        """
        Determine the enemy's color based on its health.
        Using the RGB color model.(R,G,B)
        """
        if self.health == 3:
            return (0, 255, 0)  # Green
        elif self.health == 2:
            return (255, 255, 0) # Yellow
        elif self.health == 1:
            return (255, 0, 0)  # Red
        return (255, 255, 255)  # Default to white if dead or invalid health
    
    def move(self):
        """
        The enemy moves down by its speed.
        """
        self.y += self.speed
        logger.debug(f"Enemy moved to position ({self.x}, {self.y})")

    def take_damage(self):
        """
        Reduce the enemy's health by 1 and update its color.
        If health reaches 0, the enemy is considered dead.
        """
        if self.health > 0:
            self.health -= 1
            self.color = self.get_color()
            logger.debug(f"Enemy at ({self.x}, {self.y}) took damage, new health: {self.health}, color: {self.color}")
    
    def is_off_screen(self, screen_height):
        """
        Check if the enemy is off the screen.
        :param screen_height: Height of the game screen
        :return: True if the enemy is off the screen, False otherwise
        """
        off_screen = self.y > screen_height
        logger.debug(f"Enemy at ({self.x}, {self.y}) off screen: {off_screen}")
        return off_screen
    
    def render(self):
        """
        Render the enemy on the screen using pygame.
        :param screen: The pygame screen surface to draw on. 
        This is a placeholder for rendering logic.
        """
        import pygame
        pygame.draw.rect(pygame.display.get_surface(), self.color, (self.x, self.y, 50, 50))
        logger.debug(f"Rendering enemy at position ({self.x}, {self.y}) with color {self.color}")
        
# let this be the last line of this file
logger.info("Avian_Blasters loaded")
