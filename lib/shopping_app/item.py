class Item:
    from ownable import set_owner
    instances = []
    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Cuando se crea una instancia de Item (self), se agrega a la lista de instancias (instances) de la clase.
        Item.instances.append(self)

    def label(self):
        return {"nombre": self.name, "precio": self.price}  # Cambio de "name" y "price" a "nombre" y "precio"

    @staticmethod
    def item_all():
        # Devuelve la lista de instancias generadas hasta ahora usando Item.item_all().
        return Item.instances
