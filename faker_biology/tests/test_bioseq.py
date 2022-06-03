#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest

from faker import Faker

from faker_biology.bioseq import Bioseq, bioseq_data


fake = Faker()
fake.add_provider(Bioseq)
re_provider = Bioseq(None)


class BioseqTest(unittest.TestCase):
    def test_random_dna(self):
        dna_seq = fake.dna(200)
        self.assertTrue(i in dna_seq for i in "ATCG")
        rna_seq = fake.rna(200)
        self.assertTrue(i in rna_seq for i in "AUCG")

    def test_cds(self):
        cds = fake.cds(20)
        self.assertEqual(66, len(cds))
        self.assertTrue(cds.startswith("ATG"))
        self.assertTrue(cds[-3:] in bioseq_data.stop_codons)

    def test_protein(self):
        protein = fake.protein(20)
        self.assertEqual(21, len(protein))
        self.assertTrue(protein.startswith("M"))

    def test_protein_name(self):
        protein = fake.protein_name()

    def test_amino_acid_name(self):
        amino_acid_names = [
            "Alanine",
            "Arginine",
            "Asparagine",
            "Aspartic Acid",
            "Cysteine",
            "Glutamic Acid",
            "Glutamine",
            "Glycine",
            "Histidine",
            "Isoleucine",
            "Leucine",
            "Lysine",
            "Methionine",
            "Phenylalanine",
            "Proline",
            "Serine",
            "Threonine",
            "Tryptophan",
            "Tyrosine",
            "Valine",
        ]

        amino_acid = fake.amino_acid_name()
        self.assertIn(amino_acid, amino_acid_names)

    def test_amino_acid_3_letters(self):
        amino_acid_names = [
            "Ala",
            "Arg",
            "Asn",
            "Asp",
            "Cys",
            "Glu",
            "Gln",
            "Gly",
            "His",
            "Ile",
            "Leu",
            "Lys",
            "Met",
            "Phe",
            "Pro",
            "Ser",
            "Thr",
            "Trp",
            "Tyr",
            "Val",
        ]

        amino_acid = fake.amino_acid_3_letters()
        self.assertIn(amino_acid, amino_acid_names)

    def test_amino_acid_1_letter(self):
        amino_acid_names = "ARNDCEQGHILKMFPSTWYV"

        amino_acid = fake.amino_acid_1_letter()
        self.assertIn(amino_acid, amino_acid_names)
