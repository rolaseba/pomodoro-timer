# Pomodoro Timer Application

This is a Pomodoro timer application that helps manage work and break intervals based on the Pomodoro Technique. The application reads configuration settings from a JSON file, displays ASCII art, and plays audio notifications for work and break periods.

**Pomodoro Technique** is a time management method that involves breaking work into intervals, typically 25 minutes long, followed by short breaks. After completing a set number of Pomodoros (work intervals), you take a longer break. Once the long break is taken, the Pomodoros count resets to zero, and a basket count increments by one. This basket feature is my custom addition to track completed cycles of Pomodoros.

## Features

- Configurable work and break durations.
- Audio notifications for different phases.
- Visual display of the number of Pomodoros completed.
- Automatic clearing of the screen between phases.
- ASCII art display for Pomodoro information and long break messages.

## Requirements

- Python 3.11.9
- `pygame` library
- `tqdm` library
- `art` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/pomodoro-timer.git
    ```

2. Navigate to the project directory:

    ```sh
    cd pomodoro-timer
    ```

3. Install the required libraries:

    ```sh
    pip install pygame tqdm art
    ```

## Configuration

Create a `config.json` file in the project directory with the following structure:

```json
{
    "work_duration": 25,
    "short_break_duration": 5,
    "long_break_duration": 15,
    "pomodoros_before_long_break": 4,
    "text_for_long_break": "Take a Long Break!",
    "audio_notification": true,
    "audio_file_work": "start_work.mp3",
    "audio_file_break": "start_break.mp3",
    "audio_file_long_break": "start_long_break.mp3"
}
```

- `work_duration`: Duration of the work period in minutes.
- `short_break_duration`: Duration of the short break in minutes.
- `long_break_duration`: Duration of the long break in minutes.
- `pomodoros_before_long_break`: Number of Pomodoros before a long break.
- `text_for_long_break`: Text to display during the long break.
- `audio_notification`: Whether to play audio notifications (true/false).
- `audio_file_work`: Path to the audio file for the start of work periods.
- `audio_file_break`: Path to the audio file for the start of short breaks.
- `audio_file_long_break`: Path to the audio file for the start of long breaks.

## Usage

To run the Pomodoro timer application, execute the following command:

```sh
python pomodoro.py
```

## Code Overview

- `load_config(config_file)`: Loads configuration from a JSON file.
- `run_timer(minutes, message)`: Runs a timer for a specified number of minutes with a progress bar.
- `clean_screen()`: Clears the terminal screen.
- `print_pomodoro_info(pomodoros, pomodoro_basket, pomodoros_before_long_break, pomodoro_art)`: Prints Pomodoro information with ASCII art.
- `play_audio_notification(audio_file)`: Plays an audio notification.
- `main()`: Main function to run the Pomodoro timer application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
