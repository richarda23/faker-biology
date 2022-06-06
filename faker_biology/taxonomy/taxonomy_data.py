from collections import namedtuple

## these 2 lists should be equal length
MODEL_ORGANISMS_ENGLISH = [
    "Fly",
    "Mouse",
    "Nematode",
    "Rat",
    "Xenopus",
    "Fission yeast",
    "Budding Yeast",
    "Zebrafish",
]


MODEL_ORGANISMS_LATIN = [
    "Drosophila melanogaster",
    "Mus musculus",
    "Caenorhabditis elegans",
    "Rattus norvegicus",
    "Xenopus laevis",
    "Schizosaccharomyces pombe",
    "Saccharomyces cervisiae",
    "Danio Rerio",
]

MODEL_ORGANISM = namedtuple("model_organism", ["english", "latin"])

zipped = zip(MODEL_ORGANISMS_ENGLISH, MODEL_ORGANISMS_LATIN)
list_zipped = list(zipped)
MODEL_ORGANISMS = [MODEL_ORGANISM(*mo) for mo in list_zipped]




