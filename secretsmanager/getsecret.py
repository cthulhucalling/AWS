import json
import boto3

from botocore.exceptions import ClientError



def get_secret():
    secret_name = "test_key"
    region_name = "us-east-1"
    session = boto3.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e
        
    secret = get_secret_value_response['SecretString']
    
    return {
        'key': json.dumps(secret)
    }
