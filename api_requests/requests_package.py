import requests


# Make a GET request to the ISS location API
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Raise an exception if the request returned an error
response.raise_for_status()

# Extract the "iss_position" data from the response JSON
data = response.json()

# Extract the longitude and latitude from the response
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Create a tuple by using the longitude and latitude variables
iss_position = (longitude, latitude)

# Print the current location of the ISS (latitude and longitude)
print(data)
print(iss_position)
