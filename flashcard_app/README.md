# Flashcard Learning App - Documentation

This project is a simple flashcard-based learning application implemented in Python using the Tkinter module for the graphical user interface.

## Features

- **Flashcard System**: Displays words and their meanings for learning.
- **Word Storage**: Loads words from a CSV file and keeps track of words to learn.
- **Automated Card Flipping**: Automatically flips the card to reveal the meaning after a delay.
- **Progress Tracking**: Users can mark words as known, and they will be removed from the study list.
- **User-Friendly UI**: Built with Tkinter for an interactive learning experience.

## How It Works

1. **Start the App**: Run the script to open the flashcard learning interface.
2. **View a Word**: The application displays a word on the flashcard.
3. **See the Meaning**: After 3 seconds, the card flips to reveal the meaning.
4. **Mark as Known**: If you know the word, click the "✔" button, and it will be removed from the study list.
5. **Mark as Unknown**: If you don’t know the word, click the "✖" button to move to the next word.
6. **Progress Saves Automatically**: The app keeps track of words you still need to learn.

## File Structure

- **main.py**: The main script that runs the flashcard app.
- **word_list.csv**: The original word list in the data folder.
- **words_to_learn.csv**: The file that stores words the user has yet to master in the data folder.
- **card_front.png**: The front side of the flashcard in the images folder.
- **card_back.png**: The back side of the flashcard in the images folder.
- **right.png**: Image for the "✔" button in the images folder.
- **wrong.png**: Image for the "✖" button in the images folder.

## UI Controls

- **Flashcard Display**: Shows the word initially and flips to reveal the meaning.
- **"✔" Button**: Marks the word as known and removes it from the study list.
- **"✖" Button**: Moves to the next card without removing it from the study list.

## How to Run

### Running from Command Line
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```bash
   pip install pandas
   ```
3. Place the required image and data files in the correct directories.
4. Run the `main.py` file:
   ```bash
   python main.py
   ```
   
### Running on PyCharm  
1. Open **PyCharm** and ensure it is installed on your system.  
2. Click on **File > Open** and select the project folder.  
3. Set up the Python interpreter:  
   - Go to **File > Settings > Project: flashcard_app > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.

## Customization

- **Modify Word List**: Update `data/word_list.csv` to include new words.
- **Change Flip Time**: Modify `window.after(3000, func=flip_card)` to adjust the delay.
- **Enhance UI**: Modify the Tkinter setup for different themes and layouts.

## Dependencies

- Python 3.x
- Tkinter (built-in with Python)
- pandas (for CSV file handling)

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.