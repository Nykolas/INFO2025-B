-- Crear base de datos
CREATE DATABASE IF NOT EXISTS VeterinariaDB;
USE VeterinariaDB;

-- Tabla: Tutor
CREATE TABLE Tutor (
    id_tutor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    email VARCHAR(100)
);

-- Tabla: Mascota
CREATE TABLE Mascota (
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especie VARCHAR(50),
    raza VARCHAR(50),
    fecha_nacimiento DATE,
    id_tutor INT NOT NULL,
    FOREIGN KEY (id_tutor) REFERENCES Tutor(id_tutor)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Tabla: Veterinario
CREATE TABLE Veterinario (
    id_veterinario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- Tabla: Consulta
CREATE TABLE Consulta (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    motivo VARCHAR(255),
    id_mascota INT NOT NULL,
    id_veterinario INT,
    FOREIGN KEY (id_mascota) REFERENCES Mascota(id_mascota)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (id_veterinario) REFERENCES Veterinario(id_veterinario)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- Tabla: Tratamiento
CREATE TABLE Tratamiento (
    id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    costo DECIMAL(10,2),
    id_consulta INT NOT NULL,
    FOREIGN KEY (id_consulta) REFERENCES Consulta(id_consulta)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Tabla: Factura
CREATE TABLE Factura (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    id_tutor INT NOT NULL,
    FOREIGN KEY (id_tutor) REFERENCES Tutor(id_tutor)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Tabla intermedia: DetalleFactura
CREATE TABLE DetalleFactura (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT NOT NULL,
    id_tratamiento INT NOT NULL,
    cantidad INT DEFAULT 1,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES Factura(id_factura)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (id_tratamiento) REFERENCES Tratamiento(id_tratamiento)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


