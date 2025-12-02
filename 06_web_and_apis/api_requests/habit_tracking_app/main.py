import requests
import os
from urllib import response
from dotenv import load_dotenv
import datetime

load_dotenv()

## This script demonstrates how to use the Pixela API to create a user, set up a graph for tracking a habit, and post, update, and delete values in that graph.
## The API calls should be used separately, as they are not designed to be run all at once. Comment out the sections you don't want to run.
## Refer to the Pixela API documentation for more details: https://docs.pixe.la/


pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph1"  # Replace with your desired graph ID

# User parameters for creating a new Pixela user
# Replace "PIXELA_USERNAME" and "PIXELA_API_TOKEN" with your actual Pixela username and API token

user_params = {
    "USERNAME": os.getenv("PIXELA_USERNAME"),
    "TOKEN": os.getenv("PIXELA_API_TOKEN"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Sending a POST request to create a new user
reponse = requests.post(url=pixela_endpoint, json=user_params)

# hecking if the request was successful
print(response.text)

# Create a new graph for tracking a habit
graph_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs"


# Parameters for creating a new graph
graph_params = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu",
}

response = requests.post(
    url=graph_endpoint,
    json=graph_params,
    headers={"X-USER-TOKEN": os.getenv("PIXELA_API_TOKEN")},
)

print(response.text)


# Navigate to the Pixela website to see your graph
# E.g. https://pixe.la/v1/users/PIXELA_USERNAME/graphs/graph1.html
# In this case the URL would be: https://pixe.la/v1/users/psyll0n/graphs/graph1.html


# Post a value to the graph
response = post_value = requests.post(
    url=f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{graph_id}",
    headers={"X-USER-TOKEN": os.getenv("PIXELA_API_TOKEN")},
    json={
        "date": datetime.datetime.now().strftime(
            "%Y%m%d"
        ),  # Current date in YYYYMMDD format
        "quantity": "10",  # Replace with the quantity you want to log
    },
)

print(response.text)


# Update a value in the graph

# Example date, replace with your desired date
today = datetime.datetime(year=2025, month=6, day=25)

update_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

headers = {"X-USER-TOKEN": os.getenv("PIXELA_API_TOKEN")}

new_pixela_data = {
    "quantity": "15"  # Replace with the updated quantity you want to log
}

response = requests.put(url=update_endpoint, headers=headers, json=new_pixela_data)

print(response.text)


## Delete a value from the graph


# # Example date, replace with your desired date
# today = datetime.datetime(year=2025, month=6, day=25)

# headers = {
#         "X-USER-TOKEN": os.getenv("PIXELA_API_TOKEN")
# }

# delete_endpoint = f"{pixela_endpoint}/{os.getenv('PIXELA_USERNAME')}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

# response = requests.delete(
#     url=delete_endpoint,
#     headers=headers
# )

# print(response.text)
