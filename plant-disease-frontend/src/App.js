import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [imageFile, setImageFile] = useState(null);
  const [previewURL, setPreviewURL] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  const API_URL = 'http://localhost:8000';

  const fetchPredictions = async () => {
    try {
      const res = await axios.get(`${API_URL}/predictions`);
      // Data is already sorted on backend (latest first)
      setHistory(res.data);
    } catch (err) {
      console.error('Error fetching history:', err);
      alert('Failed to load prediction history.');
    }
  };

  useEffect(() => {
    fetchPredictions();
  }, []);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImageFile(file);
    setPreviewURL(URL.createObjectURL(file));
    setResult(null);
  };

  const handlePredict = async () => {
    if (!imageFile) return alert('Please select an image first.');

    const formData = new FormData();
    formData.append('file', imageFile);

    try {
      setLoading(true);
      const res = await axios.post(`${API_URL}/predict/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setResult(res.data);
      // Add new prediction to the top of history list
      setHistory((prev) => [res.data, ...prev]);
    } catch (err) {
      console.error('Prediction error:', err);
      alert('Prediction failed. Check backend server.');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API_URL}/predictions/${id}`);
      setHistory((prev) => prev.filter((record) => record._id !== id));
    } catch (err) {
      console.error('Delete error:', err);
      alert('Failed to delete prediction.');
    }
  };

  return (
    <div className="App">
      <h1 className="mb-4">🌿 Plant Disease Predictor</h1>

      <div className="upload-section">
        <input type="file" accept="image/*" onChange={handleImageChange} />
        <button className="predict-btn" onClick={handlePredict} disabled={loading}>
          {loading ? 'Predicting...' : 'Predict'}
        </button>
      </div>

      {previewURL && (
        <div className="image-preview">
          <img src={previewURL} alt="Preview" />
        </div>
      )}

      {result && (
        <div className="result-card">
          <h2>🧪 Prediction Result</h2>
          <p><strong>Prediction:</strong> {result.prediction}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(2)}%</p>
        </div>
      )}

      <h2 className="table-title">📊 Prediction History</h2>
      <div className="table-wrapper">
        <table className="styled-table">
          <thead>
            <tr>
              <th>Filename</th>
              <th>Prediction</th>
              <th>Confidence</th>
              <th>Timestamp</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {history.map((record) => (
              <tr key={record._id}>
                <td>{record.filename}</td>
                <td>{record.prediction}</td>
                <td>{(record.confidence * 100).toFixed(2)}%</td>
                <td>{new Date(record.timestamp).toLocaleString()}</td>
                <td>
                  <button className="delete-btn" onClick={() => handleDelete(record._id)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
