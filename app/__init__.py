from flask import Flask
from flask_cors import CORS

from app.ai_bp import ai_bp
from app.datastore_bp import datastore_bp


def create_app():
    app = Flask(__name__)

    CORS(app)

    # register blueprints
    app.register_blueprint(datastore_bp, url_prefix='/db')
    app.register_blueprint(ai_bp, url_prefix='/ai')
    return app
