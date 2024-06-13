import os
import sys
from flask import Flask, request, jsonify, render_template
from database import add_person, add_collection, get_person, get_collection, get_index_context
from db import init_db, SessionLocal
from create_tables import create_tables

# Ensure the current directory is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Initialize the database and create tables
db = init_db()
print("start create tables...")
create_tables(db)
print("finish create tables")

@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    person_id = add_person(
        data['name'], data['image'], data['description'],
        data['bio_docs'], data['authored_docs'], data['owner'],
        data.get('is_public', False)
    )
    return jsonify({'id': person_id}), 201

@app.route('/collection', methods=['POST'])
def create_collection():
    data = request.get_json()
    collection_id = add_collection(
        data['name'], data['image'], data['description'],
        data['bio_docs'], data['people'], data['owner'],
        data.get('is_public', False)
    )
    return jsonify({'id': collection_id}), 201

@app.route('/person/<int:person_id>', methods=['GET'])
def get_person_by_id(person_id):
    person = get_person(person_id)
    if person:
        return jsonify(person), 200
    return jsonify({'error': 'Person not found'}), 404

@app.route('/collection/<int:collection_id>', methods=['GET'])
def get_collection_by_id(collection_id):
    collection = get_collection(collection_id)
    if collection:
        return jsonify(collection), 200
    return jsonify({'error': 'Collection not found'}), 404

@app.route("/", methods=["GET"])
def render_index():
    """Serves the index page of the app."""
    # db = SessionLocal()
    context = get_index_context()
    # db.close()
    return render_template("index_v2.html", **context)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="127.0.0.1", port=8080, debug=True)