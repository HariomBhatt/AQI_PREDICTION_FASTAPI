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
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
│
├── models/
│   └── tree_gridcv.pkl
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
├── .gitignore
├── requirements.txt
└── README.md
