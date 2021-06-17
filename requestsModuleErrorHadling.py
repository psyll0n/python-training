import requests

"""
Always call the raise_for_status() method after calling requests.get(). You want to be
sure that the download has actually worked before your program continues.
"""

res = requests.get("http://inventwithpython.com/page_that_does_not_exist")

try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
