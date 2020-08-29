from credentials import getCredentials, makeApiCall
from loguru import logger



def check_data(func_check,value):

	try:
		result = func_check[value]
		return result
	except Exception as e:
		logger.error(f"Did not get  information from {e}")
		return None


def getUserMedia( params, pagingUrl = '' ) :

	""" Get users media
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	if ( '' == pagingUrl ) : # get first page
		url = params['endpoint_base'] + params['instagram_account_id'] + '/media' # endpoint url
	else : # get specific page
		url = pagingUrl  # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call




if __name__ == "__main__":
	
	params = getCredentials() # get creds
	params['debug'] = 'no' # set debug
	response = getUserMedia( params ) # get users media from the api
	try:
		logger.info("############################ PAGE 1 ##############################") # display page 1 of the posts

		for post in response['json_data']['data']:
			logger.info("---------- POST ----------") # post heading
			logger.info(f"Link to post: {check_data(post,'permalink')}") # link to post
			logger.info(f"Post caption: {check_data(post,'caption')}") # post caption
			logger.info(f"Media type: {check_data(post,'media_type')}") # type of media
			logger.info(f"Posted at: {check_data(post,'timestamp')}") # when it was posted
	except Exception as e:
		logger.error(f"you have some unresolved error {e}")

	try:
		params['debug'] = 'no' # set debug
		response = getUserMedia( params, response['json_data']['paging']['next'] ) # get next page of posts from the api

		logger.info("######################## PAGE 2 ##########################") # display page 2 of the posts

		for post in response['json_data']['data'] :
			logger.info("---------- POST ----------") # post heading
			logger.info(f"Link to post: {check_data(post,'permalink')}") # link to post
			logger.info(f"Post caption: {check_data(post,'caption')}") # post caption
			logger.info(f"Media type: {check_data(post,'media_type')}") # type of media
			logger.info(f"Posted at: {check_data(post,'timestamp')}") # when it was posted
			logger.info(post['timestamp']) # when it was posted

	except Exception as e:
		logger.error(f"This profile does not have next page {e}")