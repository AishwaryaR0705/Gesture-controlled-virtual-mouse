# AI Gesture Controlled Virtual Mouse
This project implements a Virtual Mouse that allows users to control their computer using hand gestures captured through a webcam. It uses computer vision techniques to detect hand landmarks and translate them into mouse movements and actions.

## Features
-Move the mouse cursor using the index finger
-Left click using thumb and index finger gesture
-Right click using thumb and middle finger gesture
-Drag and drop functionality
-Scroll up and down using two-finger gesture
-Real-time hand tracking using webcam

## Technologies Used
-Python
-OpenCV
-MediaPipe
-PyAutoGUI

## How the System Works
The system captures video from the webcam and detects hand landmarks using MediaPipe. Specific finger positions and distances are used to interpret gestures. These gestures are then mapped to mouse operations such as cursor movement, clicking, dragging, and scrolling.

## Installation
1. Install Python (3.8 or above)
2. Install required libraries
pip install opencv-python mediapipe pyautogui
3. Clone the repository
git clone https://github.com/AishwaryaR0705/Gesture-controlled-virtual-mouse.git
4. Run the program
python main.py

## Project Demo
The webcam tracks the user's hand and detects gestures in real time. These gestures are converted into mouse commands allowing touchless interaction with the computer.

## Author
Aishwarya Raju
Cs-IOT Cybersecurity including Blockchain student
