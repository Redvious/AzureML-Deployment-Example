import requests
import json

# Endpoint URL (replace with your actual endpoint URL)
scoring_uri = "http://d0628494-869a-4b20-ae93-710a7ebf4fba.francecentral.azurecontainer.io/score"

# Example data (one Iris flower)
data = {"data": [[5.1, 3.5, 1.4, 0.2]]}  # Example input data
headers = {"Content-Type": "application/json"}

# Send the request
response = requests.post(scoring_uri, data=json.dumps(data), headers=headers)

# Print the response
print(f"Model response: {response.json()}"))