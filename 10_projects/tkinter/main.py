"""Tkinter GUI Basics - Interactive Label and Button Example.

A simple tkinter application demonstrating basic widgets and event handling.
Shows how to create windows, labels, buttons, and entry fields with grid layout.

Features:
- Window configuration (title, size, padding)
- Label widget with custom font
- Button widgets with click event handlers
- Entry widget for text input
- Grid layout management

Widgets Used:
- Tk: Main window
- Label: Display text
- Button: Clickable buttons
- Entry: Text input field
"""

from tkinter import Tk, Label, Button, Entry


def button_click():
    """
    Event handler for the button click event.
    This function retrieves the user input from the entry widget and updates the label text.
    """
    print("Button was clicked!")
    # Get the text from the Entry widget and update the label.
    new_text = user_input.get()
    label.config(text=new_text)

# Create the main window.
window = Tk()
window.title("My First Python GUI")
window.minsize(width=500, height=300)
# Adjust column width by adding padding (optional).
window.config(padx=20, pady=20)

# Label widget to display text.
label = Label(window, text="This is a Label", font=("Arial", 18, "bold"))
label.grid(column=0, row=0)  # Place label at the top-left corner (0, 0).
label.config(padx=10, pady=10)

# Button widget to trigger an event when clicked.
button_1 = Button(window, text="Click Me", command=button_click)
button_1.grid(column=1, row=1)  # Place button at row 1, column 1.

# Second button widget.
button_2 = Button(window, text="Click Me, too", command=button_click)
button_2.grid(column=2, row=0)  # Place button at row 0, column 2.

# Entry widget for user text input.
user_input = Entry(window, width=15)
user_input.grid(column=3, row=2)  # Place entry at row 2, column 3.

# Start the main event loop to display the window.
window.mainloop()
