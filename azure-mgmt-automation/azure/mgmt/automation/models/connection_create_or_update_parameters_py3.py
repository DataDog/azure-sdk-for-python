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


class ConnectionCreateOrUpdateParameters(Model):
    """The parameters supplied to the create or update connection operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or sets the name of the connection.
    :type name: str
    :param description: Gets or sets the description of the connection.
    :type description: str
    :param connection_type: Required. Gets or sets the connectionType of the
     connection.
    :type connection_type:
     ~azure.mgmt.automation.models.ConnectionTypeAssociationProperty
    :param field_definition_values: Gets or sets the field definition
     properties of the connection.
    :type field_definition_values: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'connection_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'connection_type': {'key': 'properties.connectionType', 'type': 'ConnectionTypeAssociationProperty'},
        'field_definition_values': {'key': 'properties.fieldDefinitionValues', 'type': '{str}'},
    }

    def __init__(self, *, name: str, connection_type, description: str=None, field_definition_values=None, **kwargs) -> None:
        super(ConnectionCreateOrUpdateParameters, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.connection_type = connection_type
        self.field_definition_values = field_definition_values