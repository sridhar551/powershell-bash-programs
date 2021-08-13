#/bin/bash

echo "updating kubecontext of staging enviroment"
aws eks --region REGION update-kubeconfig --name EKS-CLUSTER-NAME --role ROLE-ARN

echo "Creating velero environment"
velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.0.1 --bucket $VELERO_BUCKET --backup-location-config region=$AWS_REGION --snapshot-location-config region=$AWS_REGION --secret-file ./velero-credentials

echo "velero namesapces"
kubectl get all -n velero
