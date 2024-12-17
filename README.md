# Volume and Brightness Control using Hand Gestures

## Introduction
This project enables users to control the system’s volume and screen brightness using hand gestures. The application utilizes a combination of computer vision, gesture recognition, and system control libraries to provide an intuitive and touch-free way of managing these settings.

---

## Features
- **Volume Control**: Adjust the system's volume by specific hand gestures.
- **Brightness Control**: Increase or decrease screen brightness through predefined gestures.
- **Real-Time Gesture Recognition**: Smooth and responsive gesture detection.
- **Customizable Thresholds**: Modify sensitivity and gesture mappings as per user preference.
- **Cross-Platform Support**: Works on Windows, macOS, and Linux with minor adjustments.

---

## Requirements

### Hardware:
- A webcam (integrated or external).

### Software:
- Python 3.7 or higher.
- Required Python Libraries:
  - OpenCV
  - Mediapipe
  - Pycaw (for Windows volume control)
  - Screen-brightness-control (for brightness adjustment)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/volume-brightness-gestures.git
   cd volume-brightness-gestures
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) For Linux and macOS users, ensure you have appropriate permissions for controlling volume and brightness.

---

## Usage
1. **Run the Application:**
   ```bash
   python gesture_control.py
   ```

2. **Hand Gestures:**
   - **Volume Control:**
     - Move your index and thumb fingers closer to reduce volume.
     - Move them apart to increase volume.
   - **Brightness Control:**
     - Use a similar pinching motion but in a vertical orientation.

3. **Exit:**
   - Press `Ctrl+C` in the terminal to stop the program.

---

## Configuration
You can adjust thresholds and gestures by modifying the `config.json` file:
```json
{
  "volume_sensitivity": 5,
  "brightness_sensitivity": 3,
  "gesture_timeout": 0.5
}
```
- `volume_sensitivity`: Controls how quickly the volume changes.
- `brightness_sensitivity`: Controls brightness adjustment speed.
- `gesture_timeout`: Prevents rapid gesture changes within the timeout duration.

---

## Troubleshooting
- **Gesture Not Detected:**
  - Ensure good lighting conditions.
  - Position your hand within the camera’s view.

- **Permission Errors:**
  - On Linux/macOS, run the script with elevated permissions.

- **Dependencies Issue:**
  - Verify all required libraries are installed.
  - Use a virtual environment to avoid conflicts.

---

## Acknowledgments
This project leverages the following technologies:
- [OpenCV](https://opencv.org/)
- [Mediapipe](https://google.github.io/mediapipe/)
- [Pycaw](https://github.com/AndreMiras/pycaw)
- [Screen-brightness-control](https://github.com/Crozzers/screen-brightness-control)

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request with detailed explanations of changes.

---

## Contact
For queries, issues, or feedback, please reach out via the GitHub repository’s [issues page](https://github.com/your-repo/volume-brightness-gestures/issues).

