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

from .job import Job


class MabJob(Job):
    """MAB workload-specific job.

    :param entity_friendly_name: Friendly name of the entity on which the
     current job is executing.
    :type entity_friendly_name: str
    :param backup_management_type: Backup management type to execute the
     current job. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB',
     'DPM', 'AzureBackupServer', 'AzureSql'
    :type backup_management_type: str or :class:`BackupManagementType
     <azure.mgmt.recoveryservicesbackup.models.BackupManagementType>`
    :param operation: The operation name.
    :type operation: str
    :param status: Job status.
    :type status: str
    :param start_time: The start time.
    :type start_time: datetime
    :param end_time: The end time.
    :type end_time: datetime
    :param activity_id: ActivityId of job.
    :type activity_id: str
    :param job_type: Polymorphic Discriminator
    :type job_type: str
    :param duration: Time taken by job to run.
    :type duration: timedelta
    :param actions_info: The state/actions applicable on jobs like
     cancel/retry.
    :type actions_info: list of str or :class:`JobSupportedAction
     <azure.mgmt.recoveryservicesbackup.models.JobSupportedAction>`
    :param mab_server_name: Name of server protecting the DS.
    :type mab_server_name: str
    :param mab_server_type: Server type of MAB container. Possible values
     include: 'Invalid', 'Unknown', 'IaasVMContainer',
     'IaasVMServiceContainer', 'DPMContainer', 'AzureBackupServerContainer',
     'MABContainer', 'Cluster', 'AzureSqlContainer', 'Windows', 'VCenter'
    :type mab_server_type: str or :class:`MabServerType
     <azure.mgmt.recoveryservicesbackup.models.MabServerType>`
    :param workload_type: Workload type of backup item. Possible values
     include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB', 'Exchange',
     'Sharepoint', 'VMwareVM', 'SystemState', 'Client', 'GenericDataSource'
    :type workload_type: str or :class:`WorkloadType
     <azure.mgmt.recoveryservicesbackup.models.WorkloadType>`
    :param error_details: The errors.
    :type error_details: list of :class:`MabErrorInfo
     <azure.mgmt.recoveryservicesbackup.models.MabErrorInfo>`
    :param extended_info: Additional information on the job.
    :type extended_info: :class:`MabJobExtendedInfo
     <azure.mgmt.recoveryservicesbackup.models.MabJobExtendedInfo>`
    """

    _validation = {
        'job_type': {'required': True},
    }

    _attribute_map = {
        'entity_friendly_name': {'key': 'entityFriendlyName', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'activity_id': {'key': 'activityId', 'type': 'str'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'duration': {'key': 'duration', 'type': 'duration'},
        'actions_info': {'key': 'actionsInfo', 'type': '[JobSupportedAction]'},
        'mab_server_name': {'key': 'mabServerName', 'type': 'str'},
        'mab_server_type': {'key': 'mabServerType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'error_details': {'key': 'errorDetails', 'type': '[MabErrorInfo]'},
        'extended_info': {'key': 'extendedInfo', 'type': 'MabJobExtendedInfo'},
    }

    def __init__(self, entity_friendly_name=None, backup_management_type=None, operation=None, status=None, start_time=None, end_time=None, activity_id=None, duration=None, actions_info=None, mab_server_name=None, mab_server_type=None, workload_type=None, error_details=None, extended_info=None):
        super(MabJob, self).__init__(entity_friendly_name=entity_friendly_name, backup_management_type=backup_management_type, operation=operation, status=status, start_time=start_time, end_time=end_time, activity_id=activity_id)
        self.duration = duration
        self.actions_info = actions_info
        self.mab_server_name = mab_server_name
        self.mab_server_type = mab_server_type
        self.workload_type = workload_type
        self.error_details = error_details
        self.extended_info = extended_info
        self.job_type = 'MabJob'