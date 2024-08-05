from flask import Blueprint, request, jsonify
from app.datastore_handler import Handler

datastore_bp = Blueprint('datastore_bp', __name__)
handler = Handler()


@datastore_bp.route("/addUser", methods=["POST"])
def addUser():
    """
    Creates a new user with the provided information.

    Request JSON:
        - name (str): The name of the user.
        - imageLink (str): Link to the user's image.
        - googleUserId (str): Google user ID.
        - gmail (str): User's Gmail address.
        - description (str): Description of the user.

    Returns:
        - JSON response with a success message and user data if creation is successful.
        - JSON response with an error message if the user already exists.
    """
    data = request.get_json()
    result = handler.addUser(
        data['name'],
        data['imageLink'],
        data['googleUserId'],
        data['gmail'],
        data['description']
    )
    if result:
        return jsonify({"message": "New user created successfully", "data": data}), 200
    else:
        return jsonify({"message": "User already exists"}), 409


@datastore_bp.route("/getUser", methods=["POST"])
def getUser():
    """
    Retrieves a user by their Google user ID.

    Request JSON:
        - googleUserId (str): Google user ID.

    Returns:
        - JSON response with a success message and user data if the user exists.
        - JSON response with an error message if the user does not exist.
    """
    data = request.get_json()
    user = handler.getUserByUserId(data['googleUserId'])
    if user:
        return jsonify({
            "message": "User retrieved successfully",
            "data": user
        }), 200
    else:
        return jsonify({"message": "User doesn't exist"}), 404

@datastore_bp.route("/listUsers", methods=["GET"])
def listUsers():
    """
    Lists all users and provides a count of total users.

    Returns:
        - JSON response with a success message, user data, and total count of users.
    """
    users = handler.getAllUsers()
    total_count = handler.countEntities('User')

    return jsonify({
        "message": "Users retrieved successfully",
        "data": users,
        "total_count": total_count
    }), 200

@datastore_bp.route("/updateUser", methods=["PUT"])
def updateUser():
    """
    Updates an existing user with new information.

    Request JSON:
        - googleUserId (str): Google user ID.
        - name (str): Updated name of the user.
        - imageLink (str): Updated link to the user's image.
        - description (str): Updated description of the user.

    Returns:
        - JSON response with a success message if the update is successful.
        - JSON response with an error message if the user is not found.
    """
    data = request.get_json()
    updated = handler.updateUserByUserId(
        data["googleUserId"],
        data["name"],
        data["imageLink"],
        data["description"]
    )
    if updated:
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"message": "User updated failed, user not found"}), 404


@datastore_bp.route("/deleteUser", methods=["DELETE"])
def deleteUser():
    """
    Deletes a user by their Google user ID.

    Request JSON:
        - googleUserId (str): Google user ID.

    Returns:
        - JSON response with a success message if the deletion is successful.
        - JSON response with an error message if the user is not found.
    """
    data = request.get_json()
    deleted = handler.deleteUserByUserId(data["googleUserId"])
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User deleted failed, user not found"}), 404


@datastore_bp.route("/addPerson", methods=["POST"])
def addPerson():
    """
    Creates a new person and associates it with an assistant ID.

    Request JSON:
        - name (str): The name of the person.
        - imageLink (str): Link to the person's image.
        - description (str): Description of the person.
        - googleUserId (str): Google user ID of the person.
        - public (bool): Public visibility of the person.

    Returns:
        - JSON response with a success message and person data.
    """
    data = request.get_json()
    assistant_id = handler.createAssistant(data["name"], data["description"])
    handler.addPerson(
        data["name"],
        data["imageLink"],
        data["description"],
        data["googleUserId"],
        data["public"],
        assistant_id
    )
    return jsonify({"message": "Person created successfully", "data": data}), 200


@datastore_bp.route("/getPersonList", methods=['POST'])
def getPersonList():
    """
    Retrieves a list of persons associated with a specific user.

    Request JSON:
        - googleUserId (str): Google user ID of the user.
        - sortBy (str): Field to sort by.
        - ascending (bool): Sort order (ascending or descending).
        - limit (int): Number of records to retrieve.
        - page (int): Page number for pagination.

    Returns:
        - JSON response with a success message, list of persons, and total count of persons.
    """
    data = request.get_json()
    userId = data['googleUserId']
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']

    persons = handler.getPersonListByUserId(userId, page, limit, sortBy, ascending)
    total_count = handler.countEntities('Person', 'userId', userId)

    return jsonify({
            "message": f"PersonList of user [{userId}] retrieved successfully",
            "data": persons,
            "total_count": total_count
        }), 200


