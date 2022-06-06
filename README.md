# faker-biology
Biology-related fake data provider for Python Faker

Some providers for biology-related concepts and resources.

## Installation

```
 pip install faker-biology
```

## Usage:

Standard code to access Faker
```python
 from faker import Faker
 fake = Faker()
```

### Physiology: Cell types and  organs

```python
 from faker_biology.physiology import CellType, Organ, Organelle

 fake.add_provider(CellType)
 fake.add_provider(Organ)
 fake.add_provider(Organelle)
 
 fake.organ()
 # Sublingual glands

 fake.celltype()
 # Centroacinar cell

 fake.organelle()
 # chloroplast
```

### Biosequences

```python
 from faker_biology.bioseq import Bioseq

 fake.add_provider(Bioseq)

 fake.dna(10)
 # ATCGTGTCAT

 fake.rna(10)
 # AUCGUGUCAU

 fake.protein(10)
 # MTGHILPSTW

 fake.protein_name()
 # HYAL4_HUMAN

 fake.amino_acid()
 # AminoAcid(full_name='Glycine', three_letters_name='Gly', one_letter_name='G', mass=57)
 
 fake.amino_acid_name()
 # Glycine

 fake.amino_acid_3_letters()
 # Cys

 fake.amino_acid_1_letter()
 # W

 fake.amino_acid_mass()
 # 103
```

### Molecular Biology

```python
 from faker_biology.mol_biol import Antibody, RestrictionEnzyme, Enzyme

 fake.add_provider(RestrictionEnzyme)
 fake.add_provider(Antibody)
 fake.add_provider(Enzyme)

 fake.re()
 # EcoRI
 
 fake.blunt()
 # SmaI

 fake.antibody_isotype()
 # IgG

 fake.enzyme()
 # Ubiquitin carboxy-terminal hydrolase L1

```
### Taxonomy 

```python
 from faker_biology.taxonomy import ModelOrganism

 fake.add_provider(ModelOrganism)
 
 fake.organism()
 # Fission yeast

 fake.organism_latin()
 # Schizosaccharomyces pombe
```
