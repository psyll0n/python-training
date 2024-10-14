from tkinter import *




def button_click():
    """
    Event handler for the button click event.
    This function retrieves the user input from the entry widget and updates the label text.
    """
    print("Button was clicked!")
    # Get the text from the Entry widget and update the label.
    miles_to_km = int(user_input.get())
    conversion_output = miles_to_km * 1.6
    label_2.config(text=conversion_output)


# Create the main window.
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=280, height=100)
window.config(padx=20, pady=20)

# Entry widget for user text input.
user_input = Entry(window, width=10)
user_input.grid(column=1, row=0)  # Place entry at row 2 and column 2.


# Label widget to display text - "Miles".
label_1 = Label(window, text="Miles", font=("Arial", 12, "bold"))
label_1.grid(column=2, row=0)

# Label widget to display text - "is equal to: ".
label_2 = Label(window, text="is equal to:", font=("Arial", 12, "bold"))
label_2.grid(column=0, row=1)

# Label widget to display `conversion output` text"
label_2 = Label(window, text="0", font=("Arial", 12, "bold"))
label_2.grid(column=1, row=1)

# Label widget to display text - "Km".
label_3 = Label(window, text="Km", font=("Arial", 12, "bold"))
label_3.grid(column=3, row=1)


# Button widget to trigger an event when clicked.
button = Button(window, text="Calculate", command=button_click)
button.grid(column=1, row=2)  # Place button at the next row and column (1, 1).

# Start the main event loop to display the window.
window.mainloop()