#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:20:19 2022

@author: richard
"""
from typing import Sequence
import faker_biology.providers.nucleic_acid as dna_data
from faker.providers import BaseProvider
import random


class NucleicAcid(BaseProvider):
    """
     Provider of DNA / RNA sequences. 
             
    """
    def __init__(self, generator):
        super().__init__(generator)
  
    def dna(self, length=80)->str:
        """
        Gets a random DNA sequence. Each nucleotide has equal probability of occurrence
        Parameters
        ----------
        length : int, optional
            Desired lenght of sequence. The default is 80.
        Returns
        -------
        str
            DNA string.
        """
        return self._nucleotide_seq(length, dna_data.unambiguous_dna_letters)
    
    def rna(self, length=80)->str:
        """
        Gets a random RNA sequence. Each nucleotide has equal probability of occurrence
        Parameters
        ----------
        length : int, optional
            Desired lenght of sequence. The default is 80.
        Returns
        -------
        str
            RNA string.
        """
        return self._nucleotide_seq(length, dna_data.unambiguous_rna_letters)
    
    def _nucleotide_seq(self, length, alphabet):
        alphabet_length= len(alphabet) -1
        seq = []
        for i in range(length):       
           j = random.randint(0, alphabet_length)
           seq.append(alphabet[j])
        return ''.join(seq)
        
                            
                    