#! python3
# GoogleSearchExample.py - Gets search keywords from the command line arguments.
# Retrieves the search results page.
# Opens a browser tab for each result.

""" This script does the following:
• Reads the command line arguments from sys.argv.
• Fetches the search result page with the requests module.
• Finds the links to each search result.
• Calls the webbrowser.open() function to open the web browser.
"""

import requests
import sys
import webbrowser
import bs4


print("Googling...")  # display text while the google page is downloading

url = "http://www.google.com.au/search?q=" + " ".join(sys.argv[1:])
url = url.replace(" ", "+")


res = requests.get(url)
res.raise_for_status()


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")


# Get all of the 'a' tags after an element with the class 'kCrYT' (which are the results)
linkElements = soup.select(".kCrYT > a")

# Open a browser tab for each result.
numOpen = min(5, len(linkElements))
for i in range(numOpen):
    webbrowser.open_new_tab("http://google.com" + linkElements[i].get("href"))
