from tkinter import *
from tkinter import messagebox
import secrets, pyperclip

# Global variables to hold current website, username, and password
website = ""
username = ""
password = ""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    """
    Generates a random password based on the length specified by the slider and
    inserts it into the password entry field.

    Uses the `secrets.token_urlsafe()` function to generate a secure, random password.
    """
    global password
    password_length = length_slider.get()  # Get the length from the slider
    password = secrets.token_urlsafe(password_length)  # Generate secure random password

    password_entry.delete(0, END)  # Clear the password entry field
    password_entry.insert(END, password)  # Insert generated password
    print(f"Generated password: {password}")
    window.clipboard_append(password)  # Copy the password to the clipboard

    return password  # Return the generated password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """
    Saves the website, username, and password to a file after confirming that all fields are filled.

    If the fields are empty, a warning message will be shown. Upon confirmation,
    the credentials will be appended to `data.txt`, and the input fields will be cleared.
    """
    global website, username, password

    # Get values from the Entry widgets
    website = website_enry.get()
    username = username_enry.get()
    password = password_entry.get()

    # Check if any fields are empty and display a warning message if necessary.
    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Ops...", message="Please don't leave any fields empty!")
    else:
        # Confirm credentials before saving
        confirmed = messagebox.askokcancel(title=website,
                                           message=f"These are the credentials entered: \n"
                                                   f"Username: {username}\n"
                                                   f"Password: {password}\n"
                                                   f"Is it OK to proceed with saving them?")
        if confirmed:
            # Append the credentials to the data.txt file
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")

            # Clear the Entry fields after saving
            website_enry.delete(0, END)
            username_enry.delete(0, END)
            password_entry.delete(0, END)
            print("Credentials saved!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Setup canvas for the logo
canvas = Canvas(height=200, width=200, bg="White", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")  # Load logo image
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(window, width=16, bg="white", text="Website:", font=("Ariel", 10, "bold"))
website_label.grid(row=1, column=0)

# Website Text Entry
website_enry = Entry(width=42)
website_enry.insert(END, string="")
website_enry.grid(row=1, column=1, columnspan=2)
website_enry.focus()  # Set focus to the website field on startup

# Email/Username Label
username_label = Label(window, bg="white", text="Email/Username:", font=("Ariel", 10, "bold"))
username_label.grid(row=2, column=0)

# Email/Username Text Entry
username_enry = Entry(width=42)
username_enry.insert(END, string="")
username_enry.grid(row=2, column=1, columnspan=2)
username_enry.insert(0, "example_email@example.com")  # Pre-fill with a default email

# Password Label
password_label = Label(window, bg="white", text="Password:", font=("Ariel", 10, "bold"))
password_label.grid(row=3, column=0)

# Password Text Entry
password_entry = Entry(width=24)
password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

# Generate Password button
generate_password = Button(window, width=15, highlightthickness=0, text="Generate Password", command=generate_pass)
generate_password.grid(row=3, column=2)

# Password Length Slider
length_slider_label = Label(window, text="Password Length:", bg="white", font=("Ariel", 10, "bold"))
length_slider_label.grid(row=4, column=0)

# Slider to select password length (range 10 to 30 characters)
length_slider = Scale(window, from_=10, to=30, orient=HORIZONTAL, bg="white")
length_slider.set(15)  # Set default length to 15
length_slider.grid(row=4, column=1)

# Add Password button (Save)
add_password = Button(window, width=40, highlightthickness=0, text="Add", command=save_password)
add_password.grid(row=5, column=1, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
