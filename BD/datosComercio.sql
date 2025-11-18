-- Usar la base de datos
USE COMERCIO;

-- Insertar clientes
INSERT INTO cliente (numero, nombre_y_apellido, condicion_iva, email) VALUES
(1, 'Juan Pérez', 'Responsable Inscripto', 'juan.perez@email.com'),
(2, 'María Gómez', 'Monotributista', 'maria.gomez@email.com'),
(3, 'Carlos Ruiz', 'Exento', 'carlos.ruiz@email.com');

-- Insertar formas de pago
INSERT INTO forma_de_pago (codigo, tipo, incremento, descuento) VALUES
(1, 'Efectivo', 0.00, 10.00),
(2, 'Tarjeta de crédito', 5.00, 0.00),
(3, 'Transferencia bancaria', 0.00, 5.00);

-- Insertar productos
INSERT INTO producto (codigo, descripcion, precio, stock) VALUES
(100, 'Teclado mecánico', 25000.00, 10),
(101, 'Mouse inalámbrico', 12000.00, 25),
(102, 'Monitor 24 pulgadas', 80000.00, 5),
(103, 'Notebook 15.6"', 350000.00, 3);

-- Insertar facturas
INSERT INTO factura (numero, fecha, cliente, total) VALUES
(1, '2025-06-15', 1, 37000.00),
(2, '2025-06-16', 2, 92000.00);

-- Insertar líneas de factura
INSERT INTO linea_factura (producto, factura, cantidad, subtotal) VALUES
(100, 1, 1, 25000.00),
(101, 1, 1, 12000.00),
(102, 2, 1, 80000.00),
(101, 2, 1, 12000.00);

-- Insertar datos en factura_forma_pago (tabla N:M con ID autoincremental)
INSERT INTO factura_forma_pago (factura, forma_de_pago) VALUES
(1, 1), -- Factura 1 pagada en efectivo
(2, 2), -- Factura 2 pagada con tarjeta
(2, 3); -- Y también transferencia (combinado)
-- Usar la base de datos

-- Insertar más clientes
INSERT INTO cliente (numero, nombre_y_apellido, condicion_iva, email) VALUES
(4, 'Lucía Fernández', 'Responsable Inscripto', 'lucia.fernandez@email.com'),
(5, 'Diego Torres', 'Monotributista', 'diego.torres@email.com'),
(6, 'Laura Ríos', 'Consumidor Final', 'laura.rios@email.com'),
(7, 'Martín López', 'Exento', 'martin.lopez@email.com');

-- Insertar más formas de pago
INSERT INTO forma_de_pago (codigo, tipo, incremento, descuento) VALUES
(4, 'Tarjeta de débito', 0.00, 5.00),
(5, 'Mercado Pago', 3.00, 0.00);

-- Insertar más productos
INSERT INTO producto (codigo, descripcion, precio, stock) VALUES
(104, 'Auriculares Bluetooth', 18000.00, 15),
(105, 'Silla ergonómica', 95000.00, 7),
(106, 'Webcam HD', 15000.00, 20),
(107, 'Tablet 10"', 120000.00, 4);

-- Insertar más facturas
INSERT INTO factura (numero, fecha, cliente, total) VALUES
(3, '2025-06-15', 4, 18000.00),
(4, '2025-06-16', 5, 215000.00),
(5, '2025-06-16', 6, 167000.00),
(6, '2025-06-17', 7, 335000.00),
(7, '2025-06-17', 1, 272000.00);

-- Insertar más líneas de factura
INSERT INTO linea_factura (producto, factura, cantidad, subtotal) VALUES
(104, 3, 1, 18000.00),
(105, 4, 2, 190000.00),
(101, 4, 1, 12000.00),
(106, 5, 1, 15000.00),
(107, 5, 1, 120000.00),
(102, 6, 2, 160000.00),
(103, 6, 1, 175000.00),
(100, 7, 2, 50000.00),
(107, 7, 1, 120000.00),
(101, 7, 2, 24000.00),
(106, 7, 1, 15000.00),
(104, 7, 1, 18000.00);

-- Insertar más formas de pago en facturas (factura_forma_pago)
INSERT INTO factura_forma_pago (factura, forma_de_pago) VALUES
(3, 4), -- Débito
(4, 2), -- Crédito
(5, 2), -- Crédito
(5, 5), -- Mercado Pago (combinado)
(6, 1), -- Efectivo
(6, 3), -- Transferencia (combinado)
(7, 5), -- Mercado Pago
(7, 2); -- Tarjeta de crédito (combinado)
