-- Eliminar tablas si existen
DROP TABLE IF EXISTS canciones;
DROP TABLE IF EXISTS albumes;
DROP TABLE IF EXISTS artistas;

-- Tabla de Artistas
CREATE TABLE artistas (
    artista_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    genero VARCHAR(50)
);

-- Tabla de Álbumes
CREATE TABLE albumes (
    album_id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    artista_id INTEGER REFERENCES artistas(artista_id),
    fecha_lanzamiento DATE
);

-- Tabla de Canciones
CREATE TABLE canciones (
    cancion_id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    album_id INTEGER REFERENCES albumes(album_id),
    duracion_segundos INTEGER,
    puntuacion DECIMAL(3, 2) -- Ejemplo de puntuación de la canción
);

-- Insertar datos en la tabla de Artistas
INSERT INTO artistas (nombre, genero) VALUES
('Soda Stereo', 'Rock en Español'),
('Gustavo Cerati', 'Rock'),
('Los Fabulosos Cadillacs', 'Ska'),
('Charly García', 'Rock');

-- Insertar datos en la tabla de Álbumes
INSERT INTO albumes (titulo, artista_id, fecha_lanzamiento) VALUES
('Canción Animal', 1, '1990-08-07'),
('Bocanada', 2, '1999-05-18'),
('Vasos Vacíos', 3, '1993-06-01'),
('Clics Modernos', 4, '1983-11-05'),
('Ahí Vamos', 2, '2006-04-04');

-- Insertar datos en la tabla de Canciones
INSERT INTO canciones (titulo, album_id, duracion_segundos, puntuacion) VALUES
('De Música Ligera', 1, 333, 4.8),
('Persiana Americana', 1, 275, 4.5),
('Puente', 2, 270, 4.9),
('Crimen', 2, 295, 4.7),
('El Matador', 3, 348, 4.6),
('Mal Bicho', 3, 250, 4.3),
('Nos Siguen Pegando Abajo (Qué Dolor)', 3, 218, 4.4),
('No Soy Un Extraño', 4, 310, 4.2),
('Demoliendo Hoteles', 4, 255, 4.0),
('Adiós', 5, 238, 4.7),
('La Excepción', 5, 212, 4.5),
('Ella Usó Mi Cabeza Como Un Revólver', 1, 315, 4.7);