#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.mol_biol import Enzyme


fake = Faker()
fake.add_provider(Enzyme)
enzyme_provider = Enzyme(None)


class EnzymeTest(unittest.TestCase):
    def test_enzyme_categories(self):
        self.assertEqual(6, len(enzyme_provider.categories()))

    def test_random_enzyme(self):
        total_enzyme_count=150
        enzymes = set([fake.unique.enzyme() for i in range(total_enzyme_count)])
        self.assertEqual(total_enzyme_count, len(enzymes))


    def test_random_category(self):
        enzymes = set([fake.unique.enzyme_category() for i in range(50)])
        self.assertEqual(50, len(enzymes))