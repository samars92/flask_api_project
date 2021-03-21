import boto3, botocore

AWS_BUCKET_NAME="flaskhr"

s3 = boto3.client('s3',
                    aws_access_key_id="AKIAWWLYU5WKXU27TIIE",
                    aws_secret_access_key= "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",
                    endpoint_url='https://flaskhr.s3.amazonaws.com'
                     )