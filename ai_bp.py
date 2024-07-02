from flask import Blueprint, request, jsonify




ai_bp = Blueprint('ai_bp', __name__)



@ai_bp.route('/')
def test():
    return jsonify({
        "message": "success"
    }), 200