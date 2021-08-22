import os
import sys
from nltk.corpus import wordnet  # Import wordnet from the NLTK

from itertools import chain
from nltk.corpus import wordnet

class nltkUtils:
    def __init__(self):
        pass

    def getSynonyms(self, word):
        synset = wordnet.synsets(word)
        # print('Word and Type : ' + synset[0].name())
        # print('Synonym of Travel is: ' + synset[0].lemmas()[0].name())
        # print('The meaning of the word : ' + synset[0].definition())
        # print('Example of Travel : ' + str(synset[0].examples()))
        # return synset[0].lemmas()[0].name()

        synonyms = wordnet.synsets(word)
        lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
        #print(lemmas)
        return lemmas


