from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import io
import os

# Safe model loading
#model_path = "mini_model.h5"
model_path = os.path.join(os.path.dirname(__file__), "mini_model.h5")


if not os.path.exists(model_path):
    raise FileNotFoundError("❌ Model file 'mini_model.h5' not found. Please place it in the backend directory.")

model = load_model(model_path)
print("✅ Model loaded successfully.")

# 0-based indexing
labels = {
    0: "Potato early blight",
    1: "Potato healthy",
    2: "Potato late blight",
    3: "Tomato bacterial spot",
    4: "Tomato early blight",
    5: "Tomato healthy",
    6: "Tomato late blight",
    7: "Tomato leaf mold",
    8: "Tomato septoria leaf spot",
    9: "Tomato spider mites two-spotted spider",
    10: "Tomato target spot",
    11: "Tomato mosaic virus",
    12: "Tomato yellow leaf curl virus",
    13: "Corn cercospora leaf spot gray leaf spot",
    14: "Corn common rust",
    15: "Corn healthy",
    16: "Corn northern leaf blight"
}

# Prediction function
def make_prediction(image_bytes):
    try:
        print("🖼️ Received image. Starting preprocessing...")
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((224, 224))  # Adjust based on model input
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        print("🧠 Making prediction...")
        prediction = model.predict(img_array)
        print("🔢 Prediction vector:", prediction)

        class_idx = np.argmax(prediction[0])
        confidence = float(np.max(prediction[0]))
        label = labels[class_idx]

        print(f"✅ Prediction result: {label} ({confidence:.2f})")
        return label, confidence

    except Exception as e:
        print("❌ Error during prediction:", e)
        raise e
