# People Museum API Documentation

This documentation provides details on the endpoints available in the People Museum API. Each endpoint's purpose, required method, and necessary parameters are described below.

## Base URL

The base URL for accessing the API endpoints:
- **Online environment: `https://peoplemuseumyeah.uc.r.appspot.com/db`**
- **Local environment: `http://127.0.0.1:8080/`**

## Endpoints Overview

### User Management
- **Create User**: `/db/addUser`  
  Adds a new user to the system. 

- **Retrieve User**: `/db/getUser`  
  Retrieves a user by their Google User ID.

- **List Users**: `/db/listUsers`  
  Retrieves a list of all users.

- **Update User**: `/db/updateUser`  
  Updates the details of an existing user. 

- **Delete User**: `/db/deleteUser`  
  Deletes a user by their Google User ID. 

### Person Management
- **Create Person**: `/db/addPerson`  
  Adds a new person, associating them with an AI assistant ID. 

- **Retrieve Person List**: `/db/getPersonList`  
  Retrieves a list of people associated with a specific user. 

- **Retrieve Person**: `/db/getPerson`  
  Retrieves a person by their Person ID. 

- **Update Person**: `/db/updatePerson`  
  Updates an existing person's details. 

- **Delete Person**: `/db/deletePerson`  
  Deletes a person by their Person ID. 

### Collection Management
- **Create Collection**: `/db/addCollection`  
  Creates a new collection.

- **Retrieve Collection List**: `/db/getCollectionList`  
  Retrieves a list of collections associated with a specific user. 

- **Retrieve Collection**: `/db/getCollection`  
  Retrieves a collection by its ID. 

- **Update Collection**: `/db/updateCollection`  
  Updates an existing collection. 

- **Delete Collection**: `/db/deleteCollection`  
  Deletes a collection by its ID. 

### Additional Collection-Related Endpoints
- **Add Person to Collection**: `/db/addPersonCollection`  
  Adds a person to a collection. Detailed documentation is currently not provided in `API-doc.md`.

- **Remove Person from Collection**: `/db/deletePersonFromCollection`  
  Removes a person from a collection. Detailed documentation is currently not provided in `API-doc.md`.

### AI Integration Endpoints
- **Generate Text**: `/ai/generateText`  
  Generates text based on a prompt using a specified AI model (default: GPT-3.5-Turbo).

- **Ask Question**: `/ai/askQuestion`  
  Asks a question to a specified AI assistant and returns the response.

- **Generate Sample Prompts**: `/ai/generateSamplePrompts`  
  Generates sample prompts based on a given context and AI assistant.

- **Generate Follow-up Questions**: `/ai/generateFollowups`  
  Generates follow-up questions based on a question, response, and AI assistant.

- **Text-to-Speech**: `/ai/textToSpeech`  
  Converts text to speech using a specified voice.

- **Speech Recognition**: `/ai/speechRecognition`  
  Recognizes speech from an uploaded audio file and returns transcribed text.

## Data Models
Although not explicitly defined as an API document, the source code reveals the following data structures:

- **User**: `name`, `imageLink`, `googleUserId`, `gmail`, `description`, `favourite`.
- **Person**: `name`, `imageLink`, `description`, `userId`, `public`, `assistantId`, `date`.
- **Collection**: `userId`, `name`, `imageLink`, `description`, `date`, `isPublic`.
- **PersonCollection**: `personId`, `collectionId`, unique (composite key).

## Backend & Infrastructure
- The backend uses Flask, a Python web framework, and runs on port 8080.
- Google Cloud Datastore is used for data storage and retrieval.
- The code mentions a "PST_OFFSET" used for time-related operations, likely for storing timestamps in PST.

## AI Integration
The People Museum API integrates with OpenAI's API for AI-powered functionalities like text generation, question answering, prompt generation, and speech processing. It uses the "GPT-3.5-Turbo" model as the default for text generation.

## Endpoints

### 1. Index
- **Endpoint**: `/`
- **Method**: GET
- **Description**: Returns a message indicating the index page has been successfully reached.
- **Response**:
  - `200 OK`: `{ "message": "index page successfully reached" }`

### 2. Add User
- **Endpoint**: `/addUser`
- **Method**: POST
- **Description**: Adds a new user.
- **Request Body**:
  ```json
  {
    "name": "string",
    "imageLink": "string",
    "description": "string",
    "favourite": "string",
    "googleUserId": "string",
    "gmail": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "New user created successfully", "data": <user data> }`
  - `409 CONFLICT`: `{"message": "User already exists"}`

### 3. Get User
- **Endpoint**: `/getUser`
- **Method**: POST
- **Description**: Retrieves a user by their user ID.
- **Request Body**:
  ```json
  {
    "googleUserId": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "User retrieved successfully", "data": <user data> }`
  - `404 Not Found`: `{ "message": "User doesn't exist" }`

