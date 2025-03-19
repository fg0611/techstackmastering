create table requerimientos (
    id_requerimiento serial primary key,
    id_vacante int,
    id_habilidad int,
    foreign key (id_vacante) references vacantes(id_vacante),
    foreign key (id_habilidad) references habilidades(id_habilidad)
);

-- select * from vacantes
-- select * from habilidades
-- select * from requerimientos

-- insert into requerimientos 
-- (id_vacante, id_habilidad) 
-- values (4, 3);
-- values (1, 1), (1,2), (2,6), (2,4), (2,7);
-- insert into postulaciones 
-- (id_postulante, id_vacante) 
-- values (3, 2), (4, 5);

-- update vacantes set titulo_vacante = 'Oficinista entry level',
-- descripcion_vacante = 'Se busca oficinista para tareas administrativas'
-- where id_vacante = 3;

-- saber si los postulantes cumplen o no con los requerimientos de una vacante
-- select ps.id_postulante, ps.id_vacante, r.id_habilidad
-- from requerimientos r
-- cross join postulaciones ps
-- on ps.id_vacante = ps.id_vacante
-- left join postulantes_habilidades ph
-- on ph.id_postulante = ps.id_postulante

-- SELECT p.nombre_postulante
-- FROM Postulantes p
-- WHERE p.id_postulante IN (
--     SELECT ph.id_postulante
--     FROM Postulantes_habilidades ph
--     WHERE ph.id_habilidad IN (
--         SELECT r.id_habilidad
--         FROM Requerimientos r
--         WHERE r.id_vacante = 1 -- Cambiar el número para la vacante deseada
--     )
--     GROUP BY ph.id_postulante
--     HAVING COUNT(DISTINCT ph.id_habilidad) = (
--         SELECT COUNT(DISTINCT r.id_habilidad)
--         FROM Requerimientos r
--         WHERE r.id_vacante = 1 -- Cambiar el número para la vacante deseada
--     )
-- );

-- habs por postulante
select p.nombre_postulante, h.nombre_habilidad 
from postulantes_habilidades ph
join postulantes p on ph.id_postulante = p.id_postulante
join habilidades h on ph.id_habilidad = h.id_habilidad

-- conectar habilidades con vacantes para saber que hay alli
-- SELECT concat(h.id_habilidad, '-', h.nombre_habilidad) rhab,
-- concat(v.id_vacante, '-', v.titulo_vacante) vid 
-- FROM requerimientos r
-- FULL OUTER JOIN vacantes v on r.id_vacante = v.id_vacante
-- FULL OUTER JOIN habilidades h on r.id_habilidad = h.id_habilidad;

-- insert into requerimientos (id_vacante, id_habilidad) 
-- values (2, 3), (5,7), (4,6), (4,7), (4,4);

-- SELECT p.nombre_postulante
-- FROM Postulantes p
-- WHERE NOT EXISTS (
--     SELECT r.id_habilidad
--     FROM Requerimientos r
--     WHERE r.id_vacante = 1
--     AND NOT EXISTS (
--         SELECT ph.id_habilidad
--         FROM Postulantes_habilidades ph
--         WHERE ph.id_postulante = p.id_postulante
--         AND ph.id_habilidad = r.id_habilidad
--     )
-- );