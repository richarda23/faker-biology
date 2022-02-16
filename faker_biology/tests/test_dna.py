#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.providers.nucleic_acid.dna import NucleicAcid
import faker_biology.providers.nucleic_acid as dna_data


fake=Faker()
fake.add_provider(NucleicAcid)
re_provider = NucleicAcid(None)
class DNATest(unittest.TestCase):
    
  
            
    def test_random_dna(self):
        dna_seq = fake.dna(200)
        self.assertTrue( i in dna_seq for i in 'ATCG')
        rna_seq=fake.rna(200)
        self.assertTrue( i in rna_seq for i in 'AUCG')
        
    def test_cds(self):
        cds = fake.cds(20)
        self.assertEqual(26, len(cds))
        self.assertTrue(cds.startswith('ATG'))
        self.assertTrue(cds[-3:] in dna_data.stop_codons) 
        
    def test_protein(self):
        protein = fake.protein(20)
        self.assertEqual(21, len(protein))
        self.assertTrue(protein.startswith('M'))
        
    def test_protein_name(self):
        protein = fake.protein_name()
        for i in range(200):
            
            print (fake.protein_name_desc())
      
  
        
        
        