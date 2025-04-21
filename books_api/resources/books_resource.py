from flask import Blueprint, request, jsonify
from services.open_library_service import search_books, search_books_by_isbn

books_bp = Blueprint("books", __name__, url_prefix="/api/books")

@books_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "a param is required 'q'"}), 400
    results = search_books(query)
    return jsonify(results)


@books_bp.route("/isbn/<isbn>", methods=["GET"])
def search_by_isbn(isbn):
    libro = search_books_by_isbn(isbn)
    if libro:
        return jsonify(libro)
    return jsonify({"error": f"not found by ISBN {isbn}"}), 404


# Aquí puedes agregar más rutas para buscar por autor, fecha, etc.
# Ejemplo para buscar por autor:
@books_bp.route("/autor/<autor>", methods=["GET"])
def buscar_por_autor(autor):
    results = search_books(f"author:{autor}")
    return jsonify(results)


# Ejemplo para buscar por título (palabras contenidas):
@books_bp.route("/title/<word>", methods=["GET"])
def search_by_title(word):
    results = search_books(f"title:{word}&limit=1")
    return jsonify(results)

# Ejemplo para buscar por fecha de publicación (aproximada):
@books_bp.route("/date/<date>", methods=["GET"])
def search_by_date(date):
    results = search_books(f"publish_date:{date}")
    return jsonify(results)
