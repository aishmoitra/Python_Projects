# Pomodoro Timer - Documentation

This project is a simple Pomodoro timer implemented in Python using the Tkinter module for the graphical user interface.

## Features

- **Work and Break Sessions**: Automatically alternates between work sessions and short/long breaks based on the Pomodoro technique.
- **Customizable Timer Durations**: Set work, short break, and long break durations in minutes.
- **Visual Countdown**: Displays a dynamic timer countdown in the UI.
- **Session Tracking**: Uses checkmarks to track completed work sessions.
- **Reset Functionality**: Allows resetting the timer at any time.

## How It Works

1. **Start the Timer**: Click the "Start" button to begin a Pomodoro session.
2. **Automatic Transitions**:
   - 25-minute work session → 5-minute short break
   - Every 4th work session → 30-minute long break
3. **Session Tracking**: Each completed work session adds a checkmark (✅).
4. **Reset Timer**: Clicking "Reset" cancels the timer and resets the UI.

## File Structure

- **main.py**: The main script that runs the Pomodoro timer.
- **tomato.png**: Image used for the UI representation of the timer.

## UI Controls

- **Start Button**: Begins the timer and cycles through work/break sessions.
- **Reset Button**: Stops the timer and resets progress.

## How to Run

1. Make sure you have Python installed on your system.
2. Install Tkinter (pre-installed with Python).
3. Clone this repository or download the files.
4. Run the `main.py` file:
   ```bash
   python main.py
   ```

## Customization

- **Modify Timer Durations**: Change the values of `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` in `main.py`.
- **Change UI Appearance**: Modify colors and fonts in the constants section.
- **Replace Timer Image**: Swap `tomato.png` with another image if desired.

## Dependencies

- Python 3.x
- Tkinter (built-in with Python)

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.