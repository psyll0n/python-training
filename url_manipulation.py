#!/usr/bin/env python3
# Working with URLs

import urllib.parse


sample_url = "http://server.example.com:8080/example.html?val1=1&val2=Hello+World"

# TODO: Parse a URL with urlparse()
result = urllib.parse.urlparse(sample_url)
# print(result)
# print(result.scheme, result.hostname, result.path)
# print(result.geturl())


# TODO: quote() replaces special characters for use in URLs.
sample_string = "Hello El Niño!"
# print(urllib.parse.quote(sample_string))
# print(urllib.parse.quote_plus(sample_string))


# TODO: Use urlencode() to convert maps to parameter values.
query_data = {"Name": "John Doe", "City": "Anytown USA", "Age": 37}
result = urllib.parse.urlencode(query_data)
print(result)
