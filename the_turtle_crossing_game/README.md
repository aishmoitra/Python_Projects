# Turtle Crossing Game - Documentation

This project is a Turtle Crossing Game implemented in Python using the Turtle graphics module. The player controls a turtle trying to cross a busy road filled with moving cars. The goal is to reach the top of the screen without colliding with the cars. The game becomes progressively more challenging as the player's level increases.

## Features

- **Dynamic Gameplay**: Cars are generated at random intervals and move across the screen at increasing speeds.
- **Collision Detection**: The game ends when the player collides with a car.
- **Level System**: Each time the player successfully crosses the road, the level increases, and the cars move faster.
- **Scoreboard**: Displays the current level and shows "GAME OVER" when the game ends.

## How It Works

1. **Player Movement**: The player is a turtle controlled using the "Up" arrow key. The player starts at the bottom of the screen and aims to reach the top.
2. **Car Movement**: Cars are randomly generated and move horizontally across the screen. Their speed increases as the player levels up.
3. **Collision Detection**: The game checks for collisions between the player and cars. If a collision occurs, the game ends.
4. **Level Progression**: When the player reaches the top of the screen, they are returned to the starting position, the level increases, and car speed ramps up.

## File Structure

- **main.py**: The main script to initialize and run the game.
- **car_manager.py**: Contains the `CarManager` class to manage car generation, movement, and speed.
- **player.py**: Contains the `Player` class to manage the player's movement and position.
- **scoreboard.py**: Contains the `Scoreboard` class to display and update the player's level and end the game.

## Controls

- **Arrow Keys**:
  - `Up Arrow`: Move up

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
   - Go to **File > Settings > Project: the_turtle_crossing_game > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.   

## Customization

- **Screen Size**: Modify the `screen.setup(width, height)` in `main.py` to change the game window size.
- **Car Speed**: Adjust the `STARTING_MOVE_DISTANCE` and `MOVE_INCREMENT` in `car_manager.py` to change the initial car speed and speed increment per level.
- **Car Appearance**: Change the color or size of the cars in the `create_car()` method in `CarManager`.
- **Player Movement**: Adjust the `MOVE_DISTANCE` in `player.py` to change how far the turtle moves with each key press.

## Dependencies

- Python 3.x
- Turtle module (pre-installed with Python)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.

