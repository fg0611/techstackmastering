-- saber quienes cumplen con los requerimientos de 1 vacante

-- DO $$ 
-- DECLARE
--     vid INT := 1; -- Asigna el valor del id_vacante a la variable
-- BEGIN

-- with HabilidadesDeVacante as 
-- (select id_habilidad from requerimientos where id_vacante = vid),
-- PostulanteConHabilidades as 
-- (select ph.id_habilidad, ph.id_postulante from postulantes_habilidades ph 
-- where ph.id_habilidad in (select id_habilidad from HabilidadesDeVacante)),
-- -- Cuenta el número de habilidades distintas 
-- -- que cada postulante tiene de las requeridas para la vacante.
-- ConteoHabilidadesDePostulanteEnVacante as 
-- (select id_postulante, count(distinct id_habilidad) as habilidades_vacante
-- from PostulanteConHabilidades group by id_postulante),
-- -- Cuenta el número total de habilidades distintas requeridas para la vacante.
-- ConteoHabilidadesRequeridas as 
-- (select count(distinct id_habilidad) as habilidades_requeridas
-- from HabilidadesDeVacante)
-- -- Selecciona los postulantes que cumplen con todas las habilidades requeridas.
-- select p.nombre_postulante from postulantes p 
-- join ConteoHabilidadesDePostulanteEnVacante c
-- on p.id_postulante = c.id_postulante
-- where c.habilidades_vacante = 
-- (select habilidades_requeridas from ConteoHabilidadesRequeridas);
-- END $$;

-- DECLARANDO COMO FUNCION
-- drop function postulantes_que_cumplen_con_vacante;
-- create or replace function postulantes_que_cumplen_con_vacante(vid int)
-- returns table (nombre_postulante varchar) as $$
-- BEGIN
-- return query
-- with HabilidadesDeVacante as 
-- (select id_habilidad from requerimientos where id_vacante = vid),
-- PostulanteConHabilidades as 
-- (select ph.id_habilidad, ph.id_postulante from postulantes_habilidades ph 
-- where ph.id_habilidad in (select id_habilidad from HabilidadesDeVacante)),

-- ConteoHabilidadesDePostulanteEnVacante as 
-- (select id_postulante, count(distinct id_habilidad) as habilidades_vacante
-- from PostulanteConHabilidades group by id_postulante),

-- ConteoHabilidadesRequeridas as 
-- (select count(distinct id_habilidad) as habilidades_requeridas
-- from HabilidadesDeVacante)

-- select p.nombre_postulante from postulantes p 
-- join ConteoHabilidadesDePostulanteEnVacante c
-- on p.id_postulante = c.id_postulante
-- where c.habilidades_vacante = 
-- (select habilidades_requeridas from ConteoHabilidadesRequeridas);
-- END $$ LANGUAGE plpgsql;

-- select * from postulantes_que_cumplen_con_vacante(1);

-- externo (hab se requiere)
-- select * from postulantes p
-- where not exists (
-- select r.id_habilidad 
-- from requerimientos r
-- where r.id_vacante = 2 and
-- not exists (
-- select ph.id_habilidad, ph.id_postulante 
-- from postulantes_habilidades ph 
-- where 
-- ph.id_postulante = p.id_postulante and 
-- ph.id_habilidad = r.id_habilidad
-- ))

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
