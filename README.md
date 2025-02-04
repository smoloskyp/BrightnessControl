# Brightness Control

This program automatically adjusts the screen brightness based on the room's lighting using a camera. It analyzes the captured image and adjusts the monitor brightness accordingly. A hotkey (default: F9) is used to control brightness adjustment.

## Features

- Capturing an image from the camera.
- Analyzing the lighting level.
- Automatically adjusting monitor brightness.
- Using the hotkey (`F9`) to manually change brightness.

## Requirements

Before running the program, install all dependencies:
- Python 3.10+
- Modules:
  - `screen-brightness-control`
  - `keyboard`
  - `numpy`
  - `opencv-python`
  - `wmi`

## Usage

1. Run the program.
2. Press `F9` to update the brightness.
3. The program runs in the background and waits for the hotkey press.

## License
This project is licensed under the MIT License.
