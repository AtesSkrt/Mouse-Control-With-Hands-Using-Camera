import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1  # Optimize for one hand
)
mp_draw = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Capture video with reduced resolution for better performance
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Cursor movement smoothing
prev_x, prev_y = 0, 0
smoothing = 1  # Lower value = less delay
sensitivity = 2.0  # Increase sensitivity for faster movement

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe
    results = hands.process(rgb_frame)
    frame_height, frame_width, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Use palm landmarks (index 0, 5, 9, 13, 17) to get the center
            cx, cy = 0, 0
            for idx in [0, 5, 9, 13, 17]:
                cx += hand_landmarks.landmark[idx].x * frame_width
                cy += hand_landmarks.landmark[idx].y * frame_height
            cx, cy = int(cx / 5), int(cy / 5)  # Average center

            # Convert to screen coordinates with increased sensitivity
            screen_x = np.interp(cx, [100, frame_width - 100], [0, screen_width]) * sensitivity
            screen_y = np.interp(cy, [100, frame_height - 100], [0, screen_height]) * sensitivity

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothing
            curr_y = prev_y + (screen_y - prev_y) / smoothing
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Get key points for clicking gestures
            index_finger = hand_landmarks.landmark[8]  # Index finger tip
            thumb = hand_landmarks.landmark[4]  # Thumb tip
            middle_finger = hand_landmarks.landmark[12]  # Middle finger tip

            # Convert to pixel coordinates
            index_x, index_y = int(index_finger.x * frame_width), int(index_finger.y * frame_height)
            thumb_x, thumb_y = int(thumb.x * frame_width), int(thumb.y * frame_height)
            middle_x, middle_y = int(middle_finger.x * frame_width), int(middle_finger.y * frame_height)

            # Calculate distances
            index_thumb_distance = np.hypot(index_x - thumb_x, index_y - thumb_y)
            middle_thumb_distance = np.hypot(middle_x - thumb_x, middle_y - thumb_y)

            # **Left Click** (Index finger and thumb are close)
            if index_thumb_distance < 40:
                pyautogui.click()
                cv2.putText(frame, "Left Click", (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # **Right Click (Optional)** (Middle finger and thumb are close)
            elif middle_thumb_distance < 40:
                pyautogui.rightClick()
                cv2.putText(frame, "Right Click", (cx, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show video feed
    cv2.imshow("Hand Gesture Mouse (With Clicking)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
