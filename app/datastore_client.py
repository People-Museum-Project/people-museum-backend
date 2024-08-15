from google.cloud import datastore
import os


class Client:
    def __init__(self):
        # Set the path to service account key file
        self.__project_name = os.environ["PROJECT"]

    def connect(self):
        # Initialize the Datastore client
        client = datastore.Client(project=self.__project_name)
        return client
