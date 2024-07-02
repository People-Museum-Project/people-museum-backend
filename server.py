from flask import Flask, request, jsonify
from people_museum_handler import Handler
from flask_cors import CORS
from datastore_bp import datastore_bp
from ai_bp import ai_bp

app = Flask(__name__)
CORS(app)
handler = Handler()


app.register_blueprint(datastore_bp, url_prefix='/db')
app.register_blueprint(ai_bp, url_prefix='/ai')


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "index page successfully reached"}), 200




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
