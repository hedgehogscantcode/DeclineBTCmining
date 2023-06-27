#! python3

import datetime
import json
from welldatabase.ApiClient import ApiClient

def main():
	#
	# Initialize the stuff that will be common across calls
	#
	api_key = '2qsocSTzRYlFCKLA71iAFr5B3hX2DdhaQI69fDGl8fSWwp2GbljevovZsozVvxjs'
	client = ApiClient(api_key)

	#
	# Run our example.  In this case, we're asking for well ID 18008285 since seven days ago
	#
	modifiedSince = datetime.datetime.now() - datetime.timedelta(days=2)
	data = client.get_well_history(18008285, modifiedSince)
	print(json.dumps(data))

#
# Entrypoint if running this from a console
#
if __name__ == '__main__':
	main()