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
button_1.grid(column=1, row=1)  # Place button at the next row and column (1, 1).

# Button widget to trigger an event when clicked.
button_2 = Button(window, text="Click Me, too", command=button_click)
button_2.grid(column=2, row=0)  # Place button at the next row and column (1, 1).

# Entry widget for user text input.
user_input = Entry(window, width=15)
user_input.grid(column=3, row=2)  # Place entry at row 2 and column 2.

# Start the main event loop to display the window.
window.mainloop()
