# The Snake Game - Documentation

This project is a classic Snake Game implemented in Python using the Turtle graphics module. The game is interactive, and the player controls the snake's movement to eat food, grow longer, and avoid collisions with the walls or its own tail. The updated version includes high score tracking and the ability to reset the game without restarting the program.

## Features

- **Dynamic Gameplay**: The snake grows longer each time it eats food.
- **Collision Detection**: The game resets when the snake collides with the walls or its own tail.
- **Scoreboard with High Score**: The score is displayed at the top of the screen, and the highest score achieved across sessions is tracked.
- **Customizable Gameplay**: Adjust the screen size, snake speed, and other parameters easily.

## How It Works

1. **Snake Movement**: The snake is made up of segments that follow the head. The player can control the direction of the head using arrow keys.
2. **Food**: A small circle appears randomly on the screen. When the snake's head collides with the food, the snake grows longer, and the score increases.
3. **High Score Tracking**: The highest score is stored in a `data.txt` file and persists even after the program is closed.
4. **Game Reset**: The game resets automatically upon collision, allowing players to continue without restarting the program.

## File Structure

- **main.py**: The main script to initialize and run the game.
- **food.py**: Contains the `Food` class to manage food behavior.
- **scoreboard.py**: Contains the `Scoreboard` class to display and update the player's score and high score.
- **snake.py**: Contains the `Snake` class to handle the snake's movement, growth, and reset functionality.
- **data.txt**: Stores the highest score achieved.

## Controls

- **Arrow Keys**:
  - `Up Arrow`: Move up
  - `Down Arrow`: Move down
  - `Left Arrow`: Move left
  - `Right Arrow`: Move right

## How to Run

### Running from Command Line
1. Make sure you have Python installed on your system.
2. Clone this repository or download the files.
3. Run the `main.py` file:
   ```bash
   python main.py
   ```

### Running on PyCharm  
1. Open **PyCharm** and ensure it is installed on your system.  
2. Click on **File > Open** and select the project folder.  
3. Set up the Python interpreter:  
   - Go to **File > Settings > Project: the_snake_game > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.   

## Customization

- **Screen Size**: Modify the `screen.setup(width, height)` in `main.py` to change the game window size.
- **Snake Speed**: Adjust the `time.sleep()` value in the main game loop to increase or decrease the snake's speed.
- **Food Appearance**: Change the color or size of the food in the `Food` class in `food.py`.
- **High Score File**: Update or reset the `data.txt` file to clear the high score.

## Dependencies

- Python 3.x
- Turtle module (pre-installed with Python)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.



