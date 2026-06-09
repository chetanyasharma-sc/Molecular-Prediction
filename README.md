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
