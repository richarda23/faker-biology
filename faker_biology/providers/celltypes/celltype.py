#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 09:02:05 2022

@author: richard
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:20:19 2022

@author: richard
"""
from typing import Sequence

from faker_biology.providers.celltypes import cell_types
from faker_biology.providers import BioProvider

class CellType(BioProvider):
    """
     Provider of human cell type names. Source of data is Wikipedia:
         https://en.wikipedia.org/wiki/List_of_distinct_cell_types_in_the_adult_human_body
             
    """
    def __init__(self, generator):
        super().__init__(generator)
  
    def categories(self)-> Sequence[str]:
        """
        A list of cell-type categories
        """
        return list(cell_types.keys())
    
    def celltype(self)->str:
        """
        Gets a random mammalian cell type
        """
        leaves = []
        self._dict_leaves(cell_types, leaves)
        return self.random_element(leaves)
    
        

    
   

