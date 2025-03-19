-- SELECT postulantes.nombre_postulante, 
-- v.titulo_vacante, e.nombre_empresa,
-- p.fecha_postulacion
-- FROM Vacantes v
-- JOIN empresas e
-- ON v.id_empresa = e.id_empresa
-- JOIN postulaciones p
-- ON v.id_vacante = p.id_vacante
-- JOIN postulantes
-- ON postulantes.id_postulante = p.id_postulante
-- WHERE EXTRACT( 'year' from v.fecha_publicacion) > '2023';

-- SELECT * FROM vacantes
-- SELECT * FROM postulaciones
-- SELECT * FROM postulantes
-- insert into postulaciones 
-- (id_postulante, id_vacante, fecha_postulacion) 
-- values (5, 5, '2024-01-01');

-- select * from postulantes
-- update postulantes set email_postulante = 'pedro@gmail.com' where id_postulante = 4;
-- select * from postulantes where email_postulante like '%gmail%';
-- select * from postulantes where email_postulante not like '%gmail%';

-- SELECT * FROM Empresas WHERE sector <> 'Salud';
-- SELECT * FROM Empresas WHERE sector != 'Salud';

-- empresas con al menos una vacante publicada
-- select e.nombre_empresa, e.sector
-- from empresas e
-- where exists
-- (select 1 from vacantes v 
-- where e.id_empresa = v.id_empresa)

-- empresas con al menos una vacante publicada despues del 2023
-- select e.nombre_empresa, e.sector
-- from empresas e
-- where exists
-- (select 1 from vacantes v 
-- where e.id_empresa = v.id_empresa
-- and extract('year' from v.fecha_publicacion) > 2023)






