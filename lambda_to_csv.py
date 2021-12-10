import boto3
import csv
import io

client = boto3.client('config')
s3 = boto3.client('s3')
org = boto3.client('organizations')

def list_organizations():
    response = org.list_accounts()
    response = response['Accounts']
    account_ids = list()
    for i in range(len(response)-1):
        for k, v in response[i].items():
            if k == 'Id':
                account_ids.append(v)
    return account_ids

def lambda_handler(event, context):
    account_ids = list_organizations()
    lst = []
    for id in account_ids:
        response = client.list_aggregate_discovered_resources(
            ConfigurationAggregatorName='aws-controltower-GuardrailsComplianceAggregator',
            ResourceType= 'AWS::IAM::Role',
            Filters={
                'AccountId': id
            }
        )
        lst.append(response)
    csvio = io.StringIO()
    writer = csv.writer(csvio)
    writer.writerow(["resourceType", "resourceId", "resourceName", "AccountId", "Region"])   

    for res in lst:
        for page in res['ResourceIdentifiers']:
            resourceType = page.get('ResourceType')
            resourceId = page.get('ResourceId')
            resourceName = page.get('ResourceName')
            resourceAccount = page.get('SourceAccountId')
            sourceRegion = page.get("SourceRegion")
            writer.writerow([resourceType, resourceId, resourceName, resourceAccount, sourceRegion])
    s3.put_object(Body=csvio.getvalue(), ContentType='text/csv', Bucket='iam-invetory-test-0000', Key='roles.csv') 
    csvio.close()

    return "success"