from estadios import*
class partidos:
    def __init__(self, id_partido, equipo_local, equipo_visitante, estadio, fecha,asistencia, tickets_vendidos_cantidad=0 ):
        self.id_partido = id_partido
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio=estadio
        self.fecha=fecha
        self.asientos_tomados=[]
        self.tickets_vendidos_cantidad = tickets_vendidos_cantidad
        self.tickets = []
        self.asientos_tomados_vip = []
        self.asistencia = asistencia
    def show(self):
        return f"Partido : {self.equipo_local.name} vs {self.equipo_visitante.name} fecha: {self.fecha}, estadio : {self.estadio.get_name()}"
    def mostrarSinEstadio(self):
        return f'''Partido: {self.local.getNombre()} vs {self.visitante.getNombre()} el {self.fecha}'''
    
    def mostrarSinFecha(self):
        return f'''Partido: {self.local.getNombre()} vs {self.visitante.getNombre()}
    Estadio: {self.estadio.getNombre()}'''
    
    def mostrarSencillo(self):
        return f'''{self.equipo_local.getNombre()} vs {self.equipo_visitante.getNombre()} el {self.fecha} en el {self.estadio.getNombre()}'''
    
    def getFecha(self):
        return self.fecha
    
    def getAsientosTomados(self):
        return self.asientos_tomados
    
    def getAsientosTomadosVIP(self):
        return self.asientos_tomados_vip
    
    def getTicketsVendidosCantidad(self):
        return self.tickets_vendidos_cantidad
    def mostrar(self):
        return f'''Partido: {self.equipo_local.getNombre()} vs {self.equipo_visitante.getNombre()}
        Fecha: {self.fecha}
        Estadio: {self.estadio.getNombre()}'''
    def setTicketsVendidosCantidad(self, cantidad):
        self.tickets_vendidos_cantidad = cantidad
    
    def mostrarAsientosGeneral(self):
        diccionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        filas = len(self.estadio.capacidad_general)  # Número total de filas en el estadio

        # Imprimir la cabecera con las letras de las columnas solo una vez
        print('  |', ' | '.join(diccionario.values()), '|')

        # Imprimir cada fila con los asientos marcados
        for i in range(1, filas + 1):
            fila_str = f'{i:2} |'
            capacidad_fila = self.estadio.capacidad_general[i - 1]
            for j in range(10):
                if j < capacidad_fila:
                    asiento = f'{diccionario[j]}{i}'  # Construir la etiqueta del asiento (ej. 'A1', 'B1', ...)
                    if asiento in self.asientos_tomados:
                        fila_str += ' X |'
                    else:
                        fila_str += '   |'
                else:
                    fila_str += '   |'  # Asientos no existentes en esta columna
            print(fila_str)



    def mostrarAsientosVIP(self):
        diccionario = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
        filas = 43  # Número total de filas en el estadio

        # Imprimir la cabecera con las letras de las columnas
        header = ' | '.join([' ' + diccionario[i] for i in range(10)])
        print(f'{"":2} | {header} |')

        # Imprimir cada fila con los asientos marcados
        for i in range(1, filas + 1):
            fila_str = f'{i:2} |'
            for j in range(10):
                asiento = f'{i}-{j}'
                if asiento in self.asientos_tomados_vip:
                    fila_str += ' X  |'
                else:
                    fila_str += ' 0  |'
            print(fila_str)
        
    
