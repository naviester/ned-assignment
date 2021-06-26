import json
import re
import os

# retrieve REGEX_ORG_MANES value from serverless.yml file
REGEX_ORG_MANES = os.environ['REGEX_ORG_MANES']

# retrieve COPYRIGHT_SYMBOL value from serverless.yml file
COPYRIGHT_SYMBOL = os.environ['COPYRIGHT_SYMBOL']

def do(event, context):
    
    if event :
        # You can manually specify the number of replacements by changing the 4th argument
        result = re.sub(REGEX_ORG_MANES, COPYRIGHT_SYMBOL, event['message'], 0, re.MULTILINE | re.IGNORECASE | re.UNICODE)
        if result:
            print (result)
        response = {"statusCode": 200, "body": result}
    else :
        response = {"statusCode": 400, "body": "empty body not allowed"}

    return response