#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:03:13 2022

@author: richardadams
"""
from typing import Sequence
from faker.providers import BaseProvider

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

ANTIBODY_ISOTYPE = [
    "IgG",
    "IgA",
    "IgD",
    "IgE",
    "IgG1",
    "IgG2",
    "IgG3",
    "IgG4",
    "IgM",
    "IgY",
]

ANTIBODY_APPLICATION = [
    "ChIP",
    "ELISA",
    "Flow Cytometry",
    "Immunocytochemistry",
    "Immunofluorescence",
    "Immunohistochemistry",
    "Western blot",
]

ANTIBODY_SOURCE = [
    "Chicken",
    "Goat",
    "Guinea Pig",
    "Human",
    "Mouse",
    "Rabbit",
    "Rat",
    "Sheep",
]

DILUTIONS = ["1:10", "1:50", "1:100", "1:250", "1:500", "1:1000"]


class ModelOrganism(BaseProvider):
    """
     Provider of random model organism names. 
    """

    def __init__(self, generator):
        super().__init__(generator)

    def organism(self) -> str:
        """
        English name of a  model organism used in life-science research
        Returns
        -------
        str
            A random model organism name.
        """
        return self.random_element(MODEL_ORGANISMS_ENGLISH)

    def organism_latin(self) -> str:
        """
        Latin name of a model organism used in life-science research
        Returns
        -------
        str
            A random model organism Latin name.
        """
        return self.random_element(MODEL_ORGANISMS_LATIN)


class Antibody(BaseProvider):
    """
     Provider of fake antibody data. 
    """

    def __init__(self, generator):
        super().__init__(generator)

    def antibody_isotype(self) -> str:
        """
        A random isotype like IgG, IgM etc
        Returns
        -------
        str
        """
        return self.random_element(ANTIBODY_ISOTYPE)

    def antibody_application(self) -> str:
        """
        A random application of an antibody, e.g. ELISA, Western Blot
        Returns
        -------
        str
        """
        return self.random_element(ANTIBODY_APPLICATION)

    def antibody_source(self) -> str:
        """
        A random name of an organism used to generate antibodies
        Returns
        -------
        str
        """
        return self.random_element(ANTIBODY_SOURCE)

    def dilution(self) -> str:
        """
        A random antibody dilution in format 1:X
        Returns
        -------
        str
        """
        return self.random_element(DILUTIONS)
