import boto3
import os

# Create S3 client
s3 = boto3.client(
    's3',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def upload_file(file, filename):
    bucket = os.getenv("AWS_S3_BUCKET_NAME")

    # Upload file (NO ACL - modern S3)
    s3.upload_fileobj(
        file,
        bucket,
        filename
    )

    # Return public URL (works if bucket policy allows public read)
    return f"https://{bucket}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{filename}"
