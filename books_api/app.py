from flask import Flask
from config import Config
from extensions import init_supabase
from config import Config
from resources.books_resource import books_bp
from resources.users_resource import users_bp

app = Flask(__name__)
app.config.from_object(Config)
supabase_client = init_supabase(app)

app.extensions['supabase'] = supabase_client

app.register_blueprint(books_bp)
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)