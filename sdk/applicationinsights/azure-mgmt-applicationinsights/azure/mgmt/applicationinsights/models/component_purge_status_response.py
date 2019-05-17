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


class ComponentPurgeStatusResponse(Model):
    """Response containing status for a specific purge operation.

    All required parameters must be populated in order to send to Azure.

    :param status: Required. Status of the operation represented by the
     requested Id. Possible values include: 'pending', 'completed'
    :type status: str or ~azure.mgmt.applicationinsights.models.PurgeState
    """

    _validation = {
        'status': {'required': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComponentPurgeStatusResponse, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)