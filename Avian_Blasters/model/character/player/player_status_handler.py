from enum import Enum

class PlayerStatus:
    class Status(Enum):
        NORMAL = 1
        INVULNERABLE = 2
    
    @property
    def status(self) -> Status:
        ...
    
    @status.setter
    def status(self, new_status : Status):
        ...