from fastapi import FastAPI, File, UploadFile, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from app.predict import make_prediction
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

# Load environment variables
load_dotenv(dotenv_path="app/database.env")
print("🔌 Mongo URI:", os.getenv("MONGO_URI"))

app = FastAPI()

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client["plant_db"]
collection = db["predictions"]

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predictions")
def get_predictions():
    results = []
    for doc in collection.find():
        doc["_id"] = str(doc["_id"])
        results.append(doc)
    return results

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_data = await file.read()
    label, confidence = make_prediction(image_data)

    result = {
        "filename": file.filename,
        "prediction": label,
        "confidence": round(confidence, 3),
        "timestamp": datetime.now()
    }

    #collection.insert_one(result)
    #return {"prediction": label, "confidence": confidence}
    insert_result = collection.insert_one(result)
    result["_id"] = str(insert_result.inserted_id)  # <-- Add this line
    return result  # <-- And return full data

@app.delete("/predictions/{prediction_id}")
def delete_prediction(prediction_id: str = Path(...)):
    try:
        result = collection.delete_one({"_id": ObjectId(prediction_id)})
        if result.deleted_count == 1:
            return {"message": "Deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Prediction not found")
    except Exception as e:
        print("❌ Error deleting:", e)
        raise HTTPException(status_code=400, detail="Invalid ID format")
