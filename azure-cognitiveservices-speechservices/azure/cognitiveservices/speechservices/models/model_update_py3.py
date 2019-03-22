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


class ModelUpdate(Model):
    """ModelUpdate.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the object
    :type name: str
    :param description: The description of the object
    :type description: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, name: str, description: str=None, **kwargs) -> None:
        super(ModelUpdate, self).__init__(**kwargs)
        self.name = name
        self.description = description
