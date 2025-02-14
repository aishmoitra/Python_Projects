# Password Manager - Documentation

This project is a simple password manager implemented in Python using the Tkinter module for the graphical user interface.

## Features

- **Password Generation**: Automatically generates strong passwords with a mix of letters, numbers, and symbols.
- **Clipboard Copying**: Copies the generated password to the clipboard for easy pasting.
- **Data Storage**: Saves website credentials (website, email, and password) to a text file.
- **User-Friendly UI**: Simple and interactive interface built with Tkinter.

## How It Works

1. **Generate Password**: Click the "Generate Password" button to create a strong password.
2. **Enter Details**: Fill in the website and email fields.
3. **Save Password**: Click the "Add" button to store credentials in a text file.
4. **Clipboard Copy**: The generated password is automatically copied to the clipboard.

## File Structure

- **main.py**: The main script that runs the password manager.
- **logo.png**: Image used for UI representation.
- **data.txt**: File where saved credentials are stored.

## UI Controls

- **Website Entry**: Enter the website name.
- **Email Entry**: Enter the email/username associated with the account.
- **Password Entry**: Displays the generated password.
- **Generate Password Button**: Creates a random password and inserts it into the password field.
- **Add Button**: Saves the entered details to the text file.

## How to Run

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

## Customization

- **Modify Password Complexity**: Adjust the number of letters, numbers, and symbols in the `generate_password()` function.
- **Change UI Appearance**: Modify colors, fonts, and layout in the Tkinter setup.
- **Use JSON for Storage**: Change file handling to JSON format for better data management.

## Dependencies

- Python 3.x
- Tkinter (built-in with Python)
- pyperclip (for clipboard functionality)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.

