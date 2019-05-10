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

from .resource_py3 import Resource


class VirtualMachineScaleSet(Resource):
    """Describes a Virtual Machine Scale Set.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The virtual machine scale set sku.
    :type sku: ~azure.mgmt.compute.v2019_03_01.models.Sku
    :param plan: Specifies information about the marketplace image used to
     create the virtual machine. This element is only used for marketplace
     images. Before you can use a marketplace image from an API, you must
     enable the image for programmatic use.  In the Azure portal, find the
     marketplace image that you want to use and then click **Want to deploy
     programmatically, Get Started ->**. Enter any required information and
     then click **Save**.
    :type plan: ~azure.mgmt.compute.v2019_03_01.models.Plan
    :param upgrade_policy: The upgrade policy.
    :type upgrade_policy: ~azure.mgmt.compute.v2019_03_01.models.UpgradePolicy
    :param virtual_machine_profile: The virtual machine profile.
    :type virtual_machine_profile:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetVMProfile
    :ivar provisioning_state: The provisioning state, which only appears in
     the response.
    :vartype provisioning_state: str
    :param overprovision: Specifies whether the Virtual Machine Scale Set
     should be overprovisioned.
    :type overprovision: bool
    :param do_not_run_extensions_on_overprovisioned_vms: When Overprovision is
     enabled, extensions are launched only on the requested number of VMs which
     are finally kept. This property will hence ensure that the extensions do
     not run on the extra overprovisioned VMs.
    :type do_not_run_extensions_on_overprovisioned_vms: bool
    :ivar unique_id: Specifies the ID which uniquely identifies a Virtual
     Machine Scale Set.
    :vartype unique_id: str
    :param single_placement_group: When true this limits the scale set to a
     single placement group, of max size 100 virtual machines.
    :type single_placement_group: bool
    :param zone_balance: Whether to force strictly even Virtual Machine
     distribution cross x-zones in case there is zone outage.
    :type zone_balance: bool
    :param platform_fault_domain_count: Fault Domain count for each placement
     group.
    :type platform_fault_domain_count: int
    :param proximity_placement_group: Specifies information about the
     proximity placement group that the virtual machine scale set should be
     assigned to. <br><br>Minimum api-version: 2018-04-01.
    :type proximity_placement_group:
     ~azure.mgmt.compute.v2019_03_01.models.SubResource
    :param additional_capabilities: Specifies additional capabilities enabled
     or disabled on the Virtual Machines in the Virtual Machine Scale Set. For
     instance: whether the Virtual Machines have the capability to support
     attaching managed data disks with UltraSSD_LRS storage account type.
    :type additional_capabilities:
     ~azure.mgmt.compute.v2019_03_01.models.AdditionalCapabilities
    :param identity: The identity of the virtual machine scale set, if
     configured.
    :type identity:
     ~azure.mgmt.compute.v2019_03_01.models.VirtualMachineScaleSetIdentity
    :param zones: The virtual machine scale set zones.
    :type zones: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'unique_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'upgrade_policy': {'key': 'properties.upgradePolicy', 'type': 'UpgradePolicy'},
        'virtual_machine_profile': {'key': 'properties.virtualMachineProfile', 'type': 'VirtualMachineScaleSetVMProfile'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'overprovision': {'key': 'properties.overprovision', 'type': 'bool'},
        'do_not_run_extensions_on_overprovisioned_vms': {'key': 'properties.doNotRunExtensionsOnOverprovisionedVMs', 'type': 'bool'},
        'unique_id': {'key': 'properties.uniqueId', 'type': 'str'},
        'single_placement_group': {'key': 'properties.singlePlacementGroup', 'type': 'bool'},
        'zone_balance': {'key': 'properties.zoneBalance', 'type': 'bool'},
        'platform_fault_domain_count': {'key': 'properties.platformFaultDomainCount', 'type': 'int'},
        'proximity_placement_group': {'key': 'properties.proximityPlacementGroup', 'type': 'SubResource'},
        'additional_capabilities': {'key': 'properties.additionalCapabilities', 'type': 'AdditionalCapabilities'},
        'identity': {'key': 'identity', 'type': 'VirtualMachineScaleSetIdentity'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(self, *, location: str, tags=None, sku=None, plan=None, upgrade_policy=None, virtual_machine_profile=None, overprovision: bool=None, do_not_run_extensions_on_overprovisioned_vms: bool=None, single_placement_group: bool=None, zone_balance: bool=None, platform_fault_domain_count: int=None, proximity_placement_group=None, additional_capabilities=None, identity=None, zones=None, **kwargs) -> None:
        super(VirtualMachineScaleSet, self).__init__(location=location, tags=tags, **kwargs)
        self.sku = sku
        self.plan = plan
        self.upgrade_policy = upgrade_policy
        self.virtual_machine_profile = virtual_machine_profile
        self.provisioning_state = None
        self.overprovision = overprovision
        self.do_not_run_extensions_on_overprovisioned_vms = do_not_run_extensions_on_overprovisioned_vms
        self.unique_id = None
        self.single_placement_group = single_placement_group
        self.zone_balance = zone_balance
        self.platform_fault_domain_count = platform_fault_domain_count
        self.proximity_placement_group = proximity_placement_group
        self.additional_capabilities = additional_capabilities
        self.identity = identity
        self.zones = zones