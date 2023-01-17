# zscaler-api-demo
Here is a simple Python script that demonstrates how to use the Zscaler API to retrieve information about the security status of a website:


# Set the API endpoint and API key
endpoint = 'https://api.zscaler.com/v1/zsapi/status'
api_key = 'YOUR_API_KEY'

# Set the website to check
website = 'example.com'

# Send the API request
response = requests.get(endpoint, params={'api_key': api_key, 'website': website})

# Print the response
print(response.json())

This script uses the requests library to send a GET request to the Zscaler API endpoint for checking the security status of a website. The website variable should be set to the domain of the website you want to check, and the api_key variable should be set to your Zscaler API key. The API will return a JSON object containing information about the website's security status.

You can run this script by installing the requests library and running the script in your command line or terminal. It will give you the security status of the website you set in the variable 'website'.

You can also customize the script to perform other operations using the API like adding a new website, getting a list of blocked websites, etc.

You can also check the API documentation for more information on Zscaler API https://developer.zscaler.com/docs/zscaler-api-docs

You can then add this script to your GitHub repository and share it with others who may find it useful.
