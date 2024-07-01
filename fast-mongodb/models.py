from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

class Person(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    image: str
    description: str
    bio_documents: List[str]
    authored_documents: List[str]
    collections: List[str]  # List of PersonCollections
    owner: str
    shareList: List[str]
    is_public: bool

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class PeopleCollection(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    image: str
    description: str
    bio_documents: List[str]
    persons: List[str]  # List of Person ids
    owner: str
    shareList: List[str]
    is_public: bool

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str
    email: str
    password: str  # In a real application, passwords should be hashed

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Comment(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    content: str
    user_id: str
    entity_id: str  # ID of the Person or PeopleCollection being commented on
    entity_type: str  # 'person' or 'collection'
    timestamp: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
