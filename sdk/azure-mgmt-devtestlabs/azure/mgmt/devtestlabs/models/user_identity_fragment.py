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


class UserIdentityFragment(Model):
    """Identity attributes of a lab user.

    :param principal_name: Set to the principal name / UPN of the client JWT
     making the request.
    :type principal_name: str
    :param principal_id: Set to the principal Id of the client JWT making the
     request. Service principal will not have the principal Id.
    :type principal_id: str
    :param tenant_id: Set to the tenant ID of the client JWT making the
     request.
    :type tenant_id: str
    :param object_id: Set to the object Id of the client JWT making the
     request. Not all users have object Id. For CSP (reseller) scenarios for
     example, object Id is not available.
    :type object_id: str
    :param app_id: Set to the app Id of the client JWT making the request.
    :type app_id: str
    """

    _attribute_map = {
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'app_id': {'key': 'appId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UserIdentityFragment, self).__init__(**kwargs)
        self.principal_name = kwargs.get('principal_name', None)
        self.principal_id = kwargs.get('principal_id', None)
        self.tenant_id = kwargs.get('tenant_id', None)
        self.object_id = kwargs.get('object_id', None)
        self.app_id = kwargs.get('app_id', None)
