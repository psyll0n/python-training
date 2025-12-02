from datetime import datetime
import requests
import smtplib
import time


# Define email credentials for sending notifications
NOTIFICATION_EMAIL = "example_email@gmail.com"
EMAIL_PASSWORD = "PASSWORD"

# Geographical coordinates for Sofia, Bulgaria
MY_LAT = 42.697708
MY_LONG = 23.321867


def is_iss_overhead():
    """
    Check if the ISS (International Space Station) is currently overhead.

    This function makes a request to the ISS location API and compares the current ISS
    latitude and longitude with the defined coordinates (MY_LAT, MY_LONG) within a +/- 5 degree range.

    Returns:
        bool: True if the ISS is overhead, False otherwise.
    """
    # Make a GET request to fetch the current position of the ISS
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an error if the request failed

    # Parse the JSON data from the response
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Check if the ISS is within +/- 5 degrees of the current location
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    return False


def is_night():
    """
    Determine if it is currently night at the specified location.

    This function makes a request to the Sunrise-Sunset API to get the current
    sunrise and sunset times. It then compares the current time to determine
    whether it is night (i.e., the time is after sunset or before sunrise).

    Returns:
        bool: True if it is night, False otherwise.
    """
    # Define the parameters for the API request (lat, lng, formatted)
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # Use 24-hour format for the time
    }

    # Make a GET request to fetch the sunrise and sunset times
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raise an error if the request failed

    # Parse the JSON data from the response
    data = response.json()
    # Extract and convert the sunrise and sunset times to integer hours
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour in 24-hour format
    time_now = datetime.now().hour

    # If the current time is after sunset or before sunrise, it is night
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


def send_notification():
    """
    Send an email notification if the ISS is overhead and it is currently night.

    This function connects to Gmail's SMTP server and sends an email with a
    notification message when both `is_iss_overhead()` and `is_night()` return True.
    """
    # Establish an SMTP connection with Gmail's server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(
            user=NOTIFICATION_EMAIL, password=EMAIL_PASSWORD
        )  # Log in to the email account
        # Send an email with the notification message
        connection.sendmail(
            from_addr=NOTIFICATION_EMAIL,
            to_addrs=NOTIFICATION_EMAIL,
            msg="Subject: Look up!\n\nThe ISS is above you in the sky!",
        )


# Main loop: check every 60 seconds if the ISS is overhead and it's night
while True:
    time.sleep(60)  # Wait for 60 seconds between checks
    # If both conditions are true, send a notification
    if is_iss_overhead() and is_night():
        send_notification()
