import requests
import json

# Endpoint URL (replace with your actual endpoint URL)
scoring_uri = "http://2c3e42b9-3c86-4c5d-98d2-857911bbdc22.francecentral.azurecontainer.io/score"

# Example data (one Iris flower)
data = {"data": [[5.1, 3.5, 1.4, 0.2]]} 
headers = {"Content-Type": "application/json"}

response = requests.post(scoring_uri, data=json.dumps(data), headers=headers)

print(f"Model response: {response.json()}")