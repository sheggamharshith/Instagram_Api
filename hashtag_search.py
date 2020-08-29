from defines import getCreds, makeApiCall
import sys
from loguru import logger

def getHashtagInfo( params ) -> dict :

	""" Get info on a hashtag
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['q'] = params['hashtag_name'] # hashtag name
	endpointParams['fields'] = 'id,name' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'ig_hashtag_search' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getHashtagMedia( params ) -> dict:

	""" Get posts for a hashtag
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getRecentlySearchedHashtags( params ) -> dict:

	""" Get hashtags a user has recently search for
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/recently_searched_hashtags?fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,name' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/' + 'recently_searched_hashtags' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


if __name__ == "__main__":

	try:

		try : # try and get param from command line
			hashtag = sys.argv[1] # hashtag to get info on
		except : # default to coding hashtag
			hashtag = 'coding' # hashtag to get info on

		params = getCreds() # params for api call
		params['hashtag_name'] = hashtag # add on the hashtag we want to search for
		hashtagInfoResponse = getHashtagInfo( params ) # hit the api for some data!
		params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; # store hashtag id

		logger.info("#################### HASHTAG INFO #########################") # section heading
		
		logger.info(f"Hashtag:  {hashtag}") # display hashtag
		logger.info(f"Hashtag ID:  {params['hashtag_id']}") # display hashtag id

		logger.info("###################### HASHTAG TOP MEDIA #######################") # section heading
		
		params['type'] = 'top_media' # set call to get top media for hashtag
		hashtagTopMediaResponse = getHashtagMedia( params ) # hit the api for some data!
		for post in hashtagTopMediaResponse['json_data']['data'] : # loop over posts
			logger.info(f"---------- POST ---------") # post heading
			logger.info(f"Link to post: {post['permalink']}") # link to post
			logger.info(f"\nPost caption: {post['caption']}") # post caption
			logger.info(f"Media type: {post['media_type']}") # type of media

		logger.info("##########################$$$ HASHTAG RECENT MEDIA $$$####################") # section heading
		params['type'] = 'recent_media' # set call to get recent media for hashtag
		hashtagRecentMediaResponse = getHashtagMedia( params ) # hit the api for some data!

		for post in hashtagRecentMediaResponse['json_data']['data'] : # loop over posts
			logger.info(f"---------- POST ---------") # post heading
			logger.info(f"Link to post: {post['permalink']}") # link to post
			logger.info(f"\nPost caption: {post['caption']}") # post caption
			logger.info(f"Media type: {post['media_type']}") # type of media

		logger.info("##################### USERS RECENTLY SEARCHED HASHTAGS $$$#################") # section heading
		getRecentSearchResponse = getRecentlySearchedHashtags( params ) # hit the api for some data!

		for hashtag in getRecentSearchResponse['json_data']['data'] : # looop over hashtags
			logger.info("---------- SEARCHED HASHTAG ----------") # searched heading
			logger.info(f"Hashtag:  {hashtag['name']}") # display hashtag
			logger.info(f"Hashtag ID:  {hashtag['id']}") # display hashtag id


	except Exception as e:
		logger.error(f"There is some error in the hashtag {e}")