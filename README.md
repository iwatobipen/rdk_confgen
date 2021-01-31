# Conformation generator with RDKit


## Description
 - This is simple script for generating conformers from single molfiles
 - This script generates conformers with MMFF94s FF which is implemented in rdkit


## Requirements
 - RDKit
 - Click


## Install
 
 ```
 $ git clone https://github.com/iwatobipen/rdk_confgen.git
 $ cd rdk_confgen
 $ pip install -e .
 ```

## Basic usage
 - User need to prepare input molfile as a template.
 - Then run confgen command (with deafault settings) 

 ```
 $ confgen -i ligand.mol -o genconfs.sdf
 ``` 

## Useful informations
 - [Coformer Generation using RDKit](https://www.rdkit.org/UGM/2012/Ebejer_20110926_RDKit_1stUGM.pdf)
 - [Freely Available Conformer Generation Methods: How Good Are They?](https://pubs.acs.org/doi/abs/10.1021/ci2004658)
