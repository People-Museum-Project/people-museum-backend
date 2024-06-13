import psycopg2
from db_utils import connect_with_connector_auto_iam_authn
import sqlalchemy

engine = connect_with_connector_auto_iam_authn()

def get_connection():
    # return psycopg2.connect(**DB_CONFIG)
    return engine.connect()

def add_person(name, image, description, bio_docs, authored_docs, owner, is_public):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Person (name, image, description, bio_docs, authored_docs, owner, is_public)
    VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
    """, (name, image, description, bio_docs, authored_docs, owner, is_public))
    person_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return person_id

def add_collection(name, image, description, bio_docs, people, owner, is_public):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO PeopleCollection (name, image, description, bio_docs, people, owner, is_public)
    VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
    """, (name, image, description, bio_docs, people, owner, is_public))
    collection_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return collection_id

def get_person(person_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Person WHERE id = %s", (person_id,))
    person = cur.fetchone()
    cur.close()
    conn.close()
    return person

def get_collection(collection_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM PeopleCollection WHERE id = %s", (collection_id,))
    collection = cur.fetchone()
    cur.close()
    conn.close()
    return collection

# Add more functions for updating, deleting, and querying data