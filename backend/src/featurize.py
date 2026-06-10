from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator, Descriptors, rdMolDescriptors
import numpy as np

morgan_generator = rdFingerprintGenerator.GetMorganGenerator(
    radius=2,
    fpSize=2048
)

def smiles_to_fingerprint(smiles: str):
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    fingerprint = morgan_generator.GetFingerprint(mol)
    fingerprint_array = np.array(fingerprint)

    descriptors = np.array([
        Descriptors.MolWt(mol),
        Descriptors.MolLogP(mol),
        rdMolDescriptors.CalcTPSA(mol),
        rdMolDescriptors.CalcNumHBD(mol),
        rdMolDescriptors.CalcNumHBA(mol),
        rdMolDescriptors.CalcNumRings(mol),
        rdMolDescriptors.CalcNumRotatableBonds(mol)
    ])

    features = np.concatenate([fingerprint_array, descriptors])

    return features.reshape(1, -1)