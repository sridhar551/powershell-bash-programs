import boto3

cf = boto3.client('cloudformation')
elb_list = boto3.client('elb')
# client = boto3.client('servicediscovery')

def lambda_handler(event, context):
    delete_cft = cf.delete_stack(
        StackName=('krysp-stage-eks')
    )
    load_balancers = elb_list.describe_load_balancers()
    for elb in load_balancers['LoadBalancerDescriptions']:
        elb_name = elb['LoadBalancerName']
    delete_elb = elb_list.delete_load_balancer(LoadBalancerName=elb_name)
    return "Success"
