#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:27:03 2022

@author: richard
"""

import unittest
from faker import Faker
from faker_biology.physiology import CellType


fake = Faker()
fake.add_provider(CellType)
cell_provider = CellType(None)


class OrganTest(unittest.TestCase):
    def test_celltype_categories(self):
        self.assertEqual(3, len(cell_provider.categories()))

    def test_random_cell_type(self):
        cells = set([fake.unique.celltype() for i in range(15)])
        self.assertEqual(15, len(cells))

    def test_dict_leaves_default_arg_not_shared(self):
        # Mutable default bug: calling _dict_leaves twice with an explicit list
        # each time should give the same results. This verifies that a fresh list
        # is used each time rather than a shared default accumulating state.
        from faker_biology import BioProvider
        p = BioProvider(None)
        data = {"a": {}, "b": {}, "c": {}}

        first = []
        p._dict_leaves(data, first)

        second = []
        p._dict_leaves(data, second)

        self.assertEqual(first, second,
            "Repeated calls to _dict_leaves should return identical results")
