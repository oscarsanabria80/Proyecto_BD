USE tienda;
-- CREACION DE LAS TABLAS.
CREATE TABLE cliente (
    id int(5) NOT NULL AUTO_INCREMENT,
    email varchar(20),
    tlf int(9),
    provincia varchar(20),
    PRIMARY KEY (id),
    UNIQUE (email)
);
CREATE TABLE producto (
    id int(5) NOT NULL AUTO_INCREMENT,
    ropa varchar(20),
    color varchar(15),
    precio int(4),
    PRIMARY KEY (id)
);
CREATE TABLE vendedor (
    id int(5) NOT NULL AUTO_INCREMENT,
    nombre varchar(20),
    PRIMARY KEY (id)
);
CREATE TABLE venta (
    idcliente int(5),
    idproducto int(5),
    idvendedor int(5),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (idcliente) REFERENCES cliente(id) ON DELETE CASCADE,
    FOREIGN KEY (idproducto) REFERENCES producto(id),
    FOREIGN KEY (idvendedor) REFERENCES vendedor(id),
    PRIMARY KEY(idcliente, idproducto, idvendedor, fecha)
);
-- INSERTS DE LA TABLA CLIENTE
INSERT cliente(email, tlf, provincia)
values ('pepe@gmail.com', 453267839, 'Sevilla');
INSERT cliente( email, tlf, provincia)
values ('oscar@gmail.com', 453267342, 'Cordoba');
INSERT cliente( email, tlf, provincia)
values ('luca@gmail.com', 384569235, 'Albacete');
INSERT cliente( email, tlf, provincia)
values ('emilio@gmail.com', 267894567, 'Madrid');
INSERT cliente( email, tlf, provincia)
values ('ana@gmail.com', 321245432, 'Barcelona');
INSERT cliente( email, tlf, provincia)
values ('rocio@gmail.com', 876564356, 'Bilbao');
INSERT cliente( email, tlf, provincia)
values ('juanma@gmail.com', 654675643, 'Avila');
-- INSERTS DE LA TABLA PRODUCTO
INSERT producto(id, ropa, color, precio)
values (1, 'vaqueros', 'rojo', 10);
INSERT producto(id, ropa, color, precio)
values (2, 'camiseta', 'blanco', 20);
INSERT producto(id, ropa, color, precio)
values (3, 'chaqueta', 'verde', 50);
INSERT producto(id, ropa, color, precio)
values (4, 'jersey', 'amarillo', 100);
INSERT producto(id, ropa, color, precio)
values (5, 'sudadera', 'azul', 200);
INSERT producto(id, ropa, color, precio)
values (6, 'calcetines', 'azul', 500);
INSERT producto(id, ropa, color, precio)
values (7, 'vaquerosslim', 'negro', 1000);
-- INSERTS DE LA TABLA VENDEDOR
INSERT vendedor(id, nombre)
values (1, 'pepe');
INSERT vendedor(id, nombre)
values (2, 'paco');
INSERT vendedor(id, nombre)
values (3, 'edu');
INSERT vendedor(id, nombre)
values (4, 'ramon');
INSERT vendedor(id, nombre)
values (5, 'salvi');
INSERT vendedor(id, nombre)
values (6, 'juanjo');
INSERT vendedor(id, nombre)
values (7, 'lucas');
INSERT vendedor(id, nombre)
values (8, 'alberto');
-- INSERTS DE LA TABLA VENTA
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (1, 4, 1, '2020-12-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (1, 3, 1, '2020-11-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (2, 4, 1, '2020-10-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (2, 7, 1, '2020-09-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (3, 4, 1, '2021-08-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (3, 6, 1, '2020-07-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (4, 1, 2, '2020-06-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (4, 4, 2, '2020-05-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (5, 5, 3, '2022-04-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (5, 7, 4, '2022-03-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (6, 2, 5, '2022-02-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (6, 3, 6, '2022-01-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (7, 4, 7, '2022-01-01 10:50:00');
INSERT venta(idcliente, idproducto, idvendedor, fecha)
values (7, 5, 8, '2022-01-01 10:50:00');
