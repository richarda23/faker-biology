# faker-biology
Biology-related fake data provider for Python Faker

Some providers for biology-related concepts and resources.

## Usage:

Standard code to access Faker
```python
 from faker import Faker
 fake = Faker()
```

### Physiology: Cell types and  organs

```python
 from faker_biology.physiology import CellType, Organ

 fake.add_provider(CellType)
 fake.add_provider(Organ)
 
 fake.organ()
 # Sublingual glands

 fake.celltype()
 # Centroacinar cell
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
