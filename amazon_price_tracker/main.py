from bs4 import BeautifulSoup
import requests

# Replace these with your own values
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
url = "https://www.amazon.in" # Replace with the url of the amazon you want to track

# Header
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Adding headers to the request
response = requests.get(url, headers=header)

# Parse the page content
soup = BeautifulSoup(response.content, "html.parser")

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Remove the currency symbol and commas, then split the price
price_without_currency = price.split("₹")[1].replace(",", "")

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title and trim it to 50 characters
title = soup.find(id="productTitle").get_text().strip()
title = title[:50] + "..." if len(title) > 50 else title
print(title)

# Set the price below or equal to which you would like to get a notification
BUY_PRICE = 5000 # Replace this with your target price

if price_as_float <= BUY_PRICE:
    message = (f"Price Drop Alert!🔥🚨"
               f"{title} is on sale for {price}!"
               f"\n{url}")

    # Send the message via Telegram Bot
    telegram_api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(telegram_api_url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

    # Check if the message was sent successfully
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Error code: {response.status_code}")

