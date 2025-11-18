-- Seleccionar todas las columnas y datos de la tabla tutro 
-- select * from tutor; 
-- where es un filtro;
-- select * from factura where total > 3000 and id_tutor = 1;
-- el % se llama comodin (ene ste ejemplo filtro los que terminan con a
-- select * from tutor where nombre like '%a'
-- ordenar los resultados sentencia order by
-- select * from tutor order by direccion

-- relacionar tablas
select tutor.nombre, factura.id_factura, factura.total  from factura inner join tutor on factura.id_tutor = tutor.id_tutor





