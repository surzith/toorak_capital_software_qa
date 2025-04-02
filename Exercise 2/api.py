import requests

# URL of the demo API
url = "https://reqres.in/api/users/2"

# Make the GET request
response = requests.get(url)

# Validate the response status code
if response.status_code == 200:
    print("Test Passed: Status code is 200")
else:
    print(f"Test Failed: Status code is {response.status_code}")
