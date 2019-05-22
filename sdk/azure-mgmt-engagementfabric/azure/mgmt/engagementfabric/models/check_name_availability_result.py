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


class CheckNameAvailabilityResult(Model):
    """The result of name availability check.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name_available: The name to be checked
    :vartype name_available: bool
    :ivar reason: The reason if name is unavailable. Possible values include:
     'Invalid', 'AlreadyExists'
    :vartype reason: str or
     ~azure.mgmt.engagementfabric.models.CheckNameUnavailableReason
    :ivar message: The message if name is unavailable
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = None
