from Avian_Blasters.model.entity import Entity

class Item(Entity):

    """ Item is a class that represents an item in the game """

    @property
    def active(self) -> bool:
        """ Returns True if the item is active """
        ...

    def destroy(self):
        """ Destroys the item, making it inactive """
        ...