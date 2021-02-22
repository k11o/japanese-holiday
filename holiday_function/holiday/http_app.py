from boto3.dynamodb.conditions import Key
import json
import datetime
import boto3
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table('HolidayDB')
    if event['queryStringParameters'] is not None:
        try:
            target_date = datetime.datetime.strptime(
                event['queryStringParameters'].get("date"), '%Y-%m-%d').date()
            if len(table.query(KeyConditionExpression=Key('Date').eq(target_date.strftime("%Y-%m-%d")))) > 0:
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "result": "true",
                    }),
                }
        except ValueError:
            pass

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": "false",
        }),
    }
