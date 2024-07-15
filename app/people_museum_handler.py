
from google.cloud import datastore

from app.people_museum_client import Client


# UID will auto POST without detected by users


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

        for user in users:
            user['id'] = user.key.id_or_name
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

    def addPerson(self, name, imageLink, description, context, userId, collectionId=None, public=0):
        # userId, name, image, description, context, public/private
        key = self.__client.key(self.__person)
        person = datastore.Entity(key=key)
        person['name'] = name
        person['imageLink'] = imageLink
        person['description'] = description
        person['context'] = context
        person['userId'] = userId
        person['public'] = public
        self.__client.put(person)

    def getPersonListByUserId(self, userId, sortBy, order, page, limit):
        query = self.__client.query(kind=self.__person)
        query.add_filter('userId', '=', userId)

        if order == 'asc':
            query.order = sortBy
        else:
            query.order = ['-' + sortBy]

        for person in query.fetch(limit=limit, offset=(page - 1) * limit):
            yield person


    def getPersonKeysByCollectionId(self, collectionId):
        query = self.__client.query(kind='PersonCollection')
        query.add_filter('collectionId', '=', collectionId)
        results = query.fetch()
        return [entity['personId'] for entity in results]

    def getPersonListByCollectionId(self, collectionId, page, limit, sortBy="name", ascending=True):
        personIds = self.getPersonKeysByCollectionId(collectionId)

        keys = [self.__client.key('Person', personId) for personId in personIds]

        persons = self.__client.get_multi(keys)

        sorted_persons = sorted(persons, key=lambda x: x[sortBy], reverse=not ascending)

        start = (page - 1) * limit
        end = start + limit
        paginated_persons = sorted_persons[start:end]

        for person in paginated_persons:
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

    def getCollectionListByUserId(self, userId, sortBy, order, page, limit):
        query = self.__client.query(kind=self.__collection)

        if order == 'asc':
            query.order = sortBy
        else:
            query.order = ['-' + sortBy]

        query.add_filter('userId', "=", userId)
        for collection in query.fetch(limit=limit, offset=(page - 1) * limit):
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

    def addPersonCollection(self, personId, collectionId):
        personCollectionKey = self.__client.key('PersonCollection')
        personCollection = datastore.Entity(key=personCollectionKey)
        personCollection.update({
            "personId": personId,
            "collectionId": collectionId
        })
        self.__client.put(personCollection)
        return True


