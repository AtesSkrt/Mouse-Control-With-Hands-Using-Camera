# 🖱️ Mouse Control with Hand Gestures Using Camera

This project allows you to control the mouse cursor using hand gestures, leveraging **OpenCV**, **MediaPipe**, and **PyAutoGUI** for smooth tracking and interaction.

## 🚀 Features
- **Hand Tracking**: Uses **MediaPipe** to detect hands in real-time.
- **Cursor Control**: Moves the mouse based on the **center of the palm**.
- **Gesture-Based Clicks**:
  - **Left Click**: Touch **index finger & thumb**.
  - **Right Click**: Touch **middle finger & thumb** (optional).
- **Increased Sensitivity**: Move the cursor faster with less hand movement.
- **Optimized Performance**: Lower resolution & single-hand tracking for better FPS.

## 📦 Dependencies
Ensure you have the following Python libraries installed:
```bash
pip install opencv-python mediapipe pyautogui numpy
```

## 📜 How to Run
1. **Clone the Repository**
```bash
git clone https://github.com/YourUsername/Mouse-Control-With-Hands-Using-Camera.git
cd Mouse-Control-With-Hands
```

2. **Run the Script**
```bash
python mouse_control.py
```

3. **Controls**
- **Move Hand** → Moves the cursor.
- **Index & Thumb Close** → Left Click.
- **Middle & Thumb Close** → Right Click.
- **Press 'Q'** → Exit the program.

## 🛠️ Customization
Modify these variables in `mouse_control.py` to tweak performance:
```python
sensitivity = 2.5  # Adjust cursor speed
smoothing = 3  # Lower = smoother movement
```


## 🤝 Contributing
Pull requests are welcome! Open an issue for feature requests or bug reports.

## 📜 License
MIT License. Feel free to use and modify!

