from flask import Blueprint, request, jsonify

from app.datastore_handler import Handler

datastore_bp = Blueprint('datastore_bp', __name__)
handler = Handler()


@datastore_bp.route("/addUser", methods=["POST"])
def addUser():
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
    users = handler.getAllUsers()
    total_count = handler.countEntities('User')

    return jsonify({
        "message": "Users retrieved successfully",
        "data": users,
        "total_count": total_count
    }), 200

@datastore_bp.route("/updateUser", methods=["PUT"])
def updateUser():
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
    data = request.get_json()
    deleted = handler.deleteUserByUserId(data["googleUserId"])
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User deleted failed, user not found"}), 404


@datastore_bp.route("/addPerson", methods=["POST"])
def addPerson():
    data = request.get_json()
    handler.addPerson(
        data["name"],
        data["imageLink"],
        data["description"],
        data["context"],
        data["googleUserId"],
        data["public"]
    )
    return jsonify({"message": "Person created successfully", "data": data}), 200


@datastore_bp.route("/getPersonList", methods=['POST'])
def getPersonList():
    data = request.get_json()
    userId = data['googleUserId']
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']


    persons = handler.getPersonListByUserId(userId, page, limit, sortBy, ascending)
    total_count = handler.countEntities('Person', {'userId', userId})

    return jsonify({
            "message": f"PersonList of user [{userId}] retrieved successfully",
            "data": persons,
            "total_count": total_count
        }), 200


@datastore_bp.route("/getPersonListByCollection", methods=['POST'])
def getPersonListByCollection():
    data = request.get_json()
    collectionId = int(data['collectionId'])
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']

    persons = handler.getPersonListByCollectionId(collectionId, page, limit, sortBy=sortBy, ascending=ascending)
    total_count = handler.countEntities('PersonCollection', {'collectionId', collectionId})

    return jsonify({
        "message": f"Person list of collection {collectionId} retrieved successfully",
        "data": persons,
        "total_count": total_count
    }), 200


@datastore_bp.route("/getPerson", methods=['POST'])
def getPerson():
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
    data = request.get_json()
    handler.deletePersonByPersonId(
        data['personId']
    )
    return jsonify({"message": "Person deleted successfully"}), 200


@datastore_bp.route("/addCollection", methods=["POST"])
def addCollection():
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

    total_count = handler.countEntities('Collection', {'userId', userId})

    return jsonify({
        "message": f"Collections of user [{data.get('googleUserId')}]",
        "data": results,
        "total_count": total_count
    }), 200


@datastore_bp.route("/getCollectionListByPerson", methods=['POST'])
def getCollectionListByPerson():
    data = request.get_json()
    personId = data['personId']
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']

    persons = handler.getCollectionListByPersonId(personId, page, limit, sortBy=sortBy, ascending=ascending)
    total_count = handler.countEntities('Person', {'personId', personId})

    return jsonify({
        "message": f"Collection list of person {personId} retrieved successfully",
        "data": persons,
        "total_count": total_count
    }), 200


@datastore_bp.route("/getCollection", methods=["POST"])
def getCollection():
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
    data = request.get_json()
    handler.deleteCollectionById(
        data['collectionId']
    )

    return jsonify({"message": "Collection deleted successfully"}), 200


@datastore_bp.route("/addPersonCollection", methods=["POST"])
def addPersonCollection():
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
    data = request.get_json()
    deleted = handler.deletePersonFromCollection(
        data['personId'],
        data['collectionId']
    )
    if deleted:
        return jsonify({"message": "Person removed from collection successfully"}), 200
    else:
        return jsonify({"message": "Removal failed"}), 400
