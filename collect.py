import requests
import json
import sys
drsUrl = "https://drs.faa.gov/api/drs/data-pull/ADFRAWD"

def delete_and_modify_first_line(file_path, new_character):
    # Read the input file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove the first line
    lines = lines[1:]

    # Modify the new first line
    if lines:
        lines[0] = new_character + lines[0]

    # Write the modified content to a new file
    with open(file_path, 'w') as file:
        file.writelines(lines)

request = requests.get(drsUrl, headers = {"x-api-key": sys.argv[1]})
obj = json.loads(request.text)
f = open("data.json", "a")
f.write(json.dumps(obj, indent=4))
f.close()

delete_and_modify_first_line("data.json", "{")