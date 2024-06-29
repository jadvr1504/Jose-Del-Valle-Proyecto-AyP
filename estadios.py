from restaurante import*
class Estadio:
    def __init__(self, name,  id, location, capacity,capacidad_general,capacidad_VIP ,restaurants):
        self.name = name
        self.id = id
        self.location = location
        self.capacity = capacity
        self.capacidad_general = capacidad_general
        self.capacidad_VIP = capacidad_VIP
        self.restaurants = restaurants.copy()
    def show(self):
        print(f"Estadio: {self.name}, ID: {self.id}, Ubicacion: {self.location}, Capacidad: {self.capacity}")
    def get_name(self):
        return self.name

    def __str__(self):
        restaurantes_str = "\n".join([str(restaurant) for restaurant in self.restaurants])
        return f"Estadio: {self.name}, Ubicación: {self.location}\nRestaurantes:\n{restaurantes_str}"
    def getNombre(self):
        return self.name
    def getCapacidadGeneral(self):
        return sum(self.capacidad_general)
    
    def getCapacidadVIP(self):
        return self.capacidad_VIP
