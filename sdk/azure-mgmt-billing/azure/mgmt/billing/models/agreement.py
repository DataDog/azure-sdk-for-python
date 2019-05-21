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

from .resource import Resource


class Agreement(Resource):
    """An agreement resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar agreement_link: The link to the agreement.
    :vartype agreement_link: str
    :ivar effective_date: Effective date.
    :vartype effective_date: datetime
    :ivar expiration_date: Expiration date.
    :vartype expiration_date: datetime
    :param participants: Participants or signer of the agreement.
    :type participants: list[~azure.mgmt.billing.models.Participants]
    :ivar status: The agreement status
    :vartype status: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'agreement_link': {'readonly': True},
        'effective_date': {'readonly': True},
        'expiration_date': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'agreement_link': {'key': 'properties.agreementLink', 'type': 'str'},
        'effective_date': {'key': 'properties.effectiveDate', 'type': 'iso-8601'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'participants': {'key': 'properties.participants', 'type': '[Participants]'},
        'status': {'key': 'properties.status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Agreement, self).__init__(**kwargs)
        self.agreement_link = None
        self.effective_date = None
        self.expiration_date = None
        self.participants = kwargs.get('participants', None)
        self.status = None
