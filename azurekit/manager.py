from os import environ
from .services import *

class AzureManager(object):

    _compute = None

    @property
    def compute(self):
        if self._compute is None:
            self._compute = ComputeService()
        return self._compute
