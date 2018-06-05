from os import environ
import sys
from azure.common.client_factory import get_client_from_auth_file

class BaseService(object):

    def set_client(self, service):
                
        self.service = service
        try:
            self.client = get_client_from_auth_file(service)
        except (FileNotFoundError, KeyError):
            print ('[!] Credentials file not found. Set path in "AZURE_AUTH_LOCATION" environment variable')
            sys.exit(0)

    def __init__(self, service):
        self.set_client(service)
