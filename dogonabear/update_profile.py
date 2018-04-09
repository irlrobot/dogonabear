#!/usr/bin/env python
import json
import datetime

def handler(event, context):
    data = {
        'output': 'Profile Updated'
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
