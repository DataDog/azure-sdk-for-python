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

from enum import Enum


class ProvisioningState(str, Enum):

    not_specified = "NotSpecified"
    accepted = "Accepted"
    running = "Running"
    ready = "Ready"
    creating = "Creating"
    created = "Created"
    deleting = "Deleting"
    deleted = "Deleted"
    canceled = "Canceled"
    failed = "Failed"
    succeeded = "Succeeded"
    updating = "Updating"
