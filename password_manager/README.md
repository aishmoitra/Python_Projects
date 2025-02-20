# Password Manager - Documentation

This project is a simple password manager implemented in Python using the Tkinter module for the graphical user interface.

## Features

- **Password Generation**: Automatically generates strong passwords with a mix of letters, numbers, and symbols.
- **Clipboard Copying**: Copies the generated password to the clipboard for easy pasting.
- **Data Storage**: Saves website credentials (website, email, and password) in a JSON file.
- **User-Friendly UI**: Simple and interactive interface built with Tkinter.
- **Password Retrieval**: Search for stored passwords by website name.

## How It Works

1. **Generate Password**: Click the "Generate Password" button to create a strong password.
2. **Enter Details**: Fill in the website and email fields.
3. **Save Password**: Click the "Add" button to store credentials in a JSON file.
4. **Clipboard Copy**: The generated password is automatically copied to the clipboard.
5. **Search Password**: Enter a website name and click "Search" to retrieve saved credentials.

## File Structure

- **main.py**: The main script that runs the password manager.
- **logo.png**: Image used for UI representation.
- **data.json**: File where saved credentials are stored in JSON format.

## UI Controls

- **Website Entry**: Enter the website name.
- **Email Entry**: Enter the email/username associated with the account.
- **Password Entry**: Displays the generated password.
- **Generate Password Button**: Creates a random password and inserts it into the password field.
- **Search Button**: Finds stored credentials for a website.
- **Add Button**: Saves the entered details to the JSON file.

## How to Run

### Running from Command Line

1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```bash
   pip install pyperclip
   ```
3. Clone this repository or download the files.
4. Run the `main.py` file:
   ```bash
   python main.py
   ```
### Running on PyCharm  
1. Open **PyCharm** and ensure it is installed on your system.  
2. Click on **File > Open** and select the project folder.  
3. Set up the Python interpreter:  
   - Go to **File > Settings > Project: password_manager > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.

## Customization

- **Modify Password Complexity**: Adjust the number of letters, numbers, and symbols in the `generate_password()` function.
- **Change UI Appearance**: Modify colors, fonts, and layout in the Tkinter setup.
- **Enhance Security**: Implement encryption for stored passwords.

## Dependencies

- Python 3.x
- Tkinter (built-in with Python)
- pyperclip (for clipboard functionality)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.