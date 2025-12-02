import requests
import json


parameters = {
    "amount": 10,
    "type": "boolean",
}


# This file contains the data for the quiz application.
response = requests.get("https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
