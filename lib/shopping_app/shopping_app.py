from customer import Customer
from item import Item
from seller import Seller

seller = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa madre", 28980, seller)
    Item("Fuente de alimentación", 8980, seller)
    Item("Caja de PC", 8727, seller)
    Item("Disco duro de 3.5 pulgadas", 10980, seller)
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("SSD M.2", 12980, seller)
    Item("Refrigerador de CPU", 13400, seller)
    Item("Tarjeta gráfica", 23800, seller)

print("🤖 Por favor, introduce tu nombre")
cliente = Customer(input())

print("🏧 Ingresa la cantidad que deseas cargar en tu billetera")
cliente.wallet.deposit(int(input()))

print("🛍️ Comenzando la compra")
finalizar_compra = False
while not finalizar_compra:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Ingresa el número del producto")
    numero = int(input())

    print("⛏ Ingresa la cantidad del producto")
    cantidad = int(input())

    productos = seller.pick_items(numero, cantidad)
    for producto in productos:
        cliente.cart.add(producto)
    print("🛒 Contenido del carrito")
    cliente.cart.show_items()
    print(f"🤑 Monto total: {cliente.cart.total_amount()}")

    print("😭 ¿Deseas finalizar la compra? (si/no)")
    finalizar_compra = input() == "si"

print("💸 ¿Deseas confirmar la compra? (sí/no)")
if input() == "si":
    cliente.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ Resultados ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Productos de {cliente.name}")
cliente.show_items()
print(f"😱👛 Saldo de billetera de {cliente.name}: {cliente.wallet.balance}")

print(f"📦 Inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo de billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
cliente.cart.show_items()
print(f"🌚 Monto total: {cliente.cart.total_amount()}")

print("🎉 Fin")