### 4. List Users
- **Endpoint**: `/listUsers`
- **Method**: GET
- **Description**: Retrieves a list of all users.
- **Response**:
  - `200 OK`: `{ "message": "Users retrieved successfully", "data": <list of users> }`

### 5. Update User
- **Endpoint**: `/updateUser`
- **Method**: PUT
- **Description**: Updates a user by their user ID.
- **Request Body**:
  ```json
  {
    "googleUserId": "string",
    "name": "string",
    "imageLink": "string",
    "description": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "User updated successfully" }`
  - `404 Not Found`: `{ "message": "User update failed, user not found" }`

### 6. Delete User
- **Endpoint**: `/deleteUser`
- **Method**: DELETE
- **Description**: Deletes a user by their user ID.
- **Request Body**:
  ```json
  {
    "googleUserId": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "User deleted successfully" }`
  - `404 Not Found`: `{ "message": "User delete failed, user not found" }`

### 7. Add Person
- **Endpoint**: `/addPerson`
- **Method**: POST
- **Description**: Adds a new person.
- **Request Body**:
  ```json
  {
    "name": "string",
    "imageLink": "string",
    "description": "string",
    "context": "string",
    "googleUserId": "integer",
    "public": "boolean"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Person created successfully", "data": <person data> }`

### 8. Get Person List
- **Endpoint**: `/getPersonList`
- **Method**: POST
- **Description**: Retrieves a list of persons associated with a user by their user ID.
- **Request Body**:
  ```json
  {
    "googleUserId": "string",
    "sortBy": "string",
    "ascending": "boolean",
    "limit": "integer",
    "page": "integer"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "PersonList of user [<userId>] retrieved successfully", "data": <list of persons> }`

### 9. Get Person
- **Endpoint**: `/getPerson`
- **Method**: POST
- **Description**: Retrieves a person by their person ID.
- **Request Body**:
  ```json
  {
    "personId": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Person retrieved successfully", "person": <person data> }`
  - `404 Not Found`: `{ "message": "Person not found" }`

### 10. Update Person
- **Endpoint**: `/updatePerson`
- **Method**: PUT
- **Description**: Updates a person by their person ID.
- **Request Body**:
  ```json
  {
    "personId": "string",
    "newName": "string",
    "newImageLink": "string",
    "newDescription": "string",
    "newContext": "string",
    "newPublic": "boolean"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Person updated successfully" }`
  - `404 Not Found`: `{ "message": "Person update failed, person not found" }`

### 11. Delete Person
- **Endpoint**: `/deletePerson`
- **Method**: DELETE
- **Description**: Deletes a person by their person ID.
- **Request Body**:
  ```json
  {
    "personId": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Person deleted successfully" }`

### 12. Add Collection
- **Endpoint**: `/addCollection`
- **Method**: POST
- **Description**: Adds a new collection.
- **Request Body**:
  ```json
  {
    "googleUserId": "string",
    "name": "string",
    "imageLink": "string",
    "description": "string",
    "isPublic": "boolean"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "New collection created successfully" }`

### 13. Get Collection List
- **Endpoint**: `/getCollectionList`
- **Method**: POST
- **Description**: Retrieves a list of collections associated with a user by their user ID.
- **Request Body**:
  ```json
  {
    "googleUserId": "integer",
    "page": "integer",
    "limit": "integer",
    "sortBy": "string",
    "ascending": "boolean"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Collections of user [<userId>] retrieved successfully", "data": <list of collections> }`

### 14. Get Collection
- **Endpoint**: `/getCollection`
- **Method**: POST
- **Description**: Retrieves a collection by its collection ID.
- **Request Body**:
  ```json
  {
    "collectionId": "integer"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Collection retrieved successfully", "data": <collection data> }`

### 15. Update Collection
- **Endpoint**: `/updateCollection`
- **Method**: PUT
- **Description**: Updates a collection by its collection ID.
- **Request Body**:
  ```json
  {
    "collectionId": "string",
    "newName": "string",
    "newImageLink": "string",
    "newDescription": "string",
    "newIsPublic": "boolean"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Collection updated successfully" }`
  - `404 Not Found`: `{ "message": "Collection update failed, collection not found" }`

### 16. Delete Collection
- **Endpoint**: `/deleteCollection`
- **Method**: DELETE
- **Description**: Deletes a collection by its collection ID.
- **Request Body**:
  ```json
  {
    "collectionId": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "Collection deleted successfully" }`

---

This API documentation covers the essential endpoints for managing users, persons, and collections in the People Museum application. Ensure the `people_museum_handler` module provides the necessary functionalities for these endpoints to work correctly.