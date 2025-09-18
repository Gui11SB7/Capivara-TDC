import json
import boto3
import os
from decimal import Decimal
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Dados de impacto ambiental atualizados
        current_impact = {
            'id': 'current-impact',
            'trees_planted': Decimal('15420'),
            'co2_reduced_tons': Decimal('2847'),
            'active_projects': Decimal('23'),
            'volunteers': Decimal('156'),
            'states_covered': Decimal('12'),
            'hectares_protected': Decimal('3200'),
            'last_updated': datetime.now().isoformat()
        }
        
        # Salvar no DynamoDB
        table.put_item(Item=current_impact)
        
        # Converter Decimal para float para JSON
        response_data = {
            'trees_planted': int(current_impact['trees_planted']),
            'co2_reduced_tons': int(current_impact['co2_reduced_tons']),
            'active_projects': int(current_impact['active_projects']),
            'volunteers': int(current_impact['volunteers']),
            'states_covered': int(current_impact['states_covered']),
            'hectares_protected': int(current_impact['hectares_protected']),
            'last_updated': current_impact['last_updated'],
            'message': 'Dados de impacto ambiental da Verde Vivo ONG'
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response_data)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }
