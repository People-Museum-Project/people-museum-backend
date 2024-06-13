from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

from models import Person, PeopleCollection
from connect_connector_auto_iam_authn import connect_with_connector_auto_iam_authn

# Initiate database connection
db = connect_with_connector_auto_iam_authn()

# Check if the table exists before creating it
inspector = inspect(db)
if not inspector.has_table("person"):
    Person.__table__.create(db)
    # PeopleCollection.__table__.create(db

Session = sessionmaker(bind=db)

def create_person(name, image, description, bio_docs, authored_docs, collections, owner, share_list, is_public):
    session = Session()
    person = Person(
        name=name,
        image=image,
        description=description,
        bio_docs=bio_docs,
        authored_docs=authored_docs,
        collections=collections,
        owner=owner,
        share_list=share_list,
        is_public=is_public
    )
    session.add(person)
    session.commit()
    session.close()

def read_person(person_id):
    session = Session()
    person = session.query(Person).filter_by(id=person_id).first()
    session.close()
    return person

def update_person(person_id, **kwargs):
    session = Session()
    person = session.query(Person).filter_by(id=person_id).first()
    if person:
        for key, value in kwargs.items():
            setattr(person, key, value)
        session.commit()
    session.close()

def delete_person(person_id):
    session = Session()
    person = session.query(Person).filter_by(id=person_id).first()
    if person:
        session.delete(person)
        session.commit()
    session.close()

def create_collection(name, image, description, bio_docs, people, owner, share_list, is_public):
    collection = PeopleCollection(
        name=name,
        image=image,
        description=description,
        bio_docs=bio_docs,
        people=people,
        owner=owner,
        share_list=share_list,
        is_public=is_public
    )
    session.add(collection)
    session.commit()

def read_collection(collection_id):
    return session.query(PeopleCollection).filter_by(id=collection_id).first()

def update_collection(collection_id, **kwargs):
    collection = session.query(PeopleCollection).filter_by(id=collection_id).first()
    for key, value in kwargs.items():
        setattr(collection, key, value)
    session.commit()

def delete_collection(collection_id):
    collection = session.query(PeopleCollection).filter_by(id=collection_id).first()
    session.delete(collection)
    session.commit()
