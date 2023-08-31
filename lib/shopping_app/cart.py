
class Cart:
    from item_manager import show_items
    from ownable import set_owner
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("No tienes suficiente dinero para comprar los items.")
            pass

        # Transferencia de dinero y propiedad
        for item in self.items:
            item_owner_wallet = item.owner.wallet
            cart_owner_wallet = self.owner.wallet
            item_owner_wallet.deposit(item.price)
            cart_owner_wallet.withdraw(item.price)
            item.set_owner(self.owner)

        # Vaciar el contenido del carrito
        print("La compra fuer realizada con exito.")
        self.items = []

