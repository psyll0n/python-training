import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class FlightData:
    """
    This class is responsible for structuring the flight data and finding the cheapest flight.
    """

    def __init__(
        self,
        originLocationCode,
        destinationLocationCode,
        departureDateTimeRange,
        travellers=1,
        price=None,
    ):
        """
        Initializes the FlightData object with flight search parameters.

        :param originLocationCode: IATA code of the origin airport
        :param destinationLocationCode: IATA code of the destination airport
        :param departureDateTimeRange: Tuple or list with (start_date, end_date) in 'YYYY-MM-DD' format
        :param travellers: Number of travellers
        :param price: Maximum price filter (optional, can be None)
        """
        self.originLocationCode = originLocationCode
        self.destinationLocationCode = destinationLocationCode
        self.departureDateTimeRange = departureDateTimeRange
        self.travellers = travellers
        self.price = price

    def find_cheapest_flight(self):
        """
        Finds the cheapest flight based on the provided flight data attributes.

        Returns:
            dict: Details of the cheapest flight found, or None if no flights are found.
        """
        FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # Get API credentials from environment
        api_key = os.environ.get("FLIGHT_SEARCH_API_KEY")
        api_secret = os.environ.get("FLIGHT_SEARCH_API_SECRET")

        # Get a bearer token
        token_response = requests.post(
            url=TOKEN_ENDPOINT,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "client_credentials",
                "client_id": api_key,
                "client_secret": api_secret,
            },
        )
        token = token_response.json().get("access_token")
        if not token:
            print("Failed to get access token.")
            return None

        headers = {"Authorization": f"Bearer {token}"}
        params = {
            "originLocationCode": self.originLocationCode,
            "destinationLocationCode": self.destinationLocationCode,
            "departureDate": self.departureDateTimeRange[0],
            "adults": self.travellers,
            "max": 20,  # Get up to 20 offers to increase chance of finding cheapest
        }
        if self.price:
            params["maxPrice"] = self.price

        response = requests.get(FLIGHT_ENDPOINT, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error fetching flight data: {response.status_code} {response.text}")
            return None

        data = response.json().get("data", [])
        if not data:
            print("No flights found.")
            return None

        # Find the cheapest flight
        try:
            cheapest = min(data, key=lambda x: float(x["price"]["total"]))
            return {
                "itinerary": cheapest.get("itineraries", []),
                "price": cheapest["price"]["total"],
                "currency": cheapest["price"]["currency"],
                "departure_airport": self.originLocationCode,
                "arrival_airport": self.destinationLocationCode,
                "departure_date": self.departureDateTimeRange[0],
                "details": cheapest,
            }
        except (KeyError, ValueError, IndexError):
            print("Error parsing flight data.")
            return None
