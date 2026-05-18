import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lotspotter-spaces')


def handler(event, context):
    """Return current occupancy for a given lot."""
    lot_id = event.get('queryStringParameters', {}).get('lot_id', 'lot_ksu_main')

    response = table.get_item(Key={'lot_id': lot_id})
    item = response.get('Item', {})

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(item, default=str),
    }
