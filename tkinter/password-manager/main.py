import json
from tkinter import *
from tkinter import messagebox
import secrets


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """
    Generates a secure random password using `secrets.token_urlsafe()`,
    based on the length specified by the slider. The password is inserted
    into the password entry field and copied to the clipboard.
    """
    password_length = length_slider.get()  # Get the password length from the slider
    password = secrets.token_urlsafe(password_length)  # Generate secure random password

    # Clear and insert the generated password into the password entry field
    password_entry.delete(0, END)
    password_entry.insert(END, password)

    # Copy the generated password to the clipboard
    window.clipboard_append(password)

    print(f"Generated password: {password}")
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """
    Saves the website, username, and password to a JSON file after ensuring
    all fields are filled. If any field is empty, it displays a warning.
    The data is saved or updated in 'data.json', and the input fields are cleared.
    """
    website = website_enry.get()  # Get website from the entry field
    username = username_enry.get()  # Get username from the entry field
    password = password_entry.get()  # Get password from the entry field

    # Data structure to be saved in the JSON file
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # Check for empty fields and show a warning if necessary
    if website == "" or password == "":
        messagebox.showinfo(title="Oops...", message="Please don't leave any fields empty!")
    else:
        try:
            # Try opening the existing JSON file to update it
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Load existing data
        except FileNotFoundError:
            # If file doesn't exist, create a new data dictionary
            data = {}

        # Update the data with new credentials
        data.update(new_data)

        # Save the updated data back to 'data.json'
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        # Clear the entry fields after saving
        website_enry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """
    Searches for a website's password in the JSON file based on the input from
    the website entry field. If the website is found, the password is displayed;
    otherwise, a message informs the user that the website is not found.
    """
    website = website_enry.get()  # Get website from the entry field

    try:
        # Try opening the JSON file to search for the password
        with open("data.json", "r") as data_file:
            data = json.load(data_file)  # Load existing data

            # Check if the website exists in the data
            if website in data:
                # Display the found password in a messagebox
                messagebox.showinfo(
                    title="Password Found",
                    message=f"Website: {website}\n"
                            f"Username: {data[website]['username']}\n"
                            f"Password: {data[website]['password']}"
                )
            else:
                # Website not found in the data
                messagebox.showinfo(title="Error", message=f"Website '{website}' not found!")
    except FileNotFoundError:
        # Handle case when the JSON file doesn't exist
        messagebox.showerror(title="Error", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Logo setup
canvas = Canvas(height=200, width=200, bg="White", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")  # Load logo image
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(window, text="Website:", bg="white", font=("Ariel", 10, "bold"))
website_label.grid(row=1, column=0)

# Website entry field
website_enry = Entry(width=24)
website_enry.grid(row=1, column=1)
website_enry.focus()  # Set focus to the website field on startup

# Search button
search_button = Button(window, text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

# Email/Username label
username_label = Label(window, text="Email/Username:", bg="white", font=("Ariel", 10, "bold"))
username_label.grid(row=2, column=0)

# Email/Username entry field
username_enry = Entry(width=42)
username_enry.grid(row=2, column=1, columnspan=2)
username_enry.insert(0, "example_email@example.com")  # Pre-fill with default email

# Password label
password_label = Label(window, text="Password:", bg="white", font=("Ariel", 10, "bold"))
password_label.grid(row=3, column=0)

# Password entry field
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

# Generate password button
generate_password_button = Button(window, text="Generate Password", width=14, command=generate_pass)
generate_password_button.grid(row=3, column=2)

# Password length slider label
length_slider_label = Label(window, text="Password Length:", bg="white", font=("Ariel", 10, "bold"))
length_slider_label.grid(row=4, column=0)

# Slider to select password length (10 to 30 characters)
length_slider = Scale(window, from_=10, to=30, orient=HORIZONTAL, bg="white")
length_slider.set(15)  # Default length is set to 15
length_slider.grid(row=4, column=1)

# Add password button (save button)
add_password_button = Button(window, text="Add", width=40, command=save_password)
add_password_button.grid(row=5, column=1, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
