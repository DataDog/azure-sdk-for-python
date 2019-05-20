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


class ExportExecutionListResult(Model):
    """Result of listing exports execution history of a export by name.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: The list of export executions.
    :vartype value: list[~azure.mgmt.costmanagement.models.ExportExecution]
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ExportExecution]'},
    }

    def __init__(self, **kwargs) -> None:
        super(ExportExecutionListResult, self).__init__(**kwargs)
        self.value = None
