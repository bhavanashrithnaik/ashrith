# HANDTRACK: Personalized Virtual Mouse with Secure Access, Brightness & Volume Control

import cv2
import mediapipe as mp
import pyautogui
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import face_recognition
import os
import numpy as np

# Initialize Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Load Known Faces
known_face_encodings = []
known_names = []
path = "faces"
for file in os.listdir(path):
    img = face_recognition.load_image_file(f"{path}/{file}")
    encoding = face_recognition.face_encodings(img)[0]
    known_face_encodings.append(encoding)
    known_names.append(file.split(".")[0])

# Authenticate User
def authenticate_user():
    video = cv2.VideoCapture(0)
    success = False
    while not success:
        ret, frame = video.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)
        for encoding in encodings:
            matches = face_recognition.compare_faces(known_face_encodings, encoding)
            if True in matches:
                name = known_names[matches.index(True)]
                print(f"Authenticated: {name}")
                success = True
                break
        cv2.imshow("Authentication", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    video.release()
    cv2.destroyAllWindows()
    return success

# Get hand landmarks
def get_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    if results.multi_hand_landmarks:
        return results.multi_hand_landmarks[0]
    return None

# Control mouse
def control_mouse(landmarks, width, height):
    index = landmarks.landmark[8]
    x, y = int(index.x * width), int(index.y * height)
    pyautogui.moveTo(x, y)

# Control brightness
def control_brightness(landmarks):
    if abs(landmarks.landmark[4].y - landmarks.landmark[8].y) < 0.05:
        level = int((1 - landmarks.landmark[8].y) * 100)
        sbc.set_brightness(level)

# Control volume
def control_volume(landmarks):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    diff = abs(landmarks.landmark[8].x - landmarks.landmark[4].x)
    level = min(max(diff * 2, 0), 1)
    volume.SetMasterVolumeLevelScalar(level, None)

# Capture Screenshot
def capture_screenshot(landmarks):
    thumb = landmarks.landmark[4]
    index = landmarks.landmark[8]
    if abs(thumb.x - index.x) < 0.02 and abs(thumb.y - index.y) < 0.02:
        pyautogui.screenshot("screenshot.png")
        print("Screenshot captured!")

# Scroll Screen
scroll_state = None

def control_scroll(landmarks):
    global scroll_state
    middle = landmarks.landmark[12]
    ring = landmarks.landmark[16]
    if abs(middle.y - ring.y) < 0.02:
        if scroll_state != "scrolling":
            pyautogui.scroll(-300)  # scroll down
            scroll_state = "scrolling"
    else:
        scroll_state = None

# Main execution
if authenticate_user():
    cap = cv2.VideoCapture(0)
    screen_w, screen_h = pyautogui.size()
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        lm = get_landmarks(frame)
        if lm:
            control_mouse(lm, screen_w, screen_h)
            control_brightness(lm)
            control_volume(lm)
            capture_screenshot(lm)
            control_scroll(lm)
        cv2.imshow("HANDTRACK", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
