from flask import Flask, request, jsonify
from people_museum_handler import Handler
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
handler = Handler()


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "index page successfully reached"}), 200


@app.route("/addUser", methods=["POST"])
def addUser():
    data = request.get_json()
    handler.addUser(
        data['name'],
        data['imageLink'],
        data['description']
    )
    return jsonify({"message": "New user created successfully"}), 200


@app.route("/getUser", methods=["POST"])
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

@app.route("/listUsers", methods=["GET"])
def listUsers():
    users = handler.getAllUsers()
    return jsonify({
        "message": "Users retrieved successfully",
        "data": users
    }), 200

@app.route("/updateUser", methods=["PUT"])
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


@app.route("/deleteUser", methods=["DELETE"])
def deleteUser():
    data = request.get_json()
    deleted = handler.deleteUserByUserId(data["userId"])
    if deleted:
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User deleted failed, user not found"}), 404

@app.route("/addPerson", methods=["POST"])
def addPerson():
    data = request.get_json()
    handler.addPerson(
        data["name"],
        data["imageLink"],
        data["description"],
        data["context"],
        data["public"]
    )
    return jsonify({"message": "Person created successfully"}), 200


@app.route("/getPersonList", methods=['POST'])
def getPersonList():
    data = request.get_json()
    return jsonify({
        "message": f"PersonList of user [{data['userId']}] retrieved successfully",
        "data": [person for person in handler.getPersonListByUserId(data['userId'])]
    }), 200

@app.route("/getPerson", methods=['POST'])
def getPerson():
    data = request.get_json()
    person = handler.getPersonByPersonId(
        data['personId']
    )
    if person:
        return jsonify({"message": "Person retrieved successfully", "person": person}), 200
    else:
        return jsonify({"message": "Person not found"}), 404


@app.route("/updatePerson", methods=["PUT"])
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


@app.route("/deletePerson", methods=["DELETE"])
def deletePerson():
    data = request.get_json()
    handler.deletePersonByPersonId(
        data['personId']
    )
    return jsonify({"message": "Person deleted successfully"}), 200


@app.route("/addCollection", methods=["POST"])
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


@app.route("/getCollectionList", methods=["POST"])
def getCollectionList():
    data = request.get_json()
    return jsonify({
        "message": f"Collections of user [{data.get('userId')}]",
        "data": [collection for collection in handler.getCollectionListByUserId(data.get('userId'))]
    }), 200


@app.route("/getCollection", methods=["POST"])
def getCollection():
    data = request.get_json()
    collection = handler.getCollectionById(
        data['collectionId']
    )
    return jsonify({
        "message": f"Collection retrieved successfully",
        "data": collection
    }), 200


@app.route("/updateCollection", methods=["PUT"])
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


@app.route("/deleteCollection", methods=["DELETE"])
def deleteCollection():
    data = request.get_json()
    handler.deleteCollectionById(
        data['collectionId']
    )

    return jsonify({"message": "Collection deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


