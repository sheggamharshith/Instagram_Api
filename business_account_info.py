from credentials import getCredentials, makeApiCall
from loguru import logger

def getAccountInfo( params ) -> dict :

	""" Get info on a users account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


if __name__ == "__main__":
	
	try:
		params = getCredentials() # get creds
		params['debug'] = 'no' # set debug
		response = getAccountInfo( params ) # hit the api for some data!
		logger.info("---- ACCOUNT INFO -----") # display latest post info
		logger.info(f"username: {response['json_data']['business_discovery']['username']}") # display username
		try:
			logger.info(f"website: {response['json_data']['business_discovery']['website']}")
		except Exception as e:
			logger.error("There is no website for this profile")
		logger.info(f"number of posts: {response['json_data']['business_discovery']['media_count']}") # display number of posts user has made
		logger.info(f"followers: {response['json_data']['business_discovery']['followers_count']}") # display number of followers the user has
		logger.info(f"following: {response['json_data']['business_discovery']['follows_count']}") # display number of people the user follows
		logger.info(f"profile picture url: {response['json_data']['business_discovery']['profile_picture_url']}") # display profile picutre url
		logger.info(f"biography: {response['json_data']['business_discovery']['biography']}") # display users about section


	except Exception as e:
		logger.error(f"There is some error in the bussines discovery module {e}")