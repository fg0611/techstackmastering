-- create table skills (id serial primary key, name varchar(255) not null);

-- alter table paises rename column name to nombre; 

-- CREATE TABLE roles (
--     id SERIAL PRIMARY KEY,
--     nombre VARCHAR(255) NOT NULL,
--     id_empresa INT REFERENCES empresas(id),
--     id_skills INT[] -- Array de IDs de skills asociados
-- );

-- create type estado_vacante as enum ('activa', 'inactiva');

-- CREATE TABLE vacantes (
--     id SERIAL PRIMARY KEY,
--     id_empresa INT REFERENCES Empresas(id),
--     aplicantes int,
--     activa BOOLEAN, -- true para activa, false para inactiva
--     fecha_publicacion DATE,
--     id_pais INT REFERENCES paises(id),
--     id_rol INT REFERENCES roles(id)
-- );

-- Insertar empresas
-- INSERT INTO empresas (nombre) VALUES ('Empresa A'), ('Empresa B');

-- Insertar países
-- INSERT INTO paises (nombre) VALUES ('México'), ('Venezuela'), ('Argentina'), ('Colombia');

-- Insertar skills
-- INSERT INTO skills (nombre) VALUES ('Python'), ('JavaScript'), ('SQL');

-- select * from roles




