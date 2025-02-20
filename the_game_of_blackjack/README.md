# The Game of Blackjack - Documentation

This project is a console-based Blackjack game implemented in Python. The player competes against the computer to achieve the highest score without exceeding 21.

## Features

- **Interactive Gameplay**: Players can choose to draw more cards or pass their turn.
- **Blackjack Logic**: Automatic handling of special rules such as Blackjack and Ace adjustments.
- **Randomized Deck**: Cards are dealt randomly for each game session.

## How It Works

1. **Card Dealing**:
   - Both the player and the computer start with two cards.
   - The player can decide to draw additional cards or keep their hand.
   - The computer will draw cards until its score is 17 or higher.

2. **Scoring**:
   - Aces can count as either 11 or 1, depending on the total score.
   - A two-card score of 21 is considered a "Blackjack" and automatically wins unless both have it.

3. **Win/Lose Conditions**:
   - The player or computer goes over 21: they lose.
   - The highest score under or equal to 21 wins.
   - Draws occur if both scores are equal.

## File Structure

- **art.py**: Contains the ASCII art logo for the game.
- **main.py**: The main script to run the game and implement the game logic.

## Controls

- During the game, type:
  - `y` to draw another card.
  - `n` to pass your turn and let the computer play.

## How to Run  

### Running from Command Line  
1. Ensure Python is installed on your system.  
2. Clone this repository or download the files.  
3. Open a terminal and navigate to the project directory.  
4. Run the `main.py` file:  
   ```bash
   python main.py
   ```

### Running on PyCharm  
1. Open **PyCharm** and ensure it is installed on your system.  
2. Click on **File > Open** and select the project folder.  
3. Set up the Python interpreter:  
   - Go to **File > Settings > Project: the_game_of_blackjack > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.   

## Customization

- **Deck Composition**: Modify the `cards` list in the `deal_card()` function to include additional cards or adjust the values.
- **Game Rules**: Adjust the computer's behavior or scoring logic in the `play_game()` function.
- **Interface**: Replace the console-based interface with a graphical one for an enhanced user experience.

## Dependencies

- Python 3.x

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as you wish.

