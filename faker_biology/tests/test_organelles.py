#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.physiology import Organelle


fake = Faker()
fake.add_provider(Organelle)
organ_provider = Organelle(None)


class OrganelleTest(unittest.TestCase):
 

    def test_random_unique_organelle(self):
        organ_set = set([fake.unique.organelle() for i in range(15)])
        self.assertEqual(15, len(organ_set))
        
    def test_common_organell(self):
        for _ in range (100):
         self.assertNotEqual(fake.common_eukaryotic_organelle(), "glycosome")
         
    def test_animal_organell(self):
        for _ in range (100):
            self.assertNotEqual(fake.animal_organelle(), "chloroplast")
            
    def test_plant_organell(self):
        for _ in range (100):
            self.assertNotEqual(fake.plant_organelle(), "lysosome")

    def test_random_organelle(self):
        print(fake.organelle())