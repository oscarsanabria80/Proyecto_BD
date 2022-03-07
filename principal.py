import sys
import MySQLdb
from funcionesBD import *

db = conectar("localhost","python","1234","tienda")
option = "0"
while option != len(opcionesMenu):
    mostrarMenu()
    try:
        option = int(input("Por favor escoge una opción: "))
    except:
        print("Entrada errónea. Por favor introduce un número.")

    if option == 1:
        ListarInformacionClientes(db)
    elif option == 2:
        ListarInformacionProductos(db)
    elif option == 3:
        BuscarInformacionRangoPrecios(db)
    elif option == 4:
        BuscarVentasPorNombreVendedor(db)
    elif option == 5:
        AgregarCliente(db)
    elif option == 6:
        EliminarClientesPorProvincia(db)
    elif option == 7:
        ActualizarPrecioProductoPorColor(db)
    elif option == 8:
        print(u"\nGracias por usar el programa de gestión de [La Tienda De Ropa\u2122 Copyright: Oscar\xa9 2022]\n")
    else:
        print("Opción inválida. Por favor introduce un número entre 1 y %d.\n" % (len(opcionesMenu)))
        
desconectar(db)
