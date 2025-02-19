# Stock Alert Telegram Bot - Documentation

This project is a simple Telegram bot that sends stock price alerts along with the latest news articles using the NewsAPI and Yahoo Finance. It notifies users when a specific stock’s price changes significantly and provides them with the latest news articles related to that stock.

## Features

- **Stock Price Monitoring**: Monitors a specific stock for significant price changes (e.g., greater than 5%).
- **Latest News**: Fetches the latest news articles for the stock using the NewsAPI.
- **Telegram Notifications**: Sends notifications to the user via Telegram, including stock price alerts and news articles.

## How It Works

1. **Fetch Stock Data**: The bot fetches stock data using the Yahoo Finance library and calculates the percentage change in price between the previous two days.
2. **Check Price Change**: If the price change is more than 5%, the bot proceeds to fetch the latest news articles for the stock.
3. **Send Alerts**: The bot sends a message with the stock price alert and the latest news articles to the user via Telegram.

## File Structure

- **main.py**: The main Python script that contains the code to fetch stock data, news, and send messages via Telegram.
- **requirements.txt**: A file to list the Python dependencies needed to run the code.

## How to Set Up

### 1. **Create Your Telegram Bot**

   - Open the [Telegram app](https://telegram.org/) and search for the "BotFather".
   - Start a chat with BotFather, then send `/newbot`.
   - Follow the instructions to create your bot and get the **bot token**.
   - Example:
     ```
     Your bot token: 123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
     ```

### 2. **Get Your Chat ID**

   - To get your **chat ID**, open the Telegram app and search for the bot **userinfobot**.
   - Start a conversation with it, and it will give you your unique chat ID.
   - Alternatively, you can get your chat ID programmatically by using the following URL:
     ```
     https://api.telegram.org/bot<YourBotToken>/getUpdates
     ```
     Replace `<YourBotToken>` with your bot's token. The response will contain your chat ID.

### 3. **Get Your NewsAPI Key**

   - Visit [NewsAPI](https://newsapi.org/) and sign up for an API key.
   - You will receive an API key that allows you to fetch news articles related to any topic.

### 4. **Choose Your Stock Symbol**

   - To fetch stock data for your favorite stock, use Yahoo Finance. The ticker symbol for your stock is typically a unique identifier. For example, the ticker symbol for ITC (Indian Tobacco Company) is `ITC.NS`.
   - You can find the ticker symbol for your stock by visiting [Yahoo Finance](https://finance.yahoo.com/) and searching for the company.

### 5. **Replace Placeholders in Code**

   Open the `main.py` file and replace the placeholders with your actual values:

   ```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
NEWS_API_KEY = "YOUR_NEWSAPI_KEY"
STOCK_TICKER_SYMBOL = "YOUR_FAVOURITE_STOCK"
   ```

   - Replace `YOUR_TELEGRAM_BOT_TOKEN` with the bot token you obtained from BotFather.
   - Replace `YOUR_TELEGRAM_CHAT_ID` with your chat ID.
   - Replace `YOUR_NEWSAPI_KEY` with the API key you received from NewsAPI.
   - Replace `YOUR_FAVOURITE_STOCK` with the ticker symbol of your favorite stock (e.g., `ITC.NS` for ITC).

### 6. **Install Dependencies**

   The script requires a few Python packages to function properly. Install them using the following commands:

   ```bash
   pip install yfinance requests
   ```

### 7. **Run the Script**

   Once the setup is complete, run the `main.py` script:

   ```bash
   python main.py
   ```

   The script will check the stock price and, if there is a significant change (e.g., > 5%), it will send you a Telegram message with the stock alert and the top news articles related to that stock.

## Hosting the Python Script on the Cloud

To ensure that the script runs continuously without requiring your local machine, you can host the Python script on a cloud platform such as [PythonAnywhere](https://www.pythonanywhere.com/).

### **Free and Paid Options**

#### 1. **Free Hosting with PythonAnywhere**:
   PythonAnywhere offers a free plan with basic functionality for running scripts. Here's how to host the script on PythonAnywhere:

   1. **Sign Up**: Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
   2. **Upload Your Files**: Upload your `main.py` and `requirements.txt` files using the PythonAnywhere file interface.
   3. **Set Up a Virtual Environment**: If needed, set up a virtual environment in PythonAnywhere and install dependencies:
      ```bash
      pip install yfinance requests
      ```
   4. **Run the Script**: Use the PythonAnywhere console to run your script:
      ```bash
      python main.py
      ```
   The script will now run on PythonAnywhere and send you stock alerts via Telegram when the conditions are met.

#### 2. **Paid Hosting (More Flexibility)**:
   PythonAnywhere's paid plans offer additional resources (e.g., longer-running processes, more CPU time), so if you need a more powerful setup, consider upgrading to one of the paid plans.

   - **Paid Plans**: [Explore Paid Plans](https://www.pythonanywhere.com/pricing/)

## Customization

- **Modify Stock Symbol**: Change the `STOCK_TICKER_SYMBOL` to track different stocks.
- **Adjust Stock Alert Threshold**: Modify the percentage change threshold (currently set to 5%) to trigger alerts.
- **Customize News**: Change the stock-related query in the `fetch_news()` function to fetch news about a different topic.
- **Multiple Stocks**: Expand the script to track multiple stocks by looping through a list of tickers.

## Dependencies

- Python 3.x
- yfinance (for stock data)
- requests (for API requests)
- Telegram Bot API (for sending messages)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.

