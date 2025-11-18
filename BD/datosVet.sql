USE VeterinariaDB;
-- ======= DATOS PARA TABLA TUTOR =======
INSERT INTO Tutor (nombre, apellido, telefono, direccion, email) VALUES
('María', 'Gómez', '3511234567', 'Av. Colón 1234', 'maria.gomez@gmail.com'),
('Carlos', 'Pérez', '3517654321', 'Bv. San Juan 876', 'carlos.perez@hotmail.com'),
('Lucía', 'Fernández', '3519876543', 'Calle Belgrano 456', 'lucia.fernandez@yahoo.com');

-- ======= DATOS PARA TABLA MASCOTA =======
INSERT INTO Mascota (nombre, especie, raza, fecha_nacimiento, id_tutor) VALUES
('Luna', 'Perro', 'Caniche', '2020-05-10', 1),
('Simba', 'Gato', 'Siames', '2019-11-25', 2),
('Rocky', 'Perro', 'Labrador', '2018-03-15', 3);

-- ======= DATOS PARA TABLA VETERINARIO =======
INSERT INTO Veterinario (nombre, apellido, especialidad, telefono, email) VALUES
('Ana', 'Lopez', 'Clínica general', '3511112233', 'ana.lopez@veterinaria.com'),
('Javier', 'Martínez', 'Cirugía', '3512223344', 'javier.martinez@veterinaria.com'),
('Paula', 'Ruiz', 'Dermatología', '3513334455', 'paula.ruiz@veterinaria.com');

-- ======= DATOS PARA TABLA CONSULTA =======
INSERT INTO Consulta (fecha, motivo, id_mascota, id_veterinario) VALUES
('2025-11-01 10:30:00', 'Vacunación anual', 1, 1),
('2025-11-02 15:00:00', 'Revisión general', 2, 1),
('2025-11-03 11:00:00', 'Alergia en la piel', 3, 3),
('2025-11-04 09:15:00', 'Control posquirúrgico', 1, 2);

-- ======= DATOS PARA TABLA TRATAMIENTO =======
INSERT INTO Tratamiento (descripcion, costo, id_consulta) VALUES
('Vacuna antirrábica', 3500.00, 1),
('Desparasitación interna', 2500.00, 2),
('Pomada antibiótica', 4200.00, 3),
('Análisis de sangre', 6800.00, 4);

-- ======= DATOS PARA TABLA FACTURA =======
INSERT INTO Factura (fecha, total, id_tutor) VALUES
('2025-11-01', 3500.00, 1),
('2025-11-02', 2500.00, 2),
('2025-11-03', 4200.00, 3),
('2025-11-04', 6800.00, 1);

-- ======= DATOS PARA TABLA DETALLEFACTURA =======
INSERT INTO DetalleFactura (id_factura, id_tratamiento, cantidad, subtotal) VALUES
(1, 1, 1, 3500.00),
(2, 2, 1, 2500.00),
(3, 3, 1, 4200.00),
(4, 4, 1, 6800.00);
