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


class CassandraKeyspaceResource(Model):
    """Cosmos DB Cassandra keyspace id object.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Name of the Cosmos DB Cassandra keyspace
    :type id: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str, **kwargs) -> None:
        super(CassandraKeyspaceResource, self).__init__(**kwargs)
        self.id = id
