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


class ConnectionMonitorQueryResult(Model):
    """List of connection states snaphots.

    :param states: Information about connection states.
    :type states:
     list[~azure.mgmt.network.v2017_11_01.models.ConnectionStateSnapshot]
    """

    _attribute_map = {
        'states': {'key': 'states', 'type': '[ConnectionStateSnapshot]'},
    }

    def __init__(self, **kwargs):
        super(ConnectionMonitorQueryResult, self).__init__(**kwargs)
        self.states = kwargs.get('states', None)