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


class ResourceDetails(Model):
    """Details of the resource that was assessed.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureResourceDetails

    All required parameters must be populated in order to send to Azure.

    :param assessed_resource_source: Required. Constant filled by server.
    :type assessed_resource_source: str
    """

    _validation = {
        'assessed_resource_source': {'required': True},
    }

    _attribute_map = {
        'assessed_resource_source': {'key': 'assessedResourceSource', 'type': 'str'},
    }

    _subtype_map = {
        'assessed_resource_source': {'Azure': 'AzureResourceDetails'}
    }

    def __init__(self, **kwargs):
        super(ResourceDetails, self).__init__(**kwargs)
        self.assessed_resource_source = None
