#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

"""
- Loads the XKCD home page.
- Saves the comic image on that page.
- Follows the Previous Comic link.
- Repeats until it reaches the first comic. 
"""

import requests, os, bs4


url = "http://xkcd.com"  # starting URL
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd

while not url.endswith("#"):

    # Download the image.
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find URL of the comic image.
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = "http:" + comicElem[0].get("src")

        # Download the image.
        print("Downloading image %s" % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get prev button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "http://xkcd.com" + prevLink.get("href")

print("Done.")
