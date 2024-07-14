# API Testing:
# Use a library like requests to write a Python script for testing a RESTful API. Perform actions like making GET,
# POST, PUT, and DELETE requests.

import requests

def get_users_by_id(user_id):
	requests.get(f"http://catman.qa.rpay.int.roku.com/products/{user_id}")


# The URL you want to send the POST request to
url = 'https://example.com/api/endpoint'

# Data to be sent in the POST request (can be a dictionary, JSON, etc.)
data = {
	'key1': 'value1',
	'key2': 'value2'
}

# Sending the POST request with the data
response = requests.post(url, data=data)

# Check the response status code
if response.status_code == 200:
	print("POST request was successful!")
	print("Response content:", response.text)
else:
	print("POST request failed with status code:", response.status_code)	