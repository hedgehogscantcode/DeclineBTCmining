#! python3

import datetime
import requests
import json

def main():
	#
	# Initialize the stuff that will be common across calls
	#
	api_key = '2qsocSTzRYlFCKLA71iAFr5B3hX2DdhaQI69fDGl8fSWwp2GbljevovZsozVvxjs'
	client = WellDatabaseApiClient(api_key)

	#
	# Run our example.  In this case, we're asking for well ID 18008285 since seven days ago
	#
	modifiedSince = datetime.datetime.now() - datetime.timedelta(days=7)
	data = client.get_well_production_forecast(18008285, modifiedSince)
	print(data)


class WellDatabaseApiClient:
	"""Allows programmatic access of the [Well Database API](https://app.welldatabase.com/apihelp)
	"""
	def __init__(self, api_key: str) -> None:
		"""
		:param api_key: The key used to authenticate / authorize ourselves with the API.
		"""
		self.headers: dict[str, str] = {
			'Content-Type' : 'application/json',
			'User-Agent' : 'Your Application Name',
			'Api-Key' : api_key
		}

	def get_well_history(self, id: int, since: datetime.datetime):
		return self.get_well_data(id, 'post', since, 'history/search')

	def get_well_production_forecast(self, id: int, since: datetime.datetime):
		return self.get_well_data(id, 'post', since, 'productionForecast/search')
	
	def get_well_data(self, id: int, method: str, since: datetime.datetime, data_type: str) -> dict[str, any]:
		request = {
			'endpoint_url': f'https://app.welldatabase.com/api/v2/{data_type}',
			'method': method,
			'data': {
				"Filters": {
					"DateLastModified": {
						"Min": since.strftime("%Y-%m-%d")
					},
					"SimpleIds": [ id ]
				},
				"SortBy": "",
				"SortDirection": "Descending",
				"PageSize": "2",
				"Page": "1"
			}
		}
		# print(json.dumps(request))
		return self._exec_api_rpc(request)

	def _exec_api_rpc(self, request: dict[str, any]):
		"""The lowest-level call that performs the heavy-lifting in this scenario.
		This method assumes a simple, JSON-encoded, REST-based RPC that obey HTTP status codes.
		All interactions that match this criteria _should_ go through this method.

		:param request: the object to ultimately be passed to the API in JSON form.
		"""
		payload = json.dumps(request['data'])

		response = requests.request(
			method = request['method'] or 'get',
			url = request['endpoint_url'],
			headers = self.headers,
			data = payload)

		if response.status_code != 200:
			code = response.status_code
			reason = response.content
			raise ValueError(f"The API returned an error code of {code} with a reason of {reason}")

		return json.loads(response.content)

#
# Entrypoint if running this from a console
#
if __name__ == '__main__':
	main()