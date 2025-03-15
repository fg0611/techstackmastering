CREATE OR REPLACE PROCEDURE insertar_vacante(
    p_empresa_nombre TEXT,
    p_aplicantes INT,
    p_activa BOOLEAN,
    p_fecha_publicacion DATE,
    p_pais_nombre TEXT,
    p_rol_nombre TEXT,
    p_descripcion TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_empresa INT;
    v_id_pais INT;
    v_id_rol INT;
BEGIN
    -- Iniciar la transacción
    BEGIN
        -- Buscar el ID de la empresa por su nombre
        SELECT id INTO v_id_empresa
        FROM empresas
        WHERE nombre = p_empresa_nombre;

        -- Si no se encuentra la empresa, lanzar un error
        IF v_id_empresa IS NULL THEN
            RAISE EXCEPTION 'Empresa no encontrada: %', p_empresa_nombre;
        END IF;

        -- Buscar el ID del país por su nombre
        SELECT id INTO v_id_pais
        FROM paises
        WHERE nombre = p_pais_nombre;

        -- Si no se encuentra el país, lanzar un error
        IF v_id_pais IS NULL THEN
            RAISE EXCEPTION 'País no encontrado: %', p_pais_nombre;
        END IF;

        -- Buscar el ID del rol por su nombre
        SELECT id INTO v_id_rol
        FROM roles
        WHERE nombre = p_rol_nombre;

        -- Si no se encuentra el rol, lanzar un error
        IF v_id_rol IS NULL THEN
            RAISE EXCEPTION 'Rol no encontrado: %', p_rol_nombre;
        END IF;

        -- Insertar la vacante en la tabla vacantes
        INSERT INTO vacantes (
            id_empresa, aplicantes, activa, fecha_publicacion, id_pais, id_rol, descripcion
        ) VALUES (
            v_id_empresa, p_aplicantes, p_activa, p_fecha_publicacion, v_id_pais, v_id_rol, p_descripcion
        );

        -- Confirmar la transacción si todo está bien
        COMMIT;
    EXCEPTION
        WHEN OTHERS THEN
            -- Si ocurre un error, deshacer la transacción
            ROLLBACK;
            -- Relanzar el error para que el cliente lo vea
            RAISE EXCEPTION 'Error al insertar la vacante: %', SQLERRM;
    END;
END;
$$;

-- ALTER TABLE vacantes 
-- ADD COLUMN descripcion varchar not null;

-- alter table roles drop column id_empresa
-- select * from roles

-- select nombre from skills where nombre like 'P%'

-- do $$
-- begin
-- 	begin
-- 		insert into skills (nombre) values ('Pandas');
-- 		commit;
-- 	exception when others then
-- 		rollback;
-- 		raise exception 'Error al insertar: %', SQLERRM;
-- 	end;
-- end $$;

-- DO $$
-- BEGIN
--     BEGIN
--         -- Intenta insertar un registro
--         INSERT INTO skills (nombre) VALUES ('Pandas');
--     EXCEPTION WHEN OTHERS THEN
--         RAISE EXCEPTION 'Error al insertar: %', SQLERRM;
--     END;
-- END $$;

-- DO $$
-- BEGIN
--     -- Iniciar la transacción
--     BEGIN
--         -- Insertar los 50 registros
--         INSERT INTO skills (nombre) VALUES
--         ('JavaScript'),
--         ('Python'),
--         ('Excel'),
--         ('React.js'),
--         ('Node.js'),
--         ('Flask'),
--         ('Django'),
--         ('HTML'),
--         ('CSS'),
--         ('SQL'),
--         ('MongoDB'),
--         ('PostgreSQL'),
--         ('Git'),
--         ('GitHub'),
--         ('Docker'),
--         ('Kubernetes'),
--         ('AWS'),
--         ('Azure'),
--         ('Google Cloud'),
--         ('Machine Learning'),
--         ('Data Science'),
--         ('Pandas'),
--         ('NumPy'),
--         ('Matplotlib'),
--         ('Seaborn'),
--         ('TensorFlow'),
--         ('PyTorch'),
--         ('Java'),
--         ('C++'),
--         ('C#'),
--         ('PHP'),
--         ('Ruby'),
--         ('Ruby on Rails'),
--         ('Swift'),
--         ('Kotlin'),
--         ('TypeScript'),
--         ('Angular'),
--         ('Vue.js'),
--         ('SASS'),
--         ('Bootstrap'),
--         ('Tailwind CSS'),
--         ('GraphQL'),
--         ('REST API'),
--         ('Linux'),
--         ('Bash'),
--         ('PowerShell'),
--         ('Unity'),
--         ('Unreal Engine'),
--         ('Figma'),
--         ('Adobe XD'),
--         ('Scrum')
--         ON CONFLICT (nombre) DO NOTHING; -- Ignorar duplicados

--         -- Confirmar la transacción si todo está bien
--         COMMIT;
--     EXCEPTION WHEN OTHERS THEN
--         -- Si ocurre un error, deshacer la transacción
--         ROLLBACK;
--         RAISE NOTICE 'Ocurrió un error. Se realizó un ROLLBACK.';
--     END;
-- END $$;
-- BEGIN; -- Inicia la transacción
-- -- Insertar los 50 registros
-- INSERT INTO skills (nombre) VALUES
-- ('JavaScript'),
-- ('Python'),
-- ('Excel'),
-- ('React.js'),
-- ('Node.js'),
-- ('Flask'),
-- ('Django'),
-- ('HTML'),
-- ('CSS'),
-- ('SQL'),
-- ('MongoDB'),
-- ('PostgreSQL'),
-- ('Git'),
-- ('GitHub'),
-- ('Docker'),
-- ('Kubernetes'),
-- ('AWS'),
-- ('Azure'),
-- ('Google Cloud'),
-- ('Machine Learning'),
-- ('Data Science'),
-- ('Pandas'),
-- ('NumPy'),
-- ('Matplotlib'),
-- ('Seaborn'),
-- ('TensorFlow'),
-- ('PyTorch'),
-- ('Java'),
-- ('C++'),
-- ('C#'),
-- ('PHP'),
-- ('Ruby'),
-- ('Ruby on Rails'),
-- ('Swift'),
-- ('Kotlin'),
-- ('TypeScript'),
-- ('Angular'),
-- ('Vue.js'),
-- ('SASS'),
-- ('Bootstrap'),
-- ('Tailwind CSS'),
-- ('GraphQL'),
-- ('REST API'),
-- ('Linux'),
-- ('Bash'),
-- ('PowerShell'),
-- ('Unity'),
-- ('Unreal Engine'),
-- ('Figma'),
-- ('Adobe XD'),
-- ('Scrum');

-- -- Si todo está bien, confirmar la transacción
-- COMMIT;

-- -- EXCEPTION WHEN OTHERS THEN
--     -- Si ocurre un error, deshacer la transacción
--     ROLLBACK;
--     RAISE NOTICE 'Ocurrió un error. Se realizó un ROLLBACK.';