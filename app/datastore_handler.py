import time

from google.cloud import datastore

from app.datastore_client import Client


class Handler:
    def __init__(self):
        self.__client = Client().connect()
        self.__collection = "Collection"
        self.__user = "User"
        self.__person = "Person"
        self.__PST_OFFSET = -7 * 60 * 60

    def addUser(self, name, imageLink, googleUserId, gmail, description="", favourite=None):
        # check existence
        user = self.getUserByUserId(googleUserId)
        if user:
            return False

        key = self.__client.key(self.__user)
        user = datastore.Entity(key=key)
        user['name'] = name
        user['imageLink'] = imageLink
        user['description'] = description
        user['favourite'] = favourite
        user['googleUserId'] = googleUserId
        user['gmail'] = gmail
        self.__client.put(user)
        return True

    def getUserByUserId(self, googleUserId):
        query = self.__client.query(kind=self.__user)
        query.add_filter('googleUserId', '=', googleUserId)
        users = list(query.fetch())
        for user in users:
            user['id'] = user.key.id_or_name
        return users

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

    def addPerson(self, name, imageLink, description, context, userId, public=0):
        key = self.__client.key(self.__person)
        person = datastore.Entity(key=key)
        person['name'] = name
        person['imageLink'] = imageLink
        person['description'] = description
        person['context'] = context
        person['userId'] = userId
        person['public'] = public
        person['date'] = int(time.time()) + self.__PST_OFFSET
        self.__client.put(person)

    def getPersonListByUserId(self, userId, page, limit, sortBy='name', ascending=True):
        query = self.__client.query(kind=self.__person)

        query.add_filter('userId', '=', userId)

        query.order = sortBy if ascending else ['-' + sortBy]

        persons = list(query.fetch(limit=limit, offset=(page - 1) * limit))

        # add ID into person
        for person in persons:
            person['id'] = person.key.id_or_name
        return persons

    def __getPersonKeysByCollectionId(self, collectionId):
        query = self.__client.query(kind='PersonCollection')
        query.add_filter('collectionId', '=', collectionId)
        results = query.fetch()
        return [entity['personId'] for entity in results]

    def getPersonListByCollectionId(self, collectionId, page, limit, sortBy="name", ascending=True):
        personIds = self.__getPersonKeysByCollectionId(collectionId)

        keys = [self.__client.key('Person', personId) for personId in personIds]

        persons = self.__client.get_multi(keys)

        sorted_persons = sorted(persons, key=lambda x: x[sortBy], reverse=not ascending)

        start = (page - 1) * limit
        end = start + limit
        paginated_persons = sorted_persons[start:end]

        persons_list = list(paginated_persons)
        for person in persons_list:
            person['id'] = person.key.id_or_name
        return persons_list

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
        collection['date'] = int(time.time()) + self.__PST_OFFSET
        collection['isPublic'] = isPublic
        self.__client.put(collection)

    def getCollectionListByUserId(self, userId, page, limit, sortBy='name', ascending=True):
        query = self.__client.query(kind=self.__collection)

        query.order = sortBy if ascending else ['-' + sortBy]

        query.add_filter('userId', "=", userId)
        for collection in query.fetch(limit=limit, offset=(page - 1) * limit):
            yield collection

    def getCollectionById(self, collectionId):
        key = self.__client.key(self.__collection, int(collectionId))
        collection = self.__client.get(key)
        return collection

    def __getCollectionKeysByPersonId(self, personId):
        query = self.__client.query(kind="PersonCollection")
        query.add_filter('personId', '=', personId)
        results = query.fetch()
        return [entity['collectionId'] for entity in results]

    def getCollectionListByPersonId(self, personId, page, limit, sortBy="name", ascending=True):
        collectionIds = self.__getCollectionKeysByPersonId(personId)
        keys = [self.__client.key('Collection', collectionId) for collectionId in collectionIds]
        collections = self.__client.get_multi(keys)
        sorted_collections = sorted(collections, key=lambda x: x[sortBy], reverse=not ascending)

        start = (page - 1) * limit
        end = start + limit
        paginated_collections = sorted_collections[start:end]
        collection_list = list(paginated_collections)
        for collection in collection_list:
            collection['id'] = collection.key.id_or_name
        return collection_list

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
        query = self.__client.query(kind='PersonCollection')

        unique_key = f"{personId}_{collectionId}"
        query.add_filter('unique', '=', unique_key)
        existing_entities = list(query.fetch())

        if not existing_entities:
            personCollectionKey = self.__client.key('PersonCollection')
            personCollection = datastore.Entity(key=personCollectionKey)
            personCollection.update({
                "personId": personId,
                "collectionId": collectionId,
                "unique": unique_key
            })
            self.__client.put(personCollection)
            # log: succeed
            return True
        else:
            # log: already existed
            return False

    def deletePersonFromCollection(self, personId, collectionId):
        query = self.__client.query(kind='PersonCollection')
        query.add_filter('personId', '=', personId)
        query.add_filter('collectionId', '=', collectionId)
        results = list(query.fetch())
        for entity in results:
            self.__client.delete(entity.key)
        return True

    def countEntities(self, kind, filter=None):
        query = self.__client.query(kind=kind)
        if filter:
            key, value = filter
            query.add_filter(key, "=", value)
            pass
        count = len(list(query.fetch()))
        return count