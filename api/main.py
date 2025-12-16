from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import numpy as np
import cv2
import tensorflow as tf

# -------------------------------------------------
# Create FastAPI app
# -------------------------------------------------
app = FastAPI(title="Boom Barrier Open-Close Detection API")

# -------------------------------------------------
# CORS: frontend (HTML/JS) ko backend access dene ke liye
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # kisi bhi frontend se request allow
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# STATIC FILES: frontend files yahin se serve honge
# /static/style.css, /static/script.js etc.
# -------------------------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# -------------------------------------------------
# Load trained ML model (backend logic same, no change)
# -------------------------------------------------
model = tf.keras.models.load_model("../model/boom_barrier_open_close_model.h5")

# -------------------------------------------------
# ROOT ROUTE: browser par frontend page dikhega
# -------------------------------------------------
@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# -------------------------------------------------
# PREDICTION API: image upload → OPEN / CLOSED
# -------------------------------------------------
@app.post("/predict")
async def predict_barrier_status(file: UploadFile = File(...)):

    # Read uploaded image
    image_bytes = await file.read()
    np_arr = np.frombuffer(image_bytes, np.uint8)

    # Decode and preprocess image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Model prediction
    prediction = model.predict(img)
    confidence = float(np.max(prediction))
    result = "OPEN" if np.argmax(prediction) == 0 else "CLOSED"

    return {
        "prediction": result,
        "confidence": round(confidence, 3)
    }
