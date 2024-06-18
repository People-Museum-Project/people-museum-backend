# models.py

from sqlalchemy import ARRAY, Boolean, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255))
    description = Column(Text)
    bio_docs = Column(ARRAY(Text))
    authored_docs = Column(ARRAY(Text))
    collections = Column(ARRAY(Integer))
    owner = Column(Integer)
    share_list = Column(ARRAY(Integer))
    is_public = Column(Boolean, default=False)

class PeopleCollection(Base):
    __tablename__ = 'people_collection'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255))
    description = Column(Text)
    bio_docs = Column(ARRAY(Text))
    people = Column(ARRAY(Integer))
    owner = Column(Integer)
    share_list = Column(ARRAY(Integer))
    is_public = Column(Boolean, default=False)

# Define other tables similarly
