from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import numpy as np
import cv2
import tensorflow as tf
import os

app = FastAPI(title="Boom Barrier Open-Close Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- PATH SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # /api
STATIC_DIR = os.path.join(BASE_DIR, "static")
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "boom_barrier_open_close_model.h5")

# ---------- STATIC FILES ----------
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

# ---------- LOAD MODEL ----------
model = tf.keras.models.load_model(MODEL_PATH)

# ---------- PREDICT API ----------
@app.post("/predict")
async def predict_barrier_status(file: UploadFile = File(...)):

    image_bytes = await file.read()
    np_arr = np.frombuffer(image_bytes, np.uint8)

    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    confidence = float(np.max(prediction))
    result = "OPEN" if np.argmax(prediction) == 0 else "CLOSED"

    return {
        "prediction": result,
        "confidence": round(confidence, 3)
    }
