import requests
import json
import sys
drsUrl = "https://drs.faa.gov/api/drs/data-pull/ADFRAWD"

print("test123")
def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))

request = requests.get(drsUrl, headers = {"x-api-key": sys.argv[0]})
print(request)
f = open("data.json", "a")
f.write(get_pretty_print(request.text))
f.close()
