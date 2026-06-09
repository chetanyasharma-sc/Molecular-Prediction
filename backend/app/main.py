from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.predict import predict_solubility

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MoleculeInput(BaseModel):
    smiles: str

@app.post("/predict")
def predict(data: MoleculeInput):
    return predict_solubility(data.smiles)