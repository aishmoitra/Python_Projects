# Stock Trading News Alert using APIs - Documentation

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

   **To fetch news from a specific country (e.g., India):**
   - You can use the `top-headlines` endpoint with the `country` parameter to filter news by country.
   - Example for India:
     ```bash
     https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=YOUR_NEWSAPI_KEY
     ```
   - Replace `YOUR_NEWSAPI_KEY` with your actual API key. You can also change the category (e.g., `business`, `technology`) to suit your needs.

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


### 6. **Run the Script**
#### Running from Command Line

1. The script requires a few Python packages to function properly. Install them using the following commands:

   ```bash
   pip install -r requirements.txt
   ```

2. Once the setup is complete, run the `main.py` script:

   ```bash
   python main.py
   ```
#### Running on PyCharm  

1. Open **PyCharm** and ensure it is installed on your system.  
2. Click on **File > Open** and select the project folder.  
3. Set up the Python interpreter:  
   - Go to **File > Settings > Project: stock_news_alert_project > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.

## Automating the Script Execution

To run this script automatically every day without needing to keep Python running all the time, you can use **task schedulers**:

### 1. **Automate with `cron` (Linux/macOS)**

#### Steps:
1. Open your terminal and type `crontab -e` to open the cron job configuration.
2. Add a new cron job to run the Python script at a specific time. For example, to run your script every day at 8:00 AM, you would add:
   ```bash
   0 8 * * * /usr/bin/python3 /path/to/your/script.py
   ```
   - `0 8 * * *` means 8:00 AM every day.
   - `/usr/bin/python3` is the path to the Python interpreter (you can find the path using `which python3` or `which python`).
   - `/path/to/your/script.py` is the full path to your Python script.

3. Save and exit the editor. Now, your Python script will run every day at 8:00 AM.

### 2. **Automate with Task Scheduler (Windows)**

#### Steps:
1. Open **Task Scheduler** from the Start menu.
2. Click on **Create Basic Task** in the right panel.
3. Enter a name for the task and click **Next**.
4. Choose **Daily** and click **Next**.
5. Set the time to run (e.g., 8:00 AM) and click **Next**.
6. Choose **Start a Program**, and browse for the Python executable (`python.exe` or `python3.exe`) as the program to run.
7. In the **Add Arguments** field, enter the full path to your Python script (e.g., `"C:\path\to\your\script.py"`).
8. Click **Next** and **Finish**.

Now, Task Scheduler will run your script every day at the specified time.

## Hosting the Python Script on the Cloud

You can host the Python script on a cloud platform such as [PythonAnywhere](https://www.pythonanywhere.com/), if you prefer doing it online.

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

