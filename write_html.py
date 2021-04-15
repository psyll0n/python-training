# The script creates a simple html web page and then opens it in your Internet browser.
# Import the webbrowser module.
import webbrowser

f = open('helloworld.html', 'w')

message = """<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-text-red">
    <p><h2>Hello World!</h2></p>
</div>

<div class="w3-text-blue">
    <p><h3>Congrats! You have just created your first html web site through a Python script!</h3></p>
</div>

</body>
</html> 
"""

f.write(message)
f.close()

# Change path to reflect file location
filename = 'file:///Users/aleksandar.yakimov/git/python/scripts/' + 'helloworld.html'
webbrowser.open_new_tab(filename)
