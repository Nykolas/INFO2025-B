-- Ver todos los tutores y sus mascotas.
-- select tutor.nombre, tutor.apellido, mascota.nombre, mascota.especie from tutor inner join mascota on tutor.id_tutor = mascota.id_tutor

-- Mostrar las mascotas atendidas por el veterinario que más consultas realizó

-- ver que veterinario realizo mas consultas

select id_veterinario from consulta group by id_veterinario order by count(id_veterinario) desc LIMIT 1

-- que mascotas atendio

select mascota.nombre, consulta.id_veterinario from consulta inner join mascota on mascota.id_mascota = consulta.id_mascota

-- ahora juntamos los 2

select mascota.nombre, consulta.id_veterinario from consulta inner join mascota on mascota.id_mascota = consulta.id_mascota and 
consulta.id_veterinario = (select id_veterinario from consulta group by id_veterinario order by count(id_veterinario) desc LIMIT 1)
