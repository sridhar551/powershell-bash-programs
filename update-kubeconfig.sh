#/bin/bash

echo "updating kubecontext of staging enviroment"
aws eks --region us-east-1 update-kubeconfig --name krysp-eks --role arn:aws:iam::642168441636:role/krysp-staging-CognitoKubernetesLambdaRole-1LQGM9DHQO5MX

echo "Creating velero environment"
velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.0.1 --bucket $VELERO_BUCKET --backup-location-config region=$AWS_REGION --snapshot-location-config region=$AWS_REGION --secret-file ./velero-credentials

echo "velero namesapces"
kubectl get all -n velero
