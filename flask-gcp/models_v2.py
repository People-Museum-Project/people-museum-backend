from sqlalchemy import Column, Integer, String, Boolean, Text, ARRAY
from db import Base


class Person(Base):
    __tablename__ = 'Person'

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
    __tablename__ = 'PeopleCollection'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255))
    description = Column(Text)
    bio_docs = Column(ARRAY(Text))
    people = Column(ARRAY(Integer))
    owner = Column(Integer)
    share_list = Column(ARRAY(Integer))
    is_public = Column(Boolean, default=False)
