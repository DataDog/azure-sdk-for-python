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


class StepProperties(Model):
    """The properties of a step resource.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: WaitStepProperties

    All required parameters must be populated in order to send to Azure.

    :param step_type: Required. Constant filled by server.
    :type step_type: str
    """

    _validation = {
        'step_type': {'required': True},
    }

    _attribute_map = {
        'step_type': {'key': 'stepType', 'type': 'str'},
    }

    _subtype_map = {
        'step_type': {'Wait': 'WaitStepProperties'}
    }

    def __init__(self, **kwargs):
        super(StepProperties, self).__init__(**kwargs)
        self.step_type = None
