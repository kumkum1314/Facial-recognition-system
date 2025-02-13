from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
import face_recognition # type: ignore
import pickle
import sqlite3
from io import BytesIO

app = FastAPI()

# Database setup
conn = sqlite3.connect("employees.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        encoding BLOB
    )
""")
conn.commit()

def get_face_encoding(image):
    """Extract face encoding from an image"""
    npimg = np.frombuffer(image, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    face_encodings = face_recognition.face_encodings(frame)
    return face_encodings[0] if face_encodings else None

@app.post("/register/")
async def register_employee(name: str, file: UploadFile = File(...)):
    """Register employee face"""
    image = await file.read()
    encoding = get_face_encoding(image)
    
    if encoding is None:
        return {"status": "error", "message": "No face detected!"}
    
    cursor.execute("INSERT INTO employees (name, encoding) VALUES (?, ?)", (name, pickle.dumps(encoding)))
    conn.commit()
    return {"status": "success", "message": f"Employee {name} registered!"}

@app.post("/verify/")
async def verify_employee(file: UploadFile = File(...)):
    """Verify employee face"""
    image = await file.read()
    encoding = get_face_encoding(image)

    if encoding is None:
        return {"status": "error", "message": "No face detected!"}
    
    cursor.execute("SELECT name, encoding FROM employees")
    employees = cursor.fetchall()

    for name, enc in employees:
        stored_encoding = pickle.loads(enc)
        if face_recognition.compare_faces([stored_encoding], encoding)[0]:
            return {"status": "success", "message": f"Employee verified: {name}"}
    
    return {"status": "error", "message": "Employee not recognized!"}
