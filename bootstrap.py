import yaml
import boto3
import os
import json

from botocore.exceptions import ClientError

def main():
    db = boto3.resource('dynamodb',
        endpoint_url=os.environ.get("DYNAMO_ENDPOINT", default="http://localhost:8000"),
        region_name=os.environ.get("AWS_REGION", default=None)
    )

    with open('/code/data/schemas.yaml') as stream:
        schemas = yaml.safe_load(stream)

    for schema in schemas:
        table_name = schema['TableName']
        table = db.Table(table_name)
        try:
            table.delete()
        except ClientError:
            pass
        db.create_table(
            TableName=table_name,
            KeySchema=schema['KeySchema'],
            AttributeDefinitions=schema['AttributeDefinitions'],
            ProvisionedThroughput=schema['ProvisionedThroughput']
        )
        with open('/code/data/{}.json'.format(table_name)) as stream:
            data = json.load(stream)

        for item in data:
            table.put_item(Item=item)

if __name__ == '__main__':
    main()
