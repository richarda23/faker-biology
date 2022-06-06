from faker.providers import BaseProvider
import faker_biology.taxonomy.taxonomy_data as td


class ModelOrganism(BaseProvider):
    """
     Provider of random model organism names used in life-science research. 
    """

    def __init__(self, generator):
        super().__init__(generator)

    def organism_english(self) -> str:
        """
        English name of a  model organism used in life-science research
        Returns
        -------
        str
            A random model organism name.
        """
        return self.random_element(td.MODEL_ORGANISMS_ENGLISH)

    def organism_latin(self) -> str:
        """
        Latin name of a model organism used in life-science research
        Returns
        -------
        str
            A random model organism Latin name.
        """
        return self.random_element(td.MODEL_ORGANISMS_LATIN)
    
    def organism(self):
        """
        Object encapsulating data about a model organism used in life-science research
        Returns
        -------
        ModelOrganism
            A named tuple including  all information about the model organism.
        """
        return self.random_element(td.MODEL_ORGANISMS)
