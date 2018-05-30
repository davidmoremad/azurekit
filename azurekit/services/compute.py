from azure.mgmt.compute import ComputeManagementClient
from .base import BaseService


class ComputeService(BaseService):

    def get_instances(self):
        return self.client.virtual_machines.list_all()


    def __init__(self):
        BaseService.__init__(self, ComputeManagementClient)
