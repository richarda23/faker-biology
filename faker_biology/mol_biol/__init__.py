from typing import Sequence

from faker.providers import BaseProvider
from faker_biology import BioProvider

from faker_biology.mol_biol.re import rest_dict
import faker_biology.mol_biol.antibody as ab
from faker_biology.mol_biol.enzyme_data import enzymes


class Antibody(BaseProvider):
    """
     Provider of fake antibody data. 
    """

    def __init__(self, generator):
        super().__init__(generator)

    def antibody_isotype(self) -> str:
        """
        A random isotype like IgG, IgM etc
        Returns
        -------
        str
        """
        return self.random_element(ab.ANTIBODY_ISOTYPE)

    def antibody_application(self) -> str:
        """
        A random application of an antibody, e.g. ELISA, Western Blot
        Returns
        -------
        str
        """
        return self.random_element(ab.ANTIBODY_APPLICATION)

    def antibody_source(self) -> str:
        """
        A random name of an organism used to generate antibodies
        Returns
        -------
        str
        """
        return self.random_element(ab.ANTIBODY_SOURCE)

    def dilution(self) -> str:
        """
        A random antibody dilution in format 1:X
        Returns
        -------
        str
        """
        return self.random_element(ab.DILUTIONS)


class RestrictionEnzyme(BaseProvider):
    """
     Restriction enzyme: source is https://github.com/biopython/biopython/blob/master/Bio/Restriction/Restriction_Dictionary.py
     which in turn is derived from REBASE emboss files version 112 (2021).
    """

    def __init__(self, generator):
        super().__init__(generator)

    def restriction_enzyme(self, min_length=0) -> str:
        """
         Returns name of a restriction enzyme. Can choose enzymes cutting above a particular length
         Raises ValueError if no enzymes match search criteria
        """
        keys = []
        if min_length > 0:
            for k, v in rest_dict.items():
                if v["size"] >= min_length:
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
        for k, v in rest_dict.items():
            if v["ovhg"] is None or v["ovhg"] == 0:
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
        for k, v in rest_dict.items():
            if v["ovhg"] is not None and v["ovhg"] > 0:
                keys.append(k)
        return self.random_element(keys)

class Enzyme(BioProvider):
    """
     Provider of enzyme names. Source of data is Wikipedia:
         https://en.wikipedia.org/wiki/List_of_enzymes
             
    """

    def __init__(self, generator):
        super().__init__(generator)

    def categories(self) -> Sequence[str]:
        """
        A list of enzyme categories
        """
       
        return list(enzymes.keys())
    
    def _all_enzymes(self):
        ## cache 
        if not hasattr(self, '_enzymes'):
            leaves = []
            self._dict_leaves(enzymes, leaves)
            self._enzymes = list(filter(lambda e: not e.startswith("Category"),  leaves))
        return self._enzymes
      
    def enzyme_category(self):
        if not hasattr(self, '_categories'):
            all_vals = []
            self._dict_all(enzymes, all_vals)
            _categories = list(filter(lambda e:  e.startswith("Category"),  all_vals))
            self._categories = [x[9:] for x in _categories if x.startswith('Category:')]
        return self.random_element(self._categories)
        

    def enzyme(self) -> str:
        """
        Gets a random enzyme name
        """
        return self.random_element(self._all_enzymes())