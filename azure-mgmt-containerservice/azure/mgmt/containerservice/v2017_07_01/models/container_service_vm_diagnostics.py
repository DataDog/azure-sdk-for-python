# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerServiceVMDiagnostics(Model):
    """Profile for diagnostics on the container service VMs.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Whether the VM diagnostic agent is provisioned
     on the VM.
    :type enabled: bool
    :ivar storage_uri: The URI of the storage account where diagnostics are
     stored.
    :vartype storage_uri: str
    """

    _validation = {
        'enabled': {'required': True},
        'storage_uri': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'storage_uri': {'key': 'storageUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceVMDiagnostics, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.storage_uri = None