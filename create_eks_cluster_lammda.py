import boto3

cf = boto3.client('cloudformation')

def lambda_handler(event, context):
    response = cf.create_stack(
        StackName=('YOUR-STACK-NAME'),
        TemplateURL='S3 TEMPLATE PATH',
        Parameters=[
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': 'YOUR NODE GROUP KEY'
            },
            {
                'ParameterKey': 'NodeInstanceType',
                'ParameterValue': 't3.medium'
            },
            {
                'ParameterKey': 'NodeAutoScalingGroupMinSize',
                'ParameterValue': '1'
            },
            {
                'ParameterKey': 'NodeAutoScalingGroupMaxSize',
                'ParameterValue': '10'
            },
            {
                'ParameterKey': 'NodeAutoScalingGroupDesiredCapacity',
                'ParameterValue': '2'
            },
            {
                'ParameterKey': 'NodeVolumeSize',
                'ParameterValue': '20'
            },
            {
                'ParameterKey': 'ClusterName',
                'ParameterValue': 'YOUR EKS CLUSTER NAME'
            },
            {
                'ParameterKey': 'VpcId',
                'ParameterValue': 'YOUR VPC ID'
            },
            {
                'ParameterKey': 'NodeGroupName',
                'ParameterValue': 'YOUR NODEGROUP NAME'
            },
            {
                'ParameterKey': 'PublicSubnet1ID',
                'ParameterValue': 'YOUR SUBNET ID'
            },
            {
                'ParameterKey': 'PublicSubnet2ID',
                'ParameterValue': 'YOUR SUBNET ID'
            },
        ],
        RoleARN='YOUR ROLE ARN',
        Capabilities=["CAPABILITY_IAM"],
    )
    return "success"
