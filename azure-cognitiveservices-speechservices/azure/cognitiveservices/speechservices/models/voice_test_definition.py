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


class VoiceTestDefinition(Model):
    """VoiceTestDefinition.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. Information about the text used in the voice test
    :type text: str
    :param model: Required. Information about the models used in the voice
     test
    :type model: ~azure.cognitiveservices.speechservices.models.ModelIdentity
    :param voice_test_kind: Required. The kind of this test (e.g. Text, SSML).
     Possible values include: 'None', 'Text', 'SSML'
    :type voice_test_kind: str or
     ~azure.cognitiveservices.speechservices.models.enum
    """

    _validation = {
        'text': {'required': True},
        'model': {'required': True},
        'voice_test_kind': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'model': {'key': 'model', 'type': 'ModelIdentity'},
        'voice_test_kind': {'key': 'voiceTestKind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VoiceTestDefinition, self).__init__(**kwargs)
        self.text = kwargs.get('text', None)
        self.model = kwargs.get('model', None)
        self.voice_test_kind = kwargs.get('voice_test_kind', None)
