
from google.cloud import datastore

from datastore_client import Client


# UID will auto POST without detected by users


"""

Person

userId, name, image, description, context, public/private

User
userId, name, image, description, favourite

Collection
userId, name, image, description, public/private

"""


class Handler:
    def __init__(self):
        self.__client = Client().connect()
        self.__collection = "Collection"
        self.__user = "User"
        self.__person = "Person"

    def addUser(self, name, imageLink, description="", favourite=None):
        key = self.__client.key(self.__user)
        user = datastore.Entity(key=key)
        user['name'] = name
        user['imageLink'] = imageLink
        user['description'] = description
        user['favourite'] = favourite
        self.__client.put(user)

    def getUserByUserId(self, userId):
        key = self.__client.key(self.__user, int(userId))
        user = self.__client.get(key)
        return user

    def getAllUsers(self):
        query = self.__client.query(kind=self.__user)
        users = list(query.fetch())
        return users

    def updateUserByUserId(self, userId, newName, newImageLink, newDescription):
        user = self.getUserByUserId(userId)
        # user not exist, update failed
        if not user:
            return False
        if newName:
            user['name'] = newName
        if newImageLink:
            user['imageLink'] = newImageLink
        if newDescription:
            user['description'] = newDescription
        self.__client.put(user)
        return True

    def deleteUserByUserId(self, userId):
        user = self.getUserByUserId(userId)
        # user not exist, already deleted
        if not user:
            return True
        self.__client.delete(user)
        return True

    def addPerson(self, name, imageLink, description, context, public=0):
        # userId, name, image, description, context, public/private
        key = self.__client.key(self.__person)
        person = datastore.Entity(key=key)
        person['name'] = name
        person['imageLink'] = imageLink
        person['description'] = description
        person['context'] = context
        person['public'] = public
        self.__client.put(person)

    def getPersonListByUserId(self, userId):
        query = self.__client.query(kind=self.__person)
        query.add_filter('id', '=', userId)
        for person in query.fetch():
            yield person

    # TODO: authorization to be added
    def getPersonByPersonId(self, personId):
        key = self.__client.key(self.__person, int(personId))
        person = self.__client.get(key)
        return person

    def updatePersonByPersonId(self, personId, newName, newImageLink, newDescription, newContext, newPublic):
        person = self.getPersonByPersonId(personId)
        # person not found, update failed
        if not person:
            return False
        if newName:
            person['name'] = newName
        if newImageLink:
            person['imageLink'] = newImageLink
        if newDescription:
            person['description'] = newDescription
        if newContext:
            person['context'] = newContext
        if newPublic:
            person['public'] = newPublic
        self.__client.put(person)
        return True

    def deletePersonByPersonId(self, personId):
        person = self.getPersonByPersonId(personId)
        if not person:
            return True
        self.__client.delete(person)
        return True

    def addCollection(self, userId, name, imageLink, description, isPublic):
        # add a new collection to current user's collection list
        # A Key in Datastore uniquely identifies an entity within a given namespace and kind
        key = self.__client.key(self.__collection)
        collection = datastore.Entity(key=key)
        collection['userId'] = userId
        collection['name'] = name
        collection['imageLink'] = imageLink
        collection['description'] = description
        collection['isPublic'] = isPublic
        self.__client.put(collection)

    def getCollectionListByUserId(self, userId):
        query = self.__client.query(kind=self.__collection)
        query.add_filter('userId', "=", userId)
        for collection in query.fetch():
            yield collection

    def getCollectionById(self, collectionId):
        key = self.__client.key(self.__collection, int(collectionId))
        collection = self.__client.get(key)
        return collection

    def updateCollectionById(self, collectionId, newName, newImageLink, newDescription, newIsPublic):
        collection = self.getCollectionById(int(collectionId))
        # collection not found
        if not collection:
            return False
        # userId, name, image, description, public/private
        if newName:
            collection['name'] = newName
        if newImageLink:
            collection['imageLink'] = newImageLink
        if newDescription:
            collection['description'] = newDescription
        if newIsPublic:
            collection['isPublic'] = newIsPublic
        self.__client.put(collection)
        return True

    def deleteCollectionById(self, collectionId):
        collection = self.getCollectionById(int(collectionId))
        if not collection:
            return True
        self.__client.delete(collection)
        return True




