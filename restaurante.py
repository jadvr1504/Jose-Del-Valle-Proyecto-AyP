from producto import*
class Restaurante:
    def __init__(self, name, products):
        self.name = name
        self.products = self.products = [Producto(**{k: v for k, v in p.items() if k in ['name', 'price', 'quantity']}) for p in products]
    def __str__(self):
        productos_str = "\n".join([str(product) for product in self.products])
        return f"{self.name}\nProductos:\n{productos_str}"