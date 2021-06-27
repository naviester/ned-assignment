# ned-assignment

Cloud Assignment to create API to find and append copyright symbol to company names

## Pre-defined conpany names to be considered while implementing the service:
- Google
- Amazon
- Oracle
- Deloitte
- Microsoft

## Swagger UI and API Documentation is available at:

https://app.swaggerhub.com/apis/DAssignment/appendCopyrightSymbol/1.0.0

## API endpoint:

https://zuzztewa5m.execute-api.us-east-1.amazonaws.com/dev/copyright

## cURL
```powershell
curl --location --request POST 'https://zuzztewa5m.execute-api.us-east-1.amazonaws.com/dev/copyright' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message":"Google, Amazon, Deloitte, Oracle & Microsoft are amazing places to work."
}'
```
## Response
```javascript
{
    "data": {
        "message": "Google©, Amazon©, Deloitte©, Oracle© & Microsoft© are amazing places to work."
    },
    "error": null,
    "status": "Succes"
}
```
## Assignment Tech-stack:
- Code developed in Python
- Infrastructure Used
    - AWS Lamdba    
    - AWS API Gateway
- Framework used: **Serverless Framework**.
- Attempeted CI/CD process via GitHub actions
