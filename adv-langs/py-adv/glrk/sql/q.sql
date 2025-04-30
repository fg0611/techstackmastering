-- INNER JOIN: Obtener el nombre de la canción y el título del álbum al que pertenece.
-- select c.titulo, a.titulo from canciones c join albumes a on c.album_id = a.album_id

-- promedio de duracion de las canciones de un album
-- select round(avg(c.duracion_segundos)) avg_time_songs from albumes a 
-- join canciones c on a.album_id = c.album_id where c.album_id = 1

-- select a.album_id, a.titulo album, round(avg(c.duracion_segundos)) prom_duracion from albumes a 
-- join canciones c on a.album_id = c.album_id GROUP BY a.album_id ORDER BY a.album_id

-- canciones por album
-- select a.titulo album, count(c.cancion_id) canciones from canciones c join albumes a 
-- on c.album_id = a.album_id group by a.titulo

-- canciones de artistas ord por artista
-- select c.titulo cancion, art.nombre from canciones c join albumes a 
-- on c.album_id = a.album_id
-- join artistas art on art.artista_id = a.artista_id 
-- where art.nombre like 'Soda%'

-- HAVING: Filtrar los artistas que tienen más de un álbum.
-- select art.nombre artista, count(album_id) als from artistas art join albumes a
-- ON art.artista_id = a.artista_id
-- GROUP BY artista
-- having count(album_id) > 1

-- window functions
-- ROW_NUMBER(): Asignar un número de fila a cada canción dentro de cada álbum, 
-- ordenado por puntuación descendente.
-- SELECT c.titulo cancion, a.titulo album, c.puntuacion puntos, 
-- row_number() over (PARTITION BY a.album_id ORDER BY c.puntuacion) as ranking
-- FROM canciones c JOIN albumes a
-- on c.album_id = a.album_id

-- AVG() OVER(): Calcular la puntuación promedio de todas las canciones hasta la fila actual
--  dentro de cada álbum (ordenado por título).
-- select c.titulo cancion, a.titulo album, c.puntuacion, a.fecha_lanzamiento pub,
-- sum(c.puntuacion) over (PARTITION by c.album_id ORDER by a.fecha_lanzamiento ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) p_acum
-- from canciones c join albumes a on c.album_id = a.album_id


-- acum de duracion de canciones
-- select c.titulo, c.album_id, sum(c.duracion_segundos) 
-- over (PARTITION BY c.album_id rows between unbounded preceding and current row) as prom_dur
-- from canciones c