@datastore_bp.route("/getPersonListByCollection", methods=['POST'])
def getPersonListByCollection():
    """
    Retrieves a list of persons associated with a specific collection.

    Request JSON:
        - collectionId (int): ID of the collection.
        - sortBy (str): Field to sort by.
        - ascending (bool): Sort order (ascending or descending).
        - limit (int): Number of records to retrieve.
        - page (int): Page number for pagination.

    Returns:
        - JSON response with a success message, list of persons, and total count of persons in the collection.
    """
    data = request.get_json()
    collectionId = int(data['collectionId'])
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']

    persons = handler.getPersonListByCollectionId(collectionId, page, limit, sortBy=sortBy, ascending=ascending)
    total_count = handler.countEntities('PersonCollection', 'collectionId', collectionId)

    return jsonify({
        "message": f"Person list of collection {collectionId} retrieved successfully",
        "data": persons,
        "total_count": total_count
    }), 200


@datastore_bp.route("/getPerson", methods=['POST'])
def getPerson():
    """
    Retrieves a person by their person ID.

    Request JSON:
        - personId (str): Person ID.

    Returns:
        - JSON response with a success message and person data if the person is found.
        - JSON response with an error message if the person is not found.
    """
    data = request.get_json()
    person = handler.getPersonByPersonId(
        data['personId']
    )
    if person:
        return jsonify({"message": "Person retrieved successfully", "person": person}), 200
    else:
        return jsonify({"message": "Person not found"}), 404


@datastore_bp.route("/updatePerson", methods=["PUT"])
def updatePerson():
    """
    Updates an existing person with new information.

    Request JSON:
        - personId (str): Person ID.
        - newName (str): Updated name of the person.
        - newImageLink (str): Updated link to the person's image.
        - newDescription (str): Updated description of the person.
        - newContext (str): Updated context for the person.
        - newPublic (bool): Updated visibility status of the person.

    Returns:
        - JSON response with a success message if the update is successful.
        - JSON response with an error message if the person is not found.
    """
    data = request.get_json()
    updated = handler.updatePersonByPersonId(
        data['personId'],
        data['newName'],
        data['newImageLink'],
        data['newDescription'],
        data['newContext'],
        data['newPublic'],
    )
    if updated:
        return jsonify({"message": "Person updated successfully"}), 200
    else:
        return jsonify({"message": "Person update failed, person not found"}), 404


@datastore_bp.route("/deletePerson", methods=["DELETE"])
def deletePerson():
    """
    Deletes a person by their person ID.

    Request JSON:
        - personId (str): Person ID.

    Returns:
        - JSON response with a success message if the deletion is successful.
    """
    data = request.get_json()
    handler.deletePersonByPersonId(
        data['personId']
    )
    return jsonify({"message": "Person deleted successfully"}), 200


@datastore_bp.route("/addCollection", methods=["POST"])
def addCollection():
    """
    Creates a new collection.

    Request JSON:
        - googleUserId (str): Google user ID of the collection owner.
        - name (str): Name of the collection.
        - imageLink (str): Link to the collection's image.
        - description (str): Description of the collection.
        - isPublic (bool): Visibility status of the collection.

    Returns:
        - JSON response with a success message.
    """
    data = request.get_json()
    handler.addCollection(
        data.get('googleUserId'),
        data.get('name'),
        data.get('imageLink'),
        data.get('description'),
        data.get('isPublic')
    )

    return jsonify({"message": "New collection created successfully"}), 200


@datastore_bp.route("/getCollectionList", methods=["POST"])
def getCollectionList():
    """
    Retrieves a list of collections associated with a specific user.

    Request JSON:
        - googleUserId (str): Google user ID of the user.
        - page (int): Page number for pagination.
        - limit (int): Number of records to retrieve.
        - sortBy (str): Field to sort by.
        - ascending (bool): Sort order (ascending or descending).

    Returns:
        - JSON response with a success message, list of collections, and total count of collections.
    """
    data = request.get_json()
    userId = data['googleUserId']
    page = data['page']
    limit = data['limit']
    sortBy = data['sortBy']
    ascending = data['ascending']

    results = []
    for collection in handler.getCollectionListByUserId(userId, page, limit, sortBy, ascending):
        collection['id'] = collection.key.id_or_name
        results.append(collection)

    total_count = handler.countEntities('Collection', 'userId', userId)

    return jsonify({
        "message": f"Collections of user [{data.get('googleUserId')}]",
        "data": results,
        "total_count": total_count
    }), 200


