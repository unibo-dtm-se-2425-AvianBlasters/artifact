from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.entity_impl import EntityImpl
from Avian_Blasters.model.item.item import Item

DEFAULT_DELTA = 1

class ItemImpl(Item, EntityImpl):

    """ ItemImpl is an implementation of the Item interface """

    def __init__(self, x : int, y : int, width : int, height : int, type : Entity.TypeArea, delta : int = DEFAULT_DELTA):
        super().__init__(x, y, width, height, type, delta)
        self._active = True

    @property
    def active(self) -> bool:
        return self._active
    
    def destroy(self):
        self._active = False