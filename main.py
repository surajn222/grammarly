import os
import sys
from wordhoardUtils import *
from osUtils import *
from nltkUtils import *
from powerThesaurasUtils import *

def main():
    obj_wordhoardUtils = wordhoardUtils()
    obj_osUtils = osUtils()

    #Read from file
    obj_file = open("rawWords")
    list_lines = obj_file.readlines()
    print(list_lines)
    obj_file.close()

    # Get synonyms
    for i in list_lines:
        list_synonyms = obj_wordhoardUtils.getSynonyms(i.replace("\n",""))
        print(list_synonyms)
        #Write to file
        obj_file = open("synonyms", "a")
        obj_file.write(i.replace("\n","") + "-------------------------" + "\n")
        for j in list_synonyms:
            obj_file.write(j + "\n")
        obj_file.close()




def main2():
    obj_osUtils = osUtils()
    obj_nltkUtils = nltkUtils()
    #Read from file
    obj_file = open("rawWords")
    list_lines = obj_file.readlines()
    print(list_lines)
    obj_file.close()

    # Get synonyms
    for i in list_lines:
        list_synonyms = obj_nltkUtils.getSynonyms(i.replace("\n",""))
        print(list_synonyms)
        #Write to file
        obj_file = open("synonyms", "a")
        obj_file.write(i.replace("\n",""))
        obj_file.write("-------------------------" + "\n")
        for j in list_synonyms:
            print(j)
            obj_file.write(j + "\n")
        obj_file.close()


def main3():
    # importing the requests library
    obj_powerThesaurasUtils = powerThesaurasUtils()

    obj_file = open("rawWords")
    list_lines = obj_file.readlines()
    print(list_lines)
    obj_file.close()


    for i in list_lines:
        list_synonyms = obj_powerThesaurasUtils.getSynonyms(i)
        print(list_synonyms)
        #Write to file
        obj_file = open("synonyms", "a")
        obj_file.write(i.replace("\n",""))
        obj_file.write("-------------------------" + "\n")
        for j in list_synonyms:
            print(j)
            obj_file.write(j + "\n")
        obj_file.close()



    for i in list_lines:
        list_antonyms = obj_powerThesaurasUtils.getAntonyms(i)
        print(list_antonyms)
        #Write to file
        obj_file = open("antonyms", "a")
        obj_file.write(i.replace("\n",""))
        obj_file.write("-------------------------" + "\n")
        for j in list_antonyms:
            print(j)
            obj_file.write(j + "\n")
        obj_file.close()


    for i in list_lines:
        list_definitions = obj_powerThesaurasUtils.getDefinition(i)
        print(list_definitions)
        #Write to file
        obj_file = open("definitions", "a")
        obj_file.write(i.replace("\n",""))
        obj_file.write("-------------------------" + "\n")
        for j in list_definitions:
            print(j)
            obj_file.write(j + "\n")
        obj_file.close()


    for i in list_lines:
        list_sentences = obj_powerThesaurasUtils.getSampleSentences(i)
        print(list_sentences)
        #Write to file
        obj_file = open("sentences", "a")
        obj_file.write(i.replace("\n",""))
        obj_file.write("-------------------------" + "\n")
        for j in list_sentences:
            print(j)
            obj_file.write(j + "\n")
        obj_file.close()


main3()
