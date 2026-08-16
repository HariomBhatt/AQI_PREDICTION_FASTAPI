# AQI Prediction using FastAPI and Machine Learning

A machine learning web application that predicts Air Quality Index (AQI)
using environmental and weather parameters.

The project uses FastAPI as the backend and a trained Decision Tree
regression model for AQI prediction.

## Features

- AQI prediction using Machine Learning
- FastAPI REST API
- Pydantic request validation
- Interactive Swagger API documentation
- HTML web interface using Jinja2
- AQI category classification
- Responsive frontend
- Pre-trained Scikit-learn model

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Pydantic
- Jinja2
- HTML
- CSS

## Project Structure

```text
AQI_PREDICTION_FASTAPI/
│
├── venv/
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   └── result.html
│
├── static/
│   └── css/
│       └── styles.css
│
├── main.py
├── tree_gridcv.pkl
├── requirements.txt
└── .gitignore


                    YOUR AQI APPLICATION

                         FastAPI
                            │
              ┌─────────────┴─────────────┐
              │                           │
       Web Application               REST API
              │                           │
     HTML + Jinja2 templates        /api/predict
              │                           │
       /predict POST                JSON request
              │                           │
              └─────────────┬─────────────┘
                            ↓
                    ML Model (.pkl)
                            ↓
                    AQI Prediction
