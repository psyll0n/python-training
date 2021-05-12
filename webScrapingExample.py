#! python3
# webScrapingExample.py - a script that uses python's 'webbrowser' built-in module for web scraping. 
# Gets a street address from the command line arguments or clipboard.
# Opens the web browser to the Google Maps page for the address.

'''
- Reads the command line arguments from sys.argv.
- Reads the clipboard contents.
- Calls the webbrowser.open() function to open the web browser.
'''

import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
else: 
    # Get address from clipboard. 
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)

