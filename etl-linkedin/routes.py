from flask import jsonify, request
import asyncpg
import asyncio
from config import Config

# Función para crear la tabla si no existe
async def create_table_if_not_exists():
    conn = await asyncpg.connect(Config.DATABASE_URL)
    try:
        await conn.execute("""
            DROP TABLE IF EXISTS job_listings;
                           
            CREATE TABLE IF NOT EXISTS job_listings (
                id SERIAL PRIMARY KEY,
                title TEXT,
                company TEXT,
                location TEXT,
                published TEXT,
                applicants TEXT,
                url TEXT UNIQUE,
                description TEXT
            );
        """)
        return True
    except Exception as e:
        return str(e)
    finally:
        await conn.close()

# Función para obtener todos los jobs
async def fetch_all_jobs():
    conn = await asyncpg.connect(Config.DATABASE_URL)
    try:
        jobs = await conn.fetch("SELECT * FROM job_listings")
        return [dict(job) for job in jobs]
    finally:
        await conn.close()

# Función para obtener un job por ID
async def fetch_job_by_id(job_id):
    conn = await asyncpg.connect(Config.DATABASE_URL)
    try:
        job = await conn.fetchrow("SELECT * FROM job_listings WHERE id = $1", job_id)
        return dict(job) if job else None
    finally:
        await conn.close()

# Función para crear un nuevo job
async def create_job(title, company, location, published, applicants, url, description):
    conn = await asyncpg.connect(Config.DATABASE_URL)
    try:
        await conn.execute("""
            INSERT INTO job_listings (title, company, location, published, applicants, url, description)
            VALUES ($1, $2, $3, $4, $5, $6, $7)
        """, title, company, location, published, applicants, url, description)
        return True
    except Exception as e:
        return str(e)
    finally:
        await conn.close()

# Función para eliminar un job por ID
async def delete_job_by_id(job_id):
    conn = await asyncpg.connect(Config.DATABASE_URL)
    try:
        await conn.execute("DELETE FROM job_listings WHERE id = $1", job_id)
        return True
    except Exception as e:
        return str(e)
    finally:
        await conn.close()

# Configurar las rutas
def setup_routes(app):
    # Ruta para crear la tabla
    @app.route('/create-table', methods=['POST'])
    def create_table():
        result = asyncio.run(create_table_if_not_exists())
        if result is True:
            return jsonify({"message": "Tabla 'job_listings' creada o ya existente."}), 200
        else:
            return jsonify({"error": result}), 500

    # Ruta para obtener todos los jobs
    @app.route('/jobs', methods=['GET'])
    def get_all_jobs():
        jobs = asyncio.run(fetch_all_jobs())
        return jsonify(jobs), 200

    # Ruta para obtener un job por ID
    @app.route('/jobs/<int:job_id>', methods=['GET'])
    def get_job_by_id(job_id):
        job = asyncio.run(fetch_job_by_id(job_id))
        if job:
            return jsonify(job), 200
        else:
            return jsonify({"error": "Job no encontrado"}), 404

    # Ruta para crear un nuevo job
    @app.route('/jobs', methods=['POST'])
    def add_job():
        data = request.get_json()
        title = data.get('title')
        company = data.get('company')
        location = data.get('location')
        published = data.get('published')
        applicants = data.get('applicants')
        url = data.get('url')
        description = data.get('description')

        if not all([title, company, location, published, applicants, url, description]):
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        result = asyncio.run(create_job(title, company, location, published, applicants, url, description))
        if result is True:
            return jsonify({"message": "Job creado exitosamente"}), 201
        else:
            return jsonify({"error": result}), 500

    # Ruta para eliminar un job por ID
    @app.route('/jobs/<int:job_id>', methods=['DELETE'])
    def delete_job(job_id):
        result = asyncio.run(delete_job_by_id(job_id))
        if result is True:
            return jsonify({"message": "Job eliminado exitosamente"}), 200
        else:
            return jsonify({"error": result}), 500