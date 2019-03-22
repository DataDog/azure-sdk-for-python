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


class InnerError(Model):
    """InnerError.

    An implementation of this interface represents a stage in a stack trace.
    If the error level is the root, the
    {Microsoft.SpeechServices.Common.Client.IInnerError.Code} and the
    {Microsoft.SpeechServices.Common.Client.IInnerError.InnerError}
    property may be omitted.

    :param code: A service-defined error code that should be human-readable.
     This code serves as a more specific indicator of the error than
     the HTTP error code specified in the response
    :type code: str
    :param innererror: A human-readable representation of the error. It is
     intended as
     an aid to developers and is not suitable for exposure to end users
    :type innererror:
     ~azure.cognitiveservices.speechservices.models.InnerError
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
    }

    def __init__(self, *, code: str=None, innererror=None, **kwargs) -> None:
        super(InnerError, self).__init__(**kwargs)
        self.code = code
        self.innererror = innererror
