# Amazon Price Tracker using Telegram Bot - Documentation

This project is a simple Python script that tracks the price of a product on Amazon and sends a price drop alert via Telegram when the price drops below a specified threshold.

## Features

- **Price Monitoring**: Tracks the price of a product on Amazon.
- **Telegram Notifications**: Sends price drop notifications to the user via Telegram.
- **Price Threshold**: Allows you to set a target price. When the price drops below this threshold, a message is sent to your Telegram.

## How It Works

1. **Fetch Amazon Data**: The script sends a request to Amazon to fetch the page content for a given product URL.
2. **Parse HTML**: Using BeautifulSoup, the script parses the HTML to extract the product title and price.
3. **Check Price**: It compares the current price with your predefined target price.
4. **Send Notification**: If the price is below the target price, it sends a message via Telegram with the product title, price, and link.

## File Structure

- **main.py**: The main Python script that fetches the price, compares it to the target price, and sends alerts via Telegram.
- **requirements.txt**: A file to list the Python dependencies needed to run the script.

## How to Set Up

### 1. **Create Your Telegram Bot**

   - Open the [Telegram app](https://telegram.org/) and search for "BotFather".
   - Start a chat with BotFather and send the command `/newbot`.
   - Follow the instructions to create your bot and get your **bot token**.
   - Example:
     ```
     Your bot token: 123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
     ```

### 2. **Get Your Chat ID**

   - Open the Telegram app and search for the bot **userinfobot**.
   - Start a conversation with it, and it will give you your unique chat ID.
   - Alternatively, you can get your chat ID programmatically by using the following URL:
     ```
     https://api.telegram.org/bot<YourBotToken>/getUpdates
     ```
     Replace `<YourBotToken>` with your bot's token. The response will contain your chat ID.

### 3. **Replace Placeholders in Code**

   Open the `main.py` file and replace the placeholders with your actual values:

   ```python
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
   ```

   - Replace `YOUR_TELEGRAM_BOT_TOKEN` with the bot token you obtained from BotFather.
   - Replace `YOUR_TELEGRAM_CHAT_ID` with your chat ID.

### 4. **Set the URL and Target Price**

   In the `main.py` file, set the URL of the Amazon product you want to track, and specify the target price below which you would like to get an alert:

   ```python
url = "https://www.amazon.in/your-product-url"
BUY_PRICE = 5000  # Replace this with your target price
   ```

### 5. **Run the Script**

#### Running from Command Line

1. The script requires a few Python packages to function properly. Install them using the following command:

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
   - Go to **File > Settings > Project: amazon_price_tracker > Python Interpreter**  
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

To ensure that the script runs continuously without requiring your local machine, you can host the Python script on a cloud platform such as [PythonAnywhere](https://www.pythonanywhere.com/).

### **Free and Paid Options**

#### 1. **Free Hosting with PythonAnywhere**:
   PythonAnywhere offers a free plan with basic functionality for running scripts. Here's how to host the script on PythonAnywhere:

   1. **Sign Up**: Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
   2. **Upload Your Files**: Upload your `main.py` and `requirements.txt` files using the PythonAnywhere file interface.
   3. **Set Up a Virtual Environment**: If needed, set up a virtual environment in PythonAnywhere and install dependencies:
      ```bash
      pip install requests beautifulsoup4
      ```
   4. **Run the Script**: Use the PythonAnywhere console to run your script:
      ```bash
      python main.py
      ```
   The script will now run on PythonAnywhere and send you price drop alerts via Telegram when the conditions are met.

#### 2. **Paid Hosting (More Flexibility)**:
   PythonAnywhere's paid plans offer additional resources (e.g., longer-running processes, more CPU time), so if you need a more powerful setup, consider upgrading to one of the paid plans.

   - **Paid Plans**: [Explore Paid Plans](https://www.pythonanywhere.com/pricing/)

## Customization

- **Modify Target Price**: Change the `BUY_PRICE` to set a new target price.
- **Track Multiple Products**: Expand the script to track multiple products by adding more URLs and corresponding target prices.
- **Customize Alerts**: Modify the alert message format to suit your preferences.

## Dependencies

- Python 3.x
- requests (for HTTP requests)
- beautifulsoup4 (for web scraping)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.
