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


class ServerEndpointSyncStatus(Model):
    """Server Endpoint sync status.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar download_health: Download Health Status. Possible values include:
     'Healthy', 'Error', 'SyncBlockedForRestore',
     'SyncBlockedForChangeDetectionPostRestore', 'NoActivity'
    :vartype download_health: str or ~azure.mgmt.storagesync.models.enum
    :ivar upload_health: Upload Health Status. Possible values include:
     'Healthy', 'Error', 'SyncBlockedForRestore',
     'SyncBlockedForChangeDetectionPostRestore', 'NoActivity'
    :vartype upload_health: str or ~azure.mgmt.storagesync.models.enum
    :ivar combined_health: Combined Health Status. Possible values include:
     'Healthy', 'Error', 'SyncBlockedForRestore',
     'SyncBlockedForChangeDetectionPostRestore', 'NoActivity'
    :vartype combined_health: str or ~azure.mgmt.storagesync.models.enum
    :ivar sync_activity: Sync activity. Possible values include: 'Upload',
     'Download', 'UploadAndDownload'
    :vartype sync_activity: str or ~azure.mgmt.storagesync.models.enum
    :ivar total_persistent_files_not_syncing_count: Total count of persistent
     files not syncing (combined upload + download).
    :vartype total_persistent_files_not_syncing_count: long
    :ivar last_updated_timestamp: Last Updated Timestamp
    :vartype last_updated_timestamp: datetime
    :ivar upload_status: Upload Status
    :vartype upload_status: ~azure.mgmt.storagesync.models.SyncSessionStatus
    :ivar download_status: Download Status
    :vartype download_status: ~azure.mgmt.storagesync.models.SyncSessionStatus
    :ivar upload_activity: Upload sync activity
    :vartype upload_activity:
     ~azure.mgmt.storagesync.models.SyncActivityStatus
    :ivar download_activity: Download sync activity
    :vartype download_activity:
     ~azure.mgmt.storagesync.models.SyncActivityStatus
    :ivar offline_data_transfer_status: Offline Data Transfer State. Possible
     values include: 'InProgress', 'Stopping', 'NotRunning', 'Complete'
    :vartype offline_data_transfer_status: str or
     ~azure.mgmt.storagesync.models.enum
    """

    _validation = {
        'download_health': {'readonly': True},
        'upload_health': {'readonly': True},
        'combined_health': {'readonly': True},
        'sync_activity': {'readonly': True},
        'total_persistent_files_not_syncing_count': {'readonly': True, 'minimum': 0},
        'last_updated_timestamp': {'readonly': True},
        'upload_status': {'readonly': True},
        'download_status': {'readonly': True},
        'upload_activity': {'readonly': True},
        'download_activity': {'readonly': True},
        'offline_data_transfer_status': {'readonly': True},
    }

    _attribute_map = {
        'download_health': {'key': 'downloadHealth', 'type': 'str'},
        'upload_health': {'key': 'uploadHealth', 'type': 'str'},
        'combined_health': {'key': 'combinedHealth', 'type': 'str'},
        'sync_activity': {'key': 'syncActivity', 'type': 'str'},
        'total_persistent_files_not_syncing_count': {'key': 'totalPersistentFilesNotSyncingCount', 'type': 'long'},
        'last_updated_timestamp': {'key': 'lastUpdatedTimestamp', 'type': 'iso-8601'},
        'upload_status': {'key': 'uploadStatus', 'type': 'SyncSessionStatus'},
        'download_status': {'key': 'downloadStatus', 'type': 'SyncSessionStatus'},
        'upload_activity': {'key': 'uploadActivity', 'type': 'SyncActivityStatus'},
        'download_activity': {'key': 'downloadActivity', 'type': 'SyncActivityStatus'},
        'offline_data_transfer_status': {'key': 'offlineDataTransferStatus', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ServerEndpointSyncStatus, self).__init__(**kwargs)
        self.download_health = None
        self.upload_health = None
        self.combined_health = None
        self.sync_activity = None
        self.total_persistent_files_not_syncing_count = None
        self.last_updated_timestamp = None
        self.upload_status = None
        self.download_status = None
        self.upload_activity = None
        self.download_activity = None
        self.offline_data_transfer_status = None
