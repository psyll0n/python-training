# Web and APIs

Web scraping, API requests, and network communication. This section covers interacting with web services, making HTTP requests, and sending emails.

## 📂 Contents

### [API Requests](./api_requests/)
Making HTTP requests to REST APIs and web services.

#### Core Examples
- **requests_package.py** - Complete guide to the requests library
  - Making GET requests
  - Error handling with raise_for_status()
  - Parsing JSON responses
  - Extracting nested data
- **requests_module_error_hadling.py** - Error handling patterns
- **google_search_example.py** - Google Search API integration
- **iss_tracking.py** - International Space Station position tracking
- **download_xkcd.py** - Downloading web comics programmatically
- **quick_weather.py** - Weather API integration

#### Projects
- **flight-deals-finder-app/** - Find cheap flight deals
  - API integration with flight search services
  - Price tracking and alerts
  - Email notifications

- **habit_tracking_app/** - Track daily habits
  - Pixela API integration
  - Habit visualization
  - Streak tracking

- **kanye_quotes/** - Random Kanye West quotes
  - API requests
  - JSON parsing
  - GUI integration

- **rainmeter_app/** - Weather and system monitoring
  - Multiple API integrations
  - Data aggregation
  - Display formatting

- **stock_price_news_alert/** - Stock monitoring and alerts
  - Stock price API
  - News API
  - Alert system

**Common HTTP Methods:**
- **GET** - Retrieve data (most common)
- **POST** - Send data / Create resources
- **PUT** - Update existing resources
- **DELETE** - Remove resources
- **PATCH** - Partial update

**HTTP Status Codes:**
- **2xx** - Success (200 OK, 201 Created)
- **3xx** - Redirection (301 Moved, 302 Found)
- **4xx** - Client errors (400 Bad Request, 404 Not Found, 401 Unauthorized)
- **5xx** - Server errors (500 Internal Server Error, 503 Service Unavailable)

**Request Headers:**
```python
headers = {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json',
    'User-Agent': 'My App/1.0'
}
response = requests.get(url, headers=headers)
```

**Query Parameters:**
```python
params = {'q': 'python', 'limit': 10}
response = requests.get(url, params=params)
# Results in: url?q=python&limit=10
```

**Key Concepts:** requests library, HTTP methods, JSON, REST APIs, authentication

---

### [Web Scraping](./web_scraping/)
Extracting data from websites using HTML parsing.

- **webScrapingExample.py** - Beautiful Soup basics
  - Parsing HTML
  - Finding elements
  - Extracting text and attributes
  - Navigating the DOM tree

**Popular Libraries:**
- **Beautiful Soup** - HTML/XML parsing
- **Scrapy** - Full web scraping framework
- **Selenium** - Browser automation for dynamic sites

**Example:**
```python
from bs4 import BeautifulSoup
import requests

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements
titles = soup.find_all('h1')
links = soup.find_all('a', class_='link')

# Extract data
for link in links:
    print(link.get('href'))
    print(link.text)
```

**Best Practices:**
- Check robots.txt before scraping
- Add delays between requests
- Use user agent headers
- Handle pagination
- Cache responses
- Respect rate limits

**Key Concepts:** Beautiful Soup, HTML parsing, CSS selectors, DOM navigation

---

### [SMTP Library](./smtplib/)
Sending emails programmatically.

- SMTP protocol basics
- Sending plain text emails
- HTML formatted emails
- Attachments
- Authentication
- Common email providers (Gmail, Outlook)

**Example:**
```python
import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Email body here')
msg['Subject'] = 'Test Email'
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('user@gmail.com', 'password')
    server.send_message(msg)
```

**Common SMTP Servers:**
- Gmail: smtp.gmail.com:587
- Outlook: smtp-mail.outlook.com:587
- Yahoo: smtp.mail.yahoo.com:587

**Key Concepts:** SMTP, email protocols, MIMEText, authentication, TLS

---

## 🎯 Learning Path

1. **API Requests** - Start with simple GET requests
2. **JSON Parsing** - Learn to work with API responses
3. **Error Handling** - Handle network and HTTP errors
4. **Web Scraping** - Extract data from websites
5. **SMTP** - Send automated emails
6. **Projects** - Build complete applications

## 💡 Tips

### API Requests
- Always check API documentation first
- Use environment variables for API keys
- Handle rate limits gracefully
- Cache responses when possible
- Use session objects for multiple requests
- Implement retry logic with exponential backoff

**Security:**
```python
import os
API_KEY = os.environ.get('API_KEY')  # Never hardcode!
```

**Sessions (reuse connections):**
```python
with requests.Session() as session:
    session.headers.update({'Authorization': f'Bearer {token}'})
    resp1 = session.get(url1)
    resp2 = session.get(url2)
```

### Web Scraping
- Always check robots.txt
- Be respectful of server resources
- Use time.sleep() between requests
- Handle missing data gracefully
- Consider using Scrapy for large projects
- Dynamic content may require Selenium

**Ethical Scraping:**
```python
import time

for page in pages:
    response = requests.get(page)
    time.sleep(2)  # Delay between requests
    process(response)
```

### Email Sending
- Use app-specific passwords (not your main password)
- Enable "Less secure app access" or use OAuth2
- Test with small batches first
- Handle bounces and errors
- Include unsubscribe options
- Follow email best practices (SPF, DKIM)

## 📊 API Response Handling

```python
import requests

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise exception for 4xx/5xx
    data = response.json()
    
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
else:
    # Process successful response
    process_data(data)
```

## ⚡ Performance Tips

### Concurrent Requests
```python
import concurrent.futures
import requests

urls = ['url1', 'url2', 'url3']

def fetch(url):
    return requests.get(url).json()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch, urls)
```

### Streaming Large Responses
```python
response = requests.get(url, stream=True)
with open('large_file.zip', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

## 🔐 Security Checklist

- ✅ Never commit API keys to version control
- ✅ Use environment variables or config files
- ✅ Validate and sanitize all user input
- ✅ Use HTTPS for API requests
- ✅ Implement rate limiting
- ✅ Handle authentication tokens securely
- ✅ Respect robots.txt when scraping
- ✅ Use OAuth2 for email when possible
