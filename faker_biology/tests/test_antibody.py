#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.mol_biol import Antibody


fake = Faker()
fake.add_provider(Antibody)
re_provider = Antibody(None)


class AntibodyTest(unittest.TestCase):
    def test_random_antibody_isotype(self):
        for i in range(10):
            fake.antibody_isotype()

    def test_random_antibody_application(self):
        for i in range(10):
            fake.antibody_application()
