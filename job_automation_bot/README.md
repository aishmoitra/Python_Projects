# LinkedIn Job Application Auto-Apply Bot - Documentation

This project is an automated bot that applies for jobs on LinkedIn using Selenium in Python. The script logs into a LinkedIn account, navigates through job listings, and attempts to apply for jobs that meet specific criteria.

## Features

- **Automated Login**: Logs into LinkedIn with provided credentials.
- **Job Search**: Searches for job listings based on specified criteria.
- **Auto-Apply**: Automatically attempts to apply for jobs.
- **Captcha Handling**: Pauses for manual captcha resolution before proceeding.
- **Application Filtering**: Skips complex applications requiring additional details.
- **Web Scraping**: Extracts job listings and applies dynamically.

## How It Works

1. **Set Up Credentials**: Update the script with your LinkedIn login email, password, and phone number.
2. **Install Dependencies**: Ensure required Python libraries are installed.
3. **Run the Script**: Launch the script to start the automated job application process.
4. **Manual Captcha Resolution**: Solve LinkedIn’s captcha manually when prompted.
5. **Job Application Process**:
   - The script scrapes job listings.
   - It attempts to auto-fill and submit applications.
   - Complex applications are skipped to prevent errors.
6. **Completion**: The script closes once all jobs are processed.

## File Structure

- **main.py**: The main script that runs the job application bot.

## Dependencies

- **Python 3.x**
- **Selenium** (for web automation)
- **webdriver-manager** (for managing ChromeDriver)

## Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```
3. Download and install **Google Chrome** and **ChromeDriver**.

## How to Run

### Running from Command Line
1. Open a terminal or command prompt.
2. Navigate to the script’s directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. Solve the CAPTCHA manually when prompted.

### Running on PyCharm
1. Open **PyCharm** and load the script.
2. Set up the Python interpreter:
   - Go to **File > Settings > Project > Python Interpreter**
   - Select the appropriate Python version.
3. Run `main.py` in PyCharm.

## Customization

- **Modify Search Parameters**: Update the LinkedIn job search URL to change job filters.
- **Adjust Sleep Timers**: Modify `time.sleep()` delays for better efficiency.
- **Enhance Filtering**: Implement additional conditions to refine job selection.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.