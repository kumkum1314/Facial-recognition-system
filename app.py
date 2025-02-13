import streamlit as st
import cv2
import numpy as np
import requests
from PIL import Image

API_URL = "http://127.0.0.1:8000"  # Backend URL

import cv2

def capture_face():
    cap = cv2.VideoCapture(0)  # Ensure 0 is correct (1 or 2 if you have multiple cameras)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("Press 'q' to capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return frame

# Call the function
frame = capture_face()
if frame is not None:
    cv2.imwrite("captured_face.jpg", frame)
    print("Face captured successfully.")
else:
    print("Failed to capture face.")

def register_employee():
    """Register a new employee"""
    name = st.text_input("Enter Employee Name:")
    
    if st.button("Capture & Register"):
        frame = capture_face()
        _, img_encoded = cv2.imencode(".jpg", frame)
        files = {"file": img_encoded.tobytes()}
        response = requests.post(f"{API_URL}/register/?name={name}", files=files)
        st.success(response.json()["message"])

def verify_employee():
    """Verify an employee"""
    if st.button("Capture & Verify"):
        frame = capture_face()
        _, img_encoded = cv2.imencode(".jpg", frame)
        files = {"file": img_encoded.tobytes()}
        response = requests.post(f"{API_URL}/verify/", files=files)
        st.success(response.json()["message"])

st.title("Facial Recognition System")
option = st.sidebar.selectbox("Choose an option", ["Register", "Verify"])

if option == "Register":
    register_employee()
elif option == "Verify":
    verify_employee()
