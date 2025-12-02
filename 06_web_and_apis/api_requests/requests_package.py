#!/usr/bin/env python3
"""requests_package.py - Demonstrates using the requests library for HTTP GET requests.

This module shows:
- Making GET requests to REST APIs
- Error handling with raise_for_status()
- Parsing JSON responses
- Extracting nested data from JSON

The requests library is the standard for making HTTP requests in Python.
It's much more user-friendly than the built-in urllib.

Install:
    pip install requests

Common HTTP Methods:
- GET: Retrieve data (used here)
- POST: Send data to create resources
- PUT: Update existing resources
- DELETE: Remove resources
"""

import requests

# ===== Making an API Request =====

# Make a GET request to the ISS (International Space Station) location API
# This API returns the current position of the ISS in real-time
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Check for HTTP errors and raise an exception if request failed
# Status codes:
#   200-299: Success
#   400-499: Client errors (bad request, not found, etc.)
#   500-599: Server errors
response.raise_for_status()

# ===== Parsing JSON Response =====

# Extract the JSON data from the response
# The .json() method automatically parses the JSON string into Python dict
data = response.json()

# ===== Extracting Nested Data =====

# Navigate through the nested JSON structure
# JSON structure: {"iss_position": {"longitude": "...", "latitude": "..."}}
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Create a tuple with the coordinates
iss_position = (longitude, latitude)

# ===== Display Results =====

print("Full API Response:")
print(data)

print("\nISS Current Position (longitude, latitude):")
print(iss_position)

# Example output:
# {'iss_position': {'longitude': '-45.1234', 'latitude': '23.5678'}, ...}
# ('-45.1234', '23.5678')