@datastore_bp.route("/getCollectionListByPerson", methods=['POST'])
def getCollectionListByPerson():
    """
    Retrieves a list of collections associated with a specific person.

    Request JSON:
        - personId (str): Person ID.
        - sortBy (str): Field to sort by.
        - ascending (bool): Sort order (ascending or descending).
        - limit (int): Number of records to retrieve.
        - page (int): Page number for pagination.

    Returns:
        - JSON response with a success message, list of collections, and total count of collections.
    """
    data = request.get_json()
    personId = data['personId']
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']

    persons = handler.getCollectionListByPersonId(personId, page, limit, sortBy=sortBy, ascending=ascending)
    total_count = handler.countEntities('Person', 'personId', personId)

    return jsonify({
        "message": f"Collection list of person {personId} retrieved successfully",
        "data": persons,
        "total_count": total_count
    }), 200


@datastore_bp.route("/getCollection", methods=["POST"])
def getCollection():
    """
    Retrieves a collection by its ID.

    Request JSON:
        - collectionId (int): Collection ID.

    Returns:
        - JSON response with a success message and collection data.
    """
    data = request.get_json()
    collection = handler.getCollectionById(
        data['collectionId']
    )
    return jsonify({
        "message": f"Collection retrieved successfully",
        "data": collection
    }), 200


@datastore_bp.route("/updateCollection", methods=["PUT"])
def updateCollection():
    """
    Updates an existing collection with new information.

    Request JSON:
        - collectionId (int): Collection ID.
        - newName (str): Updated name of the collection.
        - newImageLink (str): Updated link to the collection's image.
        - newDescription (str): Updated description of the collection.
        - newIsPublic (bool): Updated visibility status of the collection.

    Returns:
        - JSON response with a success message if the update is successful.
        - JSON response with an error message if the collection is not found.
    """
    data = request.get_json()
    updated = handler.updateCollectionById(
        data['collectionId'],
        data['newName'],
        data['newImageLink'],
        data['newDescription'],
        data['newIsPublic']
    )
    if updated:
        return jsonify({"message": "Collection updated successfully"}), 200
    else:
        return jsonify({"message": "Collection update failed, collection not found"}), 404


@datastore_bp.route("/deleteCollection", methods=["DELETE"])
def deleteCollection():
    """
    Deletes a collection by its ID.

    Request JSON:
        - collectionId (int): Collection ID.

    Returns:
        - JSON response with a success message if the deletion is successful.
    """
    data = request.get_json()
    handler.deleteCollectionById(
        data['collectionId']
    )

    return jsonify({"message": "Collection deleted successfully"}), 200


@datastore_bp.route("/addPersonCollection", methods=["POST"])
def addPersonCollection():
    """
    Adds a person to a collection.

    Request JSON:
        - personId (str): Person ID.
        - collectionId (int): Collection ID.

    Returns:
        - JSON response with a success message if the person was added successfully.
        - JSON response with a message if the relation already exists.
    """
    data = request.get_json()
    add = handler.addPersonCollection(
        data['personId'],
        data['collectionId']
    )
    if add:
        return jsonify({"message": "person added to collection successfully"}), 200
    else:
        return jsonify({"message": "relation already exists"}), 200


@datastore_bp.route("/deletePersonFromCollection", methods=["DELETE"])
def deletePersonFromCollection():
    """
    Removes a person from a collection.

    Request JSON:
        - personId (str): Person ID.
        - collectionId (int): Collection ID.

    Returns:
        - JSON response with a success message if the person was removed successfully.
        - JSON response with an error message if the removal failed.
    """
    data = request.get_json()
    deleted = handler.deletePersonFromCollection(
        data['personId'],
        data['collectionId']
    )
    if deleted:
        return jsonify({"message": "Person removed from collection successfully"}), 200
    else:
        return jsonify({"message": "Removal failed"}), 400
