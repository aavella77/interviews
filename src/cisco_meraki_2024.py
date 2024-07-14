"""
-------------------------------------------------------------------------------
-------------- DASHBOARD OVERVIEW ---------------------------------------------
-------------------------------------------------------------------------------

Meraki's differentiating product is a web application called Dashboard.
Dashboard provides a simple interface for configuring our devices.

Dashboard is organized in a hierarchical manner. A typical Dashboard
organization might look like the following:

              +--------------+
              | Organization |
              +--------------+
                |          |
      +------------+    +------------+
      | MV Network |    | MS Network |
      -------------+    +------------+
     /      |      \       |      |
  +----+ +----+ +----+  +----+  +----+
  | MV | | MV | | MV |  | MS |  | MS |
  +----+ +----+ +----+  +----+  +----+


-------------------------------------------------------------------------------
-------------- DASHBOARD API --------------------------------------------------
-------------------------------------------------------------------------------

We provide a REST API to allow customers to configure their organizations,
networks, and devices in a programmable fashion. You will be writing code to
interact with our API.
"""


import json, requests
import sys
sys.path.append('/home/coderpad/data/')
import testbed_interviews

"""
You need to implement this API using python requests package. 
It's OK for the candidate to refer internet for the 
documentation of this package to find relevant information 
required to implement this API.
"""
def base_request(path, action='GET', payload={}):
	"""
	Make a request to the Dashboard API. Dashboard API supports
	Bearer Auth using the standard Authorization header
	parameter.

	Parameters:
	  path (string): Endpoint to hit.
	  action (string): GET/POST/PUT/DELETE
	  payload (Dict): Dictionary of key/values to send.

	Returns:
	  dict: Parsed JSON response, or None if the request fails.
	"""
	api_key = testbed_interviews.retrieve_api_key()
	dash_url = "https://api.meraki.com/api/v1" + path
	headers = {"X-Cisco-Meraki-API-Key": api_key,
	           "Content-Type": "application/json"}
	if action == 'GET':
		# Add code here for handling GET requests
		print(f'Executing GET action {dash_url}')
		result = requests.get(url=dash_url, headers=headers)
		if result is not None:
			return result.json()
		else:
			return None
	elif action == 'POST':
		raise NotImplementedError
	elif action == 'PUT':
		raise NotImplementedError
	elif action == 'DELETE':
		raise NotImplementedError
	else:
		raise ValueError('Invalid action. Use "GET", "POST", "PUT", or "DELETE"')
		return
	# Error handling code. In case of any error in receiving
	# response, return empty list

	# Return valid response

print(base_request(path="/organizations/"))

"""
-------------------------------------------------------------------------------
-------------- BEGIN ----------------------------------------------------------
-------------------------------------------------------------------------------

Part 1.
  Use the provided method 'get_organizations' to find the ID of the
  organization named "Interview Organization".
"""

def get_organizations():
	"""
	Get organizations a user has privileges on.

	Returns:
	  list<dict>: List of dictionaries of organization information.

	Example:
	  >>> get_organizations()
	  [
		{ "id": 12345, "name": "My First Organization" },
		{ "id": 12346, "name": "My Second Organization" }
	  ]
	"""

	endpoint = '/organizations/'
	return base_request(endpoint)

#    <your code>
def find_id(name):
	organizations = get_organizations()
	for organization in organizations:
		if organization['name'] == name:
			return organization['id']

print(find_id("Interview Organization"))



"""
Part 2.
  Write a method to get information about the networks in the organization
  found above. Print this information in a format similar to the following:

    Network ID | Org ID | Name              | Type
    000001     | 123456 | My Camera Network | camera
    000002     | 123456 | My Switch Network | switch

  Use the following API endpoint:
    GET '/organizations/{organizationId}/networks'
"""

def get_networks(organization_id):
	# <your code>
	print("Network ID | Org ID | Name              | Type")

	url = f"/organizations/{organization_id}/networks"
	networks = base_request(path=url)
	for network in networks:
		print(f"{network['id']} | {network['organizationId']} | {network['name']} | {network['productTypes'][0]}" )
	pass

get_networks(find_id("Interview Organization"))






"""
Part 3.
  a. Write a method to get information about the devices in the camera network
  obtained in the previous question.

  Use the following endpoint:
    GET '/networks/{networkId}/devices'

  b. Provide the list of unique model types in that network.  
"""

# <your code>



"""
Part 4.
  There is something wrong with the provided 'get_device' method. Explain how
  you would debug this issue and fix the method.

  Full API documentation:
    https://developer.cisco.com/meraki/api-v1/
"""

def get_device(mac_address):
	"""
	Get information about a single device.

	Parameters:
	  mac_address (string): MAC address of the desired device.

	Returns:
	  dict: Dictionary of device information.
	"""

	device_path = '/devices/' + mac_address
	return base_request(device_path)

# Breaks!
print(get_device('0c:8d:db:00:81:a1'))
