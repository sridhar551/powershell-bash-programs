import json 

def handler(event, context):
  response = {}
  response["statusCode"]=302
  response["headers"]={'Location': 'http://marketplace-poc.s3-website-us-west-2.amazonaws.com/'}
  data = {
    "message": "please navigate to https://flow.krysp.cloud"
  }
  response["body"]=json.dumps(data)
  return response
