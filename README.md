# Molecular Prediction Project — Steps Completed So Far

## 1. Created Project Repository

You created a GitHub repository:

```text
Molecular-Prediction
```

and opened it in [GitHub Codespaces](https://github.com/features/codespaces?utm_source=chatgpt.com).

---

# 2. Created Development Branch

Created a separate development branch:

```bash
git checkout -b develop
```

Purpose:

* keep `main` stable
* develop features safely

---

# 3. Created Backend/Frontend Structure

Project structure:

```text
Molecular-Prediction/
├── backend/
│   ├── app/
│   ├── data/
│   ├── models/
│   ├── notebooks/
│   ├── src/
│   └── requirements.txt
│
├── frontend/
└── README.md
```

---

# 4. Created Clean Python Virtual Environment

Inside `backend/`:

```bash
python -m venv .venv
```

Activated:

```bash
source .venv/bin/activate
```

Purpose:

* isolated dependencies
* reproducible environment
* avoid system Python conflicts

---

# 5. Installed ML + Chemistry Dependencies

Installed:

* pandas
* NumPy
* scikit-learn
* RDKit
* XGBoost
* LightGBM
* FastAPI
* Jupyter

Purpose:

* chemistry processing
* feature engineering
* ML training
* backend API later

---

# 6. Connected Jupyter Notebook to `.venv`

Registered notebook kernel:

```bash
python -m ipykernel install --user --name=molecular-backend --display-name "Python (molecular-backend)"
```

Notebook now correctly uses:

```text
/workspaces/Molecular-Prediction/backend/.venv/bin/python
```

Purpose:

* notebook uses same environment as backend
* all installed packages accessible

---

# 7. Downloaded ESOL Dataset

Dataset:
ESOL

Saved as:

```text
backend/data/esol.csv
```

Purpose:

* real molecular property prediction dataset
* predict aqueous solubility

---

# 8. Loaded Dataset with Pandas

Used:

```python
import pandas as pd

df = pd.read_csv("../data/esol.csv")
```

Purpose:

* load CSV into DataFrame
* begin molecular data exploration

---

# 9. Explored Dataset

Checked:

```python
df.head()
df.shape
df.columns
```

Found:

* 1128 molecules
* 10 columns
* important columns:

  * `smiles`
  * `measured log solubility in mols per litre`

Purpose:

* understand data structure
* identify ML target column

---

# 10. Learned About SMILES

Examples:

| Molecule | SMILES     |
| -------- | ---------- |
| Ethanol  | `CCO`      |
| Benzene  | `c1ccccc1` |

Purpose:

* chemistry represented as text
* input format for molecular ML

---

# 11. Converted SMILES into RDKit Molecules

Used:

```python
from rdkit import Chem

df["mol"] = df["smiles"].apply(Chem.MolFromSmiles)
```

Purpose:
Convert:

```text
SMILES text
```

into:

```text
RDKit molecular objects
```

Now RDKit understands:

* atoms
* bonds
* molecular graph
* chemical structure

---

# 12. Validated Molecular Data

Checked:

```python
df["mol"].isnull().sum()
```

Result:

```text
0
```

Meaning:

* all SMILES valid
* no failed molecular conversions
* no corrupted molecular strings

Purpose:

* ensure clean chemistry data before ML

---

# Current Position

You are now here:

```text
CSV dataset
    ↓
SMILES strings
    ↓
RDKit molecular objects
    ↓
NEXT: Molecular fingerprints
```

---

# What Comes Next

Next stage:

```text
Molecule → Numerical features → ML model
```

We will generate:

* Morgan fingerprints
* molecular vectors
* machine learning input features

This is where chemistry becomes machine learning.




Create/replace your root `README.md` with this:

````md
# Molecular Solubility Prediction App

A full-stack machine learning application that predicts molecular solubility from a SMILES string.

## What This Project Does

The user enters a molecular SMILES string, and the app returns a predicted LogS solubility value.

Example:

```json
{
  "smiles": "CCO",
  "predicted_solubility": 1.06
}
````

## Project Status

Completed:

* Created GitHub repo and `develop` branch
* Built backend with FastAPI
* Built frontend with Nuxt/Vue
* Downloaded ESOL solubility dataset
* Converted SMILES into RDKit molecule objects
* Generated Morgan fingerprints
* Added molecular descriptors
* Trained multiple regression models
* Compared model performance
* Selected best model
* Saved trained model as `best_model.pkl`
* Created prediction API
* Connected frontend to backend

## ML Pipeline

```text
SMILES string
    ↓
RDKit molecule
    ↓
Morgan fingerprints + molecular descriptors
    ↓
Trained ML model
    ↓
Predicted LogS solubility
```

## Features Used

The model uses:

* Morgan fingerprint: 2048 bits
* Molecular Weight
* LogP
* TPSA
* Hydrogen bond donors
* Hydrogen bond acceptors
* Number of rings
* Rotatable bonds

Total features:

```text
2048 + 7 = 2055 features
```

## Models Compared

Models trained and evaluated:

* Linear Regression
* Ridge Regression
* Random Forest
* Gradient Boosting
* XGBoost
* LightGBM
* Neural Network

Best model:

```text
LightGBM
```

## Best Model Performance

```text
MAE:  0.497
RMSE: 0.709
R²:   0.893
```

## Example Predictions

### Ethanol

```text
SMILES: CCO
Actual LogS: 1.10
Predicted LogS: ~1.06
```

### Benzene

```text
SMILES: c1ccccc1
Actual LogS: 1.64
Predicted LogS: ~1.74
```

### Paracetamol

```text
SMILES: CC(=O)NC1=CC=C(C=C1)O
Approx Actual LogS: ~-1.1
Predicted LogS: ~-1.3
```

## Project Structure

```text
Molecular-Prediction/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── data/
│   │   └── esol.csv
│   ├── models/
│   │   └── best_model.pkl
│   ├── notebooks/
│   │   └── 01_data_exploration.ipynb
│   ├── src/
│   │   ├── featurize.py
│   │   └── predict.py
│   ├── requirements.txt
│   └── .venv/
│
├── frontend/
│   ├── app.vue
│   ├── package.json
│   └── nuxt.config.ts
│
└── README.md
```

## Backend

The backend is built with FastAPI.

Run backend:

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs:

```text
/docs
```

Prediction endpoint:

```text
POST /predict
```

Request:

```json
{
  "smiles": "CCO"
}
```

Response:

```json
{
  "smiles": "CCO",
  "predicted_solubility": 1.06
}
```

## Frontend

The frontend is built with Nuxt/Vue.

Run frontend:

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

## Technologies Used

* Python
* FastAPI
* RDKit
* pandas
* NumPy
* scikit-learn
* XGBoost
* LightGBM
* joblib
* Nuxt
* Vue
* GitHub Codespaces

## Important Note

This project is an educational ML prototype. Predictions are model estimates and should not be treated as lab-confirmed experimental values.

## Future Improvements

Planned improvements:

* Add solubility category
* Add molecular descriptor output
* Add Lipinski Rule of 5
* Add confidence/applicability warning
* Add toxicity prediction
* Add ADMET prediction
* Add model retraining pipeline
* Improve frontend UI
* Deploy backend and frontend publicly

````

Then commit:

```bash
git add README.md
git commit -m "Add project README"
git push
````
