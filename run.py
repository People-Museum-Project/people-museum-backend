from app import create_app
from flask_cors import CORS

if __name__ == "__main__":
    app = create_app()
    CORS(app)
    app.run(host="0.0.0.0", port=8080, debug=False)
