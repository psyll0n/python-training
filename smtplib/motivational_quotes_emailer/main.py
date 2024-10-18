import smtplib
import datetime as dt
import random


def get_random_quote(file_path):
    """
    Opens the specified file and returns a random quote.

    :param file_path: Path to the file containing the quotes.
    :return: A randomly selected quote as a string.
    """
    with open(file_path, "r") as file:
        return random.choice(file.readlines()).strip()


def send_email(sender_email, recipient_email, password, subject, message):
    """
    Sends an email with the given subject and message.

    :param sender_email: Sender's email address.
    :param recipient_email: Recipient's email address.
    :param password: Sender's email password.
    :param subject: The subject of the email.
    :param message: The message body of the email.
    """
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secures the connection
        connection.login(user=sender_email, password=password)  # Logs into the email account
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:{subject}\n\n{message}"  # Formats the email subject and message
        )


# Main program execution
if __name__ == "__main__":
    sender_email = "example_sender@gmail.com"  # Sender's email address
    recipient_email = "example_recipient@gmail.com"  # Recipient's email address
    password = input("Enter the email password: ")  # Prompt the user for the email password

    # Get current date and day of the week
    now = dt.datetime.now()
    present_day = now.weekday()
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_string = day_of_week[present_day]

    day = now.day
    month = now.month
    year = now.year

    # Fetch a random quote from the quotes file
    random_quote = get_random_quote("./quotes.txt")

    # Prepare the email content
    email_subject = "Quote of the Day"
    email_message = f"""
    Today is: {day_string}, {day}/{month}/{year}

    {random_quote}
    """

    # Send the email with the random quote and date information
    send_email(sender_email, recipient_email, password, email_subject, email_message)
