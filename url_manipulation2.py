# /usr/bin/env python3
# Working with URLs - Part 2

import urllib.request

sample_url = "http://httpbin.org/xml"


# TODO: Create a request to retrieve data using urllib.request
response = urllib.request.urlopen(sample_url)


# TODO: Check the status code.
status_code = response.status
print(status_code)


# TODO: If there is no error, then read the response contents.
if status_code >= 200 and status_code < 300:
    # TODO: Work with response headers.
    print(response.getheaders())
    print(response.getheader("Content-Type"))
    print(response.getheader("Content-Length"))

    # TODO: Read the data from the URL.
    data = response.read().decode("utf-8")
    print(data)
