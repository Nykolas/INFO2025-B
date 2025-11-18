-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS COMERCIO;
USE COMERCIO;

-- Tabla CLIENTE
CREATE TABLE cliente (
    numero INT PRIMARY KEY,
    nombre_y_apellido VARCHAR(100) NOT NULL,
    condicion_iva VARCHAR(50),
    email VARCHAR(100)
);

-- Tabla FORMA_DE_PAGO
CREATE TABLE forma_de_pago (
    codigo INT PRIMARY KEY,
    tipo VARCHAR(50),
    incremento DECIMAL(10,2),
    descuento DECIMAL(10,2)
);

-- Tabla PRODUCTO
CREATE TABLE producto (
    codigo INT PRIMARY KEY,
    descripcion VARCHAR(100),
    precio DECIMAL(10,2),
    stock INT
);

-- Tabla FACTURA
CREATE TABLE factura (
    numero INT PRIMARY KEY,
    fecha DATE,
    cliente INT,
    total DECIMAL(10,2),
    FOREIGN KEY (cliente) REFERENCES cliente(numero)
);

-- Tabla LINEA_FACTURA
CREATE TABLE linea_factura (
    id INT PRIMARY KEY AUTO_INCREMENT,
    producto INT,
    factura INT,
    cantidad INT,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (producto) REFERENCES producto(codigo),
    FOREIGN KEY (factura) REFERENCES factura(numero)
);

-- Tabla intermedia FACTURA_FORMA_PAGO con ID autoincremental
CREATE TABLE factura_forma_pago (
    id INT PRIMARY KEY AUTO_INCREMENT,
    factura INT,
    forma_de_pago INT,
    FOREIGN KEY (factura) REFERENCES factura(numero),
    FOREIGN KEY (forma_de_pago) REFERENCES forma_de_pago(codigo)
);
