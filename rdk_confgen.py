import click
from rdkit import Chem
from rdkit.Chem import rdDistGeom
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolAlign

@click.command()
@click.option('--input', '-i', help='inputfile MOL', required=True)
@click.option('--output', '-o', help='output file path', default='gen_confs.sdf')
@click.option('--prunermsthresh', '-t', default=0.1, type=float, help='Retain only the conformations out of ‘numConfs’')
@click.option('--numconf', default=50, type=int)
@click.option('--add_ref', '-r', default=False, type=bool)
def confgen(input, output, prunermsthresh, numconf, add_ref):
    mol = Chem.AddHs(Chem.MolFromMolFile(input), addCoords=True)
    refmol = Chem.AddHs(Chem.Mol(mol))
    param = rdDistGeom.ETKDGv2()
    param.pruneRmsThresh = prunermsthresh
    cids = rdDistGeom.EmbedMultipleConfs(mol, numconf, param)
    mp = AllChem.MMFFGetMoleculeProperties(mol, mmffVariant='MMFF94s')
    AllChem.MMFFOptimizeMoleculeConfs(mol, numThreads=0, mmffVariant='MMFF94s')
    w = Chem.SDWriter(output)
    if add_ref:
        refmol.SetProp('CID', '-1')
        refmol.SetProp('Energy', '')
        w.write(refmol)
    res = []

    for cid in cids:
        ff = AllChem.MMFFGetMoleculeForceField(mol, mp, confId=cid)
        e = ff.CalcEnergy()
        res.append((cid, e))
    sorted_res = sorted(res, key=lambda x:x[1])
    rdMolAlign.AlignMolConformers(mol)
    for cid, e in sorted_res:
        mol.SetProp('CID', str(cid))
        mol.SetProp('Energy', str(e))
        w.write(mol, confId=cid)
    w.close()

if __name__=='__main__':
    confgen()
