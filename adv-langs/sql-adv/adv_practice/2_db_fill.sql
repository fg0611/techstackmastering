-- Poblar la tabla Empresas
INSERT INTO Empresas (nombre_empresa, sector) VALUES
('Tech Innovators Inc.', 'Tecnología'),
('Global Finance Ltd.', 'Finanzas'),
('Health Solutions SA', 'Salud');

-- Poblar la tabla Vacantes
INSERT INTO Vacantes (id_empresa, titulo_vacante, descripcion_vacante, fecha_publicacion) VALUES
(1, 'Desarrollador Full Stack', 'Desarrollador con experiencia en React y Node.js.', '2023-10-26'),
(2, 'Analista Financiero Senior', 'Analista con experiencia en valoración de activos.', '2023-10-25'),
(3, 'Enfermero/a Jefe', 'Enfermero/a con experiencia en gestión de equipos.', '2023-10-24'),
(1, 'Data Scientist', 'Se busca Data Scientist con experiencia en Machine Learning', '2023-10-20');

-- Poblar la tabla Postulantes
INSERT INTO Postulantes (nombre_postulante, apellido_postulante, email_postulante) VALUES
('Laura', 'Gómez', 'laura.gomez@email.com'),
('Carlos', 'Pérez', 'carlos.perez@email.com'),
('Ana', 'Sánchez', 'ana.sanchez@email.com'),
('Pedro', 'Ruiz', 'pedro.ruiz@email.com'),
('Sofía', 'Martínez', 'sofia.martinez@email.com');

-- Poblar la tabla Habilidades
INSERT INTO Habilidades (nombre_habilidad) VALUES
('React'),
('Node.js'),
('Análisis Financiero'),
('Machine Learning'),
('Liderazgo'),
('Python'),
('SQL'),
('Java');

-- Poblar la tabla Postulantes_habilidades
INSERT INTO Postulantes_habilidades (id_postulante, id_habilidad) VALUES
(1, 1), (1, 2), (2, 3), (3, 4), (3, 6), (4,5), (5, 7), (5, 8);

-- Poblar la tabla Postulaciones
INSERT INTO Postulaciones (id_postulante, id_vacante, fecha_postulacion) VALUES
(1, 1, '2023-10-27'),
(2, 2, '2023-10-28'),
(3, 1, '2023-10-29'),
(3, 4, '2023-10-29'),
(4, 3, '2023-10-30'),
(5, 1, '2023-10-30');