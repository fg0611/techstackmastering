from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Crear la aplicación Flask
app = Flask(__name__)
# Cargar la configuración
app.config.from_object(Config)

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Definir un modelo de ejemplo
class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    company = db.Column(db.String(100), nullable=True)
    published = db.Column(db.String(100), nullable=True)
    applicants = db.Column(db.String(100), nullable=True)
    url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)

# Crear las tablas en la base de datos (si no existen)
with app.app_context():
    db.create_all()

# Ruta de ejemplo
@app.route('/')
def index():
    jobs = Job.query.all()
    return f"Total de trabajos: {len(jobs)}"

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)