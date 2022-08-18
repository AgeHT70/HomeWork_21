import requests
from random import choice
from basic_word import BasicWord


def load_random_word(url: str) -> BasicWord:
    """
    Get json_file with list of words from URL
    Choose random word from list, create an instance of the class `BasicWord`
    return this instance
    :param url: site with list of words
    :return: instance of the class `BasicWord`
    """
    data = requests.get(url).json()
    basic_word = BasicWord(*choice(data).values())
    return basic_word
