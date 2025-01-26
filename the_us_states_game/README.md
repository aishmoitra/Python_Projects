# U.S. States Game - Documentation

This project is an interactive game to help players learn and memorize the U.S. states. The game is implemented in Python using the Turtle graphics module and the Pandas library.

## Features

- **Interactive Gameplay**: Players input state names to identify their locations on a U.S. map.
- **Progress Tracking**: The number of correctly guessed states is displayed in real-time.
- **Learning Aid**: A CSV file of missing states is generated for further study.
- **Dynamic Visualization**: Correctly guessed states are labeled directly on the map.

## How It Works

1. **Map Setup**: The game displays a blank U.S. map using a `.gif` image.
2. **Player Input**: Players are prompted to type the name of a U.S. state.
3. **State Validation**: The game checks if the entered state is valid and hasn’t already been guessed.
4. **State Display**: Correct guesses are marked on the map at the corresponding state's coordinates.
5. **Exiting the Game**: Players can type "Exit" to end the game, after which a CSV file is created listing the states they missed.

## File Structure

- **main.py**: The main script to run the game.
- **50_states.csv**: Contains the list of U.S. states along with their x and y coordinates for map placement.
- **blank_states_img.gif**: The blank map of the U.S. used as the game’s visual background.
- **states_to_learn.csv**: Generated file listing states that were not guessed correctly.

## Controls

- **Text Input**: Players type the name of a U.S. state into a text box that appears during the game.
- **Exit Command**: Type "Exit" to end the game and generate the "states_to_learn.csv" file.

## How to Run

1. Make sure you have Python installed on your system.
2. Install the required dependencies using:
   ```bash
   pip install pandas
   ```
3. Clone this repository or download the files.
4. Run the `main.py` file:
   ```bash
   python main.py
   ```
5. Enter state names in the text input box as prompted and enjoy the game!

## Customization

- **Map Image**: Replace `blank_states_img.gif` with another map image (ensure proper alignment with coordinates).
- **State Data**: Update the `50_states.csv` file to use different data or add more details.
- **Game Title**: Modify the `screen.title()` line to personalize the game's window title.

## Dependencies

- Python 3.x
- Turtle module (pre-installed with Python)
- Pandas library

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.


