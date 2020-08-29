from defines import getCreds, makeApiCall
from loguru import logger
from dotenv import load_dotenv
import os
load_dotenv()

def getUserPages( params ) -> dict:
	""" Get facebook pages for a user
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] # access token

	user_id = os.getenv("USER-ID")
	url = params['endpoint_base'] +'me/accounts' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

params = getCreds() # get creds
params['debug'] = 'no' # set debug
response = getUserPages( params ) # get debug info

logger.info("---- FACEBOOK PAGE INFO ----") # section heading
logger.info(f"Page Name: {response['json_data']['data'][0]['name']}") # label
logger.info(f"Page Category: {response['json_data']['data'][0]['category']}") # Display category
logger.info(f"Page Id: {response['json_data']['data'][0]['id']}") # Display Id