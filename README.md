# 🚧 Boom Barrier Open/Close Detection using Computer Vision

## 📌 Project Overview

This project is an **end-to-end Computer Vision application** that detects whether a **boom barrier is OPEN or CLOSED** from an uploaded image.
The system uses a **CNN-based deep learning model**, served through a **FastAPI backend** with a simple **frontend UI**, and is **fully deployed on the cloud** with a live URL.

This project demonstrates the **complete AI/ML lifecycle** — from data collection to deployment.

---

## 🎯 Problem Statement

Boom barriers are widely used in:

* Parking systems
* Toll plazas
* Industrial entry/exit points

Manual monitoring is inefficient.
The goal of this project is to **automatically identify the barrier state (OPEN/CLOSED)** using computer vision.

---

## ✅ Solution Approach

* Treat the task as a **binary image classification problem**
* Train a **CNN model** to classify images into:

  * `OPEN`
  * `CLOSED`
* Build a **REST API** for inference
* Create a **frontend UI** for real-time testing
* Deploy the complete system on **Render (cloud)**

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Collection

* Open-source images collected manually
* Two classes:

  * Boom Barrier Open
  * Boom Barrier Closed
* Final dataset balanced across both classes

### 2️⃣ Data Preprocessing

* Image resizing to `128 × 128`
* Normalization (pixel values scaled between 0–1)
* Conversion to NumPy arrays
* Label encoding for binary classification

### 3️⃣ Model Architecture

* Convolutional Neural Network (CNN)
* Layers used:

  * Conv2D
  * MaxPooling
  * Flatten
  * Dense
* Output layer with Softmax for classification

### 4️⃣ Model Training

* Loss function: Categorical Crossentropy
* Optimizer: Adam
* Evaluation metric: Accuracy

### 5️⃣ Model Evaluation

* Test accuracy ~ **79%**
* Sufficient for proof-of-concept and internship-level project

---

## 🏗️ System Architecture

```
User Image
   ↓
Frontend (HTML/CSS/JS)
   ↓
FastAPI Backend
   ↓
CNN Model (.h5)
   ↓
Prediction (OPEN / CLOSED)
```

---

## 🖥️ Tech Stack Used

### 🔹 Programming & ML

* Python
* TensorFlow / Keras
* OpenCV
* NumPy

### 🔹 Backend

* FastAPI
* Uvicorn

### 🔹 Frontend

* HTML
* CSS
* JavaScript

### 🔹 Deployment & Tools

* GitHub (version control)
* Render (cloud deployment)

---

## 🌐 Live Deployment

The complete application is deployed on **Render** and accessible via a **live URL**.

**Features available on live app:**

* Upload any image
* Preview selected image
* Predict boom barrier status
* Confidence score displayed

---

## 📂 Project Structure

```
repo-root/
│
├── api/
│   ├── main.py
│   └── static/
│       ├── index.html
│       ├── style.css
│       └── script.js
│
├── model/
│   └── boom_barrier_open_close_model.h5
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 🧩 Key Challenges & Fixes

* Handled **relative vs absolute path issues** for cloud deployment
* Resolved **static file serving issues** in FastAPI
* Fixed **Render port binding** using environment variables
* Ensured model loading works across local and cloud environments

---

## 📈 Results

* Correctly predicts boom barrier state
* Real-time inference via UI
* Fully cloud deployed with live demo

---

## 🚀 Future Enhancements

* Add **“Not a Boom Barrier”** detection
* Extend to **video stream / CCTV feed**
* Use **object detection (YOLO)** instead of classification
* Improve dataset size and accuracy
* Edge deployment on embedded devices

---

## 👤 Author

**Chanchal Raikwar**
AI/ML & Computer Vision Enthusiast
End-to-End ML Project with Deployment Experience

---

## 🏁 Conclusion

This project demonstrates practical skills in:

* Computer Vision
* Deep Learning
* API development
* Frontend integration
* Cloud deployment

It reflects real-world problem solving and production-level ML thinking.

