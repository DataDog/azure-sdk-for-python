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


class HeaderActionParameters(Model):
    """Defines the parameters for the request header action.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar odatatype: Required.  Default value:
     "#Microsoft.Azure.Cdn.Models.DeliveryRuleHeaderActionParameters" .
    :vartype odatatype: str
    :param header_action: Required. Action to perform. Possible values
     include: 'Append', 'Overwrite', 'Delete'
    :type header_action: str or ~azure.mgmt.cdn.models.HeaderAction
    :param header_name: Required. Name of the header to modify
    :type header_name: str
    :param value: Value for the specified action
    :type value: str
    """

    _validation = {
        'odatatype': {'required': True, 'constant': True},
        'header_action': {'required': True},
        'header_name': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'header_action': {'key': 'headerAction', 'type': 'str'},
        'header_name': {'key': 'headerName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    odatatype = "#Microsoft.Azure.Cdn.Models.DeliveryRuleHeaderActionParameters"

    def __init__(self, **kwargs):
        super(HeaderActionParameters, self).__init__(**kwargs)
        self.header_action = kwargs.get('header_action', None)
        self.header_name = kwargs.get('header_name', None)
        self.value = kwargs.get('value', None)
