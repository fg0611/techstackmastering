-- PRACTICA DE JOINS

-- INNER JOIN: Postulantes y sus habilidades, es lo mismo que un JOIN
-- SELECT p.nombre_postulante, h.nombre_habilidad
-- FROM Postulantes p
-- INNER JOIN Postulantes_habilidades ph ON p.id_postulante = ph.id_postulante
-- INNER JOIN Habilidades h ON ph.id_habilidad = h.id_habilidad;

-- FULL OUTER JOIN: Empresas y Vacantes.
-- SELECT e.nombre_empresa, v.titulo_vacante from Empresas e 
-- LEFT JOIN Vacantes v on e.id_empresa = v.id_empresa 
-- UNION 
-- SELECT e.nombre_empresa, v.titulo_vacante 
-- from Empresas e RIGHT JOIN Vacantes v on e.id_empresa = v.id_empresa;

-- empresas y vacantes
-- SELECT e.nombre_empresa, v.titulo_vacante
-- FROM Empresas e
-- RIGHT JOIN Vacantes v ON e.id_empresa = v.id_empresa

-- select * from vacantes
-- insert INTO vacantes
--  (id_empresa, titulo_vacante, descripcion_vacante, fecha_publicacion)
-- VALUES (1, 'Desarrollador SQL', 'Sr. SQL dev', '2024-01-01');

-- select * from postulantes_habilidades
-- insert into postulantes_habilidades (id_postulante, id_habilidad)
-- values (3, 7)

-- CROSS JOIN saber los skills de cada postulante
-- select p.nombre_postulante, h.nombre_habilidad 
-- from postulantes_habilidades ph
-- cross join postulantes p
-- cross join habilidades h
-- where p.id_postulante = ph.id_postulante and
-- h.id_habilidad = ph.id_habilidad
-- order by p.nombre_postulante;

-- saber cuantos skills tiene cada postulante
-- select p.nombre_postulante, count(h.id_habilidad) n_skills 
-- from postulantes_habilidades ph
-- cross join postulantes p
-- cross join habilidades h
-- where p.id_postulante = ph.id_postulante and
-- h.id_habilidad = ph.id_habilidad
-- group by 1 
-- order by n_skills desc;

select v.titulo_vacante, e.nombre_empresa 
from vacantes v join empresas e on v.id_empresa = e.id_empresa 