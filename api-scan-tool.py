import requests
import json

JWT="YOUR_HWT"
URL="http://localhost:8082/api/v1/v3/api-docs"
OWNER_TEAM="WHAT YOU WANT IN YOUR OWNER COLUMN"

headers = {
    "Authorization": "Bearer "+JWT
}
resp = requests.get(URL, headers=headers)
print(resp)
apiJson = json.loads(resp.text)
endpoints = []
for key, value in apiJson["paths"].items():
    endpoints.append(key);

endpoints.sort()
for url in endpoints:
    for pathKey, pathValue in apiJson["paths"][url].items():
        description = pathValue["operationId"]
        if "summary" in pathValue:
            description = description + " - " + pathValue["summary"]
        print(pathKey.upper()+" "+url+"|"+OWNER_TEAM+"|"+description)
