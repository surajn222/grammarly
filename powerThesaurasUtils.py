import os
import sys
import requests
import json
import re


class powerThesaurasUtils:
    def __init__(self):
        pass

    def getSynonyms(self, word):
        # api-endpoint
        URL = "https://www.powerthesaurus.org/" + word.replace("\n","") + "/synonyms"

        headers = {
            "Connection": "keep-alive",
            "sec-ch-ua": "'Chromium';v='92', ' Not A;Brand';v='99', 'Google Chrome';v='92'",
            "sec-ch-ua-mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Referer": "https://www.powerthesaurus.org/peck/synonyms"
        }

        # sending get request and saving the response as response object
        r = requests.get(url=URL, headers=headers)

        # extracting data in json format
        # print(r.content)
        txt = r.content.decode("utf-8")

        # txt = "title='word synonym'"
        x = re.findall("title=\"(\w+) synonym\"", str(txt))

        for i in x:
            print(i)

        return x

    def getAntonyms(self, word):
        # api-endpoint
        URL = "https://www.powerthesaurus.org/" + word.replace("\n","") + "/antonyms"

        headers = {
            "Connection": "keep-alive",
            "sec-ch-ua": "'Chromium';v='92', ' Not A;Brand';v='99', 'Google Chrome';v='92'",
            "sec-ch-ua-mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Referer": "https://www.powerthesaurus.org/peck/antonyms"
        }

        # sending get request and saving the response as response object
        r = requests.get(url=URL, headers=headers)

        # extracting data in json format
        # print(r.content)
        txt = r.content.decode("utf-8")

        # txt = "title='word synonym'"
        x = re.findall("title=\"([\w\s]+) thesaurus\"", str(txt))

        for i in x:
            print(i)

        return x

    def getDefinition(self, word):
        URL = "https://www.powerthesaurus.org/" + word.replace("\n","") + "/definitions"

        headers = {
            "Connection": "keep-alive",
            "sec-ch-ua": "'Chromium';v='92', ' Not A;Brand';v='99', 'Google Chrome';v='92'",
            "sec-ch-ua-mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Referer": "https://www.powerthesaurus.org/inundate/definitions"
        }

        # sending get request and saving the response as response object
        r = requests.get(url=URL, headers=headers)

        # extracting data in json format
        #print(r.content)
        txt = r.content.decode("utf-8")

        # txt = "title='word synonym'"
        #x = re.findall("title=\"([\w\s]+) thesaurus\"", str(txt))
        #txt = '<div class="y5_ab">fill quickly beyond capacity; as with a liquid</div>'

        x = re.findall("<div class=\"y5_ab\">(.*?)</div>", str(txt))

        for i in x:
            print(i)

        return x

    def getSampleSentences(self, word):
        URL = "https://www.powerthesaurus.org/" + word.replace("\n","") + "/examples"

        headers = {
            "Connection": "keep-alive",
            "sec-ch-ua": "'Chromium';v='92', ' Not A;Brand';v='99', 'Google Chrome';v='92'",
            "sec-ch-ua-mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
            "Referer": "https://www.powerthesaurus.org/inundate/definitions"
        }

        # sending get request and saving the response as response object
        r = requests.get(url=URL, headers=headers)

        # extracting data in json format
        #print(r.content)
        txt = r.content.decode("utf-8")

        # txt = "title='word synonym'"
        #x = re.findall("title=\"([\w\s]+) thesaurus\"", str(txt))
        #"Example","sentence":"A torrent of celestial waves will inundate our abode","author"

        x = re.findall("Example\",\"sentence\":\"(.*?)\",", str(txt))

        for i in x:
            print(i)

        return x



