# Facial-recognition-system
### 📝 **Project Summary for README**  

This project is a **Facial Recognition System for Employee Entry Management** developed during a hackathon. The system uses **FastAPI (Python)** as the backend and **OpenCV** for face detection. The frontend is a simple **HTML + JavaScript** interface that allows users to capture their face and receive a success message. The goal is to streamline employee entry by recognizing faces instead of relying on traditional methods like ID cards or fingerprint scans.  

The backend runs on **FastAPI**, and the frontend interacts with it via API calls. The system successfully captures a user's face from a webcam and stores it as an image. After capturing, it displays a **confirmation message** on the UI. The project is deployed using **Render (backend)** and **GitHub Pages (frontend)** for public access.  

---

### 🚧 **Challenges Faced During Development**  

1. **OpenCV Camera Issues**  
   - Initially, the webcam **failed to open** due to incorrect device indexing.
   - Fix: Verified the camera index and ensured **cv2.VideoCapture(0)** was working.

2. **cv2.imshow() Assertion Failed Error**  
   - The error **"size.width>0 && size.height>0"** occurred because OpenCV was trying to display an empty frame.
   - Fix: Checked if `frame` was `None` before showing it.

3. **FastAPI Port Binding Error (WinError 10048)**  
   - Running `uvicorn` sometimes resulted in an **"address already in use"** error.
   - Fix: Found and killed the process using port **8000** with:
     ```sh
     netstat -ano | findstr :8000
     taskkill /PID <process_id> /F
     ```

4. **Slow Execution of Face Capture**  
   - The application took too long to capture and save the image.
   - Fix: Optimized the **frame reading and processing loop** for better performance.

5. **Displaying Success Message in UI**  
   - Initially, the UI **did not show** the success message after capturing the face.
   - Fix: Updated the **JavaScript fetch() call** to display messages dynamically.

6. **Deploying FastAPI on Render**  
   - Render deployment failed because **`uvicorn` was not configured properly**.
   - Fix: Used the correct start command:
     ```sh
     uvicorn app:app --host 0.0.0.0 --port 8000
     ```

7. **Deploying the Frontend on GitHub Pages**  
   - GitHub Pages did not support **API calls to localhost**.
   - Fix: Hosted the backend on Render and updated the frontend to call the **Render API URL**.

---

### 🏆 **Final Thoughts**  
This project was a great learning experience, especially in integrating **FastAPI, OpenCV, and JavaScript**. Debugging camera issues, fixing deployment errors, and ensuring smooth interaction between the backend and frontend helped me improve my problem-solving skills.  

🎯 **Next Steps:** Add **database support** for storing captured faces and implement **real-time facial recognition** using deep learning! 🚀  

---

Let me know if you want any edits! 😊
