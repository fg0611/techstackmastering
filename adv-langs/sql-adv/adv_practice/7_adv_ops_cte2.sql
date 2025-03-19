-- SELECT *
-- FROM Postulantes
-- WHERE id_postulante IN (1, 2, 3);

-- SELECT *
-- FROM Vacantes
-- WHERE id_empresa IN 
-- (SELECT id_empresa FROM Empresas WHERE sector = 'Tecnología');

-- select * from vacantes where id_vacante not in (
--     select id_vacante from requerimientos
-- );

-- select * from requerimientos;

-- Encontrar empresas que tienen ciertas vacantes
-- select e.nombre_empresa from 
-- empresas e where e.id_empresa in (
--     select v.id_empresa from vacantes v
--      where lower(v.descripcion_vacante) like '%dat%'
-- )

-- select * from vacantes
-- select * from vacantes

-- Encontrar postulantes que no se han postulado a ninguna vacante
-- select * from postulantes where id_postulante not in (select id_postulante from postulaciones)

-- Empresas que no tengan vacantes publicadas en 2024
-- select * from empresas where id_empresa not in
-- (select v.id_empresa from vacantes v where extract('year' from v.fecha_publicacion) = '2024')

-- vacantes sin postulantes
-- select * from vacantes where id_vacante not in (select p.id_vacante from postulaciones p)




-- VER ESTE CASO DE EMPRESAS SIN VACANTES CON DOS FORMAS DE PROCEDER CON NOT EXISTS Y NOT IN    

-- Key Difference: Handling NULL Values
-- The crucial difference lies in how NULL values are handled.
-- NOT EXISTS is immune to the NULL value problem, making it generally more reliable.
-- NOT IN is vulnerable to NULL values, and if the subquery returns any NULL values, the outer query might not return the expected results.
-- In Summary:

-- NOT EXISTS is generally preferred because it's more robust and efficient.
-- select * from empresas e where not exists (select 1 from vacantes v where v.id_empresa = e.id_empresa)

-- NOT IN can lead to unexpected results if NULL values are present in the subquery's result set.
-- select * from empresas where id_empresa not in (select v.id_empresa from vacantes v)

-- postulantes sin habilidades
-- select * from postulantes p where not exists
-- (select 1 from postulantes_habilidades ph where p.id_postulante = ph.id_postulante)

-- insert INTO postulantes (nombre_postulante, apellido_postulante) 
-- VALUES ('Roberto', 'Santos')

-- Encontrar postulantes que tienen todas las habilidades requeridas para una vacante específica

-- JOIN: Necesitamos combinar las dos tablas (postulantes_habilidades y requerimientos) 
-- usando el id_habilidad como clave de unión. Esto nos permitirá relacionar 
-- las habilidades de los postulantes con los requerimientos.
with h_x_vacante as (select r.id_vacante, count(r.id_habilidad) skills_r from requerimientos r
group by r.id_vacante),

-- uno ph por habilidad con requerimientos
h_x_postulante as (select ph.id_postulante, r.id_vacante, count(r.id_habilidad) skills_p from postulantes_habilidades ph 
join requerimientos r
on ph.id_habilidad = r.id_habilidad
group by ph.id_postulante, r.id_vacante)

-- select * from h_x_vacante
-- select * from h_x_postulante
select p.id_postulante, v.id_vacante, p.skills_p, v.skills_r, 
case when p.skills_p < v.skills_r then 'No' else 'Si' end as postulante_cumple
from h_x_postulante p join h_x_vacante v on p.id_vacante = v.id_vacante
order by p.id_postulante
-- where p.skills_p >= v.skills_r



-- GROUP BY: Agruparemos los resultados por id_postulante 
-- para contar cuántas habilidades requeridas posee cada postulante.

-- HAVING: Filtraremos los grupos para incluir solo aquellos postulantes
--  que tengan todas las habilidades requeridas.


-- select * from postulaciones WHERE id_vacante = 1
-- insert INTO postulaciones (id_postulante, id_vacante) VALUES (3, 1); 
-- select * from postulantes_habilidades