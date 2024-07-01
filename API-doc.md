# People Museum API Documentation

This documentation provides details on the endpoints available in the People Museum API. Each endpoint's purpose, required method, and necessary parameters are described below.

## Base URL

The base URL for accessing the API endpoints is currently in local environment: `http://127.0.0.1:8080/`

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
    "description": "string"
  }
  ```
- **Response**:
  - `200 OK`: `{ "message": "New user created successfully", "data": <user data> }`

### 3. Get User
- **Endpoint**: `/getUser`
- **Method**: POST
- **Description**: Retrieves a user by their user ID.
- **Request Body**:
  ```json
  {
    "userId": "string"
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
    "userId": "string",
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
    "userId": "string"
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
    "userId": "string"
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
    "userId": "string",
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
    "userId": "string"
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
    "collectionId": "string"
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