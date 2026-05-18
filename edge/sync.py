import boto3
import os
from datetime import datetime


class DynamoSync:
    def __init__(self):
        self.client = boto3.resource(
            'dynamodb',
            region_name=os.environ.get('AWS_REGION', 'us-east-1')
        )
        self.table = self.client.Table(os.environ['DYNAMODB_TABLE'])

    def update_lot(self, lot_id, occupancy, sensor_distance):
        self.table.put_item(Item={
            'lot_id': lot_id,
            'timestamp': datetime.utcnow().isoformat(),
            'occupancy': occupancy,
            'sensor_distance_cm': str(sensor_distance),
            'vacant_count': sum(1 for v in occupancy.values() if not v),
        })
