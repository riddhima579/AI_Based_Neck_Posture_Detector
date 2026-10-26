# AI-Based Neck Posture Detector

## Overview
The AI-Based Neck Posture Detector is a real-time posture monitoring project developed using Python, OpenCV, and MediaPipe Pose. It uses webcam input to identify body landmarks, calculate a posture angle, and provide visual and voice alerts when poor posture is detected.

The project aims to promote posture awareness and encourage better sitting habits.

## Objectives
- Detect body landmarks using MediaPipe Pose.
- Calculate the angle between the ear, shoulder, and hip.
- Identify posture based on a predefined angle threshold.
- Display posture status and angle on the screen.
- Provide a voice alert when poor posture is detected.

## Technologies Used
- **Python** – Main programming language
- **OpenCV** – Webcam access and image processing
- **MediaPipe Pose** – Body landmark detection
- **NumPy** – Angle calculation
- **pyttsx3** – Text-to-speech alerts

## How It Works
1. The webcam captures live video frames.
2. MediaPipe Pose detects body landmarks.
3. The left ear, left shoulder, and left hip landmarks are extracted.
4. The angle between these points is calculated.
5. If the angle is below **150°**, the system displays a poor-posture warning and provides a voice alert.
6. Otherwise, the system displays a good-posture message.

## Features
- Real-time webcam-based posture monitoring
- Body landmark visualization
- Posture angle calculation and display
- Visual warnings for poor posture
- Voice alerts to encourage sitting straight

## Installation

### Prerequisites
- Python installed on your computer
- A working webcam
- Visual Studio Code or another Python editor

### Install Dependencies
Run the following command in the terminal:

```bash
pip install opencv-python mediapipe numpy pyttsx3
```

## How to Run
1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required dependencies.
4. Run the Python script:

```bash
python posture_detector.py
```

5. Allow webcam access if prompted.
6. Press **Esc** to close the application.

## Limitations
- Detection depends on webcam positioning and lighting conditions.
- The system uses a predefined angle threshold of 150°.
- Posture classification may be affected by camera perspective and landmark detection accuracy.
- The system is intended for posture awareness and educational purposes, not medical diagnosis.

## Future Scope
- Posture monitoring using IoT-enabled devices
- Mobile application integration
- Posture history and data logging
- Improved posture detection under different viewing conditions

## Author
Developed as an academic project in Artificial Intelligence and Machine Learning for Medical Applications.
