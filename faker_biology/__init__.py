#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 08:40:33 2022

@author: richard
"""
from faker.providers import BaseProvider


class BioProvider(BaseProvider):
    """
     Base class of some bio providers
    """

    def __init__(self, generator):
        super().__init__(generator)

    def _dict_leaves(self, data: dict, leaves=[]):
        nodes = data.keys()
        for key in nodes:
            subnode = data[key]
            if len(subnode) > 0:
                self._dict_leaves(subnode, leaves)
            else:
                leaves.append(key)

    def _leaves_by_category(self, data: dict, category: str):
        leaves = []
        self._dict_leaves(data[category], leaves)
        return leaves
    
    def _dict_all(self, data: dict, leaves =[]):
         """
          Gets all keys in nested dict
         """
         nodes = data.keys()
         for key in nodes:
            subnode = data[key]
            if len(subnode) > 0:
                leaves.append(key)
                self._dict_leaves(subnode, leaves)
            else:
                leaves.append(key)
