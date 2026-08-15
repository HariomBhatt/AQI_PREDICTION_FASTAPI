from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle


app = FastAPI(
    title="AQI Prediction API",
    description="AQI Prediction using Machine Learning",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


with open("tree_gridcv.pkl", "rb") as file:
    model = pickle.load(file)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    T: float = Form(...),
    TM: float = Form(...),
    Tm: float = Form(...),
    SLP: float = Form(...),
    H: float = Form(...),
    VV: float = Form(...),
    V: float = Form(...),
    VM: float = Form(...)
):

    input_data = [[
        T,
        TM,
        Tm,
        SLP,
        H,
        VV,
        V,
        VM
    ]]

    prediction = model.predict(input_data)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "prediction": prediction[0]
        }
    )


class AQIInput(BaseModel):
    T: float
    TM: float
    Tm: float
    SLP: float
    H: float
    VV: float
    V: float
    VM: float


@app.post("/api/predict")
def api_predict(data: AQIInput):

    input_data = [[
        data.T,
        data.TM,
        data.Tm,
        data.SLP,
        data.H,
        data.VV,
        data.V,
        data.VM
    ]]

    prediction = float(model.predict(input_data)[0])

    if prediction <= 50:
        category = "Good"
        message = "Air quality is satisfactory."

    elif prediction <= 100:
        category = "Moderate"
        message = "Air quality is acceptable."

    elif prediction <= 150:
        category = "Unhealthy for Sensitive Groups"
        message = "Sensitive groups may experience health effects."

    elif prediction <= 200:
        category = "Unhealthy"
        message = "Everyone may begin to experience health effects."

    elif prediction <= 300:
        category = "Very Unhealthy"
        message = "Health alert. The risk of health effects is increased."

    else:
        category = "Hazardous"
        message = "Health warning of emergency conditions."

    return {
        "predicted_aqi": round(prediction, 2),
        "category": category,
        "message": message
    }