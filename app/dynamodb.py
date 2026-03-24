import boto3
import os
import hashlib

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

table = dynamodb.Table(os.getenv("DYNAMODB_TABLE_NAME"))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    table.put_item(Item={
        'username': username,
        'password': hash_password(password)
    })

def get_user(username):
    response = table.get_item(Key={'username': username})
    return response.get('Item')
