#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.providers.celltypes.celltype import CellType


fake=Faker()
fake.add_provider(CellType)
cell_provider = CellType(None)
class OrganTest(unittest.TestCase):
  
    def test_organ_categories(self):
        self.assertEqual(3, len(cell_provider.categories()))
        
    def test_random_organ(self):
        cells = set([fake.unique.celltype() for i in  range (15)])
        self.assertEqual(15, len(cells))
            
        
        