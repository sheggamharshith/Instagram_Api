from credentials import getCredentials, makeApiCall
import datetime
from loguru import logger

def debugAccessToken( params ) :
	""" Get info on an access token 
	
	API Endpoint:
		https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['input_token'] = params['access_token'] # input token is the access token
	endpointParams['access_token'] = params['access_token'] # access token to get debug info on

	url = params['graph_domain'] + '/debug_token' # endpoint url
	print(url)

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

params = getCredentials() # get creds

params['debug'] = 'yes' # set debug
response = debugAccessToken( params ) # hit the api for some data!
print(response)
logger.debug(f"Data Access Expires at: {datetime.datetime.fromtimestamp( response['json_data']['data']['data_access_expires_at'] )}") # display out when the token expires

logger.debug(f"Token Expires at: {datetime.datetime.fromtimestamp( response['json_data']['data']['expires_at'])}") # display out when the token expires