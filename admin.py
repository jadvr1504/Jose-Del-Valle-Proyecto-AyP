import requests
from cliente import*
from partidos import*
from ticket import*
from producto import*
from typing import List
from equipos import*
from estadios import*
import random
class Admin:
    def __init__(self):
         self.clientes = []
         self.partidos = []
         self.entradas = []
         self.tickets = []
         self.productos = []
         self.estadisticas = []
         self.equipos = []
         self.estadios = []
         self.asientos = []
         self.compras = []
         self.clientesvip=[]
         self.clientesgenerales=[]
         self.edad = 0
         self.IVA = 0.16
         self.ticket_list = []
         self.vip_gastos = []
         self.cedulas = {}
         self.relacion_asistencia_venta = 0


    def mostrar_datos(self):
            print(f"Nombre: {self.nombre}")
            print(f"Cedula: {self.cedula}")
            print(f"Edad: {self.edad}")
            print(f"Partido: {self.partido['local_team']['country_name']} vs {self.partido['visitor_team']['country_name']}, {self.partido['date_time']}, {self.partido['stadium']['name']}")
            print(f"Tipo de entrada: {self.tipo_entrada}")
            print(f"Precio: ${self.precio}")




    def register_teams(self):
        # Realizar solicitud GET a la API
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json')

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener la respuesta en formato JSON
            teams_data = response.json()

            # Iterar sobre los equipos en la respuesta JSON
            for team in teams_data:
                # Extraer la información necesaria
                team_id = team['id']
                country_name = team['name']
                fifa_code = team['code']
                group = team['group']

                # Crear un objeto Team para almacenar la información del equipo
                team_obj = equipo(team_id, fifa_code, country_name, group)

                # Agregar el equipo a la lista de equipos registrados
                self.equipos.append(team_obj)
                

            # Retornar la lista de equipos registrados
            
        else:
            # Si la solicitud falló, retornar un mensaje de error
            return 'Error al obtener la información de la API'

    
    

    def register_stadiums(self):
        # Realizar solicitud GET a la API
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json')

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener la respuesta en formato JSON
            stadiums_data = response.json()

            # Iterar sobre los estadios en la respuesta JSON
            for stadium in stadiums_data:
                # Extraer la información necesaria
                name = stadium['name']
                capacity = stadium['capacity'][0]
                restaurants = stadium['restaurants']
                location = stadium['city']
                stadium_id = stadium['id']

                # Crear un objeto Stadium para almacenar la información del estadio
                stadium_obj = Estadio(name, stadium_id, location, capacity,[],[], restaurants)

                # Agregar el estadio a la lista de estadios registrados
                self.estadios.append(stadium_obj)
                

        else:
            # Si la solicitud falló, retornar un mensaje de error
            return 'Error al obtener la información de la API'

 

    # Imprimir los estadios registrados
    def print_stadiums(self):
        for stadium in self.estadios:
            print(f"Estadio: {stadium['name']}, Ubicación: {stadium['city']}")

    def register_matches(self,):
        # Registrar equipos y estadios previamente
        teams = [equipo(team.id, team.code, team.name, team.group) for team in self.equipos]
        stadiums = [Estadio(stadium.name, stadium.id, stadium.location, stadium.capacity, stadium.capacidad_general,stadium.capacidad_VIP,stadium.restaurants) 
            for stadium in self.estadios]

        # Realizar solicitud GET a la API
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json')

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener la respuesta en formato JSON
            matches_data = response.json()

            # Iterar sobre los partidos en la respuesta JSON
            for match in matches_data:
                for estadio in self.estadios:
                     if match['stadium_id'] == estadio.id:
                # Extraer la información necesaria
                        fecha = match['date']
                        local_team=equipo(match['home']['id'],match['home']['code'],match['home']['name'],match['home']['group'])
                        visitor_team=equipo(match['away']['id'],match['away']['code'],match['away']['name'],match['away']['group'])
                        id_partido = match['id']
                # Crear un objeto Match para almacenar la información del partido
                        match_obj = partidos(id_partido, local_team, visitor_team, estadio,fecha,[],[])
                # Agregar el partido a la lista de partidos registrados
                        self.partidos.append(match_obj)
                
            
            # Si la solicitud falló, retornar un mensaje de error
            return 'Error al obtener la información de la API'
    def search_matches_by_country(self, country_name):
        """
        Buscar todos los partidos de un país
        """
        country_matches = []
        for match in self.partidos:
            if match.equipo_local.name == country_name or match.equipo_visitante.name == country_name:
                country_matches.append(match)
        return country_matches

    def search_matches_by_stadium(self, stadium_name):
        """
        Buscar todos los partidos que se jugarán en un estadio específico
        """
        stadium_matches = []
        for match in self.partidos:
            if match.estadio.get_name() == stadium_name:
                stadium_matches.append(match)
        return stadium_matches

    def search_matches_by_date(self, date):
        """
        Buscar todos los partidos que se jugarán en una fecha determinada
        """
        date_matches = []
        for match in self.partidos:
            if match.fecha == date:
                date_matches.append(match)
        return date_matches
    
    def calcular_costo(self):
            if self.cliente.es_vampiro():
                descuento = 0.5
            else:
                descuento = 0
            costo_base = self.tipo_entrada.precio
            costo_con_iva = costo_base * (1 + 0.16)
            costo_final = costo_con_iva * (1 - descuento)
            return costo_final

    def mostrar_datos(self):
            """
            Muestra los datos de una entrada para un partido de fútbol, incluyendo el costo final con descuentos y IVA.

             Imprime por pantalla la información de la entrada, incluyendo el partido, el asiento, y el costo final con un desglose de los conceptos que lo componen.

            :return: None
            """
            print(f"Entrada para el partido {self.partido.equipo_local.name} vs {self.partido.equipo_visitante.name}")
            print(f"Asiento: Fila {self.asiento[0]+1}, Columna {self.asiento[1]+1}")
            costo_base = self.tipo_entrada.precio
            cliente = None
            for cliente in self.clientes:
                if cliente.es_vampiro():
                    descuento = costo_base * 0.5
                break
            else:
                descuento = 0
            iva = costo_base * 0.16
            costo_final = costo_base - descuento + iva
            print(f"Costo:")
            print(f"  Subtotal: ${costo_base:.2f}")
            print(f"  Descuento: -${descuento:.2f}" if descuento > 0 else "")
            print(f"  IVA (16%): ${iva:.2f}")
            print(f"  Total: ${costo_final:.2f}")
    def pagar(self):
            """
            Procesa el pago de la entrada para un partido de fútbol.

            Pide al usuario si desea proceder a pagar la entrada. Si la respuesta es afirmativa,
            marca el asiento como pagado y muestra un mensaje de pago exitoso. De lo contrario,
            muestra un mensaje de pago cancelado.

            Returns:
                None
            """
            if input("¿Desea proceder a pagar la entrada? (s/n): ").lower() == 's':
                self.partido.stadium.asientos[self.asiento[0]][self.asiento[1]] = True
                print("Pago exitoso. Disfrute del partido!")
            else:
                print("Pago cancelado.")
    def validate(self):
            """
            Valida la cédula de un usuario y verifica si tiene un ticket válido.

            Pide al usuario que ingrese su cédula, luego busca en la lista de tickets si hay alguno que coincida con la cédula ingresada.
            Si se encuentra un ticket que coincida y su tipo de entrada es '2', llama al método `comprar_productos` para permitir al usuario comprar productos.
            Si no se encuentra un ticket que coincida, imprime un mensaje de error indicando que la cédula no fue encontrada.

            Parámetros:
            Ninguno

            Retorna:
            Ninguno
            """
            cedula_ingresada = input('Ingrese su cedula: ')
            for ticket in self.tickets:
                if ticket.cedula == cedula_ingresada:
                      if ticket.tipoentrada == '2':
                           self.comprar_productos(ticket)
                else:
                     print('Cedula no encontrada')
                

    def mostrar_compra(self):
            """
            Función para mostrar el resumen de una compra.
            Calcula el subtotal, descuento y total de la compra y los muestra en pantalla.
            Si el cliente tiene un número perfecto en su cédula, se aplica un descuento del 15% sobre el subtotal.
            :return: None
            """
            subtotal = sum(producto.precio for producto in self.compras)
            if self.es_numero_perfecto(self.cedula):
                descuento = subtotal * 0.15
            else:
                descuento = 0
            total = subtotal - descuento
            print("Resumen de la compra:")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Descuento: -${descuento:.2f}" if descuento > 0 else "")
            print(f"Total: ${total:.2f}")

    def pagar(self):
            if input("¿Desea proceder con la compra? (s/n): ").lower() == 's':
                print("Pago exitoso!")
                for producto in self.compras:
                    producto.restar_inventario()
            else:
                print("Compra cancelada")
    def es_vampiro(self, cedula):
        str_cedula = str(cedula)
        if len(str_cedula) % 2 != 0:
            return False

        half_len = len(str_cedula) // 2
        for i in range(10 ** (half_len - 1), 10 ** half_len):
            for j in range(i, 10 ** half_len):
                if i * j == cedula:
                    return True

        return False
    @staticmethod
    def es_numero_perfecto(n):
            sum = 0
            for x in range(1, n):
                if n % x == 0:
                    sum += x
            return sum == n
    

    def mostrar_productos(self, productos: List[Producto]):
        for producto in productos:
            print(f"Nombre: {producto.nombre}, Tipo: {producto.clasificacion}, Alcohólico: {producto.alcohólico}, Empaque: {producto.empaque}, Precio: {producto.precio:.2f}")
    
    def mostrar_todos_los_partidos(self):
        cadena_partidos = ''
        for idx, partido in enumerate(self.partidos):
            cadena_partidos += f'({idx +1}).{partido.mostrar()}\n\n'
        return cadena_partidos
    def realizar_venta_ticket(self):
        """
            Realiza la venta de un ticket para un partido de fútbol.

            Pide al usuario la información necesaria para la venta, como nombre, apellido, cedula, edad, partido seleccionado, tipo de entrada y asiento.
            Calcula el subtotal, IVA y descuento correspondientes.
            Imprime un resumen de la venta y pide confirmación al usuario.
            Si se confirma, registra la venta y crea un objeto Ticket con la información correspondiente.

            Returns:
                None
        """
        nombre = self._pedir_nombre()
        apellido = self._pedir_apellido()
        cedula = self._pedir_cedula()
        edad = self._pedir_edad()
        partido_seleccionado = self._seleccionar_partido()
        tipo_entrada = self._seleccionar_tipo_entrada()
        asiento = self._seleccionar_asiento(partido_seleccionado, tipo_entrada)
        subtotal, iva = self._calcular_subtotal_iva(tipo_entrada)
        descuento = self._calcular_descuento(cedula, subtotal)
        total = subtotal + iva - descuento
        numero_entrada = random.randint(100000, 999999)
        self.ticket_list.append(numero_entrada)
        self._imprimir_resumen(partido_seleccionado, asiento, subtotal, iva, descuento, total,numero_entrada)
        confirmar = self._pedir_confirmacion()
        if confirmar:
            pagado = True
            self._registrar_venta(partido_seleccionado, asiento, total, nombre, apellido, cedula, edad, tipo_entrada,numero_entrada)
            ticket_obj=Ticket(id,nombre,apellido,cedula,edad,partido_seleccionado,tipo_entrada,asiento,pagado,numero_entrada,[])
            self.tickets.append(ticket_obj)
            self.ticket_list.append(ticket_obj)
            self.cedulas[cedula]=[nombre,apellido,edad]
            print("¡Compra realizada con éxito!")

    def _registrar_venta(self, partido_seleccionado, asiento, total, nombre, apellido, cedula, edad, tipo_entrada,numero_entrada):
        tickets_vendidos = partido_seleccionado.getTicketsVendidosCantidad()
        if tickets_vendidos:  # Chequea si la lista no esta vacia
            partido_seleccionado.setTicketsVendidosCantidad(tickets_vendidos[0] + 1)
        else:
            partido_seleccionado.setTicketsVendidosCantidad([1])  # Empieza la lista en 1 si esta vacia
        partido_seleccionado.asientos_tomados.append(asiento)
        partido_seleccionado.setTicketsVendidosCantidad(partido_seleccionado.getTicketsVendidosCantidad()[0] + 1)
        id = partido_seleccionado.getTicketsVendidosCantidad()
        ticket_agg = Ticket(id, nombre, apellido, cedula, edad, partido_seleccionado, tipo_entrada, asiento, total,numero_entrada,[])
        partido_seleccionado.tickets.append(ticket_agg)
        print(ticket_agg.facturaEstandar())

    def _pedir_nombre(self):
        while True:
            nombre = input("Ingrese el nombre del cliente: ").strip()
            if nombre.isalpha():
                return nombre
            print("Por favor ingrese un nombre válido")

    def _pedir_apellido(self):
        while True:
            apellido = input("Ingrese el apellido del cliente: ").strip()
            if apellido.isalpha():
                return apellido
            print("Por favor ingrese un apellido válido")

    def _pedir_cedula(self):
        while True:
            cedula = input("Ingrese la cedula del cliente: ").strip()
            if cedula.isdigit() and len(cedula) == 8:
                return cedula
            print("Por favor ingrese un valor numérico válido")

    def _pedir_edad(self):
        while True:
            edad = input("Ingrese la edad del cliente: ").strip()
            if edad.isdigit() and 0 < int(edad) < 100:
                return edad
            print("Por favor ingrese una edad válida (entre 0 y 100)")

    def _seleccionar_partido(self):
        print("Seleccione un partido para comprar una entrada:")
        print("----------------------------------------------")
        for i, partido in enumerate(self.partidos, start=1):
            print(f"{i}. Partido : {partido.equipo_local.name} vs {partido.equipo_visitante.name} fecha: {partido.fecha}, estadio : {partido.estadio.get_name()}")
        print("----------------------------------------------")
        while True:
            indexpartido = input("Ingrese el número del partido deseado: ").strip()
            if indexpartido.isdigit() and 0 < int(indexpartido) <= len(self.partidos):
                return self.partidos[int(indexpartido) - 1]
            print("Por favor ingrese un valor válido")

    def _seleccionar_tipo_entrada(self):
        while True:
            opcion_entrada = input("Seleccione el tipo de entrada:\n"
                                "1. General ($35)\n"
                                "2. VIP ($75)\n"
                                "===> ").strip()
            if opcion_entrada in ['1', '2']:
                return opcion_entrada
            print("Error: Por favor ingrese un valor válido (1 o 2)")

    def _seleccionar_asiento(self, partido_seleccionado, tipo_entrada):
    
    # Bucle infinito hasta que se seleccione un asiento válido
        while True:
            # Si el tipo de entrada es '1', mostrar asientos generales y VIP
            if tipo_entrada == '1':
                partido_seleccionado.mostrarAsientosGeneral()
                partido_seleccionado.mostrarAsientosVIP()
                # Pedir columna y fila al usuario
                while True:
                    columna = input("Seleccione la columna (A-J):\n"
                                    "===> ").strip().upper()
                    # Verificar que la columna sea válida
                    if columna not in 'ABCDEFGHIJ':
                        print("Error: La columna debe ser una letra entre A y J.")
                    else:
                        break
                while True:
                    try:
                        fila = int(input("Seleccione la fila:\n"
                                        "===> ").strip())
                        # Verificar que la fila sea un número entero positivo
                        if fila <= 0:
                            print("Error: La fila debe ser un número entero positivo.")
                        else:
                            break
                    except ValueError:
                        print("Error: La fila debe ser un número entero.")
                # Crear el asiento en formato columna-fila
                asiento = f"{columna}{fila}"
                # Verificar si el asiento ya está ocupado
                if asiento not in partido_seleccionado.getAsientosTomados():
                    return asiento
                print("Error: Lo sentimos, ese asiento ya esta ocupado. Por favor seleccione otro.")
            # Si el tipo de entrada es '2', mostrar solo asientos VIP
            elif tipo_entrada == '2':
                partido_seleccionado.mostrarAsientosVIP()
                # Pedir columna y fila al usuario
                while True:
                    columna = input("Seleccione la columna (A-J):\n"
                                    "===> ").strip().upper()
                    if columna not in 'ABCDEFGHIJ':
                        print("Error: La columna debe ser una letra entre A y J.")
                        continue
                    break

                while True:
                    fila = input("Seleccione la fila:\n"
                                "===> ").strip()
                    if not fila.isdigit():
                        print("Error: La fila debe ser un número entero.")
                        continue
                    fila = int(fila)
                    if fila <= 0:
                        print("Error: La fila debe ser un número entero positivo.")
                        continue
                    break

                # Crear el asiento en formato columna-fila
                asiento = f"{columna}{fila}"
                # Verificar si el asiento ya está ocupado
                if asiento not in partido_seleccionado.getAsientosTomados():
                    return asiento
                print("Error: Lo sentimos, ese asiento ya esta ocupado. Por favor seleccione otro.")

    def _calcular_subtotal_iva(self, tipo_entrada):
    
        if tipo_entrada == '1':
            subtotal = VentaTicket.PRECIO_GENERAL
        else:
            subtotal = VentaTicket.PRECIO_VIP
        iva = round(subtotal * self.IVA, 2)
        return subtotal, iva


    def _calcular_descuento(self, cedula, subtotal):
        """
        Calcula el descuento según la cédula del comprador.

        Args:
            cedula (int): Número de cédula del comprador.
            subtotal (float): Subtotal de la venta.

        Returns:
            float: El descuento aplicado.
        """
        if self.es_vampiro(int(cedula)):
            return 0.50 * subtotal
        return 0


    def _imprimir_resumen(self, partido_seleccionado, asiento, subtotal, iva, descuento, total, numero_entrada):
        """
        Imprime un resumen de la venta.

        Args:
            partido_seleccionado: Partido seleccionado.
            asiento (str): Asiento seleccionado.
            subtotal (float): Subtotal de la venta.
            iva (float): IVA de la venta.
            descuento (float): Descuento aplicado.
            total (float): Total de la venta.
            numero_entrada (int): Número de entrada.

        Returns:
            None
        """
        numero_entrada = random.randint(100000, 999999)
        print(f"""
            Partido  : {partido_seleccionado.mostrarSencillo()}
            Asiento  : {asiento}
            Subtotal : {subtotal} $
            IVA      : {iva} $
            Descuento: {descuento} $
            Total    : {total} $
            
            """)

    def _pedir_confirmacion(self):
        while True:
            confirmar = input("¿Desea confirmar la compra?\n(S/N)\n==> ").strip().upper()
            if confirmar in ['S', 'N']:
                return confirmar == 'S'
            print("Por favor ingrese una opcion válida")
    
    def mostrarSencillo(self):
        return f'''{self.local.getNombre()} vs {self.visitante.getNombre()} el {self.fecha} en el {self.estadio.getNombre()}'''
    
    def mostrar_restaurantes_y_productos(self):
        """
            Muestra la información de los estadios, restaurantes y productos.

            Realiza una solicitud GET a una API para obtener la información de los estadios,
            y luego itera sobre cada estadio para mostrar su nombre, ID, ubicación, capacidad
            y lista de restaurantes. Para cada restaurante, muestra su nombre y lista de productos,
            incluyendo el precio sin IVA y con IVA para cada producto.

            No devuelve ningún valor, solo imprime la información en la consola.

            Parameters:
            self (object): El objeto que llama a esta función (no se utiliza en la implementación)

            Returns:
            None
            """
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json')
        data = response.json()

        for stadium in data:
            name = stadium['name']
            stadium_id = stadium['id']
            location = stadium['city']
            capacity = stadium['capacity']
            restaurants = stadium['restaurants']

            estadio = Estadio(name, stadium_id, location, capacity,[],[], restaurants)

            print(f"Estadio: {estadio.name} ID: {estadio.id} Ubicacion: {estadio.location} Capacidad: {estadio.capacity}")
            for restaurante in estadio.restaurants:
                print(f"  Restaurante: {restaurante['name']}")  
                for producto in restaurante['products']:
                    precio_sin_iva = float(producto['price'])
                    precio_con_iva = precio_sin_iva * 1.16
                    print(f"    Producto: {producto['name']}, Precio sin IVA: ${precio_sin_iva:.2f}, Precio con IVA: ${precio_con_iva:.2f}")
    
       
    def buscar_productos_nombre(self, nombre):
        for producto in self.productos:
            if producto.name in nombre:
                print(producto.show())  # Assuming producto has a show method
                return producto
        return None
                


    def descargar_productos_api(self):
        """
    Descarga productos desde la API y los almacena en la lista self.productos.

    No requiere parámetros adicionales, ya que utiliza una URL fija para la API.

    Returns:
        None

    """
        response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json')
        data = response.json()
        for stadium in data:
            for restaurant in stadium['restaurants']:
                for product_data in restaurant['products']:
                    nombre = product_data['name']
                    adicional = product_data['adicional']
                    cantidad = product_data['quantity']
                    precio = product_data['price']
                    if adicional in ['plate', 'package']:
                         tipo = 'food'
                    else:
                         tipo = 'drink'
                    producto = Producto(nombre , precio , adicional , cantidad,tipo ,[])
                    self.productos.append(producto)
    def mostrar_productos(self):
        print("Productos disponibles:")
        for producto in self.productos:
            producto.show()
        
    def buscar_productos_por_tipo(self, tipo: str):
        for producto in self.productos:
            if producto.tipo == tipo:
                producto.show()
       
            
    def buscar_productos_por_rango_precio(self):
        min_price = float(input("Ingrese el precio mínimo: "))
        max_price = float(input("Ingrese el precio máximo: "))

        resultados = []
        for producto in self.productos:
            if min_price <= producto.price <= max_price:
                resultados.append(producto)

        if resultados:
            print("Productos encontrados:")
            for producto in resultados:
                print(f"Nombre: {producto.name}, Precio: ${producto.price:.2f}")
        else:
            print("No se encontraron productos en ese rango de precio")
    def comprar_productos(self,ticket):
        print("Compra de productos")
        print("------------------")

        # Mostrar productos disponibles
        print("Productos disponibles:")
        for producto in self.productos:
            producto.show()

        # Input productos seleccionados
        productos_seleccionados = []
        while True:
            producto_seleccionado = input("Seleccione el nombre del producto que desea comprar (o 'fin' para terminar): ")
            if producto_seleccionado.lower() == 'fin':
                break
            for producto in self.productos:
                if producto.name.lower() == producto_seleccionado.lower():
                    if self.edad < 18 and producto.es_alcoholico:
                        print("No se puede vender bebidas alcohólicas a menores de 18 años")
                    else:
                        productos_seleccionados.append(producto)
                    break
            else:
                print("Producto no encontrado")

        # Mostrar resumen de la compra
        subtotal = sum(producto.price for producto in productos_seleccionados)
        if self.es_numero_perfecto(int(ticket.cedula)):
            descuento = subtotal * 0.15
        else:
            descuento = 0
        total = subtotal - descuento

        print("Resumen de la compra:")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento: -${descuento:.2f}" if descuento > 0 else "")
        print(f"Total: ${total:.2f}")

        # Procesar pago
        if input("¿Desea proceder con la compra? (s/n): ").lower() == 's':
            print("Pago exitoso!")
            for producto in productos_seleccionados:
                producto.restar_inventario(1)
        else:
            print("Compra cancelada")
    def chequear_entradas(self):
        while True:
            entrada_revisando = input("Por favor ingrese el numero de entrada a chequear: ").strip()
            while not entrada_revisando.isdigit() or int(entrada_revisando) not in range(100000, 999999):
                print('Por favor ingrese un numero de entrada valido')
                entrada_revisando = input("Por favor ingrese el numero de entrada a chequear: ")
            estatus = 'Entrada no encontrada'
            if int(entrada_revisando) in [ticket.numero_entrada for ticket in self.tickets]:
                estatus = 'Bienvenido a su partido, que disfrute!'
            else:
                estatus = f'No hay entrada numero: {entrada_revisando}'
            print(estatus)
            opcion = input('Desea registrar otra entrada?(S/N): ').upper()
            while opcion not in ['S', 'N']:
                print('Por favor ingrese una respuesta valida')
                opcion = input('Desea registrar otra entrada (S/N): ')
            if opcion == 'S':
                continue
            else:
                break
    def mostrar_menu_estat(self):
        print("Menú de opciones:")
        print("1. Ver promedio de gasto VIP")
        print("2. Ver tabla de asistencia")
        print("3. Ver partido con mayor asistencia")
        print("4. Ver partido con mayor cantidad de boletos vendidos")
        print("5. Ver top 3 productos vendidos")
        print("6. Ver top 3 clientes")
        print("7. Guardar datos en archivo")
        print("8. Salir")
    
    def promedio_gasto_vip(self):
        gastos_vip = [ticket.gasto for ticket in self.tickets if ticket.tipoentrada == 'VIP']
        if not gastos_vip:
            return 'No hay gastos VIP registrados todavía'
        else:
            total_gastos = sum(gastos_vip)
            promedio_gastos = total_gastos / len(gastos_vip)
            return f'El gasto promedio de los tickets VIP fue: {promedio_gastos}$'
            

    def tabla_asistencia(self):
        """
        Retorna una lista de partidos ordenados por la relación asistencia/venta de manera descendente.
        """
        partidos_ordenados = sorted(self.partidos, key=lambda x: x.asistencia / sum(x.tickets_vendidos_cantidad) if x.tickets_vendidos_cantidad else float('inf'))
        return partidos_ordenados


    def boletos_vendidos(self):
            """
            Muestra los partidos ordenados por la cantidad de boletos vendidos en orden descendente.

            Recorre la lista de partidos (`match_list`), recoge cada partido junto con la boletos_vendidos 
            (cantidad de boletos vendidos), y los almacena en una lista de tuplas. Luego, ordena 
            esta lista en orden descendente basado en la cantidad de boletos vendidos y muestra 
            los partidos con su boletos_vendidos.
            """
            boletos_vendidos = []
            asistencia=[]
            for partido in self.partidos:
                boletos_vendidos.append((partido, partido.tickets_vendidos_cantidad))
                asistencia.append()
            
            
            # segun la documentacion de python: 
            # "Las expresiones lambda (a veces denominadas formas lambda) son usadas para crear funciones anónimas. La expresión lambda parameters: expression produce un objeto de función."
            boletos_vendidos.sort(key=lambda x: x[1], reverse=True)

            print("Partidos con mayor venta de boletos:")
            for (i,(partido, cantidad)) in enumerate(boletos_vendidos,start=1):
                print(f"{i}-{partido.show_sinfecha()}: {cantidad} boletos vendidos")

    def partido_mayor_asistencia(self):
        if not self.partidos:
            return 'No hay partidos registrados todavía'
        
        # Ordenar la lista de partidos por asistencia en orden descendente
        partidos_ordenados = sorted(self.partidos, key=lambda x: x.asistencia, reverse=True)
        
        # Devolver el primer partido de la lista ordenada (mayor asistencia)
        return partidos_ordenados[0]



    def topproductos(self):
        # Crear una lista de tuplas con el nombre del producto y la cantidad vendida
        prod_porventas = [(producto.name, producto.vendido) for producto in self.productos]

        # Ordenar la lista por cantidad vendida en orden descendente
        productos_ord = sorted(prod_porventas, key=lambda x: x[1], reverse=True)

        # Obtener los top 3 productos (o menos si hay menos de 3 productos)
        top_productos = productos_ord[:3]

        return top_productos



    def topclientes(self):
        """
    Devuelve una lista de los 3 clientes con más tickets comprados.

    Returns:
        list: Una lista de tuplas, donde cada tupla contiene el nombre del cliente y la cantidad de tickets comprados.
              Si no hay clientes, devuelve una lista con una sola tupla que contiene un mensaje y 0.
    """
        clientes = {}
        for ticket in self.ticket_list:
            if ticket.nombre in clientes:
                clientes[ticket.nombre] += 1
            else:
                clientes[ticket.nombre] = 1
        
        clientes_ordenados = sorted(clientes.items(), key=lambda x: x[1], reverse=True)
        top_clientes = []
        for idx, cliente in enumerate(clientes_ordenados):
            top_clientes.append((cliente[0], cliente[1]))
            if idx == 2:
                break
        
        if not top_clientes:
            return [("No hay clientes todavía", 0)]
        else:
            return top_clientes
    def partido_mayor_boletos_vendidos(self):
        if not self.partidos:
            return "No hay partidos registrados todavía"
        
        partido_con_mas_boletos = max(self.partidos, key=lambda x: x.tickets_vendidos_cantidad)
        
        return f"El partido con mayor cantidad de boletos vendidos fue: {partido_con_mas_boletos.equipo_local.name} vs {partido_con_mas_boletos.equipo_visitante.name} en {partido_con_mas_boletos.estadio.name} con {partido_con_mas_boletos.tickets_vendidos_cantidad} boletos vendidos."




    def guardar_datos(self):
        """
    Guarda las estadísticas de la temporada en un archivo de texto llamado 'estadisticas.txt'.

    El archivo contiene la siguiente información:

    * Promedio de gasto de los clientes VIP
    * Tabla de asistencia por partido, incluyendo la relación entre asistencia y boletos vendidos
    * Partido con mayor asistencia
    * Partido con mayor cantidad de boletos vendidos
    * Top 3 productos vendidos, con la cantidad de unidades vendidas
    * Top 3 clientes, con la cantidad de boletos comprados

    :return: None
    """
        with open('estadisticas.txt', 'w') as f:
            f.write(f'Promedio gasto VIP: {self.promedio_gasto_vip()}\n')
            f.write('Tabla asistencia:\n')
            tabla_asistencia = self.tabla_asistencia()
            for partido in tabla_asistencia:
                relacion_asistencia_venta = partido.asistencia / partido.tickets_vendidos_cantidad if partido.tickets_vendidos_cantidad else 0
                f.write(f'  {partido.equipo_local.name} vs {partido.equipo_visitante.name}: {partido.asistencia} asistentes, {partido.tickets_vendidos_cantidad} boletos vendidos, {relacion_asistencia_venta:.2f} relacion asistencia/venta\n')
            f.write(f'Partido mayor asistencia: {self.partido_mayor_asistencia()}\n')
            f.write(f'Partido mayor boletos vendidos: {self.partido_mayor_boletos_vendidos()}\n')
            f.write('Top 3 productos vendidos:\n')
            top_productos = self.topproductos()
            for producto, cantidad in top_productos:
                f.write(f'  {producto}: {cantidad} unidades\n')
            f.write('Top 3 clientes:\n')
            top_clientes = self.topclientes()
            for cliente, cantidad in top_clientes:
                f.write(f'  {cliente}: {cantidad} boletos comprados\n')
    def calculate_relacion_asistencia_venta(self,partido):
        
        self.relacion_asistencia_venta = partido.asistencia / partido.tickets_vendidos_cantidad
        
