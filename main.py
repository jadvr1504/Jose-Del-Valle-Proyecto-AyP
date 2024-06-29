# main.py

from admin import *
admin_instance = Admin()
url_equipos = ''''https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json'''
url_partidos = '''https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json'''
url_estadios = '''https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json'''
admin_instance.register_teams()
admin_instance.register_stadiums()
admin_instance.register_matches()
admin_instance.descargar_productos_api()


def main():
    while True:
        print("Menu:")
        print("1. Buscar todos los partidos de un país")
        print("2. Buscar todos los partidos que se jugarán en un estadio específico")
        print("3. Buscar todos los partidos que se jugarán en una fecha determinada")
        print("4. Comprar entrada")
        print("5. Mostrar restaurantes y productos")
        print("6. Buscar productos")
        print("7. Comprar productos")
        print("8. Chequear entradas")
        print("9. Verificar estadisticas:")
        print("10. Salir")
        option = input("Ingrese una opción: ")

        if option == "1":
            country_name = input("Ingrese el nombre del país: ")
            if not country_name:
                print("Debe ingresar un nombre de país")
            else:
                matches = admin_instance.search_matches_by_country(country_name)
                print("Partidos encontrados:")
                for match in matches:
                    print(match.show())

        elif option == "2":
            stadium_name = input("Ingrese el nombre del estadio: ")
            if not stadium_name:
                print("Debe ingresar un nombre de estadio")

            else:
                matches = admin_instance.search_matches_by_stadium(stadium_name)
                print("Partidos encontrados:")
                for match in matches:
                    print(match.show())

        elif option == "3":
            date = input("Ingrese la fecha 2024-06-_: ").strip()
            if not date:
                print("Debe ingresar una fecha")
            else:
                date = f'2024-06-{date}'
                matches = admin_instance.search_matches_by_date(date)
                print("Partidos encontrados:")
                for match in matches:
                    print(match.show())

        elif option == "4":
                admin_instance.realizar_venta_ticket()

        elif option == "5":
            admin_instance.mostrar_restaurantes_y_productos()

        elif option == "6":
            while True:
                print('Seleccione un tipo de Busqueda:')
                print('1. Por nombre')
                print('2. Por tipo de producto')
                print('3. Por rango de precio')
                print('4. Volver al menu principal')
                option = input("Ingrese una opción: ")
                if option == '1':
                    nombre = input("Ingrese el nombre del producto: ")
                    if not nombre:
                        print("Debe ingresar un nombre de producto")
                    else:
                        print(len(admin_instance.productos))
                        admin_instance.buscar_productos_nombre(nombre)
                elif option == '2':
                    tipo_producto = input("Ingrese el tipo de producto: ")
                    if not tipo_producto:
                        print("Debe ingresar un tipo de producto")
                    else:
                        admin_instance.buscar_productos_por_tipo(tipo_producto)
                elif option == '3':
                    admin_instance.buscar_productos_por_rango_precio()
                elif option == '4':
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

        elif option == '7':
                admin_instance.validate()

        elif option == '8':
            admin_instance.chequear_entradas()
        
        elif option =='9':
            while True:
                admin_instance.mostrar_menu_estat()
                opcion = input("Ingrese una opción: ")

                if opcion == "1":
                    print(f"Promedio de gasto VIP: {admin_instance.promedio_gasto_vip()}")
                elif opcion == "2":
                    tabla_asistencia = admin_instance.tabla_asistencia()
                    print("Tabla de asistencia:")
                    for partido in tabla_asistencia:
                        print(f"  {partido.equipo_local.name} vs {partido.equipo_visitante.name}: {partido.asistencia} asistentes, {partido.tickets_vendidos_cantidad} boletos vendidos, {admin_instance.relacion_asistencia_venta:.2f} relacion asistencia/venta")
                elif opcion == "3":
                    print(f"Partido con mayor asistencia: {admin_instance.partido_mayor_asistencia()}")
                elif opcion == "4":
                    print(f"Partido con mayor cantidad de boletos vendidos: {admin_instance.boletos_vendidos()}")
                elif opcion == "5":
                    top_productos = admin_instance.topproductos()
                    print("Top 3 productos vendidos:")
                    for producto, cantidad in top_productos:
                        print(f"  {producto}: {cantidad} unidades")
                elif opcion == "6":
                    top_clientes = admin_instance.topclientes()
                    print("Top 3 clientes:")
                    for cliente, cantidad in top_clientes:
                        print(f"  {cliente}: {cantidad} boletos comprados")
                elif opcion == "7":
                    admin_instance.guardar_datos()
                    print("Datos guardados en archivo estadisticas.txt")
                elif opcion == "8":
                    print("Saliendo...")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")


                    
        elif option == '10':
            print('Saliendo...')
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()