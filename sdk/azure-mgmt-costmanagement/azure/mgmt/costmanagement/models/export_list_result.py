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


class ExportListResult(Model):
    """Result of listing exports. It contains a list of available exports in the
    scope provided.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The list of exports.
    :vartype value: list[~azure.mgmt.costmanagement.models.Export]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Export]'},
    }

    def __init__(self, **kwargs):
        super(ExportListResult, self).__init__(**kwargs)
        self.value = None
