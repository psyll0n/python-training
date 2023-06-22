#!/usr/bin/env python3
# Working with URLs - Part 3

from html.parser import HTMLParser


metacount = 0


# Define a class that will handle various parts of an HTML file.
# Create a subclass of HTMLParser and override the handle_starttag() method.
class MyHTMLParser(HTMLParser):
    # TODO: Handle an opening HTML tag of the form <tagname attr="value">
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag: ", tag)
        pos = self.getpos()
        print("At line: ", pos[0], " and char: ", pos[1])
        if len(attrs) > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])
        global metacount
        if tag == "meta":
            metacount += 1

    # TODO: Function to handle the end of a tag which looks like: </tagname>
    def handle_endtag(self, tag):
        print("Encountered an end tag: ", tag)

    # TODO: Function to handle character and text data (tag contents)
    # <tag>This data here in the the tag</tag>
    def handle_data(self, data):
        print("Encountered some text: ", data)

    # TODO: Function to handle the processing of HTML comments which look like:
    # <!-- Comment here -->
    def handle_comment(self, data):
        print("Encountered a comment: ", data)


# TODO: Create an instance of the parser.
parser = MyHTMLParser()


# Open the sample HTML file and read it.
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()  # Read the entire file.
    # TODO: Pass the contents to the parser.
    parser.feed(contents)  # Parse the HTML.


# TODO: Count the number of <meta> tags in the HTML file.
print(f"{metacount} meta tags were found.")
