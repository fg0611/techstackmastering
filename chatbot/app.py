import json
from flask import Flask, request, jsonify
from netlify.functions.llama_chatbot import handler
# from netlify.functions.chatbot import handler


app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    # Simula el formato de Netlify
    event = {"body": request.data.decode("utf-8")}
    response = handler(event, None)
    return jsonify(json.loads(response["body"])), response["statusCode"]

if __name__ == "__main__":
    app.run(port=5000, debug=True)