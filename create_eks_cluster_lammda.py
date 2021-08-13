import boto3

cf = boto3.client('cloudformation')

def lambda_handler(event, context):
    res = cf.create_stack(
        StackName=('krysp-stage-eks'),
        TemplateURL='https://krysp-eks-backup-1622638160-10048.s3.amazonaws.com//eks.yml',
        Parameters=[
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': 'iopulse'
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
                'ParameterValue': 'krysp-eks'
            },
            {
                'ParameterKey': 'VpcId',
                'ParameterValue': 'vpc-ad85ccd7'
            },
            {
                'ParameterKey': 'NodeGroupName',
                'ParameterValue': 'krysp-eks-staging'
            },
            {
                'ParameterKey': 'PublicSubnet1ID',
                'ParameterValue': 'subnet-4678b50b'
            },
            {
                'ParameterKey': 'PublicSubnet2ID',
                'ParameterValue': 'subnet-457d4419'
            },
        ],
        RoleARN='arn:aws:iam::642168441636:role/krysp-staging-CognitoKubernetesLambdaRole-1LQGM9DHQO5MX',
        Capabilities=["CAPABILITY_IAM"],
    )
    return res
