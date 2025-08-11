from enum import Enum

class PlayerStatus:
    class Status(Enum):
        NORMAL = 1
        INVULNERABLE = 2
    
    @property
    def get_current_status(self):
        ...
    
    def set_current_status(self, new_status : Status):
        ...