from azure.mgmt.compute.models import VirtualMachine


class Factory(object):

    def get_VirtualMachine(self):
        return VirtualMachine(location='UKsouth')

    def get_VirtualMachinePaged(self, count=10):
        return list(VirtualMachine(location='UKsouth') for x in range(count))
