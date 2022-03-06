import os
import manejadorBD

opcionesMenu = {
    1: "Listar clientes.",
    2: "Listar productos.",
    3: "Buscar productos en un rango de precios.",
    4: "Mostrar los ventas de un trabajador filtrando por nombre.",
    5: "Agregar nuevo cliente.",
    6: "Eliminar clientes por provincia.",
    7: "Incrementar precio de productos según color.",
    8: "Salir.",
}

def mostrarMenu():
    print("Opciones:")
    for key in opcionesMenu.keys():
        print("\t", key, ") ", opcionesMenu[key])
    print()

def mostrarBienvenida():
    print(u"Bienvenido al programa de gestión de [La Tienda De Ropa\u2122 Copyright: Oscar\xa9 2022]\n")

def ListarInformacionClientes():
    print("\n[Listado de clientes]")
    manejadorBD.select("SELECT * FROM cliente")
    print("[Número de clientes listados: {numero}]\n".format(numero=manejadorBD.selectCount("cliente")))

def ListarInformacionProductos():
    print("\n[Listado de productos]")
    manejadorBD.select("SELECT * FROM producto")
    print("[Número de productos listados: {numero}]\n".format(numero=manejadorBD.selectCount("producto")))

def BuscarInformacionRangoPrecios():

        precioMinimo = int(input("\nPor favor introduce el precio mínimo a buscar [0-9999]€: "))
        precioMaximo = int(input("Por favor introduce el precio máximo a buscar [0-9999]€: "))

        if (precioMinimo < 0 or precioMinimo > 9999 or precioMaximo < 0 or precioMaximo > 9999):
            print("El rango de precios a buscar es inválido introduce un valor entre 0€ y 9999€\n")
            return
        if (precioMinimo > precioMaximo):
            print("El precio mínimo no puede ser mayor al precio máximo\n")
            return

        print("\n[Listado de productos entre {precioMinimo}€ y {precioMaximo}€]".format(precioMinimo=precioMinimo, precioMaximo=precioMaximo))
        manejadorBD.select("SELECT * FROM producto WHERE precio >= {precioMinimo} AND precio <= {precioMaximo}".format(precioMinimo=precioMinimo, precioMaximo=precioMaximo))

def BuscarVentasPorNombreVendedor():
    nombre = input("\nPor favor introduce el nombre del vendedor a buscar, no importan mayusculas ni minúsculas ni si está completo, contra más preciso sea el nombre más precisos serán los resultados: ")
    print("\n[Listado de todos los productos vendidos por el/los vendedor(es) llamado(s) {nombre}".format(nombre=nombre))
    manejadorBD.select(
        ("SELECT producto.ropa, producto.color, producto.precio FROM producto "
         "INNER JOIN (SELECT idproducto FROM venta "
         "INNER JOIN (SELECT id FROM vendedor WHERE LOWER (nombre) LIKE '%{nombre}%') as T "
         "ON T.id = venta.idvendedor) AS U on producto.id = U.idproducto").format(nombre=nombre.lower()))

def AgregarCliente():
    email = input("\nPor favor introduce el mail del cliente: ")

        telefono = int(input("Por favor introduce el teléfono del cliente: "))
        return
    provincia = input("Por favor introduce la provincia del cliente: ")
    manejadorBD.insert("INSERT INTO cliente (email, tlf, provincia) VALUES ('{email}',{telefono},'{provincia}')".format(email=email, telefono=telefono, provincia=provincia))

def EliminarClientesPorProvincia():
    provincia = input("\nPor favor introduce la provincia de la cual eliminarás TODOS los clientes y en cascada TODAS las compras de esos clientes: ")
    manejadorBD.delete("DELETE FROM cliente WHERE provincia = '{provincia}'".format(provincia=provincia))

def ActualizarPrecioProductoPorColor():
    
        porcentaje = int(input("\nPor favor introduce el porcentaje a incrementar [1-100]%: "))
        color = input("\nPor favor introduce el color de los productos que quieres actualizar: ")

        if (porcentaje < 1 or porcentaje > 100):
            print("El procentaje a incrementar debe estar entre el 1% y el 100%\n")
            return
        
        manejadorBD.update("UPDATE producto SET precio = precio + precio * {porcentaje} / 100 WHERE color = '{color}'".format(porcentaje=porcentaje, color=color))
 


if __name__ == "__main__": #Con este if lo que estoy haciendo es ejecutarlo como programa principal.
    mostrarBienvenida()
    option = "0"
    
    while(option != len(opcionesMenu)):
        mostrarMenu()
        try:
            option = int(input("Por favor escoge una opción: "))
        except:
            print("Entrada errónea. Por favor introduce un número.")
       
        if option == 1:
            ListarInformacionClientes()
        elif option == 2:
            ListarInformacionProductos()
        elif option == 3:
            BuscarInformacionRangoPrecios()
        elif option == 4:
            BuscarVentasPorNombreVendedor()
        elif option == 5:
            AgregarCliente()
        elif option == 6:
            EliminarClientesPorProvincia()
        elif option == 7:
            ActualizarPrecioProductoPorColor()
        elif option == 8:
           
            print(u"\nGracias por usar el programa de gestión de [La Tienda De Ropa\u2122 Copyright: Oscar\xa9 2022]\n")
        else:
            print("Opción inválida. Por favor introduce un número entre 1 y {}.\n".format(len(opcionesMenu)))
    

    exit()
