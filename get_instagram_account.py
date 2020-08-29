from credentials import getCredentials, makeApiCall
from loguru import logger
def getInstagramAccount( params ) :
	""" Get instagram account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] # tell facebook we want to exchange token
	endpointParams['fields'] = 'instagram_business_account' # access token

	url = params['endpoint_base'] + params['page_id'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call



if __name__ == "__main__":

	try:
		params = getCredentials() # get creds
		params['debug'] = 'yes' # set debug
		response = getInstagramAccount( params ) # get debug info
		logger.info("---- INSTAGRAM ACCOUNT INFO -----")
		logger.info(f"Page Id: {response['json_data']['id']}") # display the page id
		logger.info(f"Instagram Business Account Id: {response['json_data']['instagram_business_account']['id']}") #display the instagram account id 

	except Exception as e:
		logger.error("there is some error with getting your account details")