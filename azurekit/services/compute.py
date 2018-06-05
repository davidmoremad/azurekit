from azure.mgmt.compute import ComputeManagementClient
from .base import BaseService


class ComputeService(BaseService):

    def get_machines(self):
        return self.client.virtual_machines.list_all()

    def get_disks(self):
        return self.client.disks.list()

    def get_snapshots(self):
        return self.client.snapshots.list()

    def get_images(self):
        return self.client.images.list()


    def __init__(self):
        BaseService.__init__(self, ComputeManagementClient)
