#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.providers.nucleic_acid.dna import NucleicAcid


fake=Faker()
fake.add_provider(NucleicAcid)
re_provider = NucleicAcid(None)
class DNATest(unittest.TestCase):
    
  
            
    def test_random_dna(self):
        dna_seq = fake.dna(200)
        self.assertTrue( i in dna_seq for i in 'ATCG')
        rna_seq=fake.rna(200)
        self.assertTrue( i in dna_seq for i in 'AUCG')
        
  
        
        
        