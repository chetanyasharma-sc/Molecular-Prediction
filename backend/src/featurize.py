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
    rdMolDescriptors.CalcNumRotatableBonds(mol),

    Descriptors.HeavyAtomCount(mol),
    rdMolDescriptors.CalcFractionCSP3(mol),
    rdMolDescriptors.CalcNumAromaticRings(mol),
    rdMolDescriptors.CalcNumAliphaticRings(mol),
    Descriptors.MolMR(mol),
    Descriptors.BertzCT(mol),
    rdMolDescriptors.CalcLabuteASA(mol),
    rdMolDescriptors.CalcNumHeteroatoms(mol),
    Chem.GetFormalCharge(mol),
])
    features = np.concatenate([fingerprint_array, descriptors])

    return features.reshape(1, -1)


def get_molecular_descriptors(mol):
    return {
        "molecular_weight": round(Descriptors.MolWt(mol), 3),
        "logp": round(Descriptors.MolLogP(mol), 3),
        "tpsa": round(rdMolDescriptors.CalcTPSA(mol), 3),
        "h_bond_donors": rdMolDescriptors.CalcNumHBD(mol),
        "h_bond_acceptors": rdMolDescriptors.CalcNumHBA(mol),
        "rings": rdMolDescriptors.CalcNumRings(mol),
        "rotatable_bonds": rdMolDescriptors.CalcNumRotatableBonds(mol),
    }


def lipinski_rule(descriptors):
    violations = []

    if descriptors["molecular_weight"] >= 500:
        violations.append("Molecular weight >= 500")

    if descriptors["logp"] >= 5:
        violations.append("LogP >= 5")

    if descriptors["h_bond_donors"] > 5:
        violations.append("H-bond donors > 5")

    if descriptors["h_bond_acceptors"] > 10:
        violations.append("H-bond acceptors > 10")

    return {
        "status": "Pass" if len(violations) == 0 else "Fail",
        "violations": violations
    }