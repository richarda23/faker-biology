# -*- coding: utf-8 -*-

from typing import Sequence
from faker_biology.providers.mol_biol import rest_dict
from faker.providers import BaseProvider


class RestrictionEnzyme(BaseProvider):
    """
     Restriction enzyme: source is https://github.com/biopython/biopython/blob/master/Bio/Restriction/Restriction_Dictionary.py
     which in turn is derived from REBASE emboss files version 112 (2021).
    """
    
    def __init__(self, generator):
        super().__init__(generator)
    
    def restriction_enzyme(self, min_length=0) ->str:
        """
         Returns name of a restriction enzyme. Can choose enzymes cutting above a particular length
         Raises ValueError if no enzymes match search criteria
        """
        keys = []
        if min_length > 0:
            for k,v in rest_dict.items():
                if v['size'] >= min_length:
                    keys.append(k)
        else:
            keys = rest_dict.keys()
        if len(keys) == 0:
            raise ValueError("No enzymes were found matching that filter.")
        return self.random_element(keys)
    
    def restriction_enzyme_data(self) -> dict:
        """
         Returns data dict of a restriction enzyme. Does not work with 'faker.unique'
         as the dict is not hashable
        """
        return rest_dict[self.restriction_enzyme()]
    
    def blunt(self) -> str:
        """
        Returns
        -------
        str
            Random blunt-end cutter.
        """
        keys = []
        for k,v in rest_dict.items():
            if v['ovhg'] is None or v['ovhg'] == 0:
                keys.append(k)
        return self.random_element(keys)
    
    def sticky(self) -> str:
        """
        Returns
        -------
        str
            Random sticky-ended cutter.
        """
        keys = []
        for k,v in rest_dict.items():
            if v['ovhg'] is not None and v['ovhg'] > 0:
                keys.append(k)
        return self.random_element(keys)
        