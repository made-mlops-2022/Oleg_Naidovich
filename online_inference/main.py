from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from data_schema import DataModel
import uvicorn
import pickle
import pandas as pd
import os


app = FastAPI()

model = None
transformer = None


@app.get("/")
async def root():
    return {"message": "hello world!"}


@app.on_event("startup")
def load_model():
    path_to_transformer = os.getenv("PATH_TO_TRANSFORMER")
    path_to_model = os.getenv("PATH_TO_MODEL")
    with open(path_to_transformer, "rb") as file:
        global transformer
        transformer = pickle.load(file)

    with open(path_to_model, "rb") as file:
        global model
        model = pickle.load(file)


@app.post("/predict")
async def predict(data: DataModel):
    data = pd.DataFrame([data.dict()])
    X = transformer.transform(data)
    y = model.predict(X)
    return {"condition": y.tolist()}


@app.get("/health")
async def check_health():
    if model is not None and transformer is not None:
        return "Model is ready to work"
    else:
        raise HTTPException(status_code=505, detail="Model was not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
