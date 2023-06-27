#! python3

import datetime
from WellDatabaseApiClient import WellDatabaseApiClient

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

#
# Entrypoint if running this from a console
#
if __name__ == '__main__':
	main()