import MySQLdb
import sys


def conectar(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as err:
        print("Algo ha ido mal con la consulta: %s\n" % err)
        sys.exit(1)

def desconectar(db):
    db.close()


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


def ListarInformacionClientes(db):
    print("\n[Listado de clientes]")
    select(db, "SELECT * FROM cliente")
    print("[Número de clientes listados: %d]\n" % (db, "cliente"))

def ListarInformacionProductos(db):
    print("\n[Listado de productos]")
    select(db, "SELECT * FROM producto")
    print("[Número de productos listados: %d]\n" % (db, "producto"))

def BuscarInformacionRangoPrecios(db):
    try:
        precioMinimo = int(input("\nPor favor introduce el precio mínimo a buscar [0-9999]€: "))
        precioMaximo = int(input("Por favor introduce el precio máximo a buscar [0-9999]€: "))
        if precioMinimo < 0 or precioMinimo > 9999 or precioMaximo < 0 or precioMaximo > 9999:
            print("El rango de precios a buscar es inválido introduce un valor entre 0€ y 9999€\n")
            return
        if precioMinimo > precioMaximo:
            print("El precio mínimo no puede ser mayor al precio máximo\n")
            return
        print("\n[Listado de productos entre %d€ y %d€]" % (precioMinimo, precioMaximo))
        select(db, "SELECT * FROM producto WHERE precio >= %d AND precio <= %d" % (precioMinimo, precioMaximo))
    except:
        print("Entrada errónea. Por favor introduce un número.\n")

def BuscarVentasPorNombreVendedor(db):
    nombre = input("\nPor favor introduce el nombre del vendedor a buscar, no importan mayusculas ni minúsculas ni si está completo, contra más preciso sea el nombre más precisos serán los resultados: ")
    print("\n[Listado de todos los productos vendidos por el/los vendedor(es) llamado(s) %s" % nombre)
    select(db,
        ("SELECT producto.ropa, producto.color, producto.precio FROM producto "
         "INNER JOIN (SELECT idproducto FROM venta "
         "INNER JOIN (SELECT id FROM vendedor WHERE LOWER (nombre) LIKE '%" + nombre.lower() + "%') as T "
         "ON T.id = venta.idvendedor) AS U on producto.id = U.idproducto"))

def AgregarCliente(db):
    email = input("\nPor favor introduce el mail del cliente: ")
    try:
        telefono = int(input("Por favor introduce el teléfono del cliente: "))
    except:
        print("Entrada errónea. Por favor introduce un número.\n")
        return
    provincia = input("Por favor introduce la provincia del cliente: ")
    insert(db, "INSERT INTO cliente (email, tlf, provincia) VALUES ('%s',%d,'%s')" % (email, telefono, provincia))

def EliminarClientesPorProvincia(db):
    provincia = input("\nPor favor introduce la provincia de la cual eliminarás TODOS los clientes y en cascada TODAS las compras de esos clientes: ")
    delete(db, "DELETE FROM cliente WHERE provincia = '%s'" % provincia)

def ActualizarPrecioProductoPorColor(db):
    try:
        porcentaje = int(input("\nPor favor introduce el porcentaje a incrementar [1-100]%: "))
        color = input("\nPor favor introduce el color de los productos que quieres actualizar: ")
        if porcentaje < 1 or porcentaje > 100:
            print("El procentaje a incrementar debe estar entre el 1% y el 100%\n")
            return
        update(db, "UPDATE producto SET precio = precio + precio * %d / 100 WHERE color = '%s'" % (porcentaje, color))
    except:
        print("Entrada errónea. Por favor introduce un número.\n")
