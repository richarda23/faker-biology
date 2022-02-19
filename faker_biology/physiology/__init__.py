#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:20:19 2022

@author: richard
"""
from typing import Sequence
from faker_biology import BioProvider

from faker_biology.physiology.celltype_data import cell_types
from faker_biology.physiology.organs_data import organ_data


class CellType(BioProvider):
    """
     Provider of human cell type names. Source of data is Wikipedia:
         https://en.wikipedia.org/wiki/List_of_distinct_cell_types_in_the_adult_human_body
             
    """

    def __init__(self, generator):
        super().__init__(generator)

    def categories(self) -> Sequence[str]:
        """
        A list of cell-type categories
        """
        return list(cell_types.keys())

    def celltype(self) -> str:
        """
        Gets a random human cell type
        """
        leaves = []
        self._dict_leaves(cell_types, leaves)
        return self.random_element(leaves)


class Organ(BioProvider):
    """
     Provider of human organ names. Source of data is Wikipedia:
         https://en.wikipedia.org/wiki/List_of_organs_of_the_human_body
             
    """

    def __init__(self, generator):
        super().__init__(generator)

    def categories(self) -> Sequence[str]:
        """
        A list of organ categories
        """
        return list(organ_data.keys())

    def organ(self) -> str:
        """
        Gets a random mammalian organ
        """
        leaves = []
        self._dict_leaves(organ_data, leaves)
        return self.random_element(leaves)

    def non_reproductive_organ(self) -> str:
        """
        Gets a random non-reproductive organ
        """
        return self.random_element(self._generate_non_repr_organs())

    def _generate_non_repr_organs(self):
        if not hasattr(self, "_nonr_items"):
            categories = filter(lambda c: "eproductive" not in c, self.categories())
            self._nonr_items = []
            for c in categories:
                leaves_by_c = self._leaves_by_category(organ_data, c)
                # print (f" leaves by c = {leaves_by_c}")
                self._nonr_items.extend(leaves_by_c)
        return self._nonr_items
