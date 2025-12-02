"""Comprehensive Tkinter Widgets Demonstration.

A complete reference showing various tkinter widgets and their usage.
Demonstrates Labels, Buttons, Entries, Text, Spinbox, Scale, Checkbutton,
Radiobutton, and Listbox widgets.

Widgets Demonstrated:
- Label: Display text
- Button: Clickable buttons with commands
- Entry: Single-line text input
- Text: Multi-line text input/display
- Spinbox: Numeric value selector
- Scale: Slider for value selection
- Checkbutton: Toggle checkbox
- Radiobutton: Mutually exclusive options
- Listbox: Selectable list of items
"""

from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)


# ===== Labels =====
label = Label(text="This is old text")
label.config(text="This is new text")  # Update label text
label.pack()


# ===== Buttons =====
def action():
    """Example action function for button click."""
    print("Do something")


# Button calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()


# ===== Entries (Single-line text input) =====
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()


# ===== Text (Multi-line text input) =====
text = Text(height=5, width=30)

# Puts cursor in textbox.
text.focus()

# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")

# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# ===== Spinbox (Numeric selector) =====
def spinbox_used():
    """Gets the current value in spinbox when changed."""
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# ===== Scale (Slider) =====
def scale_used(value):
    """Called with current scale value when slider moves."""
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# ===== Checkbutton (Checkbox) =====
def checkbutton_used():
    """Prints 1 if checkbox is checked, otherwise 0."""
    print(checked_state.get())


# Variable to hold checked state: 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
checkbutton.pack()


# ===== Radiobutton (Mutually exclusive options) =====
def radio_used():
    """Print which radio button is selected."""
    print(radio_state.get())


# Variable to hold which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# ===== Listbox (Selectable list) =====
def listbox_used(event):
    """Gets current selection from listbox when an item is clicked."""
    print(listbox.get(listbox.curselection()))


# Listbox with selection event handler
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

# Add each fruit to the listbox
for item in fruits:
    listbox.insert(fruits.index(item), item)

# Bind selection event to handler function
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Start the main event loop
window.mainloop()
