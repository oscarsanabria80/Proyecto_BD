"""
En este módulo defninimos todas las acciones para poder trabajar contra la BD.
"""

import mysql.connector

config = {
    'user': 'python',
    'password': '1234',
    'host': '127.0.0.1',
    'database': 'tienda',
    'raise_on_warnings': True
}

cnx = None

def conectar():
    global cnx
    cnx = mysql.connector.connect(**config)

def desconectar():
    global cnx
    cnx.close()

def select(query):
    try:
        conectar()
        global cnx
        cursor = cnx.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        print()
        for x in resultado:
            print(x)
        print()
    except mysql.connector.Error as err:
        print("Algo ha ido mal con la consulta: {}\n".format(err))
    finally:
        desconectar()

def selectCount(table):
    try:
        conectar()
        global cnx
        cursor = cnx.cursor()
        cursor.execute("SELECT COUNT(*) FROM {table}".format(table=table))
        resultado = cursor.fetchone()
        return resultado[0]
    except mysql.connector.Error as err:
        print("Algo ha ido mal con la consulta de agregado: {}\n".format(err))
    finally:
        desconectar()

def insert(insert):
    try:
        conectar()
        global cnx
        cursor = cnx.cursor()
        cursor.execute(insert)
        cnx.commit()
        print ("Nuevo registro insertado con éxito.\n")
    except mysql.connector.Error as err:
        print("Algo ha ido mal con la inserción: {}\n".format(err))
    finally:
        desconectar()

def delete(delete):
    try:
        conectar()
        global cnx
        cursor = cnx.cursor()
        cursor.execute(delete)
        cnx.commit()
        print ("Se ha(n) eliminado con éxito {numeroRegistros} registro(s).\n".format(numeroRegistros = cursor.rowcount))
    except mysql.connector.Error as err:
        print("Algo ha ido mal con la eliminiación: {}\n".format(err))
    finally:
        desconectar()

def update(update):
    try:
        conectar()
        global cnx
        cursor = cnx.cursor()
        cursor.execute(update)
        cnx.commit()
        print ("Se ha(n) actualizado con éxito {numeroRegistros} registro(s).\n".format(numeroRegistros = cursor.rowcount))
    except mysql.connector.Error as err:
        print("Algo ha ido mal con la actualización: {}\n".format(err))
    finally:
        desconectar()
