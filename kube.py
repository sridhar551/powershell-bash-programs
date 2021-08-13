import os

os.system("aws eks --region REGION update-kubeconfig --name EKS_CLUSTER_NAME --role ROLE-ARN")
#os.system("velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.0.1 --bucket $VELERO_BUCKET --backup-location-config region=$AWS_REGION --snapshot-location-config region=$AWS_REGION --#secret-file ./velero-credentials")
os.system("velero restore create --from-backup nginx-controller-backup")
