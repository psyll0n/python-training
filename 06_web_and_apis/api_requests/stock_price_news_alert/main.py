import os
import logging
import requests
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime
from typing import List, Dict


# Load environment variables
load_dotenv()


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Constants and Config
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALERT_THRESHOLD = 5  # in percentage
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
VIRTUAL_TWILIO_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
VERIFIED_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")
STOCK_API_KEY = os.getenv("STOCK_PRICE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_stock_data(symbol: str) -> Dict[str, Dict[str, str]]:
    logging.info("Fetching stock data...")
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(STOCK_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json().get("Time Series (Daily)", {})


def calculate_price_difference(
    data: Dict[str, Dict[str, str]],
) -> tuple[float, str, float]:
    dates = sorted(data.keys(), reverse=True)
    logging.info(f"Available dates from API: {dates}")

    if len(dates) < 2:
        raise ValueError("Not enough stock data to compare.")

    yesterday_price = float(data[dates[0]]["4. close"])
    day_before_price = float(data[dates[1]]["4. close"])
    difference = yesterday_price - day_before_price
    up_down = "🔺" if difference > 0 else "🔻"
    percent_diff = round((abs(difference) / day_before_price) * 100, 2)

    logging.info(f"Price changed by {percent_diff}% {up_down}")
    return percent_diff, up_down, yesterday_price


def get_news(company_name: str) -> List[Dict[str, str]]:
    logging.info("Fetching news articles...")
    params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": company_name,
        "sortBy": "publishedAt",
        "language": "en",
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json().get("articles", [])[:3]


def format_articles(
    articles: List[Dict[str, str]], stock: str, direction: str, percent: float
) -> List[str]:
    return [
        f"{stock}: {direction}{percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in articles
    ]


def send_alerts(messages: List[str]):
    logging.info("Sending alerts via Twilio...")
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for message in messages:
        sent_msg = client.messages.create(
            body=message, from_=VIRTUAL_TWILIO_NUMBER, to=VERIFIED_NUMBER
        )
        logging.info(f"Message sent. SID: {sent_msg.sid}")


def main():
    try:
        stock_data = get_stock_data(STOCK_NAME)
        percent_diff, direction, _ = calculate_price_difference(stock_data)

        if percent_diff > ALERT_THRESHOLD:
            articles = get_news(COMPANY_NAME)
            messages = format_articles(articles, STOCK_NAME, direction, percent_diff)
            send_alerts(messages)
        else:
            logging.info(f"No alert sent. Change is only {percent_diff}%.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
