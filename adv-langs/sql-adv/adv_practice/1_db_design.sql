CREATE TABLE Empresas (
    id_empresa serial PRIMARY KEY,
    nombre_empresa VARCHAR(100),
    sector VARCHAR(50)
);

CREATE TABLE Vacantes (
    id_vacante serial PRIMARY KEY,
    id_empresa INT,
    titulo_vacante VARCHAR(100),
    descripcion_vacante TEXT,
    fecha_publicacion DATE,
    FOREIGN KEY (id_empresa) REFERENCES Empresas(id_empresa)
);

CREATE TABLE Postulantes (
    id_postulante serial PRIMARY KEY,
    nombre_postulante VARCHAR(50),
    apellido_postulante VARCHAR(50),
    email_postulante VARCHAR(100)
);

CREATE TABLE Habilidades (
    id_habilidad serial PRIMARY KEY,
    nombre_habilidad VARCHAR(50)
);

CREATE TABLE Postulantes_habilidades (
    id_postulante_habilidad serial PRIMARY KEY,
    id_postulante INT,
    id_habilidad INT,
    FOREIGN KEY (id_postulante) REFERENCES Postulantes(id_postulante),
    FOREIGN KEY (id_habilidad) REFERENCES Habilidades(id_habilidad)
);

CREATE TABLE Postulaciones (
    id_postulacion serial PRIMARY KEY,
    id_postulante INT,
    id_vacante INT,
    fecha_postulacion DATE,
    FOREIGN KEY (id_postulante) REFERENCES Postulantes(id_postulante),
    FOREIGN KEY (id_vacante) REFERENCES Vacantes(id_vacante)
);