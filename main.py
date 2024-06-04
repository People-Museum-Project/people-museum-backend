from flask import Flask, request, jsonify
from database import add_person, add_collection, get_person, get_collection

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)