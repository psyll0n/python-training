import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


# Load environment variables from a .env file
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_API_KEY = os.getenv("STOCK_PRICE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## Use https://www.alphavantage.co/documentation/#daily to get the stock price data.
url = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_PRICE_API_KEY}"
response = requests.get(url)
data = response.json()
data_list = [value for (key, value) in data['Time Series (Daily)'].items()]

# Get yesterday's closing stock price. 
YESTERDAYS_CLOSE = float(data_list[1]['4. close'])
print(f"Stock Price - Yesterday: {YESTERDAYS_CLOSE} USD")

# Get the day before yesterday's closing stock price
DAY_BEFORE_YESTERDAY_CLOSE = float(data_list[2]['4. close'])
print(f"Stock Price - Day Before Yesterday: {DAY_BEFORE_YESTERDAY_CLOSE} USD")

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, 
# but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(YESTERDAYS_CLOSE - DAY_BEFORE_YESTERDAY_CLOSE)
print(f"Positive difference: {positive_difference:.2f} USD")

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if positive_difference > 5:
    news_parameters = {
        "apiKey": os.getenv("NEWS_API_KEY"),
        "qInTitle": COMPANY_NAME,
        "sortBy": "relevancy",
        "pageSize": 3,  # Get the first 3 articles
    }
    print("----- Get News -----")
    
# Make a request to the News API to get articles related to the COMPANY_NAME
# and print the first 3 articles' title and description.
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
# Use Python slice operator to create a list that contains the first 3 articles. 
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
articles = news_response.json().get("articles", [])[:3]  

three_articles = articles[:3]  # Get the first 3 articles
print(three_articles)

for article in three_articles:
    formatted_articles = [f"Headline: {article['title']}\n Brief: {article['description']}\n"]

# Use `twilio.com/docs/sms/quickstart/python` to send a message to your phone number 
# with the first 3 articles' title and description.
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Create a message with the first article's title and description.
for article in formatted_articles:
    # Format the message with the stock name, change percentage, headline, and brief.
    # change_percentage = (positive_difference / DAY_BEFORE_YESTERDAY_CLOSE) * 100
    # change_symbol = "🔺" if YESTERDAYS_CLOSE > DAY_BEFORE_YESTERDAY_CLOSE else "🔻"
    message = client.messages.create(
    from_='+15612038721',
    to='+359878377268',
    body=article
)
    
print(f"Message sent: {message.sid}")

