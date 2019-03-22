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


class Transcription(Model):
    """Transcription.

    All required parameters must be populated in order to send to Azure.

    :param recordings_url: Required.
    :type recordings_url: str
    :param id: Required. The identifier of this entity
    :type id: str
    :param models_property: Required.
    :type models_property:
     list[~azure.cognitiveservices.speechservices.models.Model]
    :param locale: The locale of the contained data
    :type locale: str
    :param results_urls: The results Urls for the transcription
    :type results_urls: dict[str, str]
    :param status_message: The failure reason for the transcription
    :type status_message: str
    :param created_date_time: Required. The time-stamp when the object was
     created
    :type created_date_time: datetime
    :param last_action_date_time: Required. The time-stamp when the current
     status was entered
    :type last_action_date_time: datetime
    :param status: Required. The status of the object. Possible values
     include: 'Succeeded', 'NotStarted', 'Running', 'Failed'
    :type status: str or ~azure.cognitiveservices.speechservices.models.enum
    :param name: Required. The name of the object
    :type name: str
    :param description: The description of the object
    :type description: str
    :param properties: The custom properties of this entity
    :type properties: dict[str, str]
    """

    _validation = {
        'recordings_url': {'required': True},
        'id': {'required': True},
        'models_property': {'required': True},
        'created_date_time': {'required': True},
        'last_action_date_time': {'required': True},
        'status': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'recordings_url': {'key': 'recordingsUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'models_property': {'key': 'models', 'type': '[Model]'},
        'locale': {'key': 'locale', 'type': 'str'},
        'results_urls': {'key': 'resultsUrls', 'type': '{str}'},
        'status_message': {'key': 'statusMessage', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, *, recordings_url: str, id: str, models_property, created_date_time, last_action_date_time, status, name: str, locale: str=None, results_urls=None, status_message: str=None, description: str=None, properties=None, **kwargs) -> None:
        super(Transcription, self).__init__(**kwargs)
        self.recordings_url = recordings_url
        self.id = id
        self.models_property = models_property
        self.locale = locale
        self.results_urls = results_urls
        self.status_message = status_message
        self.created_date_time = created_date_time
        self.last_action_date_time = last_action_date_time
        self.status = status
        self.name = name
        self.description = description
        self.properties = properties
