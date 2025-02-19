import yfinance as yf
import requests

# Replace these with your own credentials
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
NEWS_API_KEY = "YOUR_NEWSAPI_KEY"

# Fetch stock data
STOCK_TICKER_SYMBOL = "YOUR_FAVOURITE_STOCK"
itc = yf.Ticker(STOCK_TICKER_SYMBOL)
historical_data = itc.history(period="5d")

# Extract closing prices
yesterday_close = historical_data["Close"].iloc[-2]
day_before_yesterday_close = historical_data["Close"].iloc[-3]

# Calculate percentage change
price_difference = yesterday_close - day_before_yesterday_close
percentage_change = (price_difference / day_before_yesterday_close) * 100


# Fetch news articles
def fetch_news():
    COMPANY_NAME = "ITC"
    news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"

    response = requests.get(news_url)
    news_data = response.json()

    articles = news_data.get("articles", [])[:3]  # Fetch first 3 articles
    news_list = []

    for article in articles:
        headline = article.get("title", "No Title")
        description = article.get("description", "No Description")
        url = article.get("url", "#")  # Full article link
        news_list.append(f"📰 *{headline}*\n📌 {description}\n🔗 [Read More]({url})\n")

    return news_list


# Send message via Telegram if stock changes significantly
if abs(percentage_change) > 5:
    news_articles = fetch_news()

    if news_articles:
        message = f"📈 *ITC Stock Alert:* {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n\n"
        message += "\n".join(news_articles)  # Combine all articles

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown", "disable_web_page_preview": False}

        response = requests.post(url, data=payload)
        print("Message sent!")
    else:
        print("No news articles found.")
else:
    print("No significant stock change.")





