from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient

compute_client = get_client_from_cli_profile(ComputeManagementClient)

for vm in compute_client.virtual_machines.list_all():
            print("\tVM: {}".format(vm.name))


