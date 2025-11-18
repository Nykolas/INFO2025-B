-- select * from cliente;
-- select nombre_y_apellido from cliente;
-- select * from cliente where condicion_iva = "Exento" and numero > 5;
-- select numero from cliente;
-- select * from cliente where nombre_y_apellido like "%ez"; -- devolve todos los que termian en ez
-- select * from cliente where nombre_y_apellido like "Ma%"; -- devolve todos los que empieza en Ma

select * from factura;
select * from linea_factura;
select * from factura inner join linea_factura where factura.numero = linea_factura.factura;

select * from factura 
inner join linea_factura 
on factura.numero = linea_factura.factura 
where factura.numero = "7";

select condicion_iva, nombre_y_apellido from cliente
inner join factura on cliente.numero = factura.numero
where condicion_iva = "Exento";


select nombre_y_apellido, tipo from cliente 
inner join forma_de_pago on forma_de_pago.codigo = cliente.numero
where forma_de_pago.tipo = "Tarjeta de crédito";

select * from forma_de_pago;

-- nombre de los clientes que compraron con tarjeta de credito
select nombre_y_apellido, tipo from cliente 
inner join forma_de_pago 
where forma_de_pago.tipo = "Tarjeta de crédito";