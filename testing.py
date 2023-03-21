import requests
import json

payload  = {
    "year": 2024
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post("http://localhost:8080/is_this_year", data=json.dumps(payload), headers=headers)
response_data = json.loads(response.content)
print(response_data)