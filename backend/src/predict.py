import joblib



import os

from src.featurize import smiles_to_fingerprint

# Get absolute model path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "best_model.pkl"
)
# Load trained model
model = joblib.load(MODEL_PATH)

def predict_solubility(smiles: str):

    # Convert SMILES to fingerprint
    fingerprint = smiles_to_fingerprint(smiles)

    if fingerprint is None:
        return {"error": "Invalid SMILES string"}

    # Predict solubility
    prediction = model.predict(fingerprint)

    return {
        "smiles": smiles,
        "predicted_solubility": float(prediction[0])
    }