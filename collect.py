import requests
drsUrl = "https://drs.faa.gov/api/drs/data-pull/ADFRAWD"

request = requests.get(drsUrl, headers = {"x-api-key": "3cc99314a05bcef0a82a3aeb7b95d031"})

f = open("data.json", "a")
f.write(request.text)
f.close()