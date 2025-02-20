# The Pong Game - Documentation

This project is a classic Pong Game implemented in Python using the Turtle graphics module. The game is designed for two players, who compete by controlling paddles to hit a bouncing ball and score points.

## Features

- **Two-Player Gameplay**: Players can control paddles to prevent the ball from passing and score points when the opponent misses.
- **Dynamic Ball Movement**: The ball moves across the screen, bounces off walls, and increases in speed after each paddle hit.
- **Scoreboard**: A live scoreboard keeps track of each player’s points.
- **Collision Detection**: The ball bounces off walls and paddles or resets when a paddle misses.

## How It Works

1. **Paddle Control**: Each player controls a paddle to hit the ball.
   - The right paddle is controlled using the `Up` and `Down` arrow keys.
   - The left paddle is controlled using the `W` (up) and `S` (down) keys.
2. **Ball Movement**: The ball moves across the screen and bounces off walls and paddles. If the ball misses a paddle, the other player scores a point, and the ball resets.
3. **Scoring**: 
   - A point is added to the left player’s score when the right paddle misses.
   - A point is added to the right player’s score when the left paddle misses.

## File Structure

- **main.py**: The main script to initialize and run the game.
- **ball.py**: Contains the `Ball` class to manage the ball's movement, speed, and collision behavior.
- **paddle.py**: Contains the `Paddle` class to create paddles and handle their movement.
- **scoreboard.py**: Contains the `Scoreboard` class to display and update the player scores.

## Controls

- **Right Paddle**:
  - `Up Arrow`: Move paddle up
  - `Down Arrow`: Move paddle down
- **Left Paddle**:
  - `W`: Move paddle up
  - `S`: Move paddle down

## How to Run
### Running from Command Line
1. Ensure Python is installed on your system.
2. Clone or download the repository.
3. Run the `main.py` file:
   ```bash
   python main.py
   ```
   
### Running on PyCharm  
1. Open **PyCharm** and ensure it is installed on your system.  
2. Click on **File > Open** and select the project folder.  
3. Set up the Python interpreter:  
   - Go to **File > Settings > Project: the_pong_game > Python Interpreter**  
   - Choose the appropriate Python version.  
4. Open `main.py` in the editor.  
5. Click the **Run** button (▶) in the top-right corner or press `Shift + F10` to execute the script.   


## Customization

- **Screen Size**: Modify `screen.setup(width, height)` in `main.py` to adjust the game window dimensions.
- **Ball Speed**: Adjust the `move_speed` value in the `Ball` class in `ball.py` to change the initial speed of the ball.
- **Paddle Dimensions**: Update the `shapesize` method in the `Paddle` class in `paddle.py` to resize the paddles.
- **Scoreboard Font**: Customize the font style or size in the `Scoreboard` class in `scoreboard.py`.

## Dependencies

- Python 3.x
- Turtle module (pre-installed with Python)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you like.