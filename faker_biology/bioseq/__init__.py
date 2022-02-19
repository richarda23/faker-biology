import random
import faker_biology.bioseq.bioseq_data as dna_data
from faker.providers import BaseProvider


class Bioseq(BaseProvider):
    """
     Provider of DNA / RNA / protein sequences. 
             
    """

    def __init__(self, generator):
        super().__init__(generator)

    def dna(self, length: int = 80) -> str:
        """
        Gets a random DNA sequence. Each nucleotide has equal probability of occurrence
        Parameters
        ----------
        length : int, optional
            Desired length of sequence. The default is 80.
        Returns
        -------
        str
            DNA string.
        """
        return self._seq(length, dna_data.unambiguous_dna_letters)

    def rna(self, length: int = 80) -> str:
        """
        Gets a random RNA sequence. Each nucleotide has equal probability of occurrence
        Parameters
        ----------
        length : int, optional
            Desired length of sequence. The default is 80.
        Returns
        -------
        str
            RNA string.
        """
        return self._seq(length, dna_data.unambiguous_rna_letters)

    def stop_codon(self) -> str:
        """
        A randomly-chosen stop codon from the 3 standard stop codons.

        Returns
        -------
        str
            A stop codon.
        """
        return self.random_element(dna_data.stop_codons)

    def cds(self, length: int = 20) -> str:
        """
        Returns a DNA sequence that will encode a polypeptide. The sequence will
        always beging with 'ATG' and end with a randomly-chosen termination codon.
        
        e.g. cds(2) could return 'ATGGAAGTCTGA' 
        Parameters
        ----------
        length : int, optional
            Number of codons, excluding initial ATG and final termination codon. The default is 20.
        Returns
        -------
        str
            A DNA coding sequence.
        """
        i = 0
        codons = []
        while i < 20:
            triplet = self.dna(3)
            if triplet not in dna_data.stop_codons:
                codons.append(triplet)
                i = i + 1

        return "ATG" + "".join(codons) + self.stop_codon()

    def protein(self, length: int = 20) -> str:
        """
        Generates a random protein sequence starting with 'M' and then <length> amino acids
        in single-letter code.

        Parameters
        ----------
        length : int, optional
            Length of sequence after initial 'M'. The default is 20.

        Returns
        -------
        str
            A Protein sequence.

        """
        return "M" + self._seq(length, dna_data.protein_letters)

    def protein_name(self) -> str:
        """
        A randomly chosen protein name from a list of 500 SwissProt protein descriptions
        Returns
        -------
        str
            A name of a real protein.
        """
        return self.random_element(list(dna_data.protein_names.keys()))

    def protein_desc(self) -> str:
        """
        A randomly chosen protein description from a list of 500 SwissProt protein descriptions
        Returns
        -------
        str
            A description of a real protein.
        """
        return self.random_element(list(dna_data.protein_names.values()))

    def protein_name_desc(self) -> dict:
        """
        Returns a name-description pair from a list of 500 SwissProt proteins
        Returns
        -------
        dict
            A name,description tuple.
        """
        index = random.randint(0, len(dna_data.protein_names))
        key = list(dna_data.protein_names.keys())[index]
        return key, dna_data.protein_names[key]

    def _seq(self, length, alphabet):
        alphabet_length = len(alphabet) - 1
        seq = []
        for i in range(length):
            j = random.randint(0, alphabet_length)
            seq.append(alphabet[j])
        return "".join(seq)
