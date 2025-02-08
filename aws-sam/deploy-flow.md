# Deploy ECR

sam deploy --template ecr-template.yaml --stack-name ml-spam-detector-ecr --capabilities CAPABILITY_IAM --guided

# Push docker image

aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com

docker build -t ml-spam-detector-api-lambda .
docker tag ml-spam-detector-api-lambda:latest <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/ml-spam-detector:latest
docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/ml-spam-detector:latest

# Deploy app-template

sam deploy --template app-template.yaml --stack-name ml-spam-detector-api --capabilities CAPABILITY_IAM --guided

# Delete S3 after deployments

aws s3 rm s3://YOUR_BUCKET_NAME --recursive

# Delete stack if any error

aws cloudformation delete-stack --stack-name aws-sam-cli-managed-default
