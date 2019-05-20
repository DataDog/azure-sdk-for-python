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


class ResourceOperation(Model):
    """Individual resource operation information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param resource_name: Name of the resource as specified in the artifacts.
     For ARM resources, this is the name of the resource specified in the
     template.
    :type resource_name: str
    :ivar operation_id: Unique identifier of the operation. For ARM resources,
     this is the operationId obtained from ARM service.
    :vartype operation_id: str
    :param resource_type: Type of the resource as specified in the artifacts.
     For ARM resources, this is the type of the resource specified in the
     template.
    :type resource_type: str
    :ivar provisioning_state: State of the resource deployment. For ARM
     resources, this is the current provisioning state of the resource.
    :vartype provisioning_state: str
    :ivar status_message: Descriptive information of the resource operation.
    :vartype status_message: str
    :ivar status_code: Http status code of the operation.
    :vartype status_code: str
    """

    _validation = {
        'operation_id': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'status_message': {'readonly': True},
        'status_code': {'readonly': True},
    }

    _attribute_map = {
        'resource_name': {'key': 'resourceName', 'type': 'str'},
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'status_code': {'key': 'statusCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceOperation, self).__init__(**kwargs)
        self.resource_name = kwargs.get('resource_name', None)
        self.operation_id = None
        self.resource_type = kwargs.get('resource_type', None)
        self.provisioning_state = None
        self.status_message = None
        self.status_code = None
