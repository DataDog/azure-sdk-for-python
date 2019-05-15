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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.registration_definitions_operations import RegistrationDefinitionsOperations
from .operations.registration_assignments_operations import RegistrationAssignmentsOperations
from .operations.operation_statuses_operations import OperationStatusesOperations
from .operations.operations import Operations
from . import models


class ManagedServicesClientConfiguration(AzureConfiguration):
    """Configuration for ManagedServicesClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ManagedServicesClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-managedservices/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class ManagedServicesClient(SDKClient):
    """Specification for ManagedServices.

    :ivar config: Configuration for client.
    :vartype config: ManagedServicesClientConfiguration

    :ivar registration_definitions: RegistrationDefinitions operations
    :vartype registration_definitions: azure.mgmt.managedservices.operations.RegistrationDefinitionsOperations
    :ivar registration_assignments: RegistrationAssignments operations
    :vartype registration_assignments: azure.mgmt.managedservices.operations.RegistrationAssignmentsOperations
    :ivar operation_statuses: OperationStatuses operations
    :vartype operation_statuses: azure.mgmt.managedservices.operations.OperationStatusesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.managedservices.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = ManagedServicesClientConfiguration(credentials, base_url)
        super(ManagedServicesClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-06-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.registration_definitions = RegistrationDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.registration_assignments = RegistrationAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation_statuses = OperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
