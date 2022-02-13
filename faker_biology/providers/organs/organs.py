#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:20:19 2022

@author: richard
"""
from faker_biology.providers.organs import organ_data
from faker.providers import BaseProvider


class Organ(BaseProvider):
    """
     Provider of organ names. Source of data is Wikipedia:
         https://en.wikipedia.org/wiki/List_of_organs_of_the_human_body
             
    """
  
    def categories(self):
        return list(organ_data.keys())
    
    def organ(self)->str:
        """
        Gets a random mammalian organ
        """
        leaves = []
        self._dict_leaves(organ_data, leaves)
        return self.random_element(leaves)
    
    def non_reproductive_organ(self):
        #print(self.categories())
        categories = filter(lambda c: 'eproductive' not in c, self.categories())
        items = []
       # print(list(categories))
        for c in categories:
            leaves_by_c = self._leaves_by_category(organ_data, c)
            #print (f" leaves by c = {leaves_by_c}")
            items.extend(leaves_by_c)
        return self.random_element(items)
            

    
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

