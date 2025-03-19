-- postulaciones por empresa
-- CON JOINS
explain analyze
select e.nombre_empresa, count(v.id_vacante)  
from postulaciones p
join vacantes v
on v.id_vacante = p.id_vacante
join empresas e 
on v.id_empresa = e.id_empresa
group by e.nombre_empresa
order by 2

-- CON CTE
-- EXPLAIN ANALYZE
-- with pxe as (select v.id_empresa, count(p.id_vacante) as tot_postulaciones 
-- from vacantes v
-- join postulaciones p
-- on v.id_vacante = p.id_vacante
-- group by 1 ORDER BY 2)

-- select e.nombre_empresa, pxe.tot_postulaciones
-- from empresas e join pxe
-- on e.id_empresa = pxe.id_empresa ORDER BY 2 desc

-- CON WINDOW FUNCTIONS
-- explain analyze select distinct v.id_empresa, count(p.id_vacante) 
-- over (partition by v.id_empresa) as tot_postulaciones
-- from vacantes v
-- join postulaciones p
-- on v.id_vacante = p.id_vacante