😊 Emotion Sentiment Analysis Project
A Machine Learning-powered web application that classifies text into six core emotions. This project bridges the gap between raw Natural Language Processing (NLP) and a user-friendly interface.

🚀 Overview
This project takes a user's text input and predicts the underlying emotion using a trained classification model. It was developed to demonstrate the end-to-end process of data cleaning, vectorization, model training, and deployment.

🛠️ Tech Stack
Language: Python 3.14
ML Library: Scikit-Learn
NLP Technique: TF-IDF Vectorization
UI Framework: Streamlit
Model Persistence: Joblib

📊 How It Works
The project follows a standard NLP pipeline:
Preprocessing: Raw text is cleaned and standardized.
Vectorization: The columns.pkl (TF-IDF) converts words into a numerical feature matrix.
Prediction: The model.pkl (Classifier) analyzes the features to predict an emotion label.
Mapping: Numerical results (0-5) are mapped to human-readable emotions:
0: Sadness | 1: Anger | 2: Love | 3: Surprise | 4: Fear | 5: Joy


If you want to run this project on your own machine:
Navigate to the project folder in your terminal.
Launch the app using:
(Bash) python -m streamlit run app.py
Open your browser to the local URL provided (usually http://localhost:8501).
