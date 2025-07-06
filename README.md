
# 🌿 Plant Disease Prediction Web App

A full-stack AI-powered web app to detect plant diseases from leaf images using a trained deep learning model. Built with **FastAPI** and **React**, and backed by **MongoDB** for storing predictions.

---

## 🚀 Features

- 📸 Upload plant leaf images
- 🤖 Predicts disease using a trained TensorFlow CNN model
- ✅ Shows prediction with confidence score
- 🗃 Saves results in MongoDB Atlas
- 🧠 Uses FastAPI for backend and React for frontend

---

## 🧰 Tech Stack

| Layer       | Technology               |
|-------------|---------------------------|
| Frontend    | React, Bootstrap          |
| Backend     | FastAPI (Python)          |
| AI Model    | TensorFlow / Keras        |
| Database    | MongoDB Atlas             |

---

## 📁 Project Structure

```
PLANT-DISEASE-PREDICT-APP/
│
├── fastapi/
│   ├── main.py             # FastAPI server with prediction API
│   ├── predict.py          # Image preprocessing & model prediction
│   ├── mini_model.h5       # Trained CNN model
│   ├── database.env        # MongoDB URI (not committed to GitHub)
│   └── __pycache__/        # Python cache files
│
├── plant-disease-frontend/
│   ├── public/             # Static assets
│   ├── src/                # React components
│   ├── package.json        # React dependencies
│   ├── package-lock.json
│
├── venv/                   # Python virtual environment
│
├── .gitignore              # Git ignored files (like venv, node_modules, env)
├── README.md               # You're reading it now
└── 2025-06-21_06-00-03.mp4 # Optional demo video (not required)
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PLANT-DISEASE-PREDICT-APP.git
cd PLANT-DISEASE-PREDICT-APP
```

### ✅ 2. Backend Setup (FastAPI)

```bash
cd fastapi
python -m venv venv
source venv/bin/activate     # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create `database.env` in the `fastapi/` folder:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster-url/plant_db?retryWrites=true&w=majority
```

Run the backend server:

```bash
uvicorn main:app --reload
```

### ✅ 3. Frontend Setup (React)

```bash
cd ../plant-disease-frontend
npm install
npm start
```

---

## 🔗 Running the App

- Frontend: `http://localhost:3000/`
- Backend API: `http://localhost:8000/predict/`

---

## 🧪 Example Output

```
Prediction: Potato Early Blight
Confidence: 95.76%
```

---

## 📦 Requirements

**`requirements.txt` (for backend):**

```txt
fastapi
uvicorn
tensorflow
pillow
numpy
python-dotenv
pymongo
```

---

## 📌 To-Do

- [ ] Add progress/loading UI during prediction
- [ ] Deploy backend (Render) & frontend (Vercel/Netlify)
- [ ] Add image upload history view

---

## 📬 Author

Made by **M.Hamiz Siddiqui**

📧 Email: m.hamizsiddiqui@gmail.com

🔗 LinkedIn: www.linkedin.com/in/muhammad-hamiz-siddiqui-b21280294

