import os
import joblib
from rdkit import Chem
from rdkit.Chem import Draw
from src.featurize import smiles_to_fingerprint

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")

model = joblib.load(MODEL_PATH)

def solubility_category(logs: float):
    if logs > 0:
        return "Highly soluble"
    elif logs > -2:
        return "Moderately soluble"
    elif logs > -4:
        return "Poorly soluble"
    return "Very poorly soluble"

def molecule_svg(smiles: str):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    drawer = Draw.MolDraw2DSVG(300, 220)
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()

    return drawer.GetDrawingText()

def predict_solubility(smiles: str):
    fingerprint = smiles_to_fingerprint(smiles)

    if fingerprint is None:
        return {"error": "Invalid SMILES string"}

    prediction = float(model.predict(fingerprint)[0])

    return {
        "smiles": smiles,
        "predicted_solubility": prediction,
        "category": solubility_category(prediction),
        "molecule_svg": molecule_svg(smiles),
        "model": "LightGBM",
        "note": "Estimated ML prediction, not lab-confirmed."
    }