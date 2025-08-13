from Avian_Blasters.model.entity import Entity

class Character(Entity):

    @property
    def get_health(self) -> int:
        ...
    
    def shoot(self):
        ...