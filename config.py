import boto3, botocore

AWS_BUCKET_NAME="bucket_name"
s3_access_key = "access_key"
s3_secret_key = "secret_key"
endpoint_url = "endpoint_url"

s3 = boto3.client('s3',
                    aws_access_key_id=s3_access_key,
                    aws_secret_access_key= s3_secret_key,
                    endpoint_url=endpoint_url
                     )