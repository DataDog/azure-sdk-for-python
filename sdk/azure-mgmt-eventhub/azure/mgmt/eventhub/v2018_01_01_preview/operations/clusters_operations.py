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

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class ClustersOperations(object):
    """ClustersOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "2018-01-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-01-01-preview"

        self.config = config

    def list_available_clusters(
            self, custom_headers=None, raw=False, **operation_config):
        """List the quantity of available pre-provisioned Event Hubs Clusters,
        indexed by Azure region.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: AvailableClustersList or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.AvailableClustersList
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_available_clusters.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('AvailableClustersList', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_available_clusters.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.EventHub/availableClusters'}

    def list_by_resource_group(
            self, resource_group_name, custom_headers=None, raw=False, **operation_config):
        """Lists the available Event Hubs Clusters within an ARM resource group.

        :param resource_group_name: Name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Cluster
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.ClusterPaged[~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ClusterPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ClusterPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters'}

    def get(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, **operation_config):
        """Gets the resource description of the specified Event Hubs Cluster.

        :param resource_group_name: Name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Cluster or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str', max_length=50, min_length=6)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Cluster', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}'}


    def _put_initial(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.put.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str', max_length=50, min_length=6)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201, 202]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Cluster', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Cluster', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates or updates an instance of an Event Hubs Cluster.

        :param resource_group_name: Name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Cluster or
         ClientRawResponse<Cluster> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        raw_result = self._put_initial(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Cluster', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    put.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}'}


    def _patch_initial(
            self, resource_group_name, cluster_name, parameters, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.patch.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str', max_length=50, min_length=6)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'Cluster')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201, 202]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Cluster', response)
        if response.status_code == 201:
            deserialized = self._deserialize('Cluster', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def patch(
            self, resource_group_name, cluster_name, parameters, custom_headers=None, raw=False, polling=True, **operation_config):
        """Modifies mutable properties on the Event Hubs Cluster. This operation
        is idempotent.

        :param resource_group_name: Name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :param parameters: The properties of the Event Hubs Cluster which
         should be updated.
        :type parameters:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns Cluster or
         ClientRawResponse<Cluster> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.eventhub.v2018_01_01_preview.models.Cluster]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        raw_result = self._patch_initial(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            parameters=parameters,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('Cluster', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    patch.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}'}


    def _delete_initial(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str', max_length=50, min_length=6)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes an existing Event Hubs Cluster. This operation is idempotent.

        :param resource_group_name: Name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}'}

    def list_namespaces(
            self, resource_group_name, cluster_name, custom_headers=None, raw=False, **operation_config):
        """List all Event Hubs Namespace IDs in an Event Hubs Dedicated Cluster.

        :param resource_group_name: Name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: EHNamespaceIdListResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.eventhub.v2018_01_01_preview.models.EHNamespaceIdListResult
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.eventhub.v2018_01_01_preview.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_namespaces.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str', max_length=50, min_length=6)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('EHNamespaceIdListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_namespaces.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}/namespaces'}
