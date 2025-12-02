"""Miles to Kilometers Converter.

A simple tkinter GUI application that converts miles to kilometers.
Demonstrates event handling, arithmetic operations, and dynamic label updates.

Conversion Formula: km = miles * 1.609

Features:
- User input for miles
- Real-time conversion on button click
- Formatted output (2 decimal places)
- Grid layout for clean organization
"""

from tkinter import *


def button_click():
    """
    Event handler for the button click event.
    Converts the miles input to kilometers and displays the result.
    """
    print("Button was clicked!")
    # Get the miles value from input and convert to kilometers
    miles_to_km = int(user_input.get())
    conversion_output = miles_to_km * 1.609

    # Format the conversion output to 2 decimal places and update the label.
    label_2.config(text=f"{conversion_output:.2f}")

# Create the main window.
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=280, height=100)
window.config(padx=20, pady=20)

# Entry widget for user to input miles.
user_input = Entry(window, width=10)
user_input.grid(column=1, row=0)

# Label displaying "Miles".
label_1 = Label(window, text="Miles", font=("Arial", 12, "bold"))
label_1.grid(column=2, row=0)

# Label displaying "is equal to:".
label_static = Label(window, text="is equal to:", font=("Arial", 12, "bold"))
label_static.grid(column=0, row=1)

# Label to display the conversion result (initially "0").
label_2 = Label(window, text="0", font=("Arial", 12, "bold"))
label_2.grid(column=1, row=1)

# Label displaying "Km".
label_3 = Label(window, text="Km", font=("Arial", 12, "bold"))
label_3.grid(column=3, row=1)

# Button to trigger the conversion calculation.
button = Button(window, text="Calculate", command=button_click)
button.grid(column=1, row=2)

# Start the main event loop to display the window.
window.mainloop()
