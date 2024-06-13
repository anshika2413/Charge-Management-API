import json
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
dynamodb_table = dynamodb.Table('loan')

status_check_path = '/status'
charge_path = '/charge'
charges_path = '/charges'

def lambda_handler(event, context):
    print('Request event: ', json.dumps(event))
    response = None

    try:
        http_method = event.get('httpMethod')
        path = event.get('path')

        if http_method == 'GET' and path == status_check_path:
            response = build_response(200, 'Service is operational')
        elif http_method == 'GET' and path == charge_path:
            charge_id = event['queryStringParameters']['id']
            response = get_charge(charge_id)
        elif http_method == 'GET' and path == charges_path:
            response = get_charges()
        elif http_method == 'POST' and path == charge_path:
            response = save_charge(json.loads(event['body']))
        elif http_method == 'PATCH' and path == charge_path:
            body = json.loads(event['body'])
            response = modify_charge(body['id'], body['updateKey'], body['updateValue'])
        elif http_method == 'DELETE' and path == charge_path:
            body = json.loads(event['body'])
            response = delete_charge(body['id'])
        else:
            response = build_response(404, '404 Not Found')

    except Exception as e:
        print('Error:', str(e))
        response = build_response(400, 'Error processing request')

    return response

def get_charge(charge_id):
    try:
        response = dynamodb_table.get_item(Key={'id': charge_id})
        if 'Item' in response:
            return build_response(200, response['Item'])
        else:
            return build_response(404, 'Charge not found')
    except ClientError as e:
        print('Error:', e.response['Error']['Message'])
        return build_response(400, e.response['Error']['Message'])

def get_charges():
    try:
        scan_params = {
            'TableName': dynamodb_table.name
        }
        return build_response(200, scan_dynamo_records(scan_params, []))
    except ClientError as e:
        print('Error:', e.response['Error']['Message'])
        return build_response(400, e.response['Error']['Message'])

def scan_dynamo_records(scan_params, item_array):
    response = dynamodb_table.scan(**scan_params)
    item_array.extend(response.get('Items', []))

    if 'LastEvaluatedKey' in response:
        scan_params['ExclusiveStartKey'] = response['LastEvaluatedKey']
        return scan_dynamo_records(scan_params, item_array)
    else:
        return {'charges': item_array}

def save_charge(request_body):
    try:
        print('Saving charge:', request_body)
        # Ensure the amount is a Decimal
        request_body['amount'] = Decimal(str(request_body['amount']))
        dynamodb_table.put_item(Item=request_body)
        body = {
            'Operation': 'SAVE',
            'Message': 'SUCCESS',
            'Item': request_body
        }
        return build_response(200, body)
    except ClientError as e:
        print('Error:', e.response['Error']['Message'])
        return build_response(400, e.response['Error']['Message'])

def modify_charge(charge_id, update_key, update_value):
    try:
        if update_key == 'amount':
            update_value = Decimal(str(update_value))
        response = dynamodb_table.update_item(
            Key={'id': charge_id},
            UpdateExpression=f'SET {update_key} = :value',
            ExpressionAttributeValues={':value': update_value},
            ReturnValues='UPDATED_NEW'
        )
        body = {
            'Operation': 'UPDATE',
            'Message': 'SUCCESS',
            'UpdatedAttributes': response['Attributes']
        }
        return build_response(200, body)
    except ClientError as e:
        print('Error:', e.response['Error']['Message'])
        return build_response(400, e.response['Error']['Message'])

def delete_charge(charge_id):
    try:
        response = dynamodb_table.delete_item(
            Key={'id': charge_id},
            ReturnValues='ALL_OLD'
        )
        if 'Attributes' in response:
            body = {
                'Operation': 'DELETE',
                'Message': 'SUCCESS',
                'Item': response['Attributes']
            }
            return build_response(200, body)
        else:
            return build_response(404, 'Charge not found')
    except ClientError as e:
        print('Error:', e.response['Error']['Message'])
        return build_response(400, e.response['Error']['Message'])

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Check if it's an int or a float
            if obj % 1 == 0:
                return int(obj)
            else:
                return float(obj)
        # Let the base class default method raise the TypeError
        return super(DecimalEncoder, self).default(obj)

def build_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body, cls=DecimalEncoder)
    }

# Example of the expected JSON format for saving a charge
example_charge = {
    "id": "1",
    "name": "Processing fee",
    "amount": 50.00,
    "description": "Fee for Processing the loan application",
    "type": "application fee"
}

# Simulating a POST request
print(lambda_handler({
    'httpMethod': 'POST',
    'path': charge_path,
    'body': json.dumps(example_charge)
}, None))
