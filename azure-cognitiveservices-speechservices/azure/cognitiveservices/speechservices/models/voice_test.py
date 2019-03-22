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


class VoiceTest(Model):
    """VoiceTest.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The identifier of this entity
    :type id: str
    :param audio_uri: The audio URI of the voice test
    :type audio_uri: str
    :param text_uri: Required. The text URI of the voice test
    :type text_uri: str
    :param created_date_time: Required. The time-stamp when the object was
     created
    :type created_date_time: datetime
    :param last_action_date_time: Required. The time-stamp when the current
     status was entered
    :type last_action_date_time: datetime
    :param status: Required. The status of the object. Possible values
     include: 'Succeeded', 'NotStarted', 'Running', 'Failed'
    :type status: str or ~azure.cognitiveservices.speechservices.models.enum
    :param model: Required. Information about the models used in the voice
     test
    :type model: ~azure.cognitiveservices.speechservices.models.Model
    :param voice_test_kind: Required. The kind of this test (e.g. Text, SSML).
     Possible values include: 'None', 'Text', 'SSML'
    :type voice_test_kind: str or
     ~azure.cognitiveservices.speechservices.models.enum
    """

    _validation = {
        'id': {'required': True},
        'text_uri': {'required': True},
        'created_date_time': {'required': True},
        'last_action_date_time': {'required': True},
        'status': {'required': True},
        'model': {'required': True},
        'voice_test_kind': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'audio_uri': {'key': 'audioUri', 'type': 'str'},
        'text_uri': {'key': 'textUri', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'model': {'key': 'model', 'type': 'Model'},
        'voice_test_kind': {'key': 'voiceTestKind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VoiceTest, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.audio_uri = kwargs.get('audio_uri', None)
        self.text_uri = kwargs.get('text_uri', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.last_action_date_time = kwargs.get('last_action_date_time', None)
        self.status = kwargs.get('status', None)
        self.model = kwargs.get('model', None)
        self.voice_test_kind = kwargs.get('voice_test_kind', None)
