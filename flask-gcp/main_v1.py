import os
from flask import Flask, render_template, request, jsonify
from create_tables import create_tables
from db_utils import connect_with_connector_auto_iam_authn, connect_with_connector
from database_v1 import add_person, add_collection, get_person, get_collection
import sqlalchemy

app = Flask(__name__)

# Global variable to hold the database connection
db = None

def init_db():
    """Initializes the database connection and creates the necessary tables."""
    global db
    if db is None:
        db = init_connection_pool()
        # Call any necessary functions to create tables or perform other setup tasks
        create_tables(db)

def init_connection_pool() -> sqlalchemy.engine.base.Engine:
    """Sets up connection pool for the app."""
    # use the connector when INSTANCE_CONNECTION_NAME (e.g. project:region:instance) is defined
    if os.environ.get("INSTANCE_CONNECTION_NAME"):
        # Either a DB_USER or a DB_IAM_USER should be defined. If both are
        # defined, DB_IAM_USER takes precedence.
        return (
            connect_with_connector_auto_iam_authn() if os.environ.get("DB_IAM_USER") else connect_with_connector()
        )

    raise ValueError(
        "Missing database connection type. Please define one of INSTANCE_HOST, INSTANCE_UNIX_SOCKET, or INSTANCE_CONNECTION_NAME"
    )

# Register the init_db function to run before any request is handled
@app.before_request
def before_request():
    init_db()

@app.route("/", methods=["GET"])
def render_index():
    people = get_all_people(db)
    collections = get_all_collections(db)
    return render_template('index_v1.html', people=people, collections=collections)

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

# wrap SQL queries in a SQLAlchemy expression
def get_all_people(db):
    conn = db.connect()
    people = []
    try:
        result = conn.execute(sqlalchemy.text("SELECT id, name, image, description FROM Person"))
        for row in result:
            person = {
                'id': row[0],
                'name': row[1],
                'image': row[2],
                'description': row[3]
            }
            people.append(person)
    finally:
        conn.close()
    return people

def get_all_collections(db):
    conn = db.connect()
    collections = []
    try:
        result = conn.execute(sqlalchemy.text("SELECT id, name, image, description FROM PeopleCollection"))
        for row in result:
            collection = {
                'id': row[0],
                'name': row[1],
                'image': row[2],
                'description': row[3]
            }
            collections.append(collection)
    finally:
        conn.close()
    return collections

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
