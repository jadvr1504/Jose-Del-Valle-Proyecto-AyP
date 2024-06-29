class Producto:
    def __init__(self, name, price,  adicional,inventario, tipo,vendido,es_alcoholico=False):
        self.name = name
        self.price = float(price)
        self.adicional = adicional
        self.inventario = inventario
        self.tipo = tipo
        self.es_alcoholico = es_alcoholico
        self.vendido = vendido
    def show(self):
        print(f"Nombre : {self.name}, Precio = {self.price} adicional: {self.adicional} inventario disponible: {self.inventario} Tipo: {self.tipo} ")
    def restar_inventario(self, cantidad):
        if self.inventario >= cantidad:
            self.inventario -= cantidad
        else:
            print("No hay suficiente inventario para esta cantidad")