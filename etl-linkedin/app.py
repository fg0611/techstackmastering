from flask import Flask
from routes import setup_routes
from config import Config

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar la configuración
app.config.from_object(Config)

# Configurar las rutas
setup_routes(app)

# Ejecutar la aplicación en modo dev
# if __name__ == '__main__': # comentar esto para prod
#     app.run(debug=True) # comentar esto para prod

# Ejecutar la aplicación en prod
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Escuchar en todas las interfaces