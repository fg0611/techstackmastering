from flask import Flask
from config import Config
from extensions import init_supabase
from resources.books_resource import books_bp

app = Flask(__name__)
app.config.from_object(Config)
supabase = init_supabase(app)

app.register_blueprint(books_bp, url_prefix='/api/books')

if __name__ == '__main__':
    app.run(debug=True)