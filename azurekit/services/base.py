from azure.common.client_factory import get_client_from_auth_file

class BaseService(object):

    def set_client(self, service):
        self.service = service
        self.client = get_client_from_auth_file(service)

    def __init__(self, service):
        self.set_client(service)
