from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_v2 import Person, PeopleCollection

# Assuming the engine is created in main.py or another module
# and passed to the database module

# Session = sessionmaker()
Session = sessionmaker(bind=engine)

def init_db(engine):
    """
    Initializes the database session with the provided engine.

    Args:
        engine (sqlalchemy.engine.base.Engine): The database engine object.
    """
    Session.configure(bind=engine)

def add_person(person):
    """
    Adds a person to the database.

    Args:
        person (Person): The person object to add to the database.
    """
    session = Session()
    session.add(person)
    session.commit()
    session.close()

def add_collection(collection):
    """
    Adds a collection to the database.

    Args:
        collection (PeopleCollection): The collection object to add to the database.
    """
    session = Session()
    session.add(collection)
    session.commit()
    session.close()

def get_person(person_id):
    """
    Retrieves a person from the database by ID.

    Args:
        person_id (int): The ID of the person to retrieve.

    Returns:
        Person: The retrieved person object, or None if not found.
    """
    session = Session()
    person = session.query(Person).filter_by(id=person_id).first()
    session.close()
    return person

def get_collection(collection_id):
    """
    Retrieves a collection from the database by ID.

    Args:
        collection_id (int): The ID of the collection to retrieve.

    Returns:
        PeopleCollection: The retrieved collection object, or None if not found.
    """
    session = Session()
    collection = session.query(PeopleCollection).filter_by(id=collection_id).first()
    session.close()
    return collection

def get_index_context():
    """
    Retrieves the context for rendering the index page.

    Returns:
        dict: The context for rendering the index page.
    """
    session = Session()
    recent_people = session.query(Person).order_by(Person.id.desc()).limit(5).all()
    recent_collections = session.query(PeopleCollection).order_by(PeopleCollection.id.desc()).limit(5).all()
    session.close()

    context = {
        'recent_people': recent_people,
        'recent_collections': recent_collections
    }
    return context
