from flask import Flask, render_template, request, jsonify
from connect_connector_auto_iam_authn import connect_with_connector_auto_iam_authn
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from models import Person, PeopleCollection
from crud import create_person, read_person, update_person, delete_person

app = Flask(__name__)

def init_connection_pool():
    """Initiates connection to database and its structure."""
    return connect_with_connector_auto_iam_authn()

# Call init_connection_pool only once
db = init_connection_pool()

# Check if the table exists before creating it
inspector = inspect(db)
if not inspector.has_table("person"):
    Person.__table__.create(db)
    # PeopleCollection.__table__.create(db)

# Create a Session class to handle interactions with the database
Session = sessionmaker(bind=db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/create_person", methods=["POST"])
def create_person_route():
    # Parse JSON data from the request
    data = request.json

    # Create a new Person object with the provided data
    new_person_data = {
        'name': data['name'],
        'image': data.get('image'),
        'description': data.get('description'),
        'bio_docs': data.get('bio_docs', []),
        'authored_docs': data.get('authored_docs', []),
        'collections': data.get('collections', []),
        'owner': data.get('owner'),
        'share_list': data.get('share_list', []),
        'is_public': data.get('is_public', False)
    }

    # Call the create_person function from crud.py
    create_person(**new_person_data)

    # Return a JSON response indicating success
    return jsonify({"message": "Person created successfully"}), 200

@app.route('/read_person/<int:person_id>')
def read_person_route(person_id):
    person = read_person(person_id)
    if person:
        return jsonify({
            'id': person.id,
            'name': person.name,
            'image': person.image,
            'description': person.description,
            'bio_docs': person.bio_docs,
            'authored_docs': person.authored_docs,
            'collections': person.collections,
            'owner': person.owner,
            'share_list': person.share_list,
            'is_public': person.is_public
        })
    else:
        return 'Person not found', 404

@app.route('/update_person/<int:person_id>', methods=['PUT'])
def update_person_route(person_id):
    data = request.json
    update_person(person_id, **data)
    return 'Person updated successfully'

@app.route('/delete_person/<int:person_id>', methods=['DELETE'])
def delete_person_route(person_id):
    delete_person(person_id)
    return 'Person deleted successfully'

@app.route("/create_collection", methods=["POST"])
def create_collection_route():
    data = request.json
    new_collection_data = {
        'name': data['name'],
        'image': data.get('image'),
        'description': data.get('description'),
        'bio_docs': data.get('bio_docs', []),
        'people': data.get('people', []),
        'owner': data.get('owner'),
        'share_list': data.get('share_list', []),
        'is_public': data.get('is_public', False)
    }
    create_collection(**new_collection_data)
    return jsonify({"message": "Collection created successfully"}), 200

@app.route('/read_collection/<int:collection_id>')
def read_collection_route(collection_id):
    collection = read_collection(collection_id)
    if collection:
        return jsonify({
            'id': collection.id,
            'name': collection.name,
            'image': collection.image,
            'description': collection.description,
            'bio_docs': collection.bio_docs,
            'people': collection.people,
            'owner': collection.owner,
            'share_list': collection.share_list,
            'is_public': collection.is_public
        })
    else:
        return 'Collection not found', 404

@app.route('/update_collection/<int:collection_id>', methods=['PUT'])
def update_collection_route(collection_id):
    data = request.json
    update_collection(collection_id, **data)
    return 'Collection updated successfully'

@app.route('/delete_collection/<int:collection_id>', methods=['DELETE'])
def delete_collection_route(collection_id):
    delete_collection(collection_id)
    return 'Collection deleted successfully'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
