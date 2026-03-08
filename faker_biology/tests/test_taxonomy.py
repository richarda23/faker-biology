#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.taxonomy import ModelOrganism
from faker_biology.taxonomy.taxonomy_data import MODEL_ORGANISMS_ENGLISH, MODEL_ORGANISMS_LATIN


fake = Faker()
fake.add_provider(ModelOrganism)


class ModelOrganismTest(unittest.TestCase):
    def test_model_organism_latin(self):
        self.assertIn(fake.organism_latin(), MODEL_ORGANISMS_LATIN)

    def test_model_organism_e(self):
        self.assertIn(fake.organism_english(), MODEL_ORGANISMS_ENGLISH)

    def test_model_organism(self):
        o = fake.organism()
        self.assertIn(o.english, MODEL_ORGANISMS_ENGLISH)
        self.assertIn(o.latin, MODEL_ORGANISMS_LATIN)
            
