
# Dino Game with Hand Gesture Control

This project uses hand gesture recognition to play the Chrome Dino game by simulating the "spacebar" press when the user's hand moves up.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

## Overview

This project leverages the power of **MediaPipe** and **OpenCV** to track hand gestures and simulate keypresses to interact with the **Chrome Dino** game (the offline dinosaur game in the Chrome browser). By using the hand's Y-coordinate movement, the program triggers a "space" keypress whenever the hand moves upwards significantly, making the dinosaur jump.

## Features

- Tracks hand movements in real-time using the webcam.
- Simulates pressing the "spacebar" key when the hand moves upwards.
- Allows for interaction with the Dino game (https://chromedino.com) using hand gestures.
- Requires no physical controller, enabling hands-free play.

## Technologies Used

- **Python**: Main programming language used for this project.
- **OpenCV**: For capturing and processing video frames from the webcam.
- **MediaPipe**: For hand tracking and gesture recognition.
- **PyAutoGUI**: For simulating keypresses to control the game.
- **Selenium**: For launching and interacting with the Chrome Dino game in the browser.

## Setup Instructions

### Prerequisites

Before you begin, ensure that you have the following installed:

1. **Python** (version 3.x recommended).
2. **Google Chrome** and the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed on your machine.

### Install Dependencies

Clone the repository:

```bash
git clone https://github.com/your-username/dino-game-hand-gesture.git
cd dino-game-hand-gesture
```

Install the required libraries:

```bash
pip install opencv-python mediapipe pyautogui selenium
```

Make sure you have the appropriate version of **ChromeDriver** compatible with your version of Google Chrome.

### Running the Game

1. Run the script:

```bash
python dino_game_hand_control.py
```

2. The script will open the Dino game in your browser and start tracking your hand movements.
3. Raise your hand vertically to make the dinosaur jump (triggering the "space" keypress).
4. The game continues until you close the window.

## Usage

- **Webcam setup**: Ensure that your webcam is connected and working properly.
- **Control**: Raise your hand to trigger the "space" key press, which causes the dinosaur to jump.
- **Adjust sensitivity**: You can adjust the `prev_y - y > 100` threshold in the code for more or less sensitivity based on your preferences.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

