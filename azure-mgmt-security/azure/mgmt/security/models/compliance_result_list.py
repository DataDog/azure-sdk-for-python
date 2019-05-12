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


class ComplianceResultList(Model):
    """List of compliance results response.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. List of compliance results
    :type value: list[~azure.mgmt.security.models.ComplianceResult]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ComplianceResult]'},
    }

    def __init__(self, **kwargs):
        super(ComplianceResultList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
