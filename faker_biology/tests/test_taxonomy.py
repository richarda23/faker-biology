#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.taxonomy import ModelOrganism


fake = Faker()
fake.add_provider(ModelOrganism)
cell_provider = ModelOrganism(None)


class ModelOrganismTest(unittest.TestCase):
    def test_model_organism(self):
        for i in range(10):
            print(fake.organism_latin())
