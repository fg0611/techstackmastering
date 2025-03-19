¡Perfecto! Vamos a darle un giro interesante a la base de datos "training" para simular un escenario de vacantes laborales y postulantes.

**1. Listado de Temas (Revisado)**

¡Claro! Vamos a abordar este desafío paso a paso, construyendo una base de datos "training" robusta y explorando consultas SQL avanzadas.

**1. Listado de Temas**

* **Tipos de JOIN:**
    * INNER JOIN
    * LEFT JOIN
    * RIGHT JOIN
    * FULL OUTER JOIN
    * CROSS JOIN
    * SELF JOIN
* **Operadores:**
    * Aritméticos (+, -, \*, /)
    * Comparación (=, <>, <, >, <=, >=)
    * Lógicos (AND, OR, NOT)
    * LIKE, IN, BETWEEN, EXISTS
* **Transformación de Datos:**
    * Normalización de strings (TRIM, UPPER, LOWER, REPLACE)
    * Conversión de tipos de datos (CAST, CONVERT)
    * Manejo de fechas (DATEPART, DATEDIFF, DATEADD)
    * Funciones de agregado (SUM, AVG, COUNT, MIN, MAX)
* **Funciones Avanzadas:**
    * CASE statements
    * Common Table Expressions (CTEs)
    * CTEs recursivas
    * Window functions (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, SUM, AVG)
* **Objetos de Base de Datos:**
    * Vistas
    * Procedimientos almacenados
    * Disparadores (Triggers)
    * Índices
    * Tablas temporales
    * Cursores
    * Particionado de tablas.

**2. Estructura de la Base de Datos "training" (Revisada)**

* **Empresas:**
    * `id_empresa` (INT, clave primaria)
    * `nombre_empresa` (VARCHAR)
    * `sector` (VARCHAR)
* **Vacantes:**
    * `id_vacante` (INT, clave primaria)
    * `id_empresa` (INT, clave foránea a Empresas)
    * `titulo_vacante` (VARCHAR)
    * `descripcion_vacante` (TEXT)
    * `fecha_publicacion` (DATE)
* **Postulantes:**
    * `id_postulante` (INT, clave primaria)
    * `nombre_postulante` (VARCHAR)
    * `apellido_postulante` (VARCHAR)
    * `email_postulante` (VARCHAR)
* **Habilidades:**
    * `id_habilidad` (INT, clave primaria)
    * `nombre_habilidad` (VARCHAR)
* **Postulantes_habilidades:**
    * `id_postulante_habilidad` (INT, clave primaria)
    * `id_postulante` (INT, clave foránea a Postulantes)
    * `id_habilidad` (INT, clave foránea a Habilidades)
* **Postulaciones:**
    * `id_postulacion` (INT, clave primaria)
    * `id_postulante` (INT, clave foránea a Postulantes)
    * `id_vacante` (INT, clave foránea a Vacantes)
    * `fecha_postulacion` (DATE)

**3. Queries para Crear las Tablas (Revisadas)**

```sql
CREATE DATABASE training;
USE training;

CREATE TABLE Empresas (
    id_empresa INT PRIMARY KEY AUTO_INCREMENT,
    nombre_empresa VARCHAR(100),
    sector VARCHAR(50)
);

CREATE TABLE Vacantes (
    id_vacante INT PRIMARY KEY AUTO_INCREMENT,
    id_empresa INT,
    titulo_vacante VARCHAR(100),
    descripcion_vacante TEXT,
    fecha_publicacion DATE,
    FOREIGN KEY (id_empresa) REFERENCES Empresas(id_empresa)
);

CREATE TABLE Postulantes (
    id_postulante INT PRIMARY KEY AUTO_INCREMENT,
    nombre_postulante VARCHAR(50),
    apellido_postulante VARCHAR(50),
    email_postulante VARCHAR(100)
);

CREATE TABLE Habilidades (
    id_habilidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_habilidad VARCHAR(50)
);

CREATE TABLE Postulantes_habilidades (
    id_postulante_habilidad INT PRIMARY KEY AUTO_INCREMENT,
    id_postulante INT,
    id_habilidad INT,
    FOREIGN KEY (id_postulante) REFERENCES Postulantes(id_postulante),
    FOREIGN KEY (id_habilidad) REFERENCES Habilidades(id_habilidad)
);

CREATE TABLE Postulaciones (
    id_postulacion INT PRIMARY KEY AUTO_INCREMENT,
    id_postulante INT,
    id_vacante INT,
    fecha_postulacion DATE,
    FOREIGN KEY (id_postulante) REFERENCES Postulantes(id_postulante),
    FOREIGN KEY (id_vacante) REFERENCES Vacantes(id_vacante)
);
```

**4. Queries para Poblar las Tablas (Revisadas)**

```sql
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
```

**5. Ejercicios de Consultas SQL Avanzadas (Revisadas)**

* **JOINs:**

```sql
-- INNER JOIN: Postulantes y sus habilidades
SELECT p.nombre_postulante, h.nombre_habilidad
FROM Postulantes p
INNER JOIN Postulantes_habilidades ph ON p.id_postulante = ph.id_postulante
INNER JOIN Habilidades h ON ph.id_habilidad = h.id_habilidad;

-- LEFT JOIN: Vacantes y sus postulantes (incluyendo vacantes sin postulantes)
SELECT v.titulo_vacante, p.nombre_postulante
FROM Vacantes v
LEFT JOIN Postulaciones po ON v.id_vacante = po.id_vacante
LEFT JOIN Postulantes p ON po.id_postulante = p.id_postulante;

-- RIGHT JOIN: Habilidades y postulantes que las poseen.
SELECT h.nombre_habilidad, p.nombre_postulante from Habilidades h RIGHT JOIN Postulantes_habilidades ph on h.id_habilidad = ph.id_habilidad RIGHT JOIN Postulantes p on ph.id_postulante = p.id_postulante;

-- FULL OUTER JOIN: Empresas y Vacantes.
SELECT e.nombre_empresa, v.titulo_vacante from Empresas e LEFT JOIN Vacantes v on e.id_empresa = v.id_empresa UNION SELECT e.nombre_empresa, v.titulo_vacante from Empresas e RIGHT JOIN Vacantes v on e.id_empresa = v.id_empresa;
```

* **Operadores:**

```sql
-- Operador LIKE: Vacantes con "Desarrollador" en el título
SELECT titulo_vacante FROM Vacantes WHERE titulo_vacante LIKE '%Desarrollador%';

-- Operador IN: Postulantes con habilidades "React" o "Node.js"
SELECT p.nombre_postulante
FROM Postulantes p
INNER JOIN Postulantes_habilidades ph ON p.id_postulante = ph.id_postulante
INNER JOIN Habilidades h ON ph.id_habilidad = h.id_habilidad