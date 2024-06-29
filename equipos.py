class equipo:
    def __init__(self, id, code, name, group ):
        self.id = id
        self.code = code
        self.name = name
        self.group = group
    def show(self):
        print(f"ID: {self.id}., Code: {self.code}, Nombre: {self.name}, Grupo: {self.group}")
    def getNombre(self):
        return self.name
    
    