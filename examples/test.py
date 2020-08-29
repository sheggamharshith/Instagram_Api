from dotenv import load_dotenv
import os
load_dotenv()
import requests
import json

print(os.getenv('ACCESS_TOKEN'))

url = "https://graph.facebook.com/debug_token"
# This program is ment for the basic api call to get eh authentication token
endpointParams= dict()
endpointParams['input_token'] = os.getenv('ACCESS_TOKEN') # input token is the access token
endpointParams['access_token'] = os.getenv('ACCESS_TOKEN') # access token to get debug info on

print(endpointParams)
response = requests.get(url,endpointParams)
print(json.loads(response.text))

with open("test.json","w") as f:
    f.write(json.dumps(response.json()))