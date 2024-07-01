from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from typing import List, Optional
from models import Person, PeopleCollection, User, Comment
from database import person_collection, people_collection as collection_collection, user_collection, comments_collection

app = FastAPI()

# Create Person
@app.post("/person/", response_model=Person)
async def create_person(person: Person):
    person = jsonable_encoder(person)
    new_person = await person_collection.insert_one(person)
    created_person = await person_collection.find_one({"_id": new_person.inserted_id})
    return JSONResponse(status_code=201, content=created_person)

# Read Person
@app.get("/person/{person_id}", response_model=Person)
async def read_person(person_id: str):
    person = await person_collection.find_one({"_id": ObjectId(person_id)})
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

# List Persons
@app.get("/persons/", response_model=List[Person])
async def list_persons():
    persons = await person_collection.find().to_list(length=100)
    return persons

# Create PeopleCollection
@app.post("/people_collection/", response_model=PeopleCollection)
async def create_people_collection(collection: PeopleCollection):
    collection = jsonable_encoder(collection)
    new_collection = await collection_collection.insert_one(collection)
    created_collection = await collection_collection.find_one({"_id": new_collection.inserted_id})
    return JSONResponse(status_code=201, content=created_collection)

# Read PeopleCollection
@app.get("/people_collection/{collection_id}", response_model=PeopleCollection)
async def read_people_collection(collection_id: str):
    collection = await collection_collection.find_one({"_id": ObjectId(collection_id)})
    if collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection

# List PeopleCollections
@app.get("/people_collections/", response_model=List[PeopleCollection])
async def list_people_collections():
    collections = await collection_collection.find().to_list(length=100)
    return collections

# Create User
@app.post("/user/", response_model=User)
async def create_user(user: User):
    user = jsonable_encoder(user)
    new_user = await user_collection.insert_one(user)
    created_user = await user_collection.find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=201, content=created_user)

# Read User
@app.get("/user/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# List Users
@app.get("/users/", response_model=List[User])
async def list_users():
    users = await user_collection.find().to_list(length=100)
    return users

# Create Comment
@app.post("/comment/", response_model=Comment)
async def create_comment(comment: Comment):
    comment = jsonable_encoder(comment)
    new_comment = await comments_collection.insert_one(comment)
    created_comment = await comments_collection.find_one({"_id": new_comment.inserted_id})
    return JSONResponse(status_code=201, content=created_comment)

# Read Comment
@app.get("/comment/{comment_id}", response_model=Comment)
async def read_comment(comment_id: str):
    comment = await comments_collection.find_one({"_id": ObjectId(comment_id)})
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

# List Comments
@app.get("/comments/", response_model=List[Comment])
async def list_comments():
    comments = await comments_collection.find().to_list(length=100)
    return comments
