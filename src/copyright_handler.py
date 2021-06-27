import json
import re
import os

# retrieve REGEX_ORG_MANES value from serverless.yml file
REGEX_ORG_NAMES = os.environ['REGEX_ORG_NAMES']

# retrieve COPYRIGHT_SYMBOL value from serverless.yml file
COPYRIGHT_SYMBOL = os.environ['COPYRIGHT_SYMBOL']

RESPONSE_HEADERS = {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Credentials": "true"}

def append_copyright(event, context):
    
    try:
        message = json.loads(event['body'])['message']
        result = re.sub(REGEX_ORG_NAMES, COPYRIGHT_SYMBOL, message, 0, re.MULTILINE | re.IGNORECASE | re.UNICODE)
        status_code = 200
        body = {
            "data":{
                "message":result
            },
            "error": None
        }
    except Exception:
        status_code = 400
        body = {
            "data":None,
            "error": {
                "errorCode":400,
                "errorMessage": "Something went wrong"
            }
        }
       
    body["status"]= "Succes" if status_code == 200 else "Failure"

    response = {
        "statusCode":status_code,
        "body": json.dumps(body),
        "headers": RESPONSE_HEADERS
    }
    return response