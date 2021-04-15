# The script opens up the URL address specified below. It prints the content.
# Import the URL handling modules.
# Import the webbrowser module.
    
import urllib.request, urllib.error, urllib.parse
import webbrowser


# url, response, and webContent are all variables that we have named ourselves. 
# url holds the URL of the web page that we want to download. 

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

# On the following line, we call the function urlopen, which is stored in a Python module named urllib.py, and 
# ask that function to open the website found at the URL specified then saved the result of that process into a 
# variable named response. That variable now contains an open version of the requested website, and use the read 
# method, which used earlier, to copy the contents of that open webpage into a new variable named webContent.

response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent[0:300])  

# The code below writes the contents of the webContent string to a local file on our computer rather than to the 
# “Command Output” pane. 

f = open('obo-t17800628-33.html', 'wb')
f.write(webContent)
f.close

# Open the html file by specifying its location and name.
filename = 'file:///Users/aleksandar.yakimov/git/python/scripts/' + 'obo-t17800628-33.html'
webbrowser.open_new_tab(filename)