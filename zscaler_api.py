import requests

# Set the API endpoint and API key
endpoint = 'https://api.zscaler.com/v1/zsapi/status'
api_key = 'YOUR_API_KEY'

# Set the website to check
website = 'example.com'

# Send the API request
response = requests.get(endpoint, params={'api_key': api_key, 'website': website})

# Print the response
print(response.json())
