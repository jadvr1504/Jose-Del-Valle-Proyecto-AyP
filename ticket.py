from producto import*
from admin import*
class Ticket:
    def __init__(self,id, nombre, apellido, cedula, edad, partido, tipoentrada, asiento, pagado,numero_entrada,gasto):
            self.id= id
            self.nombre = nombre
            self.apellido = apellido
            self.cedula = cedula
            self.edad = edad
            self.partido = partido
            self.tipoentrada = tipoentrada
            self.asiento = asiento
            self.pagado = pagado
            self.numero_entrada = numero_entrada
            self.gasto = gasto
            
        
            
    def mostrar(self):
            return f'''
        Cliente : {self.nombre} {self.apellido}  
        Cedula  : {self.cedula}
        Edad    : {self.edad} años
        Partido : {self.partido.mostrarSinEstadio()}
        Entrada : {self.tipoentrada}
        Asiento : {self.asiento}'''
        
    def facturaEstandar(self):
            return f'''
        ID                 : {self.id}
        Nomrbe del cliente : {self.nombre} {self.apellido}
        Cédula             : {self.cedula}
        Edad               : {self.edad} años
        Partido            : {self.partido.mostrarSencillo()}        
        Entrada            : {self.tipoentrada}
        Asiento            : {self.asiento}
        Numero de entrada  : {self.numero_entrada}
        '''
    def total(self):
        if self.tipoentrada.nombre == 'VIP':
            return VentaTicket.PRECIO_VIP * (1 + VentaTicket.IVA)
        else:
            return VentaTicket.PRECIO_GENERAL * (1 + VentaTicket.IVA)
    

class TipoEntrada:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
class VentaTicket:
    PRECIO_GENERAL = 35
    PRECIO_VIP = 75
    IVA = 0.16
class Entrada:
    def __init__(self, chequeado=False):
        self.chequeado = chequeado