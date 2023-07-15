import requests
import json
import sys
drsUrl = "https://drs.faa.gov/api/drs/data-pull/ADFRAWD"

print("test123")

request = requests.get(drsUrl, headers = {"x-api-key": sys.argv[1]})
print(request)
print("-------")
print(request.text)
obj = json.loads(request.text)
f = open("data.json", "a")
f.write(json.dumps(obj, indent=4))
f.close()
