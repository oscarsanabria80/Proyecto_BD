
![](ModeloRelacional.png)

# Proyecto_BD

* Listar información: 1.Listar clientes.


* Contar información: 2.Listar productos.


* Buscar o filtrar información: 3.Buscar productos en un rango de precios.


* Buscar información relacionada: 4.Mostrar los ventas de un trabajador filtrando por nombre.


* Insertar información: 5.Agregar nuevo cliente.


* Borrar información: 6.Eliminar clientes por provincia.


* Actualizar información: 7.Incrementar precio de productos según color.

# CONTENIDO DEL PROYECTO

MANEJADOR DE BASES DE DATO

	Con este módulo trabajamos todas las definiciones para poder trabajar con la BD.

INSTALACIÓN DE BASE DE DATO

	Procesos de instalación de BD.

FICHERO TIENDA.PY

	Contiene todas las funciones y las opciones para poder ejecutar el programa.

FICHERO TIENDA.SQL

	Contiene todas las creaciones de tablas y sus inserción de datos.
	
MODELO RELACIONAL.

	Contiene el tipo de relación que tendra nuestra base de datos.
	
# Instalar pip
	apt-get install python3-pip

# Instalar conector de mysql para python
	pip install mysql-connector-python

# Instalar MariaDB
	apt install mariadb-server
	systemctl status mariadb
	systemctl enable mariadb

# Crear BBDD mysql
	cd
	mkdir practicaOscar && cd $_
# Copiar tienda.sql a la carpeta actual
	sudo mysql
    		CREATE DATABASE IF NOT EXISTS tienda;
    		GRANT all privileges ON tienda.* TO python identified BY '1234' WITH GRANT OPTION;
	sudo mysql tienda < tienda.sql
