from flask import Blueprint, request, jsonify

from app.people_museum_handler import Handler

datastore_bp = Blueprint('datastore_bp', __name__)
handler = Handler()


@datastore_bp.route("/addUser", methods=["POST"])
def addUser():
    data = request.get_json()
    handler.addUser(
        data['name'],
        data['imageLink'],
        data['description']
    )
    return jsonify({"message": "New user created successfully", "data": data}), 200


@datastore_bp.route("/getUser", methods=["POST"])
def getUser():
    data = request.get_json()
    user = handler.getUserByUserId(data['userId'])
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
    return jsonify({
        "message": "Users retrieved successfully",
        "data": users
    }), 200

@datastore_bp.route("/updateUser", methods=["PUT"])
def updateUser():
    data = request.get_json()
    updated = handler.updateUserByUserId(
        data["userId"],
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
    deleted = handler.deleteUserByUserId(data["userId"])
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
        data["userId"],
        data["public"]
    )
    return jsonify({"message": "Person created successfully", "data": data}), 200


@datastore_bp.route("/getPersonList", methods=['POST'])
def getPersonList():
    data = request.get_json()
    sortBy = data['sortBy']
    order = data['order']
    limit = data['limit']
    page = data['page']

    return jsonify({
            "message": f"PersonList of user [{data['userId']}] retrieved successfully",
            "data": handler.getPersonListByUserId(data['userId'], sortBy, order, page, limit)
        }), 200


@datastore_bp.route("/getPersonListByCollection", methods=['POST'])
def getPersonListByCollection():
    data = request.get_json()
    collectionId = data['collectionId']
    sortBy = data['sortBy']
    ascending = data['ascending']
    limit = data['limit']
    page = data['page']
    print("<<<<<", data)

    return jsonify({
        "message": f"Person list of collection {collectionId} retrieved successfully",
        "data": handler.getPersonListByCollectionId(collectionId, page, limit, sortBy=sortBy, ascending=ascending)
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
        data.get('userId'),
        data.get('name'),
        data.get('imageLink'),
        data.get('description'),
        data.get('isPublic')
    )

    return jsonify({"message": "New collection created successfully"}), 200


@datastore_bp.route("/getCollectionList", methods=["POST"])
def getCollectionList():
    data = request.get_json()
    userId = data.get('userId')
    page = data['page']
    limit = data['limit']
    sortBy = data['sortBy']
    order = data['order']

    results = []
    for collection in handler.getCollectionListByUserId(userId, sortBy, order, page, limit):
        collection['id'] = collection.key.id_or_name
        results.append(collection)

    return jsonify({
        "message": f"Collections of user [{data.get('userId')}]",
        "data": results
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
        return jsonify({"message": "addition failed"}), 400
