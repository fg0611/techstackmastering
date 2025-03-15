-- CREATE TABLE empleados (
--     id SERIAL PRIMARY KEY,
--     nombre VARCHAR(100) NOT NULL,
--     salario NUMERIC(10, 2) NOT NULL
-- );

-- CREATE TABLE auditoria_salarios (
--     id SERIAL PRIMARY KEY,
--     empleado_id INT NOT NULL,
--     salario_anterior NUMERIC(10, 2),
--     salario_nuevo NUMERIC(10, 2),
--     fecha_cambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );


-- CREATE OR REPLACE FUNCTION registrar_cambio_salario() 
-- RETURNS TRIGGER AS $$
-- BEGIN
--     -- Verificar si el salario ha cambiado
--     IF OLD.salario <> NEW.salario THEN
--         INSERT INTO auditoria_salarios (empleado_id, salario_anterior, salario_nuevo)
--         VALUES (OLD.id, OLD.salario, NEW.salario);
--     END IF;
    
--     -- Retornar el nuevo registro (obligatorio en PostgreSQL)
--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;



-- CREATE TRIGGER trigger_auditoria_salario
-- AFTER UPDATE ON empleados
-- FOR EACH ROW
-- EXECUTE FUNCTION registrar_cambio_salario();


-- INSERT INTO empleados (nombre, salario) VALUES
-- ('Juan', 3000),
-- ('María', 4000);

