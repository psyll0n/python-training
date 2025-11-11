import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta


# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)
flight_search = FlightSearch()

# ==================== Update the Airport Codes in Google Sheet ====================

#  In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the API.
#  You should use the code you get back to update the sheet_data dictionary.

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Find the Cheapest Flights ====================
for row in sheet_data:
    city = row["city"]
    iata_code = row["iataCode"]
    if not iata_code:
        print(f"{city}: N/A")
        row["lowestPrice"] = "N/A"
        continue

    # Set up a 6 month search window
    today = datetime.today()
    start_date = today.strftime("%Y-%m-%d")
    end_date = (today + timedelta(days=180)).strftime("%Y-%m-%d")
    fd = FlightData(
        originLocationCode="SOF",  # Example: Sofia Airport
        destinationLocationCode=iata_code,
        departureDateTimeRange=(start_date, end_date),
        travellers=1,
    )
    result = fd.find_cheapest_flight()
    if result:
        print(f"{city}: {result['price']} {result['currency']}")
        row["lowestPrice"] = result["price"]
    else:
        print(f"{city}: N/A")
        row["lowestPrice"] = "N/A"

# Update the Google Sheet with the new prices
data_manager.destination_data = sheet_data
data_manager.update_flight_prices()
