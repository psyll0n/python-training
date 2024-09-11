#!/usr/bin/env python3
# Working with JSON data.

import urllib.request
import json


# Use urllib to retrieve some sample JSON data.
req = urllib.request.urlopen("http://httpbin.org/json")
data = req.read().decode("utf-8")
# print(data)


# Use the JSON module to parse the returned data.
obj = json.loads(data)


# When the data is parsed, we can access it like any other Python object.
# print(obj["slideshow"]["author"])
# for slide in obj["slideshow"]["slides"]:
#     print(slide["title"])


# Python objects can also be converted into JSON strings.
objdata = {
    "name": "Joe Marini",
    "author": True,
    "titles": [
        "Learning Python",
        "Advanced Python",
        "Python Standard Library Essential Training",
    ],
}

with open("jsonoutput.json", "w") as fp:
    json.dump(objdata, fp, indent=4)
