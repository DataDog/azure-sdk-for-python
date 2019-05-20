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


class AzureSku(Model):
    """Azure SKU definition.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. SKU name. Possible values include:
     'Standard_DS13_v2+1TB_PS', 'Standard_DS13_v2+2TB_PS',
     'Standard_DS14_v2+3TB_PS', 'Standard_DS14_v2+4TB_PS', 'Standard_D13_v2',
     'Standard_D14_v2', 'Standard_L8s', 'Standard_L16s', 'Standard_D11_v2',
     'Standard_D12_v2', 'Standard_L4s', 'Dev(No SLA)_Standard_D11_v2'
    :type name: str or ~azure.mgmt.kusto.models.AzureSkuName
    :param capacity: SKU capacity.
    :type capacity: int
    :param tier: Required. SKU tier. Possible values include: 'Basic',
     'Standard'
    :type tier: str or ~azure.mgmt.kusto.models.AzureSkuTier
    """

    _validation = {
        'name': {'required': True},
        'tier': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name, tier, capacity: int=None, **kwargs) -> None:
        super(AzureSku, self).__init__(**kwargs)
        self.name = name
        self.capacity = capacity
        self.tier = tier
