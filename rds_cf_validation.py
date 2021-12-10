# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import datetime
from dateutil.tz import tzlocal

a = {'AllocatedStorage': 21, 'AutoMinorVersionUpgrade': False, 'BackupRetentionPeriod': 5, 'CopyTagsToSnapshot': True, 'DBInstanceClass': 'db.t3.large', 'DBInstanceIdentifier': 'csg-aexeo-a5-dev-client992-1', 'DBName': 'client992', 'DBParameterGroupName': 'a5-dev-client992-1-dbparametergroup-w8i0avielv0e', 'DBSubnetGroupName': 'citco-dbsubnetgroup', 'EnableCloudwatchLogsExports': ['upgrade', 'postgresql'], 'EnablePerformanceInsights': False, 'Engine': 'postgres', 'EngineVersion': '12.3', 'KmsKeyId': 'arn:aws:kms:us-east-1:221048274280:key/79fe69ef-2c5b-4742-b634-77e845e0fcaf', 'MasterUsername': 'postgres', 'MaxAllocatedStorage': 50, 'MonitoringInterval': 0, 'MultiAZ': False, 'Port': 4992, 'PreferredMaintenanceWindow': 'sun:11:00-sun:11:30', 'PubliclyAccessible': False, 'StorageEncrypted': True, 'StorageType': 'gp2', 'Tags': [{'Key': 'Cost', 'Value': 'A5'}, {'Key': 'Owner', 'Value': 'Aexeo - Drift testing'}, {'Key': 'Env', 'Value': 'dev'}, {'Key': 'RunSchedule', 'Value': 'stopped'}, {'Key': 'DataType', 'Value': 'CLIENT'}, {'Key': 'ClientID', 'Value': 'client992'}, {'Key': 'LOB', 'Value': 'HF'}, {'Key': 'AppName', 'Value': 'Aexeo'}, {'Key': 'ScheduleMessage', 'Value': 'Stopped on 2021/12/01 at 17:00 UTC'}], 'VPCSecurityGroups': ['sg-00dcb97a34ebcf77f']}

