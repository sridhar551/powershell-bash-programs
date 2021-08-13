import json 

def handler(event, context):
  response = {}
  response["statusCode"]=302
  response["headers"]={'Location': 'S3 BUCKET URL'}
  data = {
    "message": "please navigate to REDIRECT_URL"
  }
  response["body"]=json.dumps(data)
  return response
