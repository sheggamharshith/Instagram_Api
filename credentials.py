import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
from loguru import logger

@logger.catch
def getCredentials() -> dict :

	""" Get credentials required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""
	creds = dict() # dictionary to hold everything
	creds['access_token'] = os.getenv("ACCESS_TOKEN") # access token for use with all api calls
	creds['client_id'] = os.getenv('FB-APP-CLIENT-ID') # client id from facebook app IG Graph API Test
	creds['client_secret'] = os.getenv('FB-APP-CLIENT-SECRET') # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = os.getenv("VERSION") # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = "no" # debug mode for api call
	creds['page_id'] =os.getenv('FB-PAGE-ID') # users page id
	creds['instagram_account_id'] = os.getenv('INSTAGRAM-BUSINESS-ACCOUNT-ID') # users instagram account id
	creds['ig_username'] = os.getenv('IG-USERNAME') # ig username
	return creds


@logger.catch
def makeApiCall( url, endpointParams, debug = 'no' ) -> dict :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""
	
	data = requests.get( url, endpointParams ) # make get request

	logger.info(data.json())	
	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty logger.info for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty logger.info for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

@logger.catch
def displayApiCallData( response ) -> "Debug" :
	
	""" logger.info out to cli response from api call """

	logger.info(f"URL: {response['url']} ") # display url hit
	logger.info(f"Endpoint Params:{response['endpoint_params_pretty']}") #display params passed to the endpoint 
	logger.info(f"Response: {response['json_data_pretty']} ") 