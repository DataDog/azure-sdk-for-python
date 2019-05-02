# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationSetting(Model):
    """A configuration value.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar etag: Entity tag (etag) of the object
    :vartype etag: str
    :param key:
    :type key: str
    :param label:
    :type label: str
    :param content_type:
    :type content_type: str
    :param value:
    :type value: str
    :ivar last_modified:
    :vartype last_modified: datetime
    :ivar locked:
    :vartype locked: bool
    :param tags:
    :type tags: dict[str, str]
    """

    _validation = {
        'etag': {'readonly': True},
        'last_modified': {'readonly': True},
        'locked': {'readonly': True},
    }

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'content_type': {'key': 'content_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'last_modified': {'key': 'last_modified', 'type': 'iso-8601'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ConfigurationSetting, self).__init__(**kwargs)
        self.etag = None
        self.key = kwargs.get('key', None)
        self.label = kwargs.get('label', None)
        self.content_type = kwargs.get('content_type', None)
        self.value = kwargs.get('value', None)
        self.last_modified = None
        self.locked = None
        self.tags = kwargs.get('tags', None)


class HttpRequestError(Model):
    """HttpRequestError.
    """

    _attribute_map = {
    }


class Key(Model):
    """Key.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Key, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)


class Label(Model):
    """Label.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Label, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)