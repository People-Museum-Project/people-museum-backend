from google.cloud import datastore

from settings import PROJECT


class Client:
    def __init__(self):
        self.__project_name = PROJECT

    def connect(self):
        # Initialize the Datastore client
        client = datastore.Client(project=self.__project_name)
        return client
