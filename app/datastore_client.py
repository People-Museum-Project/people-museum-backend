from google.cloud import datastore
import os


class Client:
    #  "/Users/single/workspaces/people-museum-backend/peoplemuseumyeah-b85c3138781f.json"
    #  peoplemuseumyeah
    def __init__(self):
        # Set the path to service account key file
        self.__project_name = os.environ["PROJECT"]

    def connect(self):
        # Initialize the Datastore client
        client = datastore.Client(project=self.__project_name)
        return client
