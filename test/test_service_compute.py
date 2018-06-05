import mock
import pytest
from pytest_mock import mocker

import azurekit

from .factory import Factory


class TestServiceCompute():

    @pytest.fixture
    def client(self):
        '''Return a AzureKit client'''
        return azurekit.AzureManager().compute


    def test_get_instances(self, client, mocker):
        vms = Factory().get_VirtualMachinePaged(count=13)
        mocker.patch.object(client, 'get_machines', return_value=vms)

        instances = client.get_instances()
        assert len(instances) == 13
