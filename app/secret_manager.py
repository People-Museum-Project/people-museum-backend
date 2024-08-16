from google.cloud import secretmanager_v1


class GCPSecretManager:
    def __init__(self):
        self.__client = secretmanager_v1.SecretManagerServiceClient()

    def access(self, resource_name):
        request = secretmanager_v1.AccessSecretVersionRequest(name=resource_name)
        response = self.__client.access_secret_version(request=request)
        return response.payload.data.decode()
