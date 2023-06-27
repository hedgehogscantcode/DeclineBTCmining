#! python3

import datetime
import requests
import json

endpoint_url = "https://app.welldatabase.com/api/v2/casings/search"

headers = {
    'Content-Type' : 'application/json',
    'User-Agent' : 'Your Application Name',
    'Api-Key' : '2qsocSTzRYlFCKLA71iAFr5B3hX2DdhaQI69fDGl8fSWwp2GbljevovZsozVvxjs'
}

modifiedSince = datetime.datetime.now() - datetime.timedelta(days=10)

data = {
    "Filters": {
        "DateLastModified": {
            "Min": modifiedSince.strftime("%Y-%m-%d")
        }
    },
    "SortBy": "",
    "SortDirection": "Descending",
    "PageSize": "2",
    "Page": "1"
}

payload = json.dumps(data)

response = requests.post(url = endpoint_url, headers = headers, data = payload)
results = json.loads(response.content)

print(results)

