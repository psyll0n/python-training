#! python3
"""
GoogleSearchExample.py - Gets search keywords from the command line arguments,
retrieves the search results page from Google, and opens a browser tab for each result.

This script does the following:
• Reads the command line arguments from sys.argv.
• Fetches the search result page using the `requests` module.
• Parses the search result page to find links to each result using BeautifulSoup.
• Opens a web browser tab for each search result using `webbrowser.open()`.

Usage:
    python GoogleSearchExample.py <search_query>
"""

import requests
import sys
import webbrowser
import bs4


def google_search(query):
    """
    Perform a Google search for the given query and open the top search result links in the web browser.

    Args:
        query (list): List of words representing the search query.
    """
    print("Googling...")  # Display a message while the Google search page is downloading.

    # Build the Google search URL.
    base_url = "http://www.google.com.au/search?q="
    search_url = base_url + "+".join(query)  # Google uses '+' for spaces in the query.

    # Fetch the search results page.
    res = requests.get(search_url)
    res.raise_for_status()  # Ensure the request was successful.

    # Parse the HTML content of the page using BeautifulSoup.
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Retrieve the top search result links (Google places search results in 'a' tags under '.kCrYT' class).
    link_elements = soup.select(".kCrYT > a")

    # Open a browser tab for each of the top 5 search results or less if fewer results are found.
    num_open = min(5, len(link_elements))
    for i in range(num_open):
        link = link_elements[i].get("href")
        # Since the links are relative, prepend the base Google URL.
        webbrowser.open_new_tab("http://google.com" + link)


if __name__ == "__main__":
    # Ensure the user provided a search query.
    if len(sys.argv) > 1:
        google_search(sys.argv[1:])  # Pass the search query to the google_search function.
    else:
        print("Please provide a search query.")
