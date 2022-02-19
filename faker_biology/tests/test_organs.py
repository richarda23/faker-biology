#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.physiology import Organ


fake = Faker()
fake.add_provider(Organ)
organ_provider = Organ(None)


class OrganTest(unittest.TestCase):
    def test_organ_categories(self):
        self.assertEqual(13, len(organ_provider.categories()))

    def test_random_organ(self):
        organ_set = set([fake.unique.organ() for i in range(15)])
        self.assertEqual(15, len(organ_set))

    def test_non_reproductive_organ(self):
        organs = [fake.unique.non_reproductive_organ() for i in range(70)]
        self.assertFalse("Ovaries" in organs)
