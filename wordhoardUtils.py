import os
import sys
from wordhoard import Synonyms


class wordhoardUtils:
    def __init__(self):
        pass

    def getSynonyms(self, word):
        synonym = Synonyms(word)
        synonym_results = synonym.find_synonyms()
        return synonym_results