b = {'DBInstances': [{'DBInstanceIdentifier': 'csg-aexeo-a5-dev-client992-1', 'DBInstanceClass': 'db.t3.small', 'Engine': 'postgres', 'DBInstanceStatus': 'stopped', 'AutomaticRestartTime': datetime.datetime(2021, 12, 8, 17, 9, 22, 322000, tzinfo=tzlocal()), 'MasterUsername': 'postgres', 'DBName': 'client992', 'Endpoint': {'Address': 'csg-aexeo-a5-dev-client992-1.cupaxahi7rdo.us-east-1.rds.amazonaws.com', 'Port': 4992, 'HostedZoneId': 'Z2R2ITUGPM61AM'}, 'AllocatedStorage': 20, 'InstanceCreateTime': datetime.datetime(2021, 5, 29, 21, 53, 44, 29000, tzinfo=tzlocal()), 'PreferredBackupWindow': '07:18-07:48', 'BackupRetentionPeriod': 5, 'DBSecurityGroups': [], 'VpcSecurityGroups': [{'VpcSecurityGroupId': 'sg-00dcb97a34ebcf77f', 'Status': 'active'}], 'DBParameterGroups': [{'DBParameterGroupName': 'a5-dev-client992-1-dbparametergroup-w8i0avielv0e', 'ParameterApplyStatus': 'in-sync'}], 'AvailabilityZone': 'us-east-1b', 'DBSubnetGroup': {'DBSubnetGroupName': 'citco-dbsubnetgroup', 'DBSubnetGroupDescription': 'Default DB Subnet Group in the Data Subnets', 'VpcId': 'vpc-a4e6eddc', 'SubnetGroupStatus': 'Complete', 'Subnets': [{'SubnetIdentifier': 'subnet-011994f5def669048', 'SubnetAvailabilityZone': {'Name': 'us-east-1c'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-7c596c37', 'SubnetAvailabilityZone': {'Name': 'us-east-1b'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}, {'SubnetIdentifier': 'subnet-6e670b41', 'SubnetAvailabilityZone': {'Name': 'us-east-1a'}, 'SubnetOutpost': {}, 'SubnetStatus': 'Active'}]}, 'PreferredMaintenanceWindow': 'sun:11:00-sun:11:30', 'PendingModifiedValues': {}, 'LatestRestorableTime': datetime.datetime(2021, 12, 1, 16, 57, 45, tzinfo=tzlocal()), 'MultiAZ': False, 'EngineVersion': '12.3', 'AutoMinorVersionUpgrade': False, 'ReadReplicaDBInstanceIdentifiers': [], 'LicenseModel': 'postgresql-license', 'OptionGroupMemberships': [{'OptionGroupName': 'default:postgres-12', 'Status': 'in-sync'}], 'PubliclyAccessible': False, 'StorageType': 'gp2', 'DbInstancePort': 0, 'StorageEncrypted': True, 'KmsKeyId': 'arn:aws:kms:us-east-1:221048274280:key/79fe69ef-2c5b-4742-b634-77e845e0fcaf', 'DbiResourceId': 'db-BG4AYM7YA75GNJIJXIRYF75IZY', 'CACertificateIdentifier': 'rds-ca-2019', 'DomainMemberships': [], 'CopyTagsToSnapshot': True, 'MonitoringInterval': 0, 'DBInstanceArn': 'arn:aws:rds:us-east-1:911962207156:db:csg-aexeo-a5-dev-client992-1', 'IAMDatabaseAuthenticationEnabled': False, 'PerformanceInsightsEnabled': False, 'EnabledCloudwatchLogsExports': ['postgresql', 'upgrade'], 'DeletionProtection': False, 'AssociatedRoles': [], 'MaxAllocatedStorage': 50, 'TagList': [{'Key': 'aws:cloudformation:stack-name', 'Value': 'a5-dev-client992-1'}, {'Key': 'Owner', 'Value': 'Aexeo - Drift testing'}, {'Key': 'aws:cloudformation:stack-id', 'Value': 'arn:aws:cloudformation:us-east-1:911962207156:stack/a5-dev-client992-1/c15a7d50-c0c7-11eb-a049-12b4aab3bd0b'}, {'Key': 'RunSchedule', 'Value': 'stopped'}, {'Key': 'ScheduleMessage', 'Value': 'Stopped on 2021/12/01 at 17:00 UTC'}, {'Key': 'ClientID', 'Value': 'client992'}, {'Key': 'DataType', 'Value': 'CLIENT'}, {'Key': 'aws:cloudformation:logical-id', 'Value': 'DBInstance'}, {'Key': 'Env', 'Value': 'dev'}, {'Key': 'Cost', 'Value': 'A5'}, {'Key': 'LOB', 'Value': 'HF'}, {'Key': 'AppName', 'Value': 'Aexeo'}], 'CustomerOwnedIpEnabled': False, 'ActivityStreamStatus': 'stopped'}], 'ResponseMetadata': {'RequestId': '30cc04ef-b831-407c-961e-aa32c31e4ff8', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '30cc04ef-b831-407c-961e-aa32c31e4ff8', 'content-type': 'text/xml', 'content-length': '6608', 'date': 'Thu, 02 Dec 2021 16:14:40 GMT'}, 'RetryAttempts': 0}}



def compare_dict(dict1, dict2):
    dict1['Port'] = int(dict1.get('Port'))
    dict1['VPCSecurityGroups'] = dict1['VPCSecurityGroups'][0]

    lst1 = ["Tags", "EnablePerformanceInsights"]
    
    for key in lst1:
        dict1.pop(key, None)

    dict2 = dict2['DBInstances'][0]
    dict2['Port'] = dict2['Endpoint']['Port']
    dict2['VPCSecurityGroups'] = dict2['VpcSecurityGroups'][0]['VpcSecurityGroupId']
    dict2['DBSubnetGroupName'] = dict2['DBSubnetGroup']['DBSubnetGroupName']
    dict2['DBParameterGroupName'] = dict2['DBParameterGroups'][0]['DBParameterGroupName']
    dict2['EnableCloudwatchLogsExports'] = sorted(dict2['EnabledCloudwatchLogsExports'], reverse=True)
    
    lst2 = ["AutomaticRestartTime", "LatestRestorableTime", "VpcSecurityGroups", "DBSecurityGroups", "DBInstanceArn", "AssociatedRoles", "ReadReplicaDBInstanceIdentifiers", "DomainMemberships", "CACertificateIdentifier", "DbiResourceId", "PerformanceInsightsEnabled","CustomerOwnedIpEnabled", "InstanceCreateTime", "DBSubnetGroup", "DBInstanceStatus", "IAMDatabaseAuthenticationEnabled", "Endpoint", "DBParameterGroups", "AvailabilityZone", "DbInstancePort", "EnabledCloudwatchLogsExports", "PendingModifiedValues", "OptionGroupMemberships", "TagList", "ActivityStreamStatus", "LicenseModel", "PreferredBackupWindow", "DeletionProtection"]

    for key in lst2:
        dict2.pop(key, None)
    res_dict = {}
    res_dict['cf_dict'] = {}
    res_dict['rds_dict'] = {}
    for x1 in set(dict1.keys()).union(dict2.keys()):
        z = dict1.get(x1) == dict2.get(x1)
        if not z:
            res_dict['cf_dict'][x1] = dict1.get(x1)
            res_dict['rds_dict'][x1] = dict2.get(x1)
    return res_dict


print(compare_dict(a, b))

# Make key-value pair from dictionary
a = {
    "Parameters": [
        {
            "ParameterName": "application_name",
            "Description": "Sets the application name to be reported in statistics and logs.",
            "Source": "engine-default",
            "ApplyType": "dynamic",
            "DataType": "string",
            "IsModifiable": "true",
            "ApplyMethod": "pending-reboot"
        },
        {
            "ParameterName": "archive_command",
            "ParameterValue": "/etc/rds/dbbin/pgscripts/rds_wal_archive %p",
            "Description": "Sets the shell command that will be called to archive a WAL file.",
            "Source": "system",
            "ApplyType": "dynamic",
            "DataType": "string",
            "IsModifiable": "false",
            "ApplyMethod": "pending-reboot"
        },
        {
            "ParameterName": "archive_timeout",
            "ParameterValue": "300",
            "Description": "(s) Forces a switch to the next xlog file if a new file has not been started within N seconds.",
            "Source": "system",
            "ApplyType": "dynamic",
            "DataType": "integer",
            "AllowedValues": "0-2147483647",
            "IsModifiable": "false",
            "ApplyMethod": "pending-reboot"
       },
      
    ]
}

p = a["Parameters"]
c = [(d['ParameterName'], d['ParameterValue']) for d in p if 'ParameterName' in d and 'ParameterValue' in d]
print(dict(c))


x = {}
y = {}
common_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
print(common_items)
