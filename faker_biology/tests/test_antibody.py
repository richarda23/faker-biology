#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.providers.mol_biol.antibody import Antibody, ModelOrganism


fake=Faker()
fake.add_provider(Antibody)
fake.add_provider(ModelOrganism)
re_provider = Antibody(None)
class AntibodyTest(unittest.TestCase):
    

    def test_random_antibody_isotype(self):
       for i in range(10):
          fake.antibody_isotype()

    def test_random_antibody_application(self):
       for i in range(10):
           fake.antibody_application()
    def test_model_organism(self):
       for i in range(10):
           print(fake.organism_latin())   
  
      
  
        
        
        