from tkinter import *
import requests


def get_quote():
    """
    Fetch a random Kanye West quote from the API and update the canvas with the quote.

    This function sends a GET request to the Kanye Rest API, retrieves a random quote
    in JSON format, and updates the text on the canvas with the retrieved quote.
    """
    try:
        response = requests.get(
            "https://api.kanye.rest"
        )  # Send a GET request to the API
        response.raise_for_status()  # Raise an exception for any unsuccessful requests
        data = response.json()  # Parse the response JSON data
        kanye_quote = data["quote"]  # Extract the quote from the response data
        # Update the canvas text with the new quote
        canvas.itemconfig(quote_text, text=kanye_quote)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")


# Set up the main application window
window = Tk()
window.title("Kanye Says...")  # Set the window title
window.config(padx=50, pady=50)  # Add padding around the window

# Create a canvas to display the background image and the quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")  # Load the background image
canvas.create_image(
    150, 207, image=background_img
)  # Display the background image on the canvas
# Create a placeholder text for the quote
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Consolas", 18, "italic"),
    fill="black",
)
canvas.grid(row=0, column=0)  # Position the canvas in the grid

# Load Kanye button image and set up the button to fetch a new quote
kanye_img = PhotoImage(file="kanye.png")  # Load the Kanye image for the button
kanye_button = Button(
    image=kanye_img, highlightthickness=0, command=get_quote
)  # Create the button
kanye_button.grid(row=1, column=0)  # Position the button in the grid

# Fetch the first quote immediately when the application starts
get_quote()

# Start the Tkinter event loop to keep the application running
window.mainloop()
