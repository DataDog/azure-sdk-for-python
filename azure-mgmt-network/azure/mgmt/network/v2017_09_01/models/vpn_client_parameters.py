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


class VpnClientParameters(Model):
    """Vpn Client Parameters for package generation.

    :param processor_architecture: VPN client Processor Architecture. Possible
     values are: 'AMD64' and 'X86'. Possible values include: 'Amd64', 'X86'
    :type processor_architecture: str or :class:`ProcessorArchitecture
     <azure.mgmt.network.v2017_09_01.models.ProcessorArchitecture>`
    :param authentication_method: VPN client Authentication Method. Possible
     values are: 'EAPTLS' and 'EAPMSCHAPv2'. Possible values include: 'EAPTLS',
     'EAPMSCHAPv2'
    :type authentication_method: str or :class:`AuthenticationMethod
     <azure.mgmt.network.v2017_09_01.models.AuthenticationMethod>`
    :param radius_server_auth_certificate: The public certificate data for the
     radius server authentication certificate as a Base-64 encoded string.
     Required only if external radius authentication has been configured with
     EAPTLS authentication.
    :type radius_server_auth_certificate: str
    :param client_root_certificates: A list of client root certificates public
     certificate data encoded as Base-64 strings. Optional parameter for
     external radius based authentication with EAPTLS.
    :type client_root_certificates: list of str
    """

    _attribute_map = {
        'processor_architecture': {'key': 'processorArchitecture', 'type': 'str'},
        'authentication_method': {'key': 'authenticationMethod', 'type': 'str'},
        'radius_server_auth_certificate': {'key': 'radiusServerAuthCertificate', 'type': 'str'},
        'client_root_certificates': {'key': 'clientRootCertificates', 'type': '[str]'},
    }

    def __init__(self, processor_architecture=None, authentication_method=None, radius_server_auth_certificate=None, client_root_certificates=None):
        self.processor_architecture = processor_architecture
        self.authentication_method = authentication_method
        self.radius_server_auth_certificate = radius_server_auth_certificate
        self.client_root_certificates = client_root_certificates