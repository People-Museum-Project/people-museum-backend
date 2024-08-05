import time
from google.cloud import datastore
from app.datastore_client import Client
from app.USFGenAI_OOP import GenAILab


class Handler:
    def __init__(self):
        """
        Initializes the Handler with a Datastore client, collection names, and timezone offset.
        """
        self.__client = Client().connect()
        self.__collection = "Collection"
        self.__user = "User"
        self.__person = "Person"
        self.__PST_OFFSET = -7 * 60 * 60  # PST offset in seconds

    def addUser(self, name, imageLink, googleUserId, gmail, description="", favourite=None):
        """
        Adds a new user to the datastore if the user does not already exist.

        Args:
            - name (str): The user's name.
            - imageLink (str): The URL of the user's image.
            - googleUserId (str): The Google user ID.
            - gmail (str): The user's Gmail address.
            - description (str, optional): A description of the user (default: "").
            - favourite (str, optional): A favourite item or feature (default: None).

        Returns:
            - bool: True if the user was added successfully, False if the user already exists.
        """
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
        """
        Retrieves user(s) by their Google user ID.

        Args:
            - googleUserId (str): The Google user ID to search for.

        Returns:
            - list: A list of user entities with their IDs included.
        """
        query = self.__client.query(kind=self.__user)
        query.add_filter('googleUserId', '=', googleUserId)
        users = list(query.fetch())
        for user in users:
            user['id'] = user.key.id_or_name
        return users

    def getAllUsers(self):
        """
        Retrieves all users from the datastore.

        Returns:
            - list: A list of all user entities with their IDs included.
        """
        query = self.__client.query(kind=self.__user)
        users = list(query.fetch())
        for user in users:
            user['id'] = user.key.id_or_name
        return users

    def updateUserByUserId(self, userId, newName, newImageLink, newDescription):
        """
        Updates user details by user ID.

        Args:
            - userId (str): The user ID to update.
            - newName (str, optional): The new name for the user.
            - newImageLink (str, optional): The new image link for the user.
            - newDescription (str, optional): The new description for the user.

        Returns:
            - bool: True if the update was successful, False if the user does not exist.
        """
        user = self.getUserByUserId(userId)
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
        """
        Deletes a user by user ID.

        Args:
            - userId (str): The user ID to delete.

        Returns:
            - bool: True if the deletion was successful or if the user did not exist.
        """
        user = self.getUserByUserId(userId)
        if not user:
            return True
        self.__client.delete(user)
        return True

    def addPerson(self, name, imageLink, description, userId, public=0, assistantId=None):
        """
        Adds a new person to the datastore.

        Args:
            - name (str): The person's name.
            - imageLink (str): The URL of the person's image.
            - description (str): A description of the person.
            - userId (str): The ID of the user who added the person.
            - public (int, optional): Whether the person is public (default: 0).
            - assistantId (str, optional): The ID of the associated assistant (default: None).
        """
        key = self.__client.key(self.__person)
        person = datastore.Entity(key=key)
        person['name'] = name
        person['imageLink'] = imageLink
        person['description'] = description
        person['userId'] = userId
        person['public'] = public
        person['assistantId'] = assistantId
        person['date'] = int(time.time()) + self.__PST_OFFSET
        self.__client.put(person)

    def getPersonListByUserId(self, userId, page, limit, sortBy='name', ascending=True):
        """
        Retrieves a paginated list of persons added by a specific user.

        Args:
            - userId (str): The user ID to filter by.
            - page (int): The page number for pagination.
            - limit (int): The number of items per page.
            - sortBy (str, optional): The field to sort by (default: 'name').
            - ascending (bool, optional): Whether to sort in ascending order (default: True).

        Returns:
            - list: A paginated list of person entities with their IDs included.
        """
        query = self.__client.query(kind=self.__person)
        query.add_filter('userId', '=', userId)
        query.order = sortBy if ascending else ['-' + sortBy]
        persons = list(query.fetch(limit=limit, offset=(page - 1) * limit))
        for person in persons:
            person['id'] = person.key.id_or_name
        return persons

    def __getPersonKeysByCollectionId(self, collectionId):
        """
        Retrieves person IDs associated with a specific collection.

        Args:
            - collectionId (str): The collection ID to filter by.

        Returns:
            - list: A list of person IDs associated with the collection.
        """
        query = self.__client.query(kind='PersonCollection')
        query.add_filter('collectionId', '=', collectionId)
        results = query.fetch()
        return [entity['personId'] for entity in results]

    def getPersonListByCollectionId(self, collectionId, page, limit, sortBy="name", ascending=True):
        """
        Retrieves a paginated list of persons in a specific collection.

        Args:
            - collectionId (str): The collection ID to filter by.
            - page (int): The page number for pagination.
            - limit (int): The number of items per page.
            - sortBy (str, optional): The field to sort by (default: 'name').
            - ascending (bool, optional): Whether to sort in ascending order (default: True).

        Returns:
            - list: A paginated list of person entities with their IDs included.
        """
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

    def getPersonByPersonId(self, personId):
        """
        Retrieves a specific person by their person ID.

        Args:
            - personId (str): The person ID to retrieve.

        Returns:
            - dict: The person entity or None if not found.
        """
        key = self.__client.key(self.__person, int(personId))
        person = self.__client.get(key)
        return person

    def updatePersonByPersonId(self, personId, newName, newImageLink, newDescription, newContext, newPublic):
        """
        Updates a person's details by their person ID.

        Args:
            - personId (str): The person ID to update.
            - newName (str, optional): The new name for the person.
            - newImageLink (str, optional): The new image link for the person.
            - newDescription (str, optional): The new description for the person.
            - newContext (str, optional): The new context for the person.
            - newPublic (int, optional): Whether the person is public (default: None).

        Returns:
            - bool: True if the update was successful, False if the person was not found.
        """
        person = self.getPersonByPersonId(personId)
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
        """
        Deletes a person by their person ID.

        Args:
            - personId (str): The person ID to delete.

        Returns:
            - bool: True if the deletion was successful or if the person did not exist.
        """
        person = self.getPersonByPersonId(personId)
        if not person:
            return True
        self.__client.delete(person)
        return True

    def addCollection(self, userId, name, imageLink, description, isPublic):
        """
        Adds a new collection to the datastore.

        Args:
            - userId (str): The user ID who is adding the collection.
            - name (str): The name of the collection.
            - imageLink (str): The URL of the collection's image.
            - description (str): A description of the collection.
            - isPublic (int): Whether the collection is public (1) or private (0).
        """
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
        """
        Retrieves a paginated list of collections owned by a specific user.

        Args:
            - userId (str): The user ID to filter by.
            - page (int): The page number for pagination.
            - limit (int): The number of items per page.
            - sortBy (str, optional): The field to sort by (default: 'name').
            - ascending (bool, optional): Whether to sort in ascending order (default: True).

        Returns:
            - generator: A generator yielding collection entities.
        """
        query = self.__client.query(kind=self.__collection)
        query.order = sortBy if ascending else ['-' + sortBy]
        query.add_filter('userId', "=", userId)
        for collection in query.fetch(limit=limit, offset=(page - 1) * limit):
            yield collection

    def getCollectionById(self, collectionId):
        """
        Retrieves a specific collection by its collection ID.

        Args:
            - collectionId (str): The collection ID to retrieve.

        Returns:
            - dict: The collection entity or None if not found.
        """
        key = self.__client.key(self.__collection, int(collectionId))
        collection = self.__client.get(key)
        return collection

    def __getCollectionKeysByPersonId(self, personId):
        """
        Retrieves collection IDs associated with a specific person.

        Args:
            - personId (str): The person ID to filter by.

        Returns:
            - list: A list of collection IDs associated with the person.
        """
        query = self.__client.query(kind="PersonCollection")
        query.add_filter('personId', '=', personId)
        results = query.fetch()
        return [entity['collectionId'] for entity in results]

    def getCollectionListByPersonId(self, personId, page, limit, sortBy="name", ascending=True):
        """
        Retrieves a paginated list of collections associated with a specific person.

        Args:
            - personId (str): The person ID to filter by.
            - page (int): The page number for pagination.
            - limit (int): The number of items per page.
            - sortBy (str, optional): The field to sort by (default: 'name').
            - ascending (bool, optional): Whether to sort in ascending order (default: True).

        Returns:
            - list: A paginated list of collection entities with their IDs included.
        """
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
        """
        Updates a collection's details by its collection ID.

        Args:
            - collectionId (str): The collection ID to update.
            - newName (str, optional): The new name for the collection.
            - newImageLink (str, optional): The new image link for the collection.
            - newDescription (str, optional): The new description for the collection.
            - newIsPublic (int, optional): Whether the collection is public (1) or private (0).

        Returns:
            - bool: True if the update was successful, False if the collection was not found.
        """
        collection = self.getCollectionById(int(collectionId))
        if not collection:
            return False
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
        """
        Deletes a collection by its collection ID.

        Args:
            - collectionId (str): The collection ID to delete.

        Returns:
            - bool: True if the deletion was successful or if the collection did not exist.
        """
        collection = self.getCollectionById(int(collectionId))
        if not collection:
            return True
        self.__client.delete(collection)
        return True

    def addPersonCollection(self, personId, collectionId):
        """
        Adds a person to a collection.

        Args:
            - personId (str): The person ID to add.
            - collectionId (str): The collection ID to add the person to.

        Returns:
            - bool: True if the person was added successfully, False if the person is already in the collection.
        """
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
            return True
        return False

    def deletePersonFromCollection(self, personId, collectionId):
        """
        Removes a person from a collection.

        Args:
            - personId (str): The person ID to remove.
            - collectionId (str): The collection ID to remove the person from.

        Returns:
            - bool: True if the person was removed successfully.
        """
        query = self.__client.query(kind='PersonCollection')
        query.add_filter('personId', '=', personId)
        query.add_filter('collectionId', '=', collectionId)
        results = list(query.fetch())
        for entity in results:
            self.__client.delete(entity.key)
        return True

    def countEntities(self, kind, key=None, value=None):
        """
        Counts the number of entities in a specific kind with an optional filter.

        Args:
            - kind (str): The kind of entities to count.
            - key (str, optional): The key to filter by.
            - value (str, optional): The value to filter by.

        Returns:
            - int: The count of entities matching the filter.
        """
        query = self.__client.query(kind=kind)
        if key:
            query.add_filter(key, "=", value)
        count = len(list(query.fetch()))
        return count

    def createAssistant(self, name, instruction):
        """
        Creates a new AI assistant with the given name and instruction.

        Args:
            - name (str): The name of the assistant.
            - instruction (str): The instruction for the assistant.

        Returns:
            - str: The ID of the created assistant.
        """
        genAiLab = GenAILab()
        assistant = genAiLab.create_assistant(name, instruction)
        return assistant.id
