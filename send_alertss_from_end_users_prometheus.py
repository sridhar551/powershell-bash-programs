import boto3
import json

# client = boto3.client('secretsmanager', region_name='us-east-1')
cognito_idp = boto3.client("cognito-idp")
client = boto3.client("ses")

def lambda_handler(event, context):
    body = event.get("body")
    userPoolId = "YOUR USERPOOL ID"
    body = json.loads(body)
    alerts = body.get("alerts")
    labels = alerts[0]["labels"]
    annotations= alerts[0]["annotations"]
    deployment = labels["deployment"]
    response = cognito_idp.list_users(UserPoolId=userPoolId, AttributesToGet=["email"],
                                         Filter= f"family_name = \"{deployment}\"", )
    email = response["Users"][0]["Attributes"][0]["Value"]
    alert_name = labels["alertname"]
    container = labels["container"]
    endpoint = labels["endpoint"]
    instance = labels["instance"]
    job = labels["job"]
    namespace = labels["namespace"]
    pod = labels["pod"]
    prometheus = labels["prometheus"]
    service = labels["service"]
    severity = labels["severity"]
    description = annotations["description"]
    runbook_url = annotations["runbook_url"]
    summary = annotations["summary"]
    html_text = open("index.html").read().format(alert_name=alert_name, container=container, deployment=deployment, endpoint=endpoint,
        instance=instance, job=job, namespace=namespace, pod=pod, prometheus=prometheus, service=service, severity=severity, 
        description=description, runbook_url=runbook_url, summary=summary)
    response = client.send_email(
        Source='SOURCE EMAIL',
        Destination={
            'ToAddresses': [
                email,
            ],
        },
        Message={
            'Subject': {
                'Data': 'YOUR EMAIL SUBJECT,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Html': {
                    'Data': html_text,
                    'Charset': 'UTF-8'
                }
            }
        }, 
    )
    return "success"
