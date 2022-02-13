#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.providers.organs.organs import Organ


fake=Faker()
fake.add_provider(Organ)
#organ_provider = Organ()
class OrganTest(unittest.TestCase):
    
  
    
    def test_organ_categories(self):
        pass
     #   self.assertEqual(13, len(organ_provider.categories()))
        
    def test_random_organ(self):
        for i in range(15):
            print(fake.organ())
            
    def test_non_reproductive_organ(self):
        for i in range(30):
            print(fake.non_reproductive_organ())
        